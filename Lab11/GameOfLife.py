import copy


def neighbours(arr, x, y):
    count = 0
    # neighbours of cells in corners
    # if x+y == 0:
    #     return arr[0][1]+arr[1][0]+arr[1][1]
    #
    # if x-1 == len(arr) and y == 0:
    #     return arr[0][-2]+arr[1][-1]+arr[1][-2]
    #
    # if x == 0 and y-1 == len(arr):
    #     return arr[-2][0]+arr[-1][1]+arr[-2][1]
    #
    # if x-1 == len(arr) == y-1:
    #     return arr[-2][-1]+arr[-1][-2]+arr[-2][-2]

    # return arr[x-1][y] + arr[x+1][y] + arr[x][y-1] + arr[x][y+1]

    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if x == i and y == j:
                continue
            else:
                count += arr[i][j]

    return count


class GameOfLife:

    def __init__(self, net_size, one_size, iterations):
        if one_size > net_size:
            raise Exception('Too small net!')
        self.net = [[1 if (net_size + one_size)//2 > i >= (net_size - one_size)//2 and
                          (net_size + one_size)//2 > j >= (net_size - one_size)//2 else 0 for i in range(net_size)]
                    for j in range(net_size)]

    def evolve(self):
        copied_list = copy.deepcopy(self.net)

        for i in range(1, len(copied_list)-1):
            for j in range(1, len(copied_list)-1):
                count = neighbours(self.net, i, j)
                if self.net[i][j] == 0 and count == 3:
                    copied_list[i][j] = 1
                if self.net[i][j] == 1:
                    if count != 2 and count != 3:
                        copied_list[i][j] = 0
        self.net = copy.deepcopy(copied_list)

    def __str__(self):
        return str([['*' if i == 1 else '.' for i in j] for j in self.net])
