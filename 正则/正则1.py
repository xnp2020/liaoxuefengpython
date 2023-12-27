#!/usr/bin/env python3
# coding = utf-8

import re


def is_valid_email(addr):
    if re.match(r'[a-zA-Z\.]+@[a-zA-Z]+\.[a-zA-Z]+', addr):
        return True


assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


def name_of_email(addr):
    m = re.match(r'<?([\w\s]*?)>?\s?([\w]+)@[\w]+\.[\w]+', addr)
    if m.group(1):
        return m.group(1)
    else:
        return m.group(2)


# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
