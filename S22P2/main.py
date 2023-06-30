import threading
from collections import defaultdict

# Crearea unui RLock
lock = threading.RLock()

# Initializarea hashmapului X si a dictionarului Y
X = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
Y = {0: 10, 1: 20, 2: 30, 3: 40, 4: 50}

# Functia ce va fi executata de thread-uri
def process_data(key, index):
    global X
    global Y

    with lock:
        if index+1 in Y:
            Y[index] = X[key]*Y[index] + Y[index+1]

def main():
    # Crearea si pornirea thread-urilor
    threads = []
    for i, key in enumerate(X):
        t = threading.Thread(target=process_data, args=(key, i))
        threads.append(t)
        t.start()

    # Asteptarea ca toate thread-urile sa se incheie
    for t in threads:
        t.join()

    print(Y)

if __name__ == "__main__":
    main()