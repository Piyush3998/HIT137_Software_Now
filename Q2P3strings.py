# Input string (example provided in the question)
s = '56aAww1984sktr235270aYnm145ss785fsq31D0'

# Separate the string into number and letter substrings
number_string = ''.join([char for char in s if char.isdigit()])
letter_string = ''.join([char for char in s if char.isalpha()])

# Convert even numbers in the number string to ASCII Code Decimal Values
even_numbers_ascii = [ord(char) for char in number_string if char.isdigit() and int(char) % 2 == 0]

# Convert upper-case letters in the letter string to ASCII Code Decimal Values
uppercase_letters_ascii = [ord(char) for char in letter_string if char.isupper()]

# Output the results
print("Number String:", number_string)
print("Even Numbers in ASCII Code:", even_numbers_ascii)
print("Letter String:", letter_string)
print("Upper-case Letters in ASCII Code:", uppercase_letters_ascii)
