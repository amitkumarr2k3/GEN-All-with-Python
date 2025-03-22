import requests
import glob
import os  # Add this import
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load the pretrained processor and model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Specify the directory where your images are
image_dir = r"C:\Users\z003yujx\Pictures\Chock"
image_exts = ["jpg", "jpeg", "png"]  # specify the image file extensions to search for

# Open a file to write the captions
with open("captions.txt", "w") as caption_file:
    # Iterate over each image file in the directory
    for image_ext in image_exts:
        for img_path in glob.glob(os.path.join(image_dir, f"*.{image_ext}")):
            try:  # Move the try block here
                # Load your image
                raw_image = Image.open(img_path).convert('RGB')
                
                # Process the image
                inputs = processor(raw_image, return_tensors="pt")
                # Generate a caption for the image
                out = model.generate(**inputs, max_new_tokens=50)
                # Decode the generated tokens to text
                caption = processor.decode(out[0], skip_special_tokens=True)

                # Write the caption to the file, prepended by the image URL
                caption_file.write(f"{img_path}: {caption}\n")
            except Exception as e:  # Correct indentation
                print(f"Error processing image {img_path}: {e}")
                continue