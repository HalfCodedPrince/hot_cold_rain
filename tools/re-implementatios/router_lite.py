'''
Goal (what it must do):
- scan all *.md files under the repo.
- extract local links (ignore http/mailto), including:
--- inline [text](target), autolinks <target>, ref defs [id]: target
--- front-matter links: values that look like canon/...*.md
--- normalize each target to a repo-relative path (forward slashes).
--- drop anchors (#...), self-links, non-.md, and non-existent files.

count inbound refs per target and write tools/router_index.md:
'''

'''
Constraints & knobs:
- works in Git Bash; no rg, no non-stdlib deps.

CLI flags:
--output, --top (default 150), --exclude (glob, repeatable)
--dry-run, --quiet, --verbose
--case-insensitive (fold paths to lowercase before counting)

env: HCR_LOG=DEBUG|INFO|WARN (simple logging gate)
'''

from pathlib import Path
import argparse
import sys, os
import logging
import re
import fnmatch
import collections
import urllib.parse
import datetime


# first, a relatively fool-proof location setup: current_dir = Path.cwd() is mutable, the constants are less.
SCRIPT_PATH = Path(__file__).resolve()
SCRIPT_DIR  = SCRIPT_PATH.parent           # …/repo/tools
REPO_ROOT   = SCRIPT_DIR.parent            # …/repo
CANON_DIR   = REPO_ROOT / "canon"          # …/repo/canon

if not CANON_DIR.is_dir():
    print("No /canon directory found. Please provide ./canon directory for your project")

# first, make a list of the .md files in CANON_DIR
md_files = list(CANON_DIR.rglob("*.md"))

# fix the goddamn slashes (just in case)
for path in md_files:
    fixed_path = path.relative_to(REPO_ROOT).as_posix() 

