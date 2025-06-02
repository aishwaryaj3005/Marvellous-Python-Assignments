import multiprocessing

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def main():
    num = [1,2,3,4,5]
    
    pool = multiprocessing.Pool()
    result = pool.map(factorial, num) 

    print("Factorial :", result)

if __name__ == "__main__":
    main()

"""
OUTPUT:
Factorial : [1, 2, 6, 24, 120]
"""