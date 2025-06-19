def Display():
    fobj = open("demo.txt", "r")

    for line in fobj:
        words = line.split()
        if len(words) > 5:
            print(line.strip())
        
    fobj.close()

def main():
    Display()

if __name__ == "__main__":
    main()

'''
INPUT :
Heyy
Welcome to Marvellous Intosystems
Course : Python Machine Learning with GenAI

OUTPUT :
Course : Python Machine Learning with GenAI
'''