import threading

def thread1():
    print("Thread 1 :")
    for i in range(1, 51, 1):
        print(i, end = " ")
    print("\nThread 1 finished..")

def thread2():
    print("\nThread 2 :")
    for i in range(50, 0, -1):
        print(i, end = " ")
    print("\nThread 2 finished..")

def main():
    T1 = threading.Thread(target = thread1)
    T2 = threading.Thread(target = thread2)

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()

"""
OUTPUT:
Thread 1 :
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 
Thread 1 finished..

Thread 2 :
50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 
Thread 2 finished..
"""