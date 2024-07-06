### Import Necessary Libraries ###

import pytesseract
from PIL import Image
import re
import matplotlib.pyplot as plt

# Configure the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

### Functions for OCR and Skill Extraction ###

## Implement a function to extract text using OCR ##
def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print(f"Failed to process image: {e}")
        return ""

## Implement a function to find skills in the extracted text ##
def extract_skills(text):
    skills = ['Python', 'Java', 'Project Management', 'AutoCAD']
    found_skills = {skill: bool(re.search(skill, text, re.IGNORECASE)) for skill in skills}
    return found_skills

### Visualization ###

def plot_skills(skills):
    found_skills = {skill: found for skill, found in skills.items() if found}
    if found_skills:  # Check if there are any skills found
        plt.bar(found_skills.keys(), [1 if val else 0 for val in found_skills.values()])
        plt.xlabel('Skills')
        plt.ylabel('Presence')
        plt.title('Detected Skills in CV')
        plt.show()
    else:
        print("No skills found to plot.")

### Test the Entire Workflow ###

if __name__ == '__main__':
    sample_image_path = r'C:\Users\abhir\Desktop\modern_resume_template_word_free.jpg'  # Update this path as needed
    extracted_text = extract_text_from_image(sample_image_path)
    if extracted_text:
        print("Extracted Text:")
        print(extracted_text)
        detected_skills = extract_skills(extracted_text)
        print("Detected Skills:")
        for skill, present in detected_skills.items():
            if present:
                print(skill)
        plot_skills(detected_skills)
    else:
        print("No text extracted from image.")

