import matplotlib.pyplot as plt


def zad1(n=1, pattern="F+F-F-F+F"):
	transformedPattern = pattern
	for i in range(n):
		transformedPattern = transformedPattern.replace("F", pattern)

	print(len(transformedPattern))
	x, y = 0, 0
	coordinates = [[x, y]]
	left = [[1, 0], [-1, 0], [0, -1], [0, 1]]
	right = [[0, -1], [-1, 0], [0, 1], [1, 0]]

	for i in transformedPattern:
		if i == '-':
			x -= 1

			coordinates.extend([])


def zad2(roman):
	dictionary = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100,
	'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
	arab = 0
	for i in range(len(roman)-1):
		if dictionary[roman[i]] >= dictionary[roman[i+1]]:
			arab += dictionary[roman[i]]
		else:
			arab -= dictionary[roman[i]]
	arab += dictionary[roman[-1]]
	return arab


def zad3(arab):
	dictionary = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
				90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
	roman = ""
	for i in dictionary:
		while arab - i >= 0:
			roman += dictionary[i]
			arab -= i
	return roman


if __name__ == '__main__':
	pass
