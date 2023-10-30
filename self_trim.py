# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法

# -*- coding: utf-8 -*-
def trim(s):
    if s == '':
        return s
    while s[0] == ' ' and len(s) > 1:
        s = s[1:]
        
    while s[-1] == ' ' and len(s) > 1:
        s = s[:-1]
    
    if s == ' ':
        s=''
    return s


def trim(s):

    if s[-1:]==' ' :

        return trim(s[:-1])

    elif s[:1]==' ':

        return trim(s[1:])

    else:

        return s

