import tkinter as tk


# Interfața pentru fabrica de butoane
class ButtonFactory:
    def create_button(self, label):
        raise NotImplementedError()


# Implementarea fabricii de butoane pentru limba engleză
class EnglishButtonFactory(ButtonFactory):
    def create_button(self, label):
        return EnglishButton(label)


# Implementarea fabricii de butoane pentru limba română
class RomanianButtonFactory(ButtonFactory):
    def create_button(self, label):
        return RomanianButton(label)


# Interfața pentru buton
class Button:
    def __init__(self, label):
        self.label = label

    def display(self):
        raise NotImplementedError()


# Implementarea butonului pentru limba engleză
class EnglishButton(Button):
    def display(self):
        root = tk.Tk()
        button = tk.Button(root, text=self.label["english"], bg="light blue", fg="black")
        button.pack()
        root.mainloop()


# Implementarea butonului pentru limba română
class RomanianButton(Button):
    def display(self):
        root = tk.Tk()
        button = tk.Button(root, text=self.label["romanian"], bg="light yellow", fg="black")
        button.pack()
        root.mainloop()


# Funcția de fabricare a fabricii de butoane în funcție de limba selectată
def create_button_factory(language):
    if language == "english":
        return EnglishButtonFactory()
    elif language == "romanian":
        return RomanianButtonFactory()
    else:
        raise ValueError("Unsupported language.")


def main():
    # Dicționarul cu mesajele în diferite limbi
    messages = {
        "english": "Click me!",
        "romanian": "Apasă-mă!",
    }

    # Se selectează limba (engleză sau română)
    language = input("Select language (english/romanian): ")

    # Se creează fabrica de butoane în funcție de limba selectată
    button_factory = create_button_factory(language)

    # Se creează butonul corespunzător limbii selectate
    button = button_factory.create_button(messages)

    # Se afișează butonul
    button.display()


if __name__ == "__main__":
    main()
