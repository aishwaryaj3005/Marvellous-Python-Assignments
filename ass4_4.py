from functools import reduce

chkeven = lambda x : x % 2 == 0
cal_sq = lambda no : no ** 2
add = lambda a , b : a + b 

def main():
    data = []
    print("Enter number of elements: ")
    size = int(input())
    print("Please enter numeric values: ")
    
    for i  in range(size):
        no = int(input())
        data.append(no)

    print("Input data: ", data)

    fdata = list(filter(chkeven, data))
    print("Filter Output: ", fdata)

    mdata = list(map(cal_sq, fdata))
    print("Map Output: ", mdata)

    rdata = reduce(add, mdata)
    print("Reduce Output: ", rdata)

if __name__ == "__main__":
    main()

'''
output:
Enter number of elements: 
10
Please enter numeric values: 
5
2
3
4
3
4
1
2
8
10
Input data:  [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
Filter Output:  [2, 4, 4, 2, 8, 10]
Map Output:  [4, 16, 16, 4, 64, 100]
Reduce Output:  204
'''