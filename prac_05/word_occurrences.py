"""
Word Occurrences
Estimate: 20 minutes
Actual:   40 minutes
"""
text = input("Text: ")
count_words = {}
words = text.split()
for word in words:
    frequency = count_words.get(word, 0)
    count_words[word] = frequency + 1

words = list(count_words.keys())
words.sort()

max_length = max(len(word) for word in count_words.keys())
for word in sorted(count_words.keys()):
    print(f"{word:{max_length}} : {count_words[word]}")
