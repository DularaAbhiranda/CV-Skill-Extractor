import pytesseract
from PIL import Image

# Configure Pytesseract to know the path of the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    img = Image.open(image_path)
    # Configuring Tesseract to use a specific PSM and OEM
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(img, config=custom_config)
    return text


if __name__ == '__main__':
    # Correctly formatted path using a raw string
    sample_image_path = r'C:\Users\abhir\Desktop\outstanding_11.png'
    extracted_text = extract_text_from_image(sample_image_path)
    print("Extracted Text:")
    print(extracted_text)
