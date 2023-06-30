class CollectionMemento:
    def __init__(self, collection):
        self.collection_state = collection.copy()

    def get_state(self):
        return self.collection_state


class Collection:
    def __init__(self, collection):
        self.collection = collection.copy()

    def apply_lambda_function(self, function):
        self.collection = [function(x) for x in self.collection]

    def get_memento(self):
        return CollectionMemento(self.collection)


class FunctionManager:
    def __init__(self, collection):
        self.collection = Collection(collection)
        self.memento_stack = []

    def apply_lambda_function(self, function):
        self.memento_stack.append(self.collection.get_memento())
        self.collection.apply_lambda_function(function)

    def restore_previous_state(self):
        if self.memento_stack:
            previous_state = self.memento_stack.pop()
            self.collection = Collection(previous_state.get_state())
        else:
            print("No previous state available.")

    def get_collection_state(self):
        return self.collection.collection


def main():
    # Colectia initiala
    initial_collection = [1, 2, 3, 4, 5]

    # Initializarea FunctionManager cu colectia initiala
    function_manager = FunctionManager(initial_collection)

    # Definirea functiilor lambda
    f1 = lambda x: x + 1 if x % 2 == 0 else x
    f2 = lambda x: 3 * x * x - 2 * x + 1
    f3 = lambda x, y: x + y

    # Aplicarea succesiva a functiilor lambda asupra colectiei
    function_manager.apply_lambda_function(f1)
    function_manager.apply_lambda_function(f2)
    function_manager.apply_lambda_function(lambda x: f3(x, 10))

    # Afișarea stării curente a colecției
    print("Current collection state:", function_manager.get_collection_state())

    # Restaurarea stării anterioare
    function_manager.restore_previous_state()

    # Afișarea stării actualizate după restaurare
    print("Restored collection state:", function_manager.get_collection_state())


if __name__ == "__main__":
    main()
