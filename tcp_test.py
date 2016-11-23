#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from multiprocessing import Process, freeze_support

def conns(sock):
    conn, addr = sock.accept()
    while True:
        data = conn.recv(1024).rstrip("\r\n")
        if not data:
            break
        if str(data) == 'close':
            print 'YES'
            break
        # print 'data:', data
        # print 'type:', type(data)
        conn.send(data+'\n')
    # print 'closed'
    conn.close()



freeze_support()
sock = socket.socket()
sock.bind(('', 2222))
sock.listen(10)

procs = []
nproc = 10
for i in range( nproc ):
    procs.append( Process( target = conns, args = ( sock, ) ) )
for i in range( nproc ):
    procs[ i ].start()
for i in range( nproc ):
    procs[ i ].join()
# print( 'завершается родительский процесс' )
