class MyError(Exception):
    error = "You input negative number: . Try again."

    def __init__(self, error=error):
        self.error = error

    def __str__(self):
        return str(self.error)


def check_positive(number):

    def trigger(MyError): raise MyError

    try:
        number = float(number)
        return f"You input positive number: {number}" if number > 0 else trigger(MyError)
    except ValueError:
        return "Error type: ValueError!"
    except MyError as er:
        er = str(er)
        return er[:er.index('.')] + str(number) + er[er.index('.'):]


# testset#1 - float
# print(check_positive(8.9)) # 'You input positive number: 8.9' # ✓
# print(check_positive(-19)) # You input negative number: -19.0. Try again. # ✓ NOTE in test1 - 19
# print(check_positive(0.7)) # You input positive number: 0.7 # ✓
# print(check_positive(-0.6)) # You input negative number: -0.6. Try again. # ✓
# print(check_positive("45")) # You input positive number: 45.0 # ✓
# print(check_positive("-235")) # You input negative number: -235.0. Try again. # ✓

# testset#2 - integers
# NOTE test 2 contradicts condition test2 from testset #1

# test1
# "You input positive number: 24" # mine ✓
# "You input positive number: 24" # ss ✓
# print(check_positive(24))  # output:    "You input positive number: 24" # + ok

# test 2
# "You input negative number: -19. Try again." # mine ✓
# "You input negative number: -19. Try again." # ss ✓
# print(check_positive(-19))

# test 3
# "You input positive number: 38" # mine ✓
# "You input positive number: 38" # ss ✓
# print(check_positive("38"))

# test 4
# "Error type: ValueError!" # mine ✓
# "Error type: ValueError!" # ss ✓
# print(check_positive("abc"))  # output:     "Error type: ValueError!" # + ok

# test 5
# You input negative number: -38. Try again. # mine ✓
print(check_positive("-38"))
