import threading

class OperatiiBaza:
    def __init__(self, hashmap):
        self.hashmap = hashmap

    def operatie(self):
        pass

class Adunare(OperatiiBaza, threading.Thread):
    def __init__(self, hashmap):
        OperatiiBaza.__init__(self, hashmap)
        threading.Thread.__init__(self)

    def operatie(self):
        for cheie in self.hashmap:
            self.hashmap[cheie] += 1

class Scadere(OperatiiBaza, threading.Thread):
    def __init__(self, hashmap):
        OperatiiBaza.__init__(self, hashmap)
        threading.Thread.__init__(self)

    def operatie(self):
        for cheie in self.hashmap:
            self.hashmap[cheie] -= 1

class Inmultire(OperatiiBaza, threading.Thread):
    def __init__(self, hashmap):
        OperatiiBaza.__init__(self, hashmap)
        threading.Thread.__init__(self)

    def operatie(self):
        for cheie in self.hashmap:
            self.hashmap[cheie] *= 2

def main():
    hashmap = {"a": 10, "b": 20, "c": 30}

    adunare = Adunare(hashmap)
    scadere = Scadere(hashmap)
    inmultire = Inmultire(hashmap)

    adunare.start()
    scadere.start()
    inmultire.start()

    adunare.join()
    scadere.join()
    inmultire.join()

    print("Rezultatul operațiilor:")
    print(hashmap)

if __name__ == "__main__":
    main()
