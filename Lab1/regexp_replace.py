import re

def replace_words_in_file(file_path, replacements):
    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Create a regular expression pattern
    for old_word, new_word in replacements.items():
        # relace whole words only
        pattern = r'\b' + re.escape(old_word) + r'\b'
        content = re.sub(pattern, new_word, content)

    # Write the contents back
    with open(file_path, 'w') as file:
        file.write(content)

replacements = {
    "Dzień dobry": "Witam",
    "kawusi": "rozgrzewającego napoju bezkofeinowego"
}

file_path = 'zamiana_tekstu.txt'
replace_words_in_file(file_path, replacements)
