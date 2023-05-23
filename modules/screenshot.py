import os
import base64

def run(**args):
    curr_dir = os.getcwd()
    file_name = "screenshot.ppm"

    file_path = os.path.join(curr_dir, file_name)

    with open(file_path, 'rb') as file:
        file_content = file.read()

    encoded_content = base64.b64encode(file_content).decode('utf-8')
    return(encoded_content)