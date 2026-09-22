# Team Workspace integration demo target

This repository contains a small, synthetic shopping-cart example for demonstrating Slack and GitHub issue workflows. It contains no internal company code or documents.

Run the baseline tests with `python3 -m unittest -v`.

Demo task: `summarize_cart([])` currently raises `ZeroDivisionError`. The requested behavior is `{'item_count': 0, 'total': 0, 'average_price': 0}`. Add a regression test and a minimal fix while preserving non-empty cart behavior.

Use this issue for the end-to-end demonstration: a Slack request creates a GitHub issue, an agent triages it, and an explicitly approved coding task prepares a validated local candidate. No automatic merge or deployment is included.
