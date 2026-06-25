#!/usr/bin/env python3
"""Scan README.md's "Time-limited promos" section for expiring entries and
file GitHub issues for any within EXPIRY_WINDOW_DAYS (default 7) of expiring
or already expired.

Designed to run in a GitHub Actions workflow. Uses the GitHub CLI (`gh`) for
issue creation and duplicate detection (no token handling needed beyond the
default GITHUB_TOKEN + `gh`).

Exit code 0 always — a missing/parsing problem should not fail the workflow.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from datetime import date, datetime

README = os.environ.get("README_PATH", "README.md")
WINDOW_DAYS = int(os.environ.get("EXPIRY_WINDOW_DAYS", "7"))
LABEL = os.environ.get("ISSUE_LABEL", "expiry")


def run(cmd: list[str]) -> str:
    return subprocess.run(cmd, capture_output=True, text=True).stdout


def extract_promos(text: str) -> list[tuple[str, str]]:
    """Return [(tool, 'YYYY-MM-DD'), ...] from the Time-limited promos table."""
    # Capture from the promos heading up to the next H2 heading.
    m = re.search(
        r"## ⏳ Time-limited promos.*?(?=\n## |\Z)",
        text,
        flags=re.DOTALL,
    )
    if not m:
        return []
    section = m.group(0)
    results = []
    # Table rows: | **Tool** | ... | **YYYY-MM-DD** | ...
    for line in section.splitlines():
        if not line.strip().startswith("|") or "---" in line:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        tool_cell = cells[0]
        # Find a YYYY-MM-DD anywhere in the row (the Expires column is preferred
        # but be lenient about column order).
        dm = re.search(r"\b(\d{4}-\d{2}-\d{2})\b", line)
        if not dm:
            continue
        tool = re.sub(r"[*`]", "", tool_cell).strip() or "Unknown tool"
        results.append((tool, dm.group(1)))
    return results


def existing_open_titles() -> set[str]:
    """Titles of open issues authored by the workflow / gh user."""
    out = run([
        "gh", "issue", "list",
        "--state", "open",
        "--label", LABEL,
        "--limit", "100",
        "--json", "title",
    ])
    try:
        import json
        return {item["title"] for item in json.loads(out)}
    except Exception:
        return set()


def create_issue(tool: str, expiry: str, days: int) -> None:
    title = f"[expiry] {tool} promo expires {expiry}"
    if title in existing_open_titles():
        print(f"skip (open issue exists): {title}")
        return
    status = "EXPIRED" if days < 0 else "expiring"
    body = (
        f"### ⏳ {status}: {tool} time-limited promo\n\n"
        f"- **Tool:** {tool}\n"
        f"- **Expires:** {expiry} ({days} days from scan on {date.today()})\n\n"
        "This promo in `README.md` (`## ⏳ Time-limited promos`) is "
        f"{('expiring soon' if days >= 0 else 'already expired')}.\n\n"
        "Suggested actions:\n"
        "- Verify on the official page whether the promo was extended or ended.\n"
        "- If ended: remove from the Time-limited promos section and update the "
        "tool's regular entry.\n"
        "- If extended: update the expiry date in the table.\n\n"
        "_Auto-filed by the expiry-check workflow._"
    )
    res = subprocess.run([
        "gh", "issue", "create",
        "--title", title,
        "--body", body,
        "--label", LABEL,
    ], capture_output=True, text=True)
    if res.returncode == 0:
        print(f"created: {res.stdout.strip()}")
    else:
        print(f"FAILED to create issue: {res.stderr.strip()}", file=sys.stderr)


def main() -> int:
    if not os.path.exists(README):
        print(f"README not found at {README}", file=sys.stderr)
        return 0
    text = open(README, encoding="utf-8").read()
    promos = extract_promos(text)
    if not promos:
        print("no promos found")
        return 0
    today = date.today()
    for tool, ds in promos:
        try:
            d = datetime.strptime(ds, "%Y-%m-%d").date()
        except ValueError:
            continue
        days = (d - today).days
        if days <= WINDOW_DAYS:
            create_issue(tool, ds, days)
    return 0


if __name__ == "__main__":
    sys.exit(main())
