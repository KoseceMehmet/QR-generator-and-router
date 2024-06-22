import qrcode #QR code library

# some data
data = "https://www.google.com"

# Create a QRCode object
qr = qrcode.QRCode(
    version=1,  # Version parameter (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction levels: L, M, Q, H
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Generate the QR code as an image object
img = qr.make_image(fill='black', back_color='white')

# Save the image to a file
img.save("QR.png")

