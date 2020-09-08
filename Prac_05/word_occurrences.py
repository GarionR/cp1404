text = input("Text: ")
words = text.split(" ")
word_to_count = {}
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
longest_word = ""
for word in word_to_count:
    if len(word) > len(longest_word):
        longest_word = word

for word in word_to_count:
    print("{:{}} : {}".format(word, len(longest_word), word_to_count[word]))
