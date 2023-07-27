# Checks if the last letter of word1 is equal to the first letter of word2, disregarding case sensitivity
def is_chainable(word1, word2):
    return word1[-1].lower() == word2[0].lower()


# Recursevely find the longest chain of words starting from given word
def find_longest_chain(word, words_set):
    # If the word is not present in the set or contain non-alphabetic characters
    if word not in words_set or not word.isalpha():
        return 0

    # Remove current word from the set to avoid visiting it again
    words_set.remove(word)
    max_chain = 0

    # Copy to avoid changing the original set during iteration
    for next_word in words_set.copy():
        # If current word can form a chain with the next, recursively finds the next word
        if is_chainable(word, next_word):
            chain_length = 1 + find_longest_chain(next_word, words_set)
            # Updates max chain length
            max_chain = max(max_chain, chain_length)

    # Restore the word back to the set
    words_set.add(word)
    return max_chain


def word_chain(words):
    # Checks if input list contains at least 2 words to form a chain
    if len(words) < 2:
        raise ValueError(
            "The input list must contain at least two words to form a chain."
        )

    max_chain = 0
    words_set = set(words)

    # Iterate through each word in the set to find max chain length starting from that word
    for word in words:
        chain_length = 1 + find_longest_chain(word, words_set)
        max_chain = max(max_chain, chain_length)

    return max_chain


# Example usage:
words = [
    "area",
    "aeroplane",
    "apple",
    "elephant",
    "eel",
    "land",
    "dog",
    "goat",
]
try:
    result = word_chain(words)
    print(result)
except ValueError as e:
    print("Error:", e)
