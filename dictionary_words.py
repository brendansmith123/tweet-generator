import random
import sys

def read_words(word_count):
    with open('/usr/share/dict/words') as r:
        words = r.read().splitlines()
        random_words = random.choices(words, k=word_count)
        sentence = " ".join(random_words)
        print(sentence)

if __name__ == "__main__":
    words_read = int(sys.argv[1])
    read_words(words_read)

