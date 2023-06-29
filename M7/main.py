import time
from multiprocessing import Process, Queue
from functional import seq

def State0(q):
    l = q.get()
    if len(l) > 0:
        q.put(True)
        q.put(l)
    else:
        q.put(False)
    time.sleep(1)



def State1(q):
    l: list = q.get()

    if seq(l).filter(lambda it:it%2==0).len()>0:
        aux = seq(l).filter(lambda it: it % 2 == 0).first()
        l.remove(aux)
        print(f"State 1 a eliminat {aux}")
    q.put(True)
    q.put(l)
    # time.sleep(1)


def State2(q):
    l: list = q.get()
    if seq(l).filter(lambda it:it%2!=0).len()>0:
        aux = seq(l).filter(lambda it: it % 2 != 0).first()
        l.remove(aux)
        print(f"State 2 a eliminat {aux}")
    q.put(True)
    q.put(l)
    # time.sleep(1)


class FSM:
    def __init__(self, list):
        self.__queue = Queue()
        self.__queue.put(True)
        self.__queue.put(list)
        self.__states=[State0,State1,State2]
        self.__current_state = 0

    def start(self):
        while self.__queue.get():
            process = Process(target=self.__states[self.__current_state], args=(self.__queue,))
            process.start()
            self.__current_state = (self.__current_state + 1) % 3
            process.join()


if __name__ == "__main__":
    l = list(range(10))
    fsm = FSM(l)
    fsm.start()