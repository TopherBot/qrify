# qrify

**qrify** is a one‑file Python utility that generates a QR code PNG from a string you provide on the command line.

## Features
- Single script, no external configuration.
- Works on Windows, macOS, Linux.
- Uses the popular `qrcode` library for reliable QR generation.

## Installation
```bash
# Install the tiny dependency (only once)
python -m pip install qrcode[pil]
```

Copy `qrify.py` to a directory in your `PATH` or run it directly with `python`.

## Usage
```bash
# Basic usage – output to qr.png
python qrify.py "Hello, world!"

# Specify an output filename
python qrify.py "https://example.com" -o example.png
```

## Help
```bash
python qrify.py -h
```

```
usage: qrify.py [-h] [-o OUTPUT] text

Generate a QR code PNG from the provided text.

positional arguments:
  text                The text string to encode into a QR code.

optional arguments:
  -h, --help          show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output filename for the PNG image (default: qr.png).
```

## License
MIT – see the `LICENSE` file.
