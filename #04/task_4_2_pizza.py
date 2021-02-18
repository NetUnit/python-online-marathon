'''
    Create a Pizza class with the attributes order_number and ingredients
    (which is given as a list). Only the ingredients will be given as input.

    You should also make it so that its possible to choose a ready made pizza 
    flavour rather than typing out the ingredients manually! As well as creating
    this Pizza class, hard-code the following pizza flavours.
'''


class Pizza:

    order_number = 0

    haw = ['ham', 'pineapple']
    meat_fest = ['beef', 'meatball', 'bacon']
    gard_feast = ['spinach', 'olives', 'mushroom']

    def __init__(self, ingredients=0):
        Pizza.order_number += 1
        self.ingredients = ingredients
        self.order_number = Pizza.order_number

    def hawaian(haw=haw):
        return Pizza(haw)

    def meat_festival(meat_fest=meat_fest):
        return Pizza(meat_fest)

    def garden_feast(gard_feast=gard_feast):
        return Pizza(gard_feast)


# preselected
p1 = Pizza(["bacon", "parmesan", "ham"])  # +
print(p1.ingredients)

# ready-made
# hawaian
p2 = Pizza.hawaian()  # +
print(p2.ingredients)

# meat_festival
p3 = Pizza.meat_festival()  # +
print(p3.ingredients)

# garden_feast
p4 = Pizza.garden_feast()  # +
print(p4.ingredients)

# orders
print(p1.order_number)  # 1 +
print(p2.order_number)  # 2 +
print(p3.order_number)  # 3 +
print(p4.order_number)  # 4 +
