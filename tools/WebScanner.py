import socket
import sys
import subprocess

#function to get the ip address
def get_ip(ip):
    if len(sys.argv) == 2:
        ipaddress= socket.gethostbyname(ip)
        print('IP ADDRESS:',ipaddress)
        return ipaddress
    else:
        print('wrong parameters write only the domain name of the website')

#function to do a port scanner
def portscanner(ip):
    print('web scanning..')
    subprocess.call(['nikto -h '+ip], shell=True)
    
#main of the program
def main():
    #ip = input()
    portscanner(get_ip(sys.argv[1]))
main()
