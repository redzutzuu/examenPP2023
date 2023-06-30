import threading

class HashMapProcessor:
    def __init__(self, hashmap):
        self.hashmap = hashmap
        self.lock = threading.RLock()

    def process(self, operation, key, value):
        with self.lock:
            if operation == 'add':
                self.hashmap[key] = self.add(self.hashmap.get(key, 0), value)
            elif operation == 'subtract':
                self.hashmap[key] = self.subtract(self.hashmap.get(key, 0), value)
            elif operation == 'multiply':
                self.hashmap[key] = self.multiply(self.hashmap.get(key, 0), value)

    def add(self, a, b):
        return (a + b) % 2**16

    def subtract(self, a, b):
        return (a - b) % 2**16

    def multiply(self, a, b):
        return (a * b) % 2**16


class HashMapThread(threading.Thread):
    def __init__(self, hashmap_processor, operation, key, value):
        super().__init__()
        self.hashmap_processor = hashmap_processor
        self.operation = operation
        self.key = key
        self.value = value

    def run(self):
        self.hashmap_processor.process(self.operation, self.key, self.value)


def main():
    hashmap = {}
    hashmap_processor = HashMapProcessor(hashmap)

    threads = []
    for i in range(10):
        thread = HashMapThread(hashmap_processor, 'add', 'key', i)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(hashmap)


if __name__ == "__main__":
    main()
