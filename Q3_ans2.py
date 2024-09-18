#Decrypt the Encrypted Code:

def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():  # Check if character is a letter
            shifted = ord(char) - key  # Shift back by the key
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26  # Wrap around if lower than 'a'
                elif shifted > ord('z'):
                    shifted -= 26  # Wrap around if greater than 'z'
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26  # Wrap around if lower than 'A'
                elif shifted > ord('Z'):
                    shifted -= 26  # Wrap around if greater than 'Z'
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char  # Non-alphabetic characters are unchanged
    return decrypted_text

# Encrypted code from the question (replace with the actual encrypted string)
encrypted_code = "tybony_inevoyr = 100\nzl_qvpg... (full encrypted code)"
key = 13
decrypted_code = decrypt(encrypted_code, key)
print(decrypted_code)
