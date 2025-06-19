def main():
    fobj = open("Student.txt", "r")
    data = fobj.read()
    
    lines_cnt = data.count("\n")
    print("Total lines are :", lines_cnt)

    words_cnt = data.split()
    print("Total Words are :", len(words_cnt))

    char_cnt = len(data)
    print("Total Characters are :", char_cnt)

if __name__ == "__main__":
    main()

'''
OUTPUT:
Total lines are : 5
Total Words are : 9
Total Characters are : 47
'''