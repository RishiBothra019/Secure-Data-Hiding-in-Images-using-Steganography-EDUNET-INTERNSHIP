# Secure Data Hiding in Images using Steganography

## Description
This project implements image-based steganography using Python to hide secret messages within images securely. It provides a simple and efficient method for embedding and extracting text data without noticeable image alterations.

---

## Features
- **Hide and extract text messages from images** using the Least Significant Bit (LSB) technique.
- **Password protection** ensures that only authorized users can decode the message.
- **Special end character (¶)** used to mark the end of the message for accurate extraction.
- **PNG format support** to prevent compression losses and maintain data integrity.

---

## Libraries Used
- **OpenCV:** For image processing.
- **NumPy:** For numerical operations.

---

## Installation
1. Clone the repository or download the project files.
2. Install the required libraries using pip:
   ```bash
   pip install opencv-python numpy
   ```

---

## Usage
### **Encoding a Message:**
Run the `forencrypt.py` script to embed a message:
```bash
python forencrypt.py
```
- Enter the image path, secret message, and a passcode when prompted.
- The encoded image will be saved as `encryptedimage.png`.

### **Decoding a Message:**
Run the `fordecrypt.py` script to extract the hidden message:
```bash
python fordecrypt.py
```
- Provide the path to the encoded image and the correct passcode to retrieve the message.

---

## Project Structure
- `forencrypt.py`: Script for encoding messages into images.
- `fordecrypt.py`: Script for decoding hidden messages from images.
- `password.txt`: Stores the passcode temporarily.

---

## Future Scope
- Integration of advanced encryption algorithms like AES/RSA.
- Support for additional file formats (audio, video).
- Improved GUI using Tkinter or Streamlit.
- Cloud-based and mobile app versions.

---

## Author
Developed by Rishi Bothra

---

## License
This project is open-source 

