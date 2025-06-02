import threading
import time

def numbers():
    for i in range(1,6):
        time.sleep(1)
        print(threading.current_thread().name, "prints :", i)

T1 = threading.Thread(target = numbers, name = "thread1")
T2 = threading.Thread(target = numbers, name = "thread2")
T3 = threading.Thread(target = numbers, name = "thread3")

T1.start()
T2.start()
T3.start()

T1.join()
T2.join()
T3.join()

"""
OUTPUT:
thread2 prints : 1
thread1 prints : 1
thread3 prints : 1
thread3 prints : 2
thread2 prints : 2
thread1 prints : 2
thread3 prints : 3
thread1 prints : 3
thread2 prints : 3
thread2 prints : 4
thread3 prints : 4
thread1 prints : 4
thread1 prints : 5
thread2 prints : 5
thread3 prints : 5
"""