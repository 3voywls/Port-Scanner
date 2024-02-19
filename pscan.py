from socket import *
import time
import threading
import pyfiglet

def connectionScan(targetHost, targetPort):
    
    try:
        connection=socket(AF_INET, SOCK_STREAM) # Creates a new socket object (connection) using the socket() function from the socket module. The AF_INET parameter specifies that we're going to use IPv4 addresses, and SOCK_STREAM specifies that we want to use a TCP connection.
        connection.connect((targetHost, targetPort))
        print('[+] %d/tcp open'% targetPort)
        connection.close()
    except:
        print('[-] %d/tcp closed'% targetPort)

def portScan(targetHost, targetPorts):
    
    try:
        targetIP = gethostbyname(targetHost)
    except:
        print('[-] Cannot resolve %s'% targetHost)
        return

    try:
        targetName = gethostbyaddr(targetIP)
        print('[~] Scan result of %s'% targetName[0])
    except:
        print('[~] Scan result of %s'% targetIP)

    setdefaulttimeout(1)

    for targetPort in targetPorts:
        print('\n[~] Scanning Port: %d'% targetPort)
        # thread = threading.Thread(target= connectionScan, args= (targetHost,targetPort))
        # thread.start()
        connectionScan(targetHost,targetPort)


if __name__ == '__main__':
    ascii_banner=pyfiglet.figlet_format('PORT SCANNER')
    print(ascii_banner)
    print('-'*70)
    print('Port Scanner by Suhail')
    print('-'*70)
    startTime = time.time()
    portScan('google.com', [80,22,33,44,1,2,3,4,4,5,443]) #Edit arguments (host,ports)
    endTime = time.time()
    print('\nTime elapsed:',endTime-startTime,'s')