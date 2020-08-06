def no_dups(s):
    # Your code here
    d = set()
    words = []
    for word in s.split():
        if not word in d:
            d.add(word)
            words.append(word)
    return " ".join(words)

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
