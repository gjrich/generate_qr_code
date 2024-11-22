# generate_qr_code
A QR code generating script.


# Gabriel Richards
# Nov 2024

Generated with assistance from Claude.ai / Anthropic
https://claude.ai

Pass a URL and the file name you want to output

must first install the qrcode python package via pip, e.g.

pip install qrcode[pil]

Example use of script from Powershell

python -c "from generate_qr_code import generate_qr_code; generate_qr_code('https://www.example.com', 'example_QR.png')"
