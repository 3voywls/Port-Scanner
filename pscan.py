# Import necessary modules
from socket import *
import time
import threading
import pyfiglet

# Function to scan a single port on a given host
def connectionScan(targetHost, targetPort):
    try:
        # Create a socket object and establish a TCP connection to the target host and port
        connection = socket(AF_INET, SOCK_STREAM)
        connection.connect((targetHost, targetPort))
        # Print an open port message if connection succeeds
        print('[+] %d/tcp open' % targetPort)
        connection.close()
    except:
        # Print a closed port message if connection fails
        print('[-] %d/tcp closed' % targetPort)

# Function to scan multiple ports on a given host
def portScan(targetHost, targetPorts):
    try:
        # Resolve the target host to its IP address
        targetIP = gethostbyname(targetHost)
    except:
        # Print an error message if host resolution fails
        print('[-] Cannot resolve %s' % targetHost)
        return

    try:
        # Attempt to get the hostname associated with the target IP address
        targetName = gethostbyaddr(targetIP)
        print('[~] Scan result of %s' % targetName[0])
    except:
        # Print the target IP address if hostname resolution fails
        print('[~] Scan result of %s' % targetIP)

    # Set a timeout for socket operations
    setdefaulttimeout(1)

    # Iterate through each target port and perform a scan
    for targetPort in targetPorts:
        print('\n[~] Scanning Port: %d' % targetPort)
        # Call the connectionScan function to scan the current port
        connectionScan(targetHost, targetPort)

# Main function
if __name__ == '__main__':
    # Generate ASCII art banner
    ascii_banner = pyfiglet.figlet_format('PORT SCANNER')
    print(ascii_banner)
    print('-' * 70)
    print('Port Scanner by Suhail')
    print('-' * 70)
    
    # Record start time
    startTime = time.time()
    
    # Perform port scanning on google.com with specified ports
    portScan('google.com', [80, 22, 33, 44, 1, 2, 3, 4, 4, 5, 443])
    
    # Record end time
    endTime = time.time()
    
    # Calculate and print elapsed time
    print('\nTime elapsed:', endTime - startTime, 's')
