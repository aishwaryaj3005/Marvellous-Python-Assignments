def main():
    fobj = open("demo.txt", "r")
    file = open("new.txt", "w")
    
    for line in fobj:
        if line.strip():
            file.write(line)

    fobj.close()
    file.close()

if __name__ == "__main__":
    main()