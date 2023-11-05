from PIL import Image
import numpy as np

# class Byteplot:  
def create_byteplot_image(file_path):
    IMAGE_WIDTH = 192
    IMAGE_HEIGHT = 192
    with open(file_path, "rb") as f: data = f.read()
    byte_vector = np.array(list(data), dtype=np.uint8)
    byte_vector = (byte_vector - np.mean(byte_vector)) / np.std(byte_vector)
    height = int(np.ceil(len(byte_vector) / 512))
    byte_matrix = np.zeros((height, 512), dtype=np.uint8)
    byte_matrix_flat = byte_matrix.flatten()
    byte_matrix_flat[:len(byte_vector)] = byte_vector
    byte_matrix = byte_matrix_flat.reshape((height, 512))
    byte_matrix = (255 - byte_matrix * 255).astype(np.uint8)
    image = Image.fromarray(byte_matrix)
    image = image.resize((IMAGE_WIDTH, IMAGE_HEIGHT))
    # image.save(file_path+'.test.png')
    return image


# def create_byteplot_image(file_path):
#     # Read the file data
#     with open(file_path, "rb") as f:
#         data = f.read()

#     # Convert the data to an 8-bit vector
#     byte_vector = np.array(list(data), dtype=np.uint8)

#     # Normalize the byte vector
#     byte_vector = (byte_vector - np.mean(byte_vector)) / np.std(byte_vector)

#     # Calculate the height of the image
#     height = int(np.ceil(len(byte_vector) / 512))

#     # Reshape the byte vector into a matrix with 255 columns and variable number of rows
#     byte_matrix = np.zeros((height, 512), dtype=np.uint8)
#     byte_matrix_flat = byte_matrix.flatten()
#     byte_matrix_flat[:len(byte_vector)] = byte_vector
#     byte_matrix = byte_matrix_flat.reshape((height, 512))

#     # Map pixel values to [0, 255] and invert
#     byte_matrix = (255 - byte_matrix * 255).astype(np.uint8)

#     # Create the image with original dimensions
#     image = Image.fromarray(byte_matrix)
#     return image


