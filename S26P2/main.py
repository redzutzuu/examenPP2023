import itertools

def generator_nume_temporare(s1, s2):
    contor = itertools.count(1)  # Contorul pentru index

    def next_nume_temporar():
        index = next(contor)  # Obține următorul index din contor
        return f"{s1}-{index}-{s2}.tmp"

    return next_nume_temporar

def main():
    generare_nume = generator_nume_temporare("s1", "s2")

    # Obține primele 5 nume de fișiere temporare
    for _ in range(5):
        nume_temporar = generare_nume()
        print(nume_temporar)

if __name__ == "__main__":
    main()
