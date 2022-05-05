import socket
from IPy import IP

def scan(target):
    ip = checkip(target)
    print('Enter port Range to scan')
    i=int(input('Starting port= '))
    j=int(input('Endinging port= '))
    print('\n' + 'Please wait Scanning ' + str(target)+ '\'s open Ports' )
    print("Scanning...")
    for port in range(i,j):
      port_scanner(ip,port)

def gethostbynam(ip) :
    dnam= socket.gethostbyname(ip) 
    return dnam
    
def checkip(ip) :
    try :  
        IP(ip)
        return(ip)
    except ValueError :
        dname=gethostbynam(ip)
        return dname
        

def get_banner(s):
    return s.recv(1024)

def port_scanner(ip,port):
    try:
        sock=socket.socket()
        sock.settimeout(0.5)
        sock.connect((ip,port))
        
        try :
            banner=get_banner(sock)
            print('open port ' + str(port)+ ' = ' +str(banner))
        except :
            print('Port '+str(port)+ ' is Open') 
    except:
        pass
        

targets=input('Enter Target:')
if ',' in targets :
    for ipadrs in targets.split(','):
        scan(ipadrs.strip(' '))
else:
    scan(targets)

 
