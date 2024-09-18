from collections import Counter
import string
import re

# Define a function to decrypt the Caesar cipher with a given shift
def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():  # Only decrypt alphabetic characters
            shift_amount = shift % 26
            ascii_offset = 65 if char.isupper() else 97
            new_char = chr((ord(char) - ascii_offset - shift_amount) % 26 + ascii_offset)
            decrypted_text += new_char
        else:
            decrypted_text += char  # Keep spaces and punctuation as is
    return decrypted_text

# Function to score the English-like quality of a text
def score_english(text):
    # Common English letter frequencies (approximation)
    english_freq_order = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    counter = Counter(text.upper())  # Count letter frequencies
    score = 0
    for letter, count in counter.items():
        if letter in english_freq_order:
            # Higher score for more common letters
            score += (26 - english_freq_order.index(letter)) * count
    return score

# Function to clean and format the text using regex for better word identification
def clean_text(text):
    # Remove extra spaces and properly capitalize sentences
    text = re.sub(r' +', ' ', text)  # Remove multiple spaces
    words = text.split()  # Split into words
    corrected_text = ' '.join(words)  # Join words with a single space
    corrected_text = corrected_text.capitalize()  # Capitalize the first letter
    return corrected_text

# Main function to decrypt and choose the best result
def decrypt_caesar_cipher(ciphertext):
    best_decryption = ""
    highest_score = 0
    
    # Try all possible shifts from 1 to 25
    for shift in range(1, 26):
        decrypted_text = caesar_decrypt(ciphertext, shift)
        score = score_english(decrypted_text)
        if score > highest_score:
            highest_score = score
            best_decryption = decrypted_text
    
    # Clean up the best decryption
    formatted_result = clean_text(best_decryption)
    return formatted_result

# Example usage
ciphertext = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFPRHER V ZNXRF ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAQ QRFRER ZR NG ZL ORFG ZNEVYLA ZBAEBR"
decrypted_message = decrypt_caesar_cipher(ciphertext)
print("Decrypted and formatted message:")
print(decrypted_message)
