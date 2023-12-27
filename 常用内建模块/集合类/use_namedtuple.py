# namedtuple
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)

print(p, p.x, p.y)

isinstance(p, Point)
isinstance(p, tuple)
