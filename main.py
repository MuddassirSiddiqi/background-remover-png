from rembg import remove
from PIL import Image

input_path = input("Enter the path to your input PNG file: ")
output_path = input("Enter the path to save the output PNG file: ")

input_image = Image.open(input_path)
output_image = remove(input_image)
output_image.save(output_path)

print("Background removed and image saved to:", output_path)