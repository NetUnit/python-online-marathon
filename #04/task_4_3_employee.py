'''
    Create a class Employee that will take a full name
     as argument, as well as a set of none, one or more keywords. 

    Each instance should have a name and a lastname attributes plus
     one more attribute for each of the keywords, if any.
'''


class Employee:

    def __init__(self, full_name, *args, **kwargs):

        self.__dict__.update(kwargs)
        self.full_name = full_name
        arguments = {'salary': 0, 'height': 0, 'nationality': 0}
        arguments.update(kwargs)
        self.attributes = arguments
        self.salary = arguments['salary']
        self.height = arguments['height']
        self.natioanality = arguments['nationality']
        self.name = full_name.split(' ')[0]
        self.lastname = full_name.split(' ')[1]

    def initialize_attr(self):
        return self.name


john = Employee('John Doe')
print(john.lastname)

mary = Employee("Mary Major", salary=120000)
print(mary.salary)

richard = Employee("Richard Roe", salary=110000, height=178)
print(richard.salary)
print(richard.height)

giancarlo = Employee("Giancarlo Rossi", salary=115000,
                     height=182, nationality="Italian")
print(giancarlo.name)
print(giancarlo.natioanality)


peng = Employee('Peng Zhu', salary=500000, height=185, nationality='Chinese',
                subordinates=[i.lastname for i in (john, mary, richard, giancarlo)])
print(peng.subordinates)

kwang = Employee('Jiang Jing', salary=20000, height=169, nationality='Chinese', lst=[
                 i.natioanality for i in (john, mary, richard, giancarlo)])
print(kwang.lst)
