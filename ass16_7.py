def Marks():
    fobj = open("marks.txt", "w")
    fobj.write("Student Name    Marks\n")
    fobj.write("Aishwarya J       80\n")
    fobj.write("Sharvari B        75\n")
    fobj.write("Pooja A           78") 
    fobj.close()

    fobj = open("marks.txt", "r")
    
    for line in fobj:
        Name, Marks = line.split()
        if int(Marks) > 75:
            print(Name, Marks)

    fobj.close()

def main():
    Marks()

if __name__ == "__main__":
    main()