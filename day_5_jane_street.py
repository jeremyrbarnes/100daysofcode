'''
cons(a, b) constructs a pair, and car(pair)
and cdr(pair) returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
'''


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(p):
    if p is not None:
        return p.__closure__[0].cell_contents
    return None


def cdr(p):
    if p is not None:
        return p.__closure__[1].cell_contents
    return None


print(car(cons(3, 4)))
print(cdr(cons(3, 4)))
