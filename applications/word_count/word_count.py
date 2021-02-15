SPECIAL_CHARACTERS = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split()

def word_count(s):
    # Your code here

    w = dict()
    words = ''.join(filter(lambda x : x not in SPECIAL_CHARACTERS, s)).lower().split()
    for word in words:
        if word in w:
            w[word] += 1
        else:
            w[word] = 1
    return w

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
