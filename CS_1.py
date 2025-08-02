def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (integer): "))

    encrypted_message = caesar_encrypt(message, shift)
    print("Encrypted message:", encrypted_message)

    decrypted_message = caesar_decrypt(encrypted_message, shift)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()