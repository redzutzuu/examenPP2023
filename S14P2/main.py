import multiprocessing


def worker(queue, name):
    while True:
        word = queue.get()
        if word is None:
            break
        print(f"Procesul {name}: {word}")


def main():
    with open("words.txt") as file:
        words = file.read().split()

    queue = multiprocessing.Queue()
    processes = []

    for i in range(3):
        process = multiprocessing.Process(target=worker, args=(queue, f"Procesul {i+1}"))
        processes.append(process)
        process.start()

    for word in words:
        queue.put(word)

    for _ in range(3):
        queue.put(None)

    for process in processes:
        process.join()


if __name__ == "__main__":
    main()
