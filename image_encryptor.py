from PIL import Image

# Encryption function
def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b, a = pixels[x, y]

            # Modify pixel values
            pixels[x, y] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256,
                (a + key) % 256
            )

    encrypted_path = "encrypted_image.png"
    img.save(encrypted_path)

    print("Encrypted image saved as:", encrypted_path)


# Decryption function
def decrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b, a = pixels[x, y]

            # Reverse modification
            pixels[x, y] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256,
                (a - key) % 256
            )

    decrypted_path = "decrypted_image.png"
    img.save(decrypted_path)

    print("Decrypted image saved as:", decrypted_path)


print("=== Image Encryption Tool ===")

choice = input("Type 'e' for encryption or 'd' for decryption: ")
image_path = input("Enter image file path: ")
key = int(input("Enter encryption key: "))

if choice == 'e':
    encrypt_image(image_path, key)

elif choice == 'd':
    decrypt_image(image_path, key)

else:
    print("Invalid choice.")