import cv2
import os

# Load the encrypted image
img_path = "encryptedImage.png"
if not os.path.exists(img_path):
    print(f"Error: The file '{img_path}' does not exist.")
    exit()

img = cv2.imread(img_path)
if img is None:
    print(f"Error: Unable to load image '{img_path}'.")
    exit()

# Create mapping between characters and their ASCII values
d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

# Password verification
while True:
    pas = input("Enter passcode for Decryption: ")
    password = input("Re-enter the original passcode: ")
    if password == pas:
        break
    else:
        print("Passcodes do not match. Please try again.")

# Get the length of the original message
try:
    msg_length = int(input("Enter the length of the original message: "))
except ValueError:
    print("Invalid input for message length. Please enter an integer.")
    exit()

# Decrypt the message
message = ""
n = 0
m = 0
z = 0

height, width, _ = img.shape
if msg_length > height * width * 3:
    print("Error: Message length exceeds the capacity of the image.")
    exit()

for i in range(msg_length):
    if n >= height or m >= width:
        print("Error: Message length exceeds image dimensions.")
        break
    
    # Extract the character from the image
    message += c[img[n, m, z]]
    print(f"Read pixel value: {img[n, m, z]} at ({n}, {m}, {z})")
    
    # Update indices
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

print("Decrypted message:", message)