# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Jane Street.
#
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
#
# Given this implementation of cons:
#
# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
#
# Implement car and cdr.

def cons(a, b):
    def pair(f):
        return f(a, b)
    
    return pair


def cdr(pair: cons):
    def return_last(a, b):
        return b
    return pair(return_last)


def car(pair: cons):
    def return_first(a, b):
        return a
    return pair(return_first)


if __name__ == "__main__":
    assert car(cons(3, 4)) == 3
    assert cdr(cons(3, 4)) == 4