import threading


class ThreadPool:
    def __init__(self, num_threads):
        self.num_threads = num_threads
        self.threads = []
        self.is_running = False

    def start(self):
        self.is_running = True
        for _ in range(self.num_threads):
            thread = threading.Thread(target=self._worker)
            self.threads.append(thread)
            thread.start()

    def stop(self):
        self.is_running = False

    def pause(self):
        for thread in self.threads:
            thread.paused = True

    def resume(self):
        for thread in self.threads:
            thread.paused = False

    def inspect_threads(self):
        for i, thread in enumerate(self.threads):
            print(f"Thread {i + 1}: {'Paused' if thread.paused else 'Running'}")

    def _worker(self):
        current_thread = threading.current_thread()
        current_thread.paused = False
        while self.is_running:
            if current_thread.paused:
                continue


def task():
    while True:
        pass


thread_pool = ThreadPool(num_threads=3)
thread_pool.start()

while True:
    command = input("Introduceți comanda (inspect, stop, pause, resume): ")
    if command == "inspect":
        thread_pool.inspect_threads()
    elif command == "stop":
        thread_pool.stop()
        break
    elif command == "pause":
        thread_pool.pause()
    elif command == "resume":
        thread_pool.resume()

# Așteaptă ca toate firele să se oprească înainte de a ieși din program
for thread in thread_pool.threads:
    thread.join()
