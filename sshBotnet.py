import pexpect

PROMPT = ['#', "%", ">>> ", ">", '$', "\r\n","\$", pexpect.EOF]

def send_command(child, cmd):
    child.logfile = open("blok.txt", "wb")
    child.sendline(cmd)
    child.expect("tcpdump")
    print(child.before.decode("utf-8"))

def connect(user, host, password):
    ssh_existing = f"{user}@{host}'s password: "
    connStr = f"ssh {user}@{host}" 
    child = pexpect.spawn(connStr)
    returns = child.expect([pexpect.TIMEOUT, ssh_existing,"[P|p]assword:"])
    if returns == 0 :
        ## returns time out
        print(f"[-] Error Connecting")
        return
    if returns == 1:
        child.sendline(password)
        returns = child.expect("login:")
        return child

def main() :
    host="kali"
    user = "root"
    password = "kali"
    child = connect(user, host, password)
    cmd = ("cat /etc/passwd")
    send_command(child, cmd)

if __name__ == "__main__":
    main()
