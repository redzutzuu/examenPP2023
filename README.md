Dependente necesare:
Kotlinx

" <dependency> "
       " <groupId>org.jetbrains.kotlinx</groupId> "
       " <artifactId>kotlinx-coroutines-core</artifactId> "
       " <version>1.5.0</version> "
" </dependency> "


1. Utilizand genericile sa se implementeze in Kotlin o functie extensie pe un subarbore de tipuri de date care sa verifice daca variabila contine un numar si apoi sa determine daca numarul este prim sau nu.

2. Sa se implementeze in Python echivalentul unei grupari de fire (ThreadPool) utilizand modului threading si care sa puna la dispozitie utilizand modelul comanda posibilitatea de a inspecta starea firului de executie, de a-l opri temporar sau definitiv sau de a-l porni.

3. Sa se scrie un program Python care va utiliza modelul mediator pentru a realiza o interactiune bidirectionala (folosind cozi intre procese) intre studenti si profesori utilizand asistentul (un obiect profesor, unul asistent si mai multe obiecte student). Se vor desena diagrama de clase si de obiecte. Se va explica maniera de aplicare a principiilor SOLID.

4. Intr-un fisier text cu minim 50 de valori (numere) se iau cate 10 valori consecutive care vor fi procesate intr-un thread separat (din modului threading, Python) (deci se lanseaza in executie minim 5 thread-uri). Datele sunt depuse intr-un ADT, apoi se va efectua o procesare de tip lambda care va gasi minimul, maximul si media din secventa, apoi va extrage o submultime ce contine numai numerele care se afla in intervalul media + sau - media patratica a secventei procesate.

5. Intr-un fisier text cu minim 50 de valori (numere) se iau cate 10 valori consecutive care vor fi procesate intr-un thread separat (din modului multiprocessing, Python) (deci se lanseaza in executie minim 5 thread-uri). Datele sunt depuse intr-un ADT, apoi se va efectua o procesare de tip lambda care va gasi minimul, maximul si media din secventa, apoi va extrage o submultime ce contine numai numerele care se afla in intervalul media + sau - media patratica a secventei procesate.

6. Pornind de la exemplul din curs cu functori none si some, sa se creeze in Kotlin o transformare (functor) care se aplica si asupra lui toInt. Astfel, daca este none se va inlocui cu -1, daca este some se genereaza o valoare aleatoare de zero sau unu. Apoi transformarea va fi aplicata cu map.

7. Sa se implementeze in Python un automat cu 3 stari unde fiecare stare este gestionata de un proces in care sa se proceseze cu expresii lambda o lista de numere intregi trimisa ca argument in constructor astfel: 
In s0 se verifica daca mai sunt elemente in lista (daca da, se duce in starea s1 unde se identifica si se sterge primul element par gasit, apoi se trece in s2).
In s2 se identifica si se sterge primul element impar gasit, apoi se trece in s0.
La fiecare stergere se afiseaza elementul sters.
In s0 daca nu mai exista elemente, se anunta acest lucru, iar programul se termina.

