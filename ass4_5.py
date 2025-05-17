from functools import reduce

def prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
 
mult = lambda no : no * 2
maxi = lambda a,b :  max(a,b)

def main():
    data = []
    print("Enter number of elements: ")
    size = int(input())
    print("Please enter numeric values: ")
    
    for i  in range(size):
        no = int(input())
        data.append(no)

    print("Input data: ", data)

    fdata = list(filter(prime, data))
    print("Filter Output: ", fdata)

    mdata = list(map(mult, fdata))
    print("Map Output: ", mdata)

    rdata = reduce(maxi, mdata)
    print("Reduce Output: ", rdata)

if __name__ == "__main__":
    main()

'''
OUTPUT:
Enter number of elements: 
8
Please enter numeric values: 
2
70
11
10
17
23
31
77
Input data:  [2, 70, 11, 10, 17, 23, 31, 77]
Filter Output:  [2, 11, 17, 23, 31]
Map Output:  [4, 22, 34, 46, 62]
Reduce Output:  62
'''