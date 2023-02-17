import glob
import numpy
import string
import matplotlib.pyplot as plt


def zad1(name, n):
    with open(name) as tmp:
        lst = tmp.readlines()
        print(lst[:n])  # first n lines
        print(lst[n-1:])  # last n lines
        print(lst[::n])  # every n-th line
        print(list(_[n] for _ in lst))  # n-th character in each line
        print(list(_.split()[n] for _ in lst))  # every n-th word in each line


# zad1("example.txt", 3)


def zad2():
    values = []
    for file in glob.glob("data*.in"):
        with open(file) as tmp:
            values.append([float(i) for i in tmp.readlines()])

    avg = list(map(numpy.average, zip(*values)))
    std = list(map(numpy.std, zip(*values)))

    with open('toSave.txt', 'w') as toSave:
        for i in range(len(avg)):
            toSave.write(f'{i+1}\t {avg[i]}\t {std[i]}\n')


def zad5():
    words = []
    for file in glob.glob('zad5*.in'):
        with open(file) as tmp:
            for i in tmp.readlines():
                words.extend(i.split())

    dictionary = {}

    for j in words:
        if j[0] in string.ascii_letters:
            dictionary[j[0].upper()] = dictionary.get(j[0].upper(), 0) + 1

    # sort by letters
    byLetters = dict(sorted(dictionary.items(), key=lambda i: i[1], reverse=True))
    plt.bar(byLetters.keys(), byLetters.values())
    plt.savefig("byLetters.png")
    plt.close()

    # sort by number of occurences
    byCount = dict(sorted(dictionary.items()))
    print(byCount)
    plt.bar(byCount.keys(), byCount.values())
    plt.savefig("byCount.png")
    plt.close()


zad5()
