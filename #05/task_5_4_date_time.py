import datetime
import string as st
import calendar
import time


'''
    In this peace of code i tried to distinguish 
    TypeError and ValueError in line with the next conditions:
        1) Posibbly if there is a representation of diigits in string format though,
            we can use built-in func int()
        2) int can take int(), but when it's not intgegers inside or at least one is 
        not integer it'll raise an exception:
            ValueError (int() argument must be a string, a bytes-like object or a number, not 'list')

    As we reached 'time', 'datetime' modules did a little latency as well in raws: 40, 47, 50
    So when we launch the code it is executing "smoothly" ;)

        3) Another thing I tried to use an instance of the class as a variable,
            so that a class A has been created.
'''


class A:

    def __init__(self, x):
        self.x = x

    def set_class(self):
        return A(x)


# arbitrary variable
y = A(12)


def day_of_week(day):
    try:
        name_day = dict(enumerate((calendar.day_name), 1))
        if str(day) in st.octdigits[1:]:
            time.sleep(0.5)
            return name_day[int(day)]
        if not int(day) in tuple(name_day.keys()) and isinstance(int(day), int):
            raise KeyError
        else:
            pass
    except KeyError:
        time.sleep(0.5)
        return "There is no such day of the week! Please try again."
    except (ValueError, TypeError):
        time.sleep(0.5)
        return "You did not enter a number! Please try again."


# tests Soft Serve
# test 1 - number in the range of digits
day = 2
print(day_of_week(day))  # + ok # Tuesday

# test 2 - number in the range of digits but str
day = '2'
print(day_of_week(day))  # + ok # Tuesday

# test 3 - number out of range of digits
day = 8
# + ok # There is no such day of the week! Please try again.
print(day_of_week(day))

# test 4 - number out of range of digits and str
day = '8'
# + ok # There is no such day of the week! Please try again.
print(day_of_week(day))

# test 5 - digit out of range (zero)
day = 0
# + ok # There is no such day of the week! Please try again.
print(day_of_week(day))

# test 6 - name of the day ValueError
day = "Monday"
print(day_of_week(day))  # + ok # You did not enter a number...

# test 7 - in a case of list
# day = [1, 2, 3][0]   # Monday # + ok # Monday
day = [1, 2, 3]  # TypeError # + ok # You did not enter a number...
print(day_of_week(day))

# test 8 - in case of value is an object
day = y  # instance of the class A  + ok
print(day_of_week(day))
