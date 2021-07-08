
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