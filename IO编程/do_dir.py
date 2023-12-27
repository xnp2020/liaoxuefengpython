#!/usr/bin/env python3
# coding=utf-8

from datetime import datetime
import os

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for i in os.listdir(pwd):
    size = os.path.getsize(i)
    mtime = datetime.fromtimestamp(
        os.path.getmtime(i)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(i) else ''
    print(f'{size:10}  {mtime}  {i}{flag}')
