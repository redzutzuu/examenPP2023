from collections import defaultdict


def read_words(files):
    words = []
    for file in files:
        with open(file) as f:
            aux = f.read().split(' ')
            aux = [(word, file) for word in aux]
            words.extend(aux)
    return words


if __name__ == '__main__':
    files = ["file1.txt", "file2.txt"]
    words = read_words(files)
    word_count = defaultdict(int)
    for word, _ in words:
        word_count[word] += 1
    print('{')
    for word, count in word_count.items():
        print(f"\'{word}\' : {count}")
    print('}')
    i = 0
