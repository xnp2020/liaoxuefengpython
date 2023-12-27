#!/usr/bin/env python3
# coding=utf-8

import re
from datetime import datetime, timedelta, timezone


def to_timestamp(dt_str, tz_str):
    tz = re.match(r'UTC([\+|\-][0-1]?[0-9])', tz_str).group(1)
    tz_utc = timezone(timedelta(hours=int(tz)))
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    dt_real = dt.replace(tzinfo=tz_utc)
    return dt_real.timestamp()


print(to_timestamp('2023-11-20 3:11:00', 'UTC-1:00'))

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
