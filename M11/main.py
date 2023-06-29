class Automaton:
    def __init__(self, numbers):
        self.state = self.s0
        self.numbers = numbers

    def run(self):
        while self.state is not None:
            self.state = self.state()

    def s0(self):
        if len(self.numbers) > 0:
            self.state = self.s1
            return self.state()
        else:
            print("Nu mai există elemente în listă.")
            return None

    def s1(self):
        even_number = next((x for x in self.numbers if x % 2 == 0), None)
        if even_number is not None:
            self.numbers.remove(even_number)
            print(f"Elementul par șters: {even_number}")
            self.state = self.s2
            return self.state()
        else:
            self.state = self.s2
            return self.state()

    def s2(self):
        odd_number = next((x for x in self.numbers if x % 2 != 0), None)
        if odd_number is not None:
            self.numbers.remove(odd_number)
            print(f"Elementul impar șters: {odd_number}")
            self.state = self.s0
            return self.state()
        else:
            self.state = self.s0
            return self.state()


def main():
    numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    automaton = Automaton(numbers_list)
    automaton.run()


if __name__ == "__main__":
    main()
