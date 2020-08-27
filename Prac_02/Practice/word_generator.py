"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random
import string

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
VOWEL_PLACEHOLDERS = "!@#$%^"
CONSONANT_PLACEHOLDERS = "&*()_-+={}[]|\\:;',.<>?/"

# word_format = "ccvcvvc"
word_format = input("Provide word format ").lower()

word = ""
for kind in word_format:
    if kind in CONSONANT_PLACEHOLDERS:
        word += random.choice(CONSONANTS)
    elif kind in VOWEL_PLACEHOLDERS:
        word += random.choice(VOWELS)
    elif kind in string.ascii_lowercase:
        word += kind

print(word)
