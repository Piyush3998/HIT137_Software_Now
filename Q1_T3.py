from collections import Counter
import re

def get_top_words(file_path, top_n=30):
    # Open and read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read the entire file content
        text = file.read().lower()
        
    # Use regular expressions to find all words
    words = re.findall(r'\b\w+\b', text)

    # Use Counter to count occurrences of each word
    word_counts = Counter(words)

    # Get the top N most common words
    top_words = word_counts.most_common(top_n)

    return top_words

# Example usage
file_path = r'output.txt'  # Replace with your .txt file path
top_words = get_top_words(file_path)

# Print the top 30 most common words
for word, count in top_words:
    print(f"{word}: {count}")
