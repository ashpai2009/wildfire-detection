from PIL import Image
import os
def convert_resolution(image_path, new_width, new_height, output_path):
    try:
        image = Image.open(image_path)
        resized_image = image.resize((new_width, new_height))
        resized_image.save(output_path)
        return True
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return False
    except Exception as e:
         print(f"An error occurred: {e}")
         return False

# Example usage:
new_width = 128
new_height = 128

WILDFIRE_TEST_DIRECTORY = '/Users/ashmit/Documents/code/Projects/wildfire-detection/data/test/not_wildfire'
WILDFIRE_TEST_DIRECTORY_LOW = '/Users/ashmit/Documents/code/Projects/wildfire-detection/data/test/not_wildfire_low'

for i in os.listdir(WILDFIRE_TEST_DIRECTORY):
    image_path = f'{WILDFIRE_TEST_DIRECTORY}/{i}'
    output_path = f'{WILDFIRE_TEST_DIRECTORY_LOW}/{i}'
    convert_resolution(image_path, new_width, new_height, output_path)