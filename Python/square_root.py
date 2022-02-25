import math

def square_root(n):
    if (n < 0 or not isinstance(n, int)):
        return -1
    return n**0.5


def test():
    assert square_root(4) == 2
    assert square_root(0) == 0
    assert square_root("hello") == -1
    assert square_root(-10) == -1
    print("Success!")

if __name__ == "__main__":
    test()
