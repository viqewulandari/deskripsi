def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

ciphertext = "Elly Hertita"
shift_value = 2
decrypted_text = caesar_decrypt(ciphertext, shift_value)
print("Ciphertext:", ciphertext)
print("Shift Value:", shift_value)
print("Decrypted Text:", decrypted_text)
