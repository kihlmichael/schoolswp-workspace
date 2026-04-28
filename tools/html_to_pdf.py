"""Convert an HTML file to PDF via Playwright Chromium.

Usage: .venv/Scripts/python tools/html_to_pdf.py <input.html> <output.pdf>
"""

from __future__ import annotations

import asyncio
import sys
from pathlib import Path

from playwright.async_api import async_playwright


async def convert(html_path: Path, pdf_path: Path) -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(html_path.resolve().as_uri(), wait_until="load")
        await page.pdf(
            path=str(pdf_path),
            format="A4",
            margin={"top": "15mm", "right": "15mm", "bottom": "20mm", "left": "15mm"},
            print_background=True,
        )
        await browser.close()


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: html_to_pdf.py <input.html> <output.pdf>", file=sys.stderr)
        return 1
    html_path = Path(sys.argv[1])
    pdf_path = Path(sys.argv[2])
    if not html_path.exists():
        print(f"HTML not found: {html_path}", file=sys.stderr)
        return 1
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    asyncio.run(convert(html_path, pdf_path))
    size_kb = pdf_path.stat().st_size // 1024
    print(f"OK {pdf_path} ({size_kb} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
