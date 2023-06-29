from math import sqrt
from multiprocessing import Process, Queue

min_fun = lambda lst: min(lst)
max_fun = lambda lst: max(lst)
mean_fun = lambda lst: sum(lst) / len(lst)
square_mean_fun = lambda lst: sqrt(sum(x * x for x in lst) / len(lst))
subsequence_fun = lambda lst: [x for x in lst if -square_mean_fun(lst) <= x <= square_mean_fun(lst)]


def process_sequence(sequence, results):
    min_value = min_fun(sequence)
    max_value = max_fun(sequence)
    avg_value = mean_fun(sequence)
    subsequence = subsequence_fun(sequence)

    results.put((min_value, max_value, avg_value, subsequence))


if __name__ == "__main__":
    lists = []
    with open("date.txt", "r") as file:
        numbers = list(map(int, file.read().split()))
    while numbers:
        if len(numbers) >= 10:
            lists.append(numbers[:10])
            numbers = numbers[10:]
        else:
            lists.append(numbers)
            numbers = []

    results = Queue()  # min, max, mean, subsequence
    processes = []
    for seq in lists:
        p = Process(target=process_sequence, args=(seq, results))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    rez = []
    while not results.empty():
        rez.append(results.get())

    if rez:
        for i in range(len(lists)):
            print(
                f"Sequence: {lists[i]}, min: {rez[i][0]}, max: {rez[i][1]}, mean: {rez[i][2]}, subsequence: {rez[i][3]}")
    else:
        print("No results found.")


# Se definește câteva funcții lambda pentru a calcula minimul, maximul, media și media pătratică a unei liste de numere. Aceste funcții vor fi utilizate pentru a procesa secvențele de numere.
#
# Se definește funcția process_sequence care primește o secvență de numere și o coadă de rezultate. Această funcție calculează minimul, maximul, media și subsecvența corespunzătoare în funcție de cerințele problemei și pune rezultatele în coada de rezultate.
#
# În blocul if __name__ == "__main__": se începe execuția principală a programului.
#
# Se deschide fișierul "date.txt" și se citesc numerele din el. Numerele sunt convertite la tipul int și stocate în lista numbers.
#
# Apoi, lista de numere numbers este împărțită în secvențe de câte 10 numere (dacă este posibil) și adăugate în lista lists. Dacă numerele nu se pot împărți în secvențe complete de 10, ultima secvență va conține doar numerele rămase.
#
# Se creează o coadă de rezultate results care va stoca rezultatele procesării fiecărei secvențe.
#
# Se inițializează o listă processes care va conține toate procesele create pentru a procesa secvențele.
#
# Pentru fiecare secvență din lista lists, se creează un nou proces care va apela funcția process_sequence pentru a procesa secvența respectivă. Procesul este pornit și adăugat în lista processes.
#
# Se așteaptă ca toate procesele să se încheie folosind metoda join() pentru fiecare proces din lista processes.
#
# Se creează o listă rez care va stoca rezultatele obținute din coada de rezultate results. Se extrag rezultatele din coadă și se adaugă în lista rez.
#
# Dacă există rezultate în lista rez, acestea sunt afișate pentru fiecare secvență procesată. Se afișează secvența, minimul, maximul, media și subsecvența.
#
# În caz contrar, dacă nu s-au găsit rezultate, se afișează mesajul "No results found.".
#
# Acest cod utilizează multiprocessing pentru a procesa secvențele de numere în paralel, utilizând mai multe fire de execuție (procese). Fiecare proces preia o secvență de 10 numere, calculează rezultatele cerute și le pune într-o coadă comună de rezultate. Apoi, rezultatele sunt extrase din coadă și afișate.
#
# Este important să asigurați că fișierul "date.txt" conține numere valide, separate prin spații, și se află în același director cu fișierul Python.