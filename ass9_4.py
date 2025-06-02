import threading
import multiprocessing
import time

def sumNum():
    return sum(range(1, 10000001))

def main():
    # Normal Function
    def nor_sum():
        start = time.time()
        total = sumNum()
        end = time.time()
        print("Normal sum :", total)
        print("Time :", end - start)

    # Thread Function
    def thread_sum():
        start = time.time()
        T = threading.Thread(target = sumNum)
        T.start()
        T.join()
        total = sumNum()
        end = time.time()
        print("Thread sum :", total)
        print("Time :", end - start)

    # Multiprocessing Funtion
    def multip_sum():
        start = time.time()
        pool = multiprocessing.Pool()
        result = pool.apply(sumNum)
        end = time.time()
        print("Multiprocessing sum :", result)
        print("Time :", end - start)
    
if __name__ == "__main__":
    main()
    