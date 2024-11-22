# Gabriel Richards
# Nov 2024

# Generated with assistance from Claude.ai / Anthropic
# https://claude.ai

# Pass a URL and the file name you want to output

# must first install the qrcode python package via pip, e.g.

# pip install qrcode[pil]

# Example use of script from Powershell

# python -c "from generate_qr_code import generate_qr_code; generate_qr_code('https://www.example.com', 'example_QR.png')"

import qrcode

def generate_qr_code(url, filename='qr_code.png'):
    """
    Generate a QR code for any given URL
    
    :param url: Full URL to create QR code for
    :param filename: Output filename for the QR code image
    """
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add the URL data
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image from the QR code
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    qr_image.save(filename)
    print(f"QR code saved as {filename} for URL: {url}")

# Example usage
# generate_qr_code('https://example.com', 'example_qr.png')