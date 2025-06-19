def main():
    fobj = open("student.txt", "w")
    fobj.write("Students names are :\n")
    fobj.write("Rohan\nRahul\nPriya\nRiya\nNia")
    fobj.close()

if __name__ == "__main__":
    main()