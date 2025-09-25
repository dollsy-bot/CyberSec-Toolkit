# Caesar Cipher Program

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Only shift letters
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Keep non-alphabet characters unchanged
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)  # Decryption is just reverse shift

# Main Program
if __name__ == "__main__":
    print("===== Caesar Cipher Program =====")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g., 3): "))

    if choice == 'e':
        encrypted = encrypt(message, shift)
        print(f"\n🔐 Encrypted Message: {encrypted}")
    elif choice == 'd':
        decrypted = decrypt(message, shift)
        print(f"\n🔓 Decrypted Message: {decrypted}")
    else:
        print("Invalid choice. Please select E or D.")

