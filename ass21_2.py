import psutil

def DisplayProcess(ProcessName):
    
    found = False
    for proc in psutil.process_iter(['name','pid','username']):
        if ProcessName.lower() in proc.info['name'].lower():
            found = True
            print(f"Process Name : {proc.info['name']}")
            print(f"Process PID : {proc.info['pid']}")
            print(f"Process Username : {proc.info['username']}")
            
    if(found == False):
        print("Process is not running")

def main():
    name = input("Enter name of the process : ")
    DisplayProcess(name)

if __name__ == "__main__":
    main()