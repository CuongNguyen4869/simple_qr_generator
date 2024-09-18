import qrcode
import tkinter as tk
from tkinter import simpledialog
from PIL import Image

# Create the main application window
root = tk.Tk()
root.withdraw()  # Hide the main window, we only want the dialogs
# # root.iconify()

# Configure the font size for input dialogs
root.option_add("*Font", "Helvetica 20")  # Set the default font size to be larger

# Prompt the user to enter the URL
url = simpledialog.askstring("Input", "Enter the URL to generate the QR code:")

if url is None:
    exit()

# Prompt the user to enter the file name
file_name = simpledialog.askstring("Input", "Enter the name of the image file (without .png extension):")

if file_name is None:
    exit()

# Append the .png extension to the file name
file_name = file_name + ".png"

# Generate the QR code
my_qr = qrcode.make(url)

# Save the QR code as an image file
my_qr.save(file_name)

# Open the image using PIL
img = Image.open(file_name)
img.show()
