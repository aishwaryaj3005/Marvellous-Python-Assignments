import psutil

def DisplayProcess():
    border = "-" * 54
    print(border)
    print("Information of currently running process")
    print(border)

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=['name','pid','username'])
        print(info)

def main():
    DisplayProcess()

if __name__ == "__main__":
    main()