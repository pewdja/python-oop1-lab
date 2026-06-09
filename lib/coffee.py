#!/usr/bin/env python3

class Coffee:
    valid_sizes = ("Small", "Medium", "Large")

    def __init__(self, size, price):
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size in self.valid_sizes:
            self._size = size
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1
