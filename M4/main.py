from math import sqrt

from functional import seq
from threading import Thread

min_fun = lambda list: seq(list).min()
max_fun = lambda list: seq(list).max()
mean_fun = lambda list: seq(list).sum() / seq(list).len()
square_mean_fun = lambda list: sqrt(seq(list).map(lambda it: it * it).sum() / seq(list).len())
subsequence_fun = lambda list: seq(list).filter(lambda it: -square_mean_fun(list) <= it <= square_mean_fun(list))
if __name__ == "__main__":
    lists = []
    numbers = seq(open("date.txt", "r").readline().split(' ')) \
        .map(lambda it: it.replace('\t', '')) \
        .map(lambda it: int(it))
    while numbers.len() > 0:
        if numbers.len() >= 10:
            lists.append(numbers.take(10).list())
            numbers = numbers.drop(10)
        else:
            lists.append(numbers.take(numbers.len()).list())
            numbers = numbers.drop(numbers.len())

    results = []  # min,max,mean,subsequence
    threads = []
    for list in lists:
        aux = Thread(target=lambda list, results: results.append(
            (min_fun(list), max_fun(list), mean_fun(list), subsequence_fun(list))), args=(list, results,))
        aux.start()
        threads.append(aux)
    for thread in threads:
        thread.join()

    i=0
    for i in range(len(lists)):
        print(f"Sequence:{lists[i]}, min:{results[i][0]}, max:{results[i][1]}, mean:{results[i][2]}, subsequence:{results[i][3]}")
    i = 0