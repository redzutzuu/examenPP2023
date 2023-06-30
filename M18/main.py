import sys

def search_files(search_string, file_names):
    for file_name in file_names:
        print(f"Rezultate pentru fisierul {file_name}:")
        try:
            with open(file_name, 'r') as file:
                lines = file.readlines()
                for i, line in enumerate(lines, start=1):
                    if search_string in line:
                        print(f"- Linia {i}: {line.strip()}")
        except FileNotFoundError:
            print(f"Fisierul {file_name} nu exista")
        print()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Utilizare: python program.py [sir_cautare] [fisier1] [fisier2] ...")
    else:
        search_string = sys.argv[1]
        file_names = sys.argv[2:]
        print(f"Cautare pentru sirul de cautare: {search_string}\n")
        search_files(search_string, file_names)
