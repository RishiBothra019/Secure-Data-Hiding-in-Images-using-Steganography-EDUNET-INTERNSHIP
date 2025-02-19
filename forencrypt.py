import cv2
import numpy as np

def encode_message(image_path, output_path, message, password):
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Image not found or could not be loaded!")
        return
    
    message += "¶"  # Special end character
    msg_length = len(message)

    # Convert characters to ASCII values
    ascii_values = [ord(char) for char in message]

    height, width, _ = img.shape
    total_pixels = height * width * 3  # Total available storage

    if msg_length > total_pixels:
        print("Error: Message is too long for this image!")
        return

    # Flatten image for easy manipulation
    flat_img = img.flatten()

    # Store message length in the first 4 pixels
    flat_img[:4] = [msg_length & 255, (msg_length >> 8) & 255, (msg_length >> 16) & 255, (msg_length >> 24) & 255]

    # Encode the message into the image
    for i, ascii_val in enumerate(ascii_values):
        flat_img[i + 4] = ascii_val  # Start storing after first 4 pixels

    # Reshape back to original image shape
    img_encoded = flat_img.reshape(height, width, 3).astype(np.uint8)

    # Save as PNG to prevent compression issues
    cv2.imwrite(output_path, img_encoded)
    print("Message encoded successfully!")

    # Store password in a text file
    with open("password.txt", "w") as f:
        f.write(password)

# --- Run Encoding ---
image_path = "D:\mypic.jpeg"  # Use PNG format
output_path = "encryptedimage.png"
message = input("Enter secret message: ")
password = input("Enter a passcode: ")

encode_message(image_path, output_path, message, password)
