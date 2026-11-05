#!/usr/bin/env python3
"""Rewrite the marked sections of README.md with recent katzenpost releases and blog posts."""
import json
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from pathlib import Path

README = Path(__file__).parent / "README.md"
FEED = "https://katzenpost.network/blog/index.xml"
# shortcut: one page of 100 repos, add pagination if the org grows past that
QUERY = """{organization(login: "katzenpost") {
  repositories(first: 100, privacy: PUBLIC) { nodes { name
    releases(first: 5, orderBy: {field: CREATED_AT, direction: DESC}) {
      nodes { name tagName publishedAt url isDraft isPrerelease } } } } } }"""


def releases(token, n=5):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY}).encode(),
        headers={"Authorization": f"Bearer {token}", "User-Agent": "profile-readme"},
    )
    data = json.load(urllib.request.urlopen(req, timeout=30))
    if "errors" in data:
        sys.exit(f"GraphQL errors: {data['errors']}")
    rels = [
        dict(r, repo=repo["name"])
        for repo in data["data"]["organization"]["repositories"]["nodes"]
        for r in repo["releases"]["nodes"]
        if r["publishedAt"] and not r["isDraft"]
    ]
    rels.sort(key=lambda r: r["publishedAt"], reverse=True)
    return [
        f"- [{r['repo']} {r['tagName']}]({r['url']})"
        + (f" {r['name']}" if r["name"] and r["name"] != r["tagName"] else "")
        + f" - {r['publishedAt'][:10]}"
        for r in rels[:n]
    ]


def posts(n=5):
    with urllib.request.urlopen(FEED, timeout=30) as f:
        root = ET.parse(f).getroot()
    return [
        f"- [{i.findtext('title')}]({i.findtext('link')}) - "
        f"{parsedate_to_datetime(i.findtext('pubDate')).date()}"
        for i in root.iter("item")
    ][:n]


def replace(text, marker, lines):
    pattern = re.compile(rf"(<!-- {marker} starts -->\n).*?(<!-- {marker} ends -->)", re.S)
    if not pattern.search(text):
        sys.exit(f"marker {marker} not found in README.md")
    return pattern.sub(lambda m: m[1] + "\n".join(lines) + "\n" + m[2], text)


if __name__ == "__main__":
    text = README.read_text()
    text = replace(text, "releases", releases(os.environ["GITHUB_TOKEN"]))
    text = replace(text, "blog", posts())
    README.write_text(text)
