import itertools
from collections.abc import Iterable, Iterator

# count
natuals = itertools.count(1)
print(isinstance(natuals, Iterable))
print(isinstance(natuals, Iterator))
next(natuals)


# cycle
cs = itertools.cycle('ABC')
next(cs)

# repeat
ns = itertools.repeat('ABC', 3)
next(ns)

# takewhile
natuals_limit = itertools.takewhile(lambda x: x <= 10, natuals)
list(natuals_limit)

# chain
cc = itertools.chain('ABC', '123')
print(list(cc))

# groupby
g = itertools.groupby('AaaBBBCCAAAA')
for key, group in g:
    print(key, list(group))

gg = itertools.groupby('AaaBBBCCAAAA', lambda x: x.upper())
for key, group in gg:
    print(key, list(group))
