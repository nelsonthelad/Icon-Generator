from PIL import Image
import os

# Define icon sizes for Chrome extension
icon_sizes = [16, 19, 32, 38, 48, 128]

# Load the base image (should be high-resolution, e.g., 512x512)
base_image_path = "icon.png"
output_folder = "icons"

# Create output directory if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Open the base image
with Image.open(base_image_path) as img:
    for size in icon_sizes:
        resized_img = img.resize((size, size), Image.LANCZOS)
        resized_img.save(os.path.join(output_folder, f"icon{size}.png"))

print(f"Icons saved in '{output_folder}' folder.")