8. Utilizand generice si functii de extensie sa se scrie in Kotlin un aplicative care aplica intr-o corutina urmatoarea transformare lambda {i -> i //3} si {i -> i * 5} asupra elementelor dintr-o lista incarcata dintr-un fisier text de intrare. Rezultatul va fi convertit la string si afisat.

9. Sa se proiecteze si sa se implementeze o aplicatie Kotlin care citeste dintr-un fisier un text scris de student care contine si erori de scriere a unor cuvinte. Aceasta extrage si analizeaza fiecare cuvant, verificand un dictionar (separat dat de student cu cateva forme corecte de cuvinte). Totul se realizeaza intr-o corutina. De asemenea, cu observer (similar cu autocorrect-ul din Word) declansez intrebarea in momentul in care intalnesc un cuvant gresit daca doresc corectarea cuvantului, iar cu memento permit sa fac undo peste corecturile deja efectuate.


10. Sa se scrie un program Python care utilizand modelul strategie va alege in fuctie de reactia unui coleg un banc dintr-un dictionar care are seturi de bancuri bune, foarte bune si cele mai bune (un fisier text care are un banc pe paragraf si la inceput are una/doua/trei stelute (codificarea calitatii bancului)). Deci este nevoie de o clasa student, o metoda de a spune bancuri si una de a asculta si furniza o reactie. Se vor desena diagrama de clase si de obiecte. Se va explica maniera de aplicare a principiilor SOLID.


11. Sa se implementeze in Python un automat cu 3 stari in care sa se proceseze cu expresii lambda o lista de numere intregi trimisa ca argument in constructor astfel:
In s0 se verifica daca mai sunt elemente in lista (daca da, se duce in starea s1 unde se identifica si se sterge primul element par gasit, apoi se trece in s2).
In s2 se identifica si se sterge primul element impar gasit, apoi se trece in s0.
La fiecare stergere se afiseaza elementul sters.
In s0 daca nu mai exista elemente, se anunta acest lucru, iar programul se termina.

12. Utilizand modelul comanda sa se scrie in Kotlin un program care pornind de la o clasa student va asigura posibilitatea unor comenzi specifice unui obiect colega care sa conduca la schimbarea starii interne a unui obiect student (de exemplu din fericit in disperat). Apoi acestea vor fi utilizate intr-un automat static (cu doua stari fericit-nefericit) implementat utilizand modelul stare. Se vor desena diagrama de clase si de obiecte. Se va explica maniera de aplicare a principiilor SOLID.

13. Sa se scrie un program Kotlin utilizand corutine si canale "conflated" pentru comunicarea intre procese care distribuie intr-o maniera ciclica (cuvant1 - proces1, cuvant2 - proces2, cuvant3 - proces3, cuvant4 - proces1), cate un cuvant citit dintr-un fisier catre alte 3 procese, iar fiecare din acestea afiseaza numele lui si cuvantul primit la consola.

14. Utilizand de 2 ori modelul de lant de responsabilitati simplu si corutine (si nivelul de alerta [0..5]) sa se creeze un program Kotlin care va distribui un mesaj (primit la intrare impreuna cu nivelul lui) pentru a fi tratat (afisat) in zona potrivita (e.g. 5-comunicari, 4-politie, 3-sri, 2-sie, 1-csat, 0-nato). Apoi se va receptiona o comanda (utilizand modelul comanda) care trebuie executata de catre nodul care a emis avertizarea (in acest caz comanda va incapsula afisarea unui mesaj simplu).

15. Utilizand modelul fatada in cadrul unui program Kotlin sa se creeze un obiect de tip boombox (acesta este compus din metode specifice: play, record, fast forward, rewind, record, radio, volume, battery status, etc.), care sa afiseaza un mesaj corespunzator. Executia metodelor va fi realizata in corutine diferite.

16. Sa se proiecteze si sa se implementeze o aplicatie Python care citeste dintr-un fisier un text scris de student care contine si erori de scriere a unor cuvinte. Aceasta extrage si analizeaza fiecare cuvant, verificand un dictionar (separat dat de student cu cateva forme corecte de cuvinte). Totul se realizeaza intr-o corutina. De asemenea, cu observer (similar cu autocorrect-ul din Word) declansez intrebarea in momentul in care intalnesc un cuvant gresit daca doresc corectarea cuvantului, iar cu memento permit sa fac undo peste corecturile deja efectuate.

17. Utilizand modelul pod sa se scrie in Python un program care va porni de la un model mamifer si apoi va permite la instantiere de obiecte de tip om, femeie, caine si pisica. Acestor obiecte li se vor adauga 3-4 functionalitati suplimentare la alegere utilizand decoratorii (de exemplu o functie care descrie/permite interactiunea dintre om si femeie sau om si pisica etc). 

18. Sa se creeze in Python un program care primeste un sir de cautare si mai multe nume de fisiere text (inclusiv sursa program). Aplicatia cauta daca acest sir se gaseste, apoi afiseaza pentru fiecare fisier numerele liniilor unde se afla acesta. Programul primeste de la linia de comanda parametrii de intrare, iar daca este nevoie, mai primeste si un sir de inlocuire a celui cautat, caz in care se face search & replace

19. Sa se implementeze in Python problema lantului dublu de responsabilitati (up & down) pornind de la proiectarea din laborator, dar cu ajutorul thread-urilor (cate unul pentru fiecare nod), iar comunicarea intre fire sa se execute cu cozi (thread-safe).

19.1 Sa se implementeze in Kotlin problema lantului dublu de responsabilitati (up & down) pornind de la proiectarea din laborator, dar cu ajutorul thread-urilor (cate unul pentru fiecare nod), iar comunicarea intre fire sa se execute cu cozi (thread-safe).

20. Pornind de la exemplu cu map_reduce din modulul more_itertools (Python), sa se calculeze indexul invers pentru un set de documente text (creat de student). Toate cele 3 functii (key_func, value_func si reduce_func) vor fi scrise ca expresii lambda. Se va citi continutul fiecarui document si apoi se va sparge si reuni intr-o singura lista de cuvinte. Functia de mapare va returna perechi de forma <word, (document_id, 1)>, in care cheia este cuvantul, iar valoarea este formata din tupla document_id (numele documentului), si 1 (o aparitie a cuvantului in document). Functia de reducere primeste toate perechile, emite o pereche de forma <word, [(document_id_i, count_word_in_document_id_i), (...), ...]>, unde al doilea element din tupla reprezinta numarul de aparitii al cuvantului in documentul respectiv. Pentru simplitate, functia de reducere poate utiliza reduce_by_key din biblioteca PyFunctional, ca sa creeze acea lista de tuple.
Exemplu de output:
{'a':		[('text/1.txt', 1), ('text/2.txt', 2)],
 'about':	[('text/3.txt', 1)],
 'always':	[('text/3.txt', 1)],
 'are':		[('text/3.txt', 2)],
...}

21. Se scriu cate 100 de valori alese aleator in doua fisiere CSV. Apoi aceste fisiere sunt deschise (se va utiliza o corutina) si informatiile sunt depuse in doua colectii X si Y. Sa se scrie un program Kotlin care utilizand functii pure sau numai calcul lambda va gasi (daca exista) perechile de numere care satisfac x * y = x + y * 3

22. Sa se scrie un program Kotlin care va utiliza subclase active (cu granularitate mare a firelor) pentru procesarea simultana a unui hashmap. Clasa de baza va stabili operatiile (aflare maxim, aflare minim, numarul de aparitii a fiecarei valori din fisier, eliminarea duplicatelor) iar subclasele vor pune la dispozitie obiecte care se executa in fire separate. Hashmap-ul va fi initializat prin preluarea unui sir de date dintr-un fisier.

23. Cu ajutorul modelului mememto sa se creeze un program Python care va permite aplicarea succesiva a unor functii lambda peste o colectie initializata cu date citite dintr-un fisier si apoi va restaura obiectele la starea anterioara in momentul in care acest lucru este cerut (la consola). Se vor aplica urmatoarele functii:
-> f1(x)=x+1 (daca x par), altfel f1(x)=x;
-> f2(x)=3x*x-2*x+1;
-> f3(x)=xi+xi+1 unde i este indexul x-ului primit ca parametru 

24. Utilizand secvente din Python (PyFunctional), corutinele (asyncio) si impartirea in mai multe bucati, sa se elimine dintr-un fisier text rezultat din conversia unui epub spatiile multiple, salturile la linie noua. La sfarsit va fi generat noul fisier. Se vor folosi abordari de tipul impacheteaza-proceseaza-despacheteaza

25. Utilizand modelul adaptor sa se creeze un program Kotlin care va primi la intrare o lista cu mai multe fisiere (care pot fi de diverse tipuri de date simple sau de tip colectie) si va realiza utilizand cate o corutina pentru fiecare fisier scrierea datelor intr-un fisier destinatie unic (ordinea de scriere a datelor nu conteaza).

26. Utilizand Kotlin si functiile de procesare (din programarea functionala), sa se proceseze un fisier text (creat de programator cu cateva propozitii in el), filtrand cuvintele care au minim 4 caractere si extragand doua caractere din mijlocul cuvantului, apoi reunind rezultatul intr-un singur string. Spre exemplu, pentru textul "Acesta este examenul la PP" se va returna "esstme". Se va utiliza combinatie cu lambda peste colectii pentru procesare iar procesarea se va efectua intr-o corutina.
