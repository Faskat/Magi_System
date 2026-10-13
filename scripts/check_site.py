"""Check local HTML resources without network access or script execution."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re

ROOT = Path(__file__).resolve().parents[1]


class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if value and name in {"src", "href", "poster"}:
                self.urls.append(value)


def check(root=ROOT):
    page = root / "index.html"
    raw = page.read_bytes()
    text = raw.decode("utf-16" if raw[:2] in {b"\xff\xfe", b"\xfe\xff"} else "utf-8-sig")
    if "<!doctype html" not in text.lower():
        raise ValueError("Missing HTML doctype")
    parser = References()
    parser.feed(text)
    urls = parser.urls + re.findall(r"url\(\s*['\"]?([^'\")]+)['\"]?\s*\)", text)
    checked = 0
    for url in urls:
        ref = urlsplit(url.strip())
        if ref.scheme or ref.netloc or not ref.path:
            continue
        target = (root / unquote(ref.path).lstrip("/")).resolve()
        if not target.is_relative_to(root.resolve()) or not target.is_file():
            raise ValueError(f"Missing or out-of-root local resource: {url}")
        checked += 1
    print(f"HTML loaded; {checked} local resource references exist")


if __name__ == "__main__":
    check()
