'''
    Hi. this is just for the first commit.
'''


class FirstCommit():

    option_one = 'Hello world!'
    option_two = 'Good bye world!'
    yes_tuple = ('Yes', 'yes', 'y', 'Y', 'of course',
                 'sure', 'Hell ya', 'Hell Ya', 'likewise')

    def __init__(self, option_one=option_one, option_two=option_two, choice=yes_tuple):
        self.option_one = option_one
        self.option_two = option_two
        self.choice = choice

    def call_option(self, inquiry):
        return f'{self.option_one}' if inquiry in self.choice else f'{self.option_two}'


instance = FirstCommit()
inquiry = str(input('Do U want to say hi to the world?. Select Y/n: '))
print(instance.call_option(inquiry))
