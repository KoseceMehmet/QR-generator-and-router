import cv2  #image processing
from pyzbar import pyzbar  #To read QR codes and barcodes
import webbrowser
import os

def decode_qr_code(image):
    # Detect and decode QR codes
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        # Get the content of the QR code
        qr_data = obj.data.decode('utf-8')
        print("QR Code content:", qr_data)
        return qr_data
    return None

# Upload the image file containing the QR code
image_path = "QR.png"


# Check if the file exists
if not os.path.exists(image_path):
    print(f"File not found: {image_path}")
else:
    image = cv2.imread(image_path)

    # Make sure the image is loaded correctly
    if image is None:
        print(f"Failed to load file: {image_path}")
    else:
        # Decode QR code
        qr_data = decode_qr_code(image)

        
        # Open the URL found in the QR code
        if qr_data:
            webbrowser.open(qr_data)
        else:
            print("QR code could not be read.")
