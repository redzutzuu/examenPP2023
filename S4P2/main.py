import threading

class BaseCalculator:
    def __init__(self):
        self.result = {}

    def process(self, key, value):
        pass

    def start_processing(self):
        threads = []

        for key, value in self.result.items():
            thread = threading.Thread(target=self.process, args=(key, value))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()


class AddCalculator(BaseCalculator):
    def process(self, key, value):
        result = value + 10
        print(f"Add: {key} + 10 = {result}")


class SubtractCalculator(BaseCalculator):
    def process(self, key, value):
        result = value - 5
        print(f"Subtract: {key} - 5 = {result}")


class MultiplyCalculator(BaseCalculator):
    def process(self, key, value):
        result = value * 2
        print(f"Multiply: {key} * 2 = {result}")


class DivideCalculator(BaseCalculator):
    def process(self, key, value):
        result = value / 3
        print(f"Divide: {key} / 3 = {result}")


def main():
    data = {
        "A": 20,
        "B": 30,
        "C": 40,
        "D": 50
    }

    calculators = [
        AddCalculator(),
        SubtractCalculator(),
        MultiplyCalculator(),
        DivideCalculator()
    ]

    for calculator in calculators:
        calculator.result = data
        calculator.start_processing()


if __name__ == "__main__":
    main()
