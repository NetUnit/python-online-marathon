import datetime
import string as st
import calendar
import time


'''
    In order tu use short hand syntax and avoid
    if, elif statements 3 messages where assighned.

'''


def check_odd_even(number):
    message1 = "Entered number is even"
    message2 = "Entered number is odd"
    message3 = "You entered not a number."
    try:
        case1 = any(map(lambda x: int(x) % 2 == 0, [number]))
        case2 = any(map(lambda x: int(x) % 2 == 1, [number]))
        return message1 if case1 else message2
    except (ValueError, TypeError) as error:
        error = message3
        return message3


# case1 number is even
# print(check_odd_even(10)) # + ok

# case2 number is str but all r digits
# when not converting x to int - raise TypeError
# print(check_odd_even('10')) # + ok

# case when incorrect data is set up to the list
# print(check_odd_even('just a string')) # + ok # You entered not a number.

# case when the data is object - Own Exception # if b
# print(check_odd_even(y)) # + ok Type Error

# tests Soft Serve
# test 1 - number is even
# print(check_odd_even(24)) # + ok even

# test 2 - number is odd
# print(check_odd_even(19))
