import paramiko
import time
import pandas as pd
import openpyxl




print('Hello, this script will help you to print output from your network or server devices into excel\n')
print('This script using paramiko and can connect to device that support ssh connection only.\n')




def converTxt2excel ():
    data = pd.read_csv('version.txt', on_bad_lines='skip', skip_blank_lines=True)
    data.to_excel('version.xlsx', 'Sheet1')
    print('file converted to excel successfully')


def savetofile(output):
    with open('version.txt', 'w') as file:
        file.write(output.decode("ascii").strip())
        file.close()
        print("file created")



def paramiko_ssh_connection(ip,password,username):
    # create ssh se session using paramiko
    SESSION = paramiko.SSHClient()
    SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    SESSION.connect(ip, port=22, username=username, password=password,look_for_keys=False,allow_agent=False) #ssh connection


    DEVICE_ACCESS = SESSION.invoke_shell()
    # DEVICE_ACCESS.send(b'terminal length 0\n') if your device support this command so remove the #

    DEVICE_ACCESS.send(command + '\n')
    time.sleep(3)


    output = DEVICE_ACCESS.recv(65000)
    print(output.decode("ascii").strip())
    return output


if __name__ == '__main__':
    ip = input('Please provide ip: ')
    password = input('please punch your password: ')
    username = input('please punch your username: ')
    command = input(b'please enter your command: ')
    output = paramiko_ssh_connection(ip,password,username)
    savetofile(output)
    converTxt2excel()