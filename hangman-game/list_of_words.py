from english_words import get_english_words_set

# Retrieve the set of English words
english_words = get_english_words_set(['web2'], lower=True)

# Define a list of common computer-related keywords
computer_keywords = ['computer', 'network', 'data', 'software', 'hardware', 'program', 'code', 'algorithm', 'database', 'internet']

# Filter words that contain any of the computer-related keywords
computer_terms = [word for word in english_words if any(keyword in word for keyword in computer_keywords)]

# Display the first 100 computer-related terms
words_list = computer_terms[:100]
# print(words_list)
