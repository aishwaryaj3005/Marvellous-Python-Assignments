def main():
    fobj = open("SourceFile.txt", "w")
    fobj.write("Hello World")

    fobj.close()

    fobj = open("SourceFile.txt", "r")
    data = fobj.read()

    fobj2 = open("DestinationFile.txt", "w")
    fobj2.write(data)

    fobj.close()
    fobj2.close()

    print("Successfully Copied contents of SourceFile to DestinationFile")

if __name__ == "__main__":
    main()

'''
OUTPUT :
Successfully Copied contents of SourceFile to DestinationFile
'''