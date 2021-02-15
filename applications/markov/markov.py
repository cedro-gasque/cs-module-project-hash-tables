import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read().split()

# TODO: analyze which words can follow other words
# Your code here
markov = dict()
startwords = set()
stopwords = set()
for i in range(len(words)):
    if words[i] in markov:
        markov[words[i]].append(words[i + 1])
    else:
        if words[i][0].isupper() or words[i][0] is '"' and words[i][1].isupper():
            startwords.add(words[i])
        elif words[i][-1] in '.?!' or words[i][-1] is '"' and words[i][-2] in '.?!':
            stopwords.add(words[i])
        if i + 1 < len(words):
            markov[words[i]] = [words[i + 1]]

# TODO: construct 5 random sentences
# Your code here
for i in range(5):
    c = random.choice(list(startwords))
    print(c, end=" ")
    while not c in stopwords:
        c = random.choice(markov[c])
        print(c, end=" ")
    print()
