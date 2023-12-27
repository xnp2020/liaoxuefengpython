#!/usr/bin/env python
# coding=utf-8

filepath = r'C:\Users\xnp2010\Desktop\工作计划.txt'
with open(filepath, 'r', encoding='utf-8') as f:
    s = f.read()
    print(s)
