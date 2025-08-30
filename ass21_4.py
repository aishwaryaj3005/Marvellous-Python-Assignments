import os
import psutil
import time
from email.message import EmailMessage
import smtplib

def CreateLog(DirectoryName, Data):
    if not os.path.exists(DirectoryName):
        os.mkdir(DirectoryName)

    timestamp = time.ctime()
    timestamp = timestamp.replace(" ", "")
    timestamp = timestamp.replace(":", "_")
    timestamp = timestamp.replace("/", "_")

    FileName = os.path.join(DirectoryName, "Marvellous%s.log" %(timestamp))

    fobj = open(FileName, "w")
    fobj.write("Process Name\tPID\tUsername\n")
    fobj.write("=" * 40 + "\n")

    for proc in Data:
        fobj.write(f"{proc['name']}\t{proc['pid']}\t{proc['username']}\n")
        
    return FileName

def DisplayProcess():
    listProcess = []

    for proc in psutil.process_iter(['name','pid','username']):
        listProcess.append(proc.info)
    return listProcess

def SendEmail(SenderMail, AppPassword, ReceiverMail, FilePath):
    msg = EmailMessage()
    msg ['Subject'] = "Process Log File"
    msg['From'] = SenderMail
    msg['To'] = ReceiverMail
    msg.set_content("Attached is the Process Log File.")

    fobj = open(FilePath, "rb")
    FileData = fobj.read()
    FileName = os.path.basename(FilePath)

    msg.add_attachment(FileData, maintype='application', subtype='octet-stream', filename=FileName)

    smpt = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smpt.login(SenderMail, AppPassword)
    smpt.send_message(msg)
    smpt.quit()

    print("Email send sucessfully..!")

def main():
    DirectoryName = input("Enter the name of Directory : ")
    SenderMail = input("Enter your Gmail : ")
    AppPassword = input("Enter your Gmail App Password : ")
    ReceiverMail = input("Enter receiver mail : ")

    Data = DisplayProcess()
    LogFile = CreateLog(DirectoryName, Data)
    SendEmail(SenderMail, AppPassword, ReceiverMail, LogFile)

if __name__ == "__main__":
    main()