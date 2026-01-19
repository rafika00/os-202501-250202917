import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()

def proses_1():
    with lock_a:
        print("Proses 1 memegang Lock A")
        time.sleep(1)
        print("Proses 1 menunggu Lock B")
        with lock_b:
            print("Proses 1 memegang Lock B")

def proses_2():
    with lock_b:
        print("Proses 2 memegang Lock B")
        time.sleep(1)
        print("Proses 2 menunggu Lock A")
        with lock_a:
            print("Proses 2 memegang Lock A")

t1 = threading.Thread(target=proses_1)
t2 = threading.Thread(target=proses_2)

t1.start()
t2.start()

t1.join()
t2.join()
