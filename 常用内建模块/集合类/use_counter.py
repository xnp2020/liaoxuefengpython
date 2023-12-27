# Counter是一个简单的计数器

from collections import Counter

c = Counter()
for i in 'programming':
    c[i] = c[i] + 1

print(c)
c.update('hello')
print(c)

list1 = [1, 2, 1, 3, 1, 5, 9, 2, 8, 6, 7, 33, 5, 10]
c2 = Counter()
for i in list1:
    c2[i] = c2[i] + 1

print(c2)
print(dict(c2))
