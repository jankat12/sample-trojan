import os
import base64
from PIL import Image

def run(**args):
    curr_dir = os.getcwd()
    file_name = "screenshot.ppm"

    ppm_file_path = os.path.join(curr_dir, file_name)

    png_file_name = 'output.png'
    png_file_path = os.path.join(curr_dir, png_file_name)
    
    with open(ppm_file_path, 'rb') as ppm_file:
        ppm_image = Image.open(ppm_file)

        # Convert the image to RGB mode (if it's not already in RGB)
        if ppm_image.mode != 'RGB':
            ppm_image = ppm_image.convert('RGB')

        # Save the image as PNG
        ppm_image.save(png_file_path, format='PNG')

    print(f"Conversion complete: {png_file_path}")

    with open(png_file_path, 'rb') as file:
        file_content = file.read()

    encoded_content = base64.b64encode(file_content).decode('utf-8')
    return encoded_content