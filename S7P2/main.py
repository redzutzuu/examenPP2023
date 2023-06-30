import threading
import time


class HashMap:
    def __init__(self):
        self.data = {}
        self.lock = threading.Lock()

    def add(self, key, value):
        with self.lock:
            self.data[key] = value
            print(f"Added key: {key}, value: {value}")

    def remove(self, key):
        with self.lock:
            if key in self.data:
                del self.data[key]
                print(f"Removed key: {key}")

    def multiply(self, key):
        with self.lock:
            if key in self.data:
                value = self.data[key]
                self.data[key] = value * 16
                print(f"Multiplied key: {key} by 16, new value: {self.data[key]}")

    def print_data(self):
        with self.lock:
            print("HashMap content:")
            for key, value in self.data.items():
                print(f"Key: {key}, Value: {value}")


class HashMapWorker(threading.Thread):
    def __init__(self, hashmap, action, key, value=None):
        super().__init__()
        self.hashmap = hashmap
        self.action = action
        self.key = key
        self.value = value

    def run(self):
        if self.action == "add":
            self.hashmap.add(self.key, self.value)
        elif self.action == "remove":
            self.hashmap.remove(self.key)
        elif self.action == "multiply":
            self.hashmap.multiply(self.key)


def main():
    hashmap = HashMap()
    workers = []

    # Crearea obiectelor Worker și pornirea firelor de execuție
    worker1 = HashMapWorker(hashmap, "add", "key1", 10)
    worker2 = HashMapWorker(hashmap, "add", "key2", 20)
    worker3 = HashMapWorker(hashmap, "remove", "key1")
    worker4 = HashMapWorker(hashmap, "multiply", "key2")

    workers.extend([worker1, worker2, worker3, worker4])

    for worker in workers:
        worker.start()

    # Așteptarea terminării tuturor firelor de execuție
    for worker in workers:
        worker.join()

    # Afișarea conținutului hashmap-ului
    hashmap.print_data()


if __name__ == "__main__":
    main()
