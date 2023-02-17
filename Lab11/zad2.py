
class Array:

    def __init__(self, size, *arguments):
        if size < len(arguments):
            raise Exception("Too many arguments!")
        self.array = [i for i in arguments]

    def __add__(self, other):
        return [i+other for i in self.array]

    __iadd__ = __add__

    def __getitem__(self, item):
        return self.array[item]

    def __setitem__(self, key, value):
        self.array[key] = value

    def __str__(self):
        return self.array


if __name__ == '__main__':
    pass
