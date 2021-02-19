
class ToSmallNumberGroupError(Exception):

    ''' 
        if there will be an attribute in __str__() 
        it obviously expects a string to be returned, 
        so we nned to make sure not to send any other data types
        here we didn't put nay kind of it, however insert ready-made to the body

        <class 'float'> is posiible as a parameter too
    '''

    message = "We obtain error: Number of your group can't be less than 10"

    def __init__(self, message=message):
        self.message = message

    def __str__(self):
        return str(self.message)


def check_number_group(number):

    tricky_digits = all([i.isdigit() for i in str(number)]) or isinstance(
        number, int) or isinstance(number, float)

    if not tricky_digits:
        return "You entered incorrect data. Please try again."
    else:
        number = int(number)
        pass

    comparison = number > 10

    try:
        if not comparison:
            raise ToSmallNumberGroupError

        if comparison:
            return "Number of your group %d is valid" % number

    except ToSmallNumberGroupError as err:
        return f'{err}'


# checking float number
number = 25.0  # ok +           #output:
print(check_number_group(number))

# tests Soft serve:
# ok +             #output  "We obtain error: Number of your group can't be less than 10
print(check_number_group(4))

# ok               #output:     "Number of your group 59 is valid"
print(check_number_group(59))

# ok             #output:    "Number of your group 25 is valid"
print(check_number_group("25"))

# ok           #output:     "You entered incorrect data. Please try again."
print(check_number_group("abc"))
