import cv2
import os

# Load the image
img_path = "image.jpg"
if not os.path.exists(img_path):
    print(f"Error: The file '{img_path}' does not exist.")
    exit()

img = cv2.imread(img_path)
if img is None:
    print(f"Error: Unable to load image '{img_path}'.")
    exit()

# Define the message and password
msg = "Sunflower"
password = "123456"

# Create mapping between characters and their ASCII values
d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

# Initialize indices
m = 0
n = 0
z = 0

# Encrypt the message
height, width, _ = img.shape
if len(msg) > height * width * 3:
    print("Error: Message is too long to fit in the image.")
    exit()

for i in range(len(msg)):
    if n >= height or m >= width:
        print("Error: Message exceeds image dimensions.")
        break
    
    # Embed the ASCII value of the character into the image
    img[n, m, z] = d[msg[i]]
    print(f"Writing pixel value: {d[msg[i]]} at ({n}, {m}, {z})")
    
    # Update indices
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

# Save the encrypted image in a lossless format
cv2.imwrite("encryptedImage.png", img)
print("Encryption complete. Encrypted image saved as 'encryptedImage.png'.")