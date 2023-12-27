def createCounter():
    x = 0
    def counter():
        nonlocal x
        x = x + 1
        return  x
    return counter