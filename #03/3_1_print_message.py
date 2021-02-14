'''
    Create function with name outer(name). This function should return inner function
    with name inner. This inner function prints message Hello <anme>!
'''


def outer(name):

    def inner():
        message = f'Hello, {name}!'
        print(message)
    
    return inner

tom = outer("tom")
tom()
