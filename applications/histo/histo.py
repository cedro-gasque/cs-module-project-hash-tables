# Your code here
SPECIAL_CHARACTERS = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split()

with open('input.txt') as f:
    words = ''.join(filter(lambda x : x not in SPECIAL_CHARACTERS, f.read())).lower().split()


hist = dict()
max = 0
for word in words:
    if not word in hist:
        hist[word] = 1
        if len(word) > max:
            max = len(word)
    else:
        hist[word] += 1
