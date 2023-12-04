from PIL import Image

# Replace 'path_to_image.jpg' with the path to your image file
image_path = 'src/datasets/examples/5.jpg'

# Open the image file using PIL (Python Imaging Library)
with Image.open(image_path) as img:
    # Get the size of the image
    width, height = img.size

print(f"Width: {width}, Height: {height}")

# # Replace 'path_to_image.jpg' with the path to your image file
# image_path = 'src/data/celeba_hq/train/male/000016.jpg'  # Path to your original image
# resized_image_path = 'src/datasets/celeba_hq/5.jpg'  # Path to save the resized image

# # Open the image file using PIL (Python Imaging Library)
# with Image.open(image_path) as img:
#     # Resize the image
#     resized_img = img.resize((256, 256))

#     # Save the resized image
#     resized_img.save(resized_image_path)

# print(f"Resized image saved to {resized_image_path}")