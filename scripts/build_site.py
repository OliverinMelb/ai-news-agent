"""Build a static website from data/summaries/*.md into site/.

Usage: python scripts/build_site.py
Output: site/index.html (latest day) + site/<YYYY-MM-DD>.html (archive)
"""

import re
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parents[1]
SUMMARIES_DIR = ROOT / "data" / "summaries"
OUT_DIR = ROOT / "site"

FILE_RE = re.compile(r"horizon-(\d{4}-\d{2}-\d{2})-zh\.md$")

PAGE_TEMPLATE = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Horizon 每日速递 · {date}</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🌅</text></svg>">
<style>
:root {{
  --bg: #faf9f7;
  --fg: #1f2328;
  --muted: #6a6f76;
  --accent: #0969da;
  --card: #ffffff;
  --border: #e4e2dd;
  --code-bg: #eceae5;
}}
@media (prefers-color-scheme: dark) {{
  :root {{
    --bg: #16181d;
    --fg: #e2e5e9;
    --muted: #9aa1ab;
    --accent: #58a6ff;
    --card: #1d2026;
    --border: #2c3038;
    --code-bg: #262a32;
  }}
}}
* {{ box-sizing: border-box; }}
body {{
  margin: 0;
  background: var(--bg);
  color: var(--fg);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC",
    "Microsoft YaHei", sans-serif;
  line-height: 1.75;
}}
.wrap {{ max-width: 760px; margin: 0 auto; padding: 24px 20px 80px; }}
header.site {{
  display: flex; align-items: baseline; justify-content: space-between;
  gap: 12px; flex-wrap: wrap;
  padding-bottom: 16px; border-bottom: 1px solid var(--border); margin-bottom: 8px;
}}
header.site .brand {{ font-size: 20px; font-weight: 700; }}
header.site .brand a {{ color: var(--fg); text-decoration: none; }}
nav.dates {{ display: flex; align-items: center; gap: 10px; font-size: 14px; }}
nav.dates a {{ color: var(--accent); text-decoration: none; }}
nav.dates a.disabled {{ color: var(--muted); pointer-events: none; }}
nav.dates select {{
  background: var(--card); color: var(--fg); border: 1px solid var(--border);
  border-radius: 6px; padding: 4px 8px; font-size: 14px;
}}
main h1 {{ font-size: 26px; line-height: 1.4; }}
main h2 {{
  font-size: 20px; line-height: 1.5; margin-top: 2.2em;
  padding-top: 1.2em; border-top: 1px solid var(--border);
}}
main h2 a {{ color: var(--fg); text-decoration: none; }}
main h2 a:hover {{ color: var(--accent); }}
main a {{ color: var(--accent); }}
main blockquote {{
  margin: 1em 0; padding: 2px 16px; color: var(--muted);
  border-left: 3px solid var(--accent); background: var(--card); border-radius: 0 8px 8px 0;
}}
main hr {{ border: none; border-top: 0; margin: 0; }}
main code {{
  background: var(--code-bg); border-radius: 4px; padding: 1px 5px;
  font-family: ui-monospace, "Cascadia Code", Consolas, monospace; font-size: 0.9em;
}}
main details {{
  background: var(--card); border: 1px solid var(--border);
  border-radius: 8px; padding: 8px 14px; margin: 10px 0;
}}
main details summary {{ cursor: pointer; color: var(--muted); font-size: 14px; }}
main details ul {{ margin: 8px 0; padding-left: 20px; font-size: 14px; }}
main ol {{ padding-left: 24px; }}
main img {{ max-width: 100%; }}
footer.site {{
  margin-top: 60px; padding-top: 16px; border-top: 1px solid var(--border);
  color: var(--muted); font-size: 13px;
}}
</style>
</head>
<body>
<div class="wrap">
<header class="site">
  <div class="brand"><a href="index.html">🌅 Horizon 每日速递</a></div>
  <nav class="dates">
    {prev_link}
    <select onchange="if(this.value)location.href=this.value">
      {date_options}
    </select>
    {next_link}
  </nav>
</header>
<main>
{content}
</main>
<footer class="site">由 Horizon 自动生成 · AI 筛选打分 · 每日更新</footer>
</div>
</body>
</html>
"""


def collect_summaries() -> list[tuple[str, Path]]:
    """Return (date, path) pairs sorted newest first."""
    found = []
    for path in SUMMARIES_DIR.glob("horizon-*-zh.md"):
        match = FILE_RE.search(path.name)
        if match:
            found.append((match.group(1), path))
    return sorted(found, key=lambda pair: pair[0], reverse=True)


def render_page(date: str, md_text: str, dates: list[str], out_name: str) -> str:
    body = markdown.markdown(md_text, extensions=["extra", "sane_lists"])

    idx = dates.index(date)
    older = dates[idx + 1] if idx + 1 < len(dates) else None
    newer = dates[idx - 1] if idx > 0 else None
    prev_link = (
        f'<a href="{older}.html">← 前一天</a>' if older else '<a class="disabled">← 前一天</a>'
    )
    if newer:
        newer_href = "index.html" if newer == dates[0] else f"{newer}.html"
        next_link = f'<a href="{newer_href}">后一天 →</a>'
    else:
        next_link = '<a class="disabled">后一天 →</a>'

    options = []
    for d in dates:
        href = "index.html" if d == dates[0] else f"{d}.html"
        selected = " selected" if d == date else ""
        options.append(f'<option value="{href}"{selected}>{d}</option>')

    return PAGE_TEMPLATE.format(
        date=date,
        content=body,
        prev_link=prev_link,
        next_link=next_link,
        date_options="\n      ".join(options),
    )


def main() -> int:
    summaries = collect_summaries()
    if not summaries:
        print("No summaries found in", SUMMARIES_DIR)
        return 1

    OUT_DIR.mkdir(exist_ok=True)
    dates = [d for d, _ in summaries]

    for date, path in summaries:
        md_text = path.read_text(encoding="utf-8")
        html_page = render_page(date, md_text, dates, f"{date}.html")
        (OUT_DIR / f"{date}.html").write_text(html_page, encoding="utf-8")

    # Latest day doubles as the homepage
    latest_date, latest_path = summaries[0]
    html_page = render_page(latest_date, latest_path.read_text(encoding="utf-8"), dates, "index.html")
    (OUT_DIR / "index.html").write_text(html_page, encoding="utf-8")

    print(f"Built {len(summaries)} page(s) into {OUT_DIR} (latest: {latest_date})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
