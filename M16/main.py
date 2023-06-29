import asyncio
import re


class TextAnalyzer:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.observers = []

    def attach_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, word):
        for observer in self.observers:
            observer.update(word)

    async def analyze_text(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                words = re.findall(r'\b\w+\b', line)
                for word in words:
                    await self.process_word(word)

    async def process_word(self, word):
        if word.lower() not in self.dictionary:
            self.notify_observers(word)


class WordCorrectionObserver:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def update(self, word):
        response = input(f"Word '{word}' is misspelled. Would you like to correct it? (y/n): ")
        if response.lower() == 'y':
            corrected_word = input(f"Please enter the corrected version of '{word}': ")
            self.analyzer.dictionary[word.lower()] = corrected_word.lower()


class Memento:
    def __init__(self, dictionary):
        self._state = {k: v for k, v in dictionary.items()}

    def restore(self, analyzer):
        analyzer.dictionary = self._state


class TextEditor:
    def __init__(self):
        self.text_analyzer = TextAnalyzer({})
        self.word_correction_observer = WordCorrectionObserver(self.text_analyzer)
        self.memento = None

    def load_dictionary(self, dictionary_file_path):
        with open(dictionary_file_path, 'r') as file:
            for word in file:
                self.text_analyzer.dictionary[word.strip().lower()] = word.strip().lower()

    async def process_text_file(self, file_path):
        await self.text_analyzer.analyze_text(file_path)

    def enable_word_correction(self):
        self.text_analyzer.attach_observer(self.word_correction_observer)

    def undo_word_corrections(self):
        if self.memento:
            self.memento.restore(self.text_analyzer)

    def create_memento(self):
        self.memento = Memento(self.text_analyzer.dictionary)


# Exemplu de utilizare
if __name__ == '__main__':
    text_editor = TextEditor()
    text_editor.load_dictionary('dictionary.txt')
    text_editor.enable_word_correction()

    # Procesarea textului și observarea cuvintelor greșite
    asyncio.run(text_editor.process_text_file('input.txt'))

    # Salvarea stării actuale a dicționarului
    text_editor.create_memento()

    # Efectuarea unui undo asupra corecțiilor făcute
    text_editor.undo_word_corrections()

    # Procesarea textului din nou pentru a verifica dacă corecțiile au fost anulate
    asyncio.run(text_editor.process_text_file('input.txt'))
