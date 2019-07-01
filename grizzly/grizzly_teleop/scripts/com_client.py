#!/usr/bin/env python
# -*- coding: utf-8 -*-

'socket example which send echo message to server.'

import socket
import click

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('192.168.31.235', 50007))
# 接收欢迎消息:
print (s.recv(1024))

while True:
    # 发送数据:
    key = click.getchar()
    if key in ['i', 'o', 'j', 'l','u',',','.','m','q','z','w','x','e','c','k',' ']:
        s.send(key.encode("UTF-8"))
    elif key == 's':
        break
    else:
        continue
    print (s.recv(1024))
s.send('exit'.encode('utf-8'))
s.close()

