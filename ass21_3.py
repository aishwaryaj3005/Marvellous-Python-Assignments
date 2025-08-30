import psutil
import os
import time

def CreateLog(DirectoryName, Data):
    if not os.path.exists(DirectoryName):
        os.mkdir(DirectoryName)

    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","")
    timestamp = timestamp.replace(":","_")
    timestamp = timestamp.replace("/","_")

    FileName = os.path.join(DirectoryName, "Marvellous%s.log" %(timestamp))

    fobj = open(FileName, "w")
    fobj.write("Process Name\tPID\tUsername\n")
    fobj.write("=" * 40 + "\n")

    for proc in Data:
        fobj.write(f"{proc['name']}\t{proc['pid']}\t{proc['username']}\n")

    print("Log file created :", FileName)

def DisplayProcess():
    listprocess = []

    for proc in psutil.process_iter(['name','pid','username']):
        listprocess.append(proc.info)
    return listprocess

def main():
    DirectoryName = input("Enter name of Directory : ")
    data = DisplayProcess()
    CreateLog(DirectoryName, data)

if __name__ == "__main__":
    main()