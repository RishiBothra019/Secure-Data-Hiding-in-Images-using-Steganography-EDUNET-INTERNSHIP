import cv2
import numpy as np

def decode_message(image_path):
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Encrypted image not found!")
        return
    
    # Read stored password
    try:
        with open("password.txt", "r") as f:
            stored_password = f.readline().strip()
    except FileNotFoundError:
        print("Error: Password file not found!")
        return

    entered_password = input("Enter passcode for decryption: ")
    
    if stored_password != entered_password:
        print("YOU ARE NOT AUTHORIZED!")
        return

    flat_img = img.flatten()

    # Retrieve message length from first 4 pixels
    msg_length = (flat_img[3] << 24) | (flat_img[2] << 16) | (flat_img[1] << 8) | flat_img[0]

    decoded_message = "".join(chr(flat_img[i + 4]) for i in range(msg_length))

    # Stop at special character
    decoded_message = decoded_message.split("¶")[0]
    
    print("Decrypted message:", decoded_message)

# --- Run Decoding ---
encrypted_image_path = "encryptedimage.png"
decode_message(encrypted_image_path)
