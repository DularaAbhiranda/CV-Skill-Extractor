import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from pdfminer.high_level import extract_text
import traceback

# Function to preprocess image-based CVs
def preprocess_image_cv(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (600, 800), interpolation=cv2.INTER_AREA)
    normalized = cv2.normalize(resized, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    return normalized

# Function to convert PDF CVs to text
def pdf_to_text(pdf_path):
    return extract_text(pdf_path)

# Function to display an image (for testing)
def display_image(image):
    plt.imshow(image, cmap='gray')
    plt.show()

# Function to process a directory containing PDFs and images
def process_cv_directory(directory_path):
    try:
        for root, dirs, files in os.walk(directory_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                if filename.endswith('.pdf'):
                    # Process each PDF file
                    text = pdf_to_text(file_path)
                    print(f"Processed {filename}:")
                    print(text[:500])  # Print first 500 characters of the extracted text
                elif filename.endswith('.jpg') or filename.endswith('.png'):
                    # Process each image file
                    processed_image = preprocess_image_cv(file_path)
                    display_image(processed_image)
    except Exception as e:
        print("Failed to process directory:", e)
        traceback.print_exc()

# Main function call
if __name__ == '__main__':
    directory_path = r'C:\Users\abhir\Desktop\ResumeAnalyzer\dataset\data\data'
    process_cv_directory(directory_path)
