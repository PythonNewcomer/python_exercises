##################################################################################
# Task:
# A robot moves in a plane starting from the original point (0,0).
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps.
# Write a program to compute the distance from current position after a sequence of movement and original point.
# If the distance is a float, then just print the nearest integer.


class Robot:

    vertical = 0
    horizon = 0

    def move_up(self):
        u = int(input('Steps UP: '))
        self.vertical += u

    def move_down(self):
        d = int(input('Steps DOWN: '))
        self.vertical -= d

    def move_left(self):
        l = int(input('Steps LEFT: '))
        self.horizon -= l

    def move_right(self):
        r = int(input('Steps RIGHT: '))
        self.horizon += r

    def compute_distance(self):
        com = self.vertical * self.horizon
        return abs(com)


robot1 = Robot()
robot1.move_up()
robot1.move_down()
robot1.move_left()
robot1.move_right()
robot1.compute_distance()


##################################################################################
# Task:
# Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.

n = input('Enter your text\n')
n_new = n.split(' ')
o_list = []
n_list = []
for word in n_new:
    amount = n_new.count(word)
    o_list.append("%s %s %s" % (word, ':', amount))

for char in o_list:
    if char not in n_list:
        n_list.append(char)

for obj in sorted(n_list):
    print(obj)


##################################################################################
# Task:
# Write a program which can map() and filter() to make a list
# whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_li = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, li)))
print(new_li)


##################################################################################
# Task:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

n = list(input('Enter your string\n'))
lower = 0
upper = 0
for char in n:
    if char.isupper() is True:
        upper += 1
    elif char.islower() is True:
        lower += 1
    else:
        pass

print("LOWER: ",lower,"\nUPPER: ",upper)


##################################################################################
# Task:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

n = list(input('Enter your string\n'))
letter_result = 0
digit_result = 0
for char in n:
    if char.isdigit() is True:
        digit_result += 1
    elif char.isalpha() is True:
        letter_result += 1

print("DIGITS: ", digit_result, "\nLETTERS: ", letter_result)


##################################################################################
# Task:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

def sum_values(n):
    f_num = int("%s%s" % (n, n))
    s_num = int("%s%s%s" % (n, n, n))
    th_num = int("%s%s%s%s" % (n, n, n ,n))
    sum_nums = n + f_num + s_num + th_num
    return sum_nums


sum_values(8)


##################################################################################
# Task:
# Write a program which accepts a sequence of words separated by whitespace as input
# to print the words composed of digits only.

def find_digit(text):
    digit_list = []
    for char in text:
        if char.isdigit() is True:
            digit_list.append(char)
    print(digit_list)


find_digit('2 cats 5 and 3 dogs.')


##################################################################################
# Task:
# Write a program using generator
# to print the even numbers between 0 and n in comma separated form
# while n is input by console.

n = int(input('Enter your number\n'))
gen_dig_list = []


def even_gen(n):
    for digit in range(0, n+1):
        if digit % 2 == 0:
            yield digit


for number in even_gen(n):
    gen_dig_list.append(str(number))

print(",".join(gen_dig_list))


##################################################################################
# Task:
# Please write a binary search function which searches an item in a sorted list.
# The function should return the index of element to be searched in the list.

dig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = int(input("Your item\n"))


def search_int(n, list):
    for digit in list:
        if digit == n:
            return list.index(digit)


search_int(n, dig_list)


##################################################################################
# Task:
# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
new_list = []
for col in color_list:
    if color_list.index(col) != 0 and color_list.index(col) != 4 and color_list.index(col) != 5:
        new_list.append(col)
print(new_list)


##################################################################################
# Task:
# Write a Python program to generate and print a list of first and last 5 elements
# where the values are square of numbers between 1 and 30 (both included).

new_list = []
for n in range(1, 31):
    sq = n**n
    new_list.append(sq)
print(new_list[0:5] + new_list[-5:-1])


##################################################################################
# Task:
# Write a Python program to count the number of strings where the string length is 2 or more
# and the first and last character are same from a given list of strings.

char_list = ['abc', 'xyz', 'aba', '1221']
new_list = []
for c in char_list:
    if len(c) > 2:
        if c[0] == c[-1]:
            new_list.append(c)
print(new_list)


##################################################################################
# Task:
# Take two lists, say for example these two:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common
# between the lists (without duplicates). Make sure your program works on two lists of different sizes.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 12, 12]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for num in a:
    if num in b:
        if num not in c:
            c.append(num)
print(c)


##################################################################################
# Task:
# Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9

n = input('Enter your string\n')
new_n = [num for num in n.split(',') if int(num) % 2 == 0]
print(",".join(new_n))


##################################################################################
# Task:
# Write a program that accepts a sequence of whitespace separated words as input and
# prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

n = input('Enter your words\n')
new_n = n.split(' ')
s = list(sorted(set(new_n)))
new_s = " ".join(s)
print(new_s)


####################################################################################
# Task:
# Write a program that accepts a comma separated sequence of words as input and
# prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

n = str(input('Enter your words\n'))
new_n = sorted(n.split(','))
print(new_n)

####################################################################################