class ErrorStrategy:
    def handle_error(self, error_message):
        pass


class WarningStrategy(ErrorStrategy):
    def handle_error(self, error_message):
        print("Warning:", error_message)
        # Scrie în fișierul de avertismente
        with open("warnings.log", "a") as file:
            file.write(f"Warning: {error_message}\n")


class ErrorStrategy(ErrorStrategy):
    def handle_error(self, error_message):
        print("Error:", error_message)
        # Scrie în fișierul de erori comune
        with open("errors.log", "a") as file:
            file.write(f"Error: {error_message}\n")


class CriticalErrorStrategy(ErrorStrategy):
    def handle_error(self, error_message):
        print("Critical Error:", error_message)
        # Scrie în fișierul de erori grave
        with open("critical_errors.log", "a") as file:
            file.write(f"Critical Error: {error_message}\n")
        # Oprește programul
        exit()


class ErrorHandler:
    def __init__(self, error_strategy):
        self.error_strategy = error_strategy

    def handle_error(self, error_message):
        self.error_strategy.handle_error(error_message)


# Excepție personalizată pentru o eroare de tip Warning
class WarningError(Exception):
    pass


# Excepție personalizată pentru o eroare de tip Error
class CommonError(Exception):
    pass


# Excepție personalizată pentru o eroare de tip Critical Error
class CriticalError(Exception):
    pass


def main():
    # Inițializare ErrorHandler cu strategia corespunzătoare pentru fiecare tip de eroare
    warning_handler = ErrorHandler(WarningStrategy())
    error_handler = ErrorHandler(ErrorStrategy())
    critical_error_handler = ErrorHandler(CriticalErrorStrategy())

    try:
        # Generare unei erori de tip Warning
        raise WarningError("This is a warning!")

    except WarningError as e:
        warning_handler.handle_error(str(e))

    try:
        # Generare unei erori de tip Error
        raise CommonError("This is an error!")

    except CommonError as e:
        error_handler.handle_error(str(e))

    try:
        # Generare unei erori de tip Critical Error
        raise CriticalError("This is a critical error!")

    except CriticalError as e:
        critical_error_handler.handle_error(str(e))


if __name__ == "__main__":
    main()
