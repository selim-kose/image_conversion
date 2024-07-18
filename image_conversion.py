from PIL import Image
import os
import glob

dest_folder = "greyscale"

if not os.path.exists(dest_folder):
    print("Creating folder...")
    os.makedirs(dest_folder)

# Create a list of all the images in the folder
images = glob.glob("images/*.jpg")
print("Images found: ", images)

if not images:
    print("No images found in the 'image' folder.")
    exit()

# Loop through the images
for image in images:
    # Open the image
    img = Image.open(image)
    # Convert the image to grayscale
    print(f"Converting {image} image to grayscale...")
    img = img.convert("L")
    # Save the image with the same name to a folder called "grayscale"
    print("Saving image...")
    img.save(f"{dest_folder}/{os.path.basename(image)}")

