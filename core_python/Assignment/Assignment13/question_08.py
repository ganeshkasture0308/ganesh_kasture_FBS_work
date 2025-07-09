# 8. Python Program to Count the Frequency of Words Appearing in a String Using
# a Dictionary
text = "this is a test this is only a test"
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)
