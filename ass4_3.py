from functools import reduce

sort = lambda x : 70 <= x <= 90
increase = lambda no : no + 10
product = lambda a , b : a * b 

def main():
    data = []
    print("Enter number of elements: ")
    size = int(input())
    print("Please enter numeric values: ")
    
    for i  in range(size):
        no = int(input())
        data.append(no)

    print("Input data: ", data)

    fdata = list(filter(sort, data))
    print("Filter Output: ", fdata)

    mdata = list(map(increase, fdata))
    print("Map Output: ", mdata)

    rdata = reduce(product, mdata)
    print("Reduce Output: ", rdata)

if __name__ == "__main__":
    main()

'''
OUTPUT:
Enter number of elements: 
12
Please enter numeric values: 
4
34
36
76
68
24
89
23
86
90
45
70
Input data:  [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
Filter Output:  [76, 89, 86, 90, 70]
Map Output:  [86, 99, 96, 100, 80]
Reduce Output:  6538752000
'''