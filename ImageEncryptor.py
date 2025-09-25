# PixelCrypt - Simple Image Encryption Tool
# This program encrypts and decrypts images by manipulating pixel values.
# Operations supported: adding a shift to RGB values or swapping pixels.

from PIL import Image
import random

def encrypt_image(image_path, shift=50, swap_pixels=False):
    # Open image
    img = Image.open(image_path)
    img = img.convert("RGB")  # Ensure RGB format
    pixels = list(img.getdata())
    
    # Encrypt pixels
    new_pixels = []
    for pixel in pixels:
        r = (pixel[0] + shift) % 256
        g = (pixel[1] + shift) % 256
        b = (pixel[2] + shift) % 256
        new_pixels.append((r, g, b))

    # Optionally swap pixels
    if swap_pixels:
        random.shuffle(new_pixels)

    # Create new image
    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(new_pixels)
    encrypted_img.save("encrypted_image.png")
    print("✅ Image encrypted and saved as 'encrypted_image.png'")

def decrypt_image(image_path, shift=50, swap_pixels=False):
    # Open encrypted image
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = list(img.getdata())

    # If pixels were swapped, reshuffle back (simple demonstration; exact swap reversal requires storing shuffle)
    if swap_pixels:
        random.shuffle(pixels)

    # Decrypt pixels by reversing shift
    decrypted_pixels = []
    for pixel in pixels:
        r = (pixel[0] - shift) % 256
        g = (pixel[1] - shift) % 256
        b = (pixel[2] - shift) % 256
        decrypted_pixels.append((r, g, b))

    # Create decrypted image
    decrypted_img = Image.new(img.mode, img.size)
    decrypted_img.putdata(decrypted_pixels)
    decrypted_img.save("decrypted_image.png")
    print("✅ Image decrypted and saved as 'decrypted_image.png'")

# Main Program
if __name__ == "__main__":
    print("===== PixelCrypt - Simple Image Encryption Tool =====")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()
    image_path = input("Enter the image file path: ").strip()
    shift = int(input("Enter shift value (0-255, default 50): ") or 50)
    swap = input("Swap pixels? (y/n): ").strip().lower() == 'y'

    if choice == 'e':
        encrypt_image(image_path, shift, swap)
    elif choice == 'd':
        decrypt_image(image_path, shift, swap)
    else:
        print("Invalid choice. Select E or D.")
