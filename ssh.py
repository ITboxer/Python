#!/usr/bin/python2.7
import paramiko                                    #ssh lib

ssh = paramiko.SSHClient()                         #set up ssh client
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  #This will add the host key if you are connecting to a server for the first time

try:                                               # try to make a connection
    ssh.connect('localhost', username='kali', password='kali')
    sdtin, stdout, stderr = ssh.exec_command('cat /etc/passwd') # execute code
    for line in stdout.readlines():
            print line.strip()      # print out the output
    ssh.close()                                     # close the connection
except:                                             # if no connection is made then pass
    pass
finally:
    exit(0)
