# 自实现str2int
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


# 自实现str2float
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2float(s):
    if '.' in s:
        index = s.index('.')
        needdivideby10 = len(s)-index-1   # 或者这样取 needdivideby10 = s[::-1].index('.')
        s = s.replace('.','')
    else:
        needdivideby10=0
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))/(10**needdivideby10)