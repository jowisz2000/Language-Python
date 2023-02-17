import datetime


def pesel(num, date, gender):
    '''

    :param num: number to check
    :param date: date of borth
    :param gender: obvious
    '''
    controlsum = 0
    scales = [1, 3, 7, 9]
    for i in range(len(num)-1):
        controlsum += int(num[i]) * scales[i % 4]
    controlsum %= 10

    if (10 - controlsum) % 10 != int(num[-1]):
        raise Exception("Invalid control sum!")

    monthWages = [[80, 1800], [60, 2200], [40, 2100], [20, 2000], [0, 1900]]
    month = int(num[2:4])
    year = int(num[0:2])

    for i in monthWages:
        if month > i[0]:
            year += i[1]
            month -= i[0]
            break

    if month != date.month or year != date.year:
        raise Exception("Invalid date!")

    if int(num[9]) % 2 and gender == 'K' or int(num[9]) % 2 == 0 and gender == 'M':
        raise Exception("Invalid gender!")


# pesel("02070803628", datetime.date(1902, 7, 8), 'K')
# pesel("02070803624", datetime.date(2002, 7, 8), 'K')
# pesel("02270812350", datetime.date(2002, 7, 8), 'M')

def correct_date(date):
    '''
    :param date: format: [DD, MM, YYYY]
    :return: True if date is correct, otherwise False
    '''

    if len(date) != 3:
        return False

    month_length = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if int(date[0]) > month_length[int(date[1])]:
        # raise Exception('Invalid length of month!')
        return False

    if int(date[1]) == '2':
        if int(date[2]) % 4 == 0 and (int(date[2]) % 100 == 0 or int(date[2]) % 400):
            # raise Exception('Invalid length of February!')
            return False

        elif int(date[0]) > 28:
            # raise Exception('Invalid length of February!')
            return False

    return True


def zad2(mode):
    # 0 - strict mode, 1 - light mode
    '''

    :param mode: 0 - light mode, 1 - throws exceptions after every invalid date
    :return: average age
    '''

    with open("data.in") as file:

        avg, count = 0, 0
        for i in file.readlines():
            date = i.split()
            if len(date) != 3 and mode == 0:
                raise Exception("Invalid length of date!")

            if correct_date(date):
                avg += int(date[-1])
                count += 1
            elif mode == 0:
                raise Exception("Invalid date!")

        return datetime.datetime.now().year - avg/count

# print(zad2(1))


def zad3(lst):

    triple = []
    quadruples = []
    if len(lst) < 3:
        raise Exception("Invalid list size!")

    for i in range(len(lst)-2):
        if lst[i]**2 + lst[i+1]**2 == lst[i+2]**2:
            triple.extend([lst[i], lst[i+1], lst[i+2]])

    for i in range(len(lst)-3):
        if lst[i]**2 + lst[i+1]**2 + lst[i+2]**2 == lst[i+3]**2:
            triple.extend([lst[i], lst[i+1], lst[i+2], lst[i+3]])

    if not triple:
        raise Exception('No triples!')

    if not quadruples:
        raise Exception('No quadruples!')

# zad3([1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,
      # 5,14,15,2,10,11,15,1,12,12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,1])

zad3([3,4,5,6,7,8,9])