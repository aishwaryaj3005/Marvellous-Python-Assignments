def main():
    fobj = open("student.txt", "r")
    data = fobj.read()
    print("Contents of the file is :\n",data)
    fobj.close()

if __name__== "__main__":
    main()

'''
OUTPUT:
Contents of the file is :
Students names are :
Rohan
Rahul
Priya
Riya
Nia
'''