#!/usr/bin/env python3
"""qrify – generate a QR code PNG from a supplied text string.

Usage:
    python qrify.py "Some text"          # saves as qr.png
    python qrify.py "Some text" -o out.png
"""

import argparse
import sys

try:
    import qrcode
except ImportError:  # pragma: no cover
    sys.stderr.write("error: the 'qrcode' package is required. Install it with:\n"
                     "    python -m pip install qrcode[pil]\n")
    sys.exit(1)

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate a QR code PNG from the provided text.")
    parser.add_argument("text", help="The text string to encode into a QR code.")
    parser.add_argument("-o", "--output", default="qr.png",
                        help="Output filename for the PNG image (default: qr.png).")
    return parser

def main() -> None:
    args = build_parser().parse_args()
    img = qrcode.make(args.text)
    img.save(args.output)
    print(f"QR code saved to {args.output}")

if __name__ == "__main__":
    main()
