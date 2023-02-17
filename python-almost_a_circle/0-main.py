#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    b1 = Base(None)
    print(b1.id)

    b2 = Base(None)
    print(b2.id)

    b3 = Base({"a": 1, "b": 2})
    print(b3.id)

    b4 = Base(None)
    print(b4.id)

    b5 = Base((1, 2, 3))
    print(b5.id)
