'''
    Create function create with one string argument. 
    This function should return anonymous function that 
    checks if the argument of function is equals to the 
    argument of outer function. 
'''


# var1 anonymous
def create(password):
    
    x = lambda x: password == x
    return x

tom = create("pass_for_Tom")


print(tom('pass_for_Tom')) # True
print(tom('pass_for_tom')) # False


# var2 closure
def create(password):

    def check(psw):
        return password == psw

    return check

tom = create("pass_for_Tom")


print(tom("pass_for_Tom")) # True
print(tom("pass_for_tom")) # False


