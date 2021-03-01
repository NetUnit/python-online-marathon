from abc import ABC, abstractmethod


'''
    According tp the test:

    ## get_dish(): should take: "main/dessert" !
    ## get factory(): "italian/french' !
'''


class Product(ABC):

    @abstractmethod
    def cook(self):
        pass


class FettuccineAlfredo(Product):

    meal1 = "Fettuccine Alfredo";
    def __init__(self, meal1=meal1):
        self.meal1 = meal1
    
    def cook(self):
        print(f"Italian main course prepared: {self.meal1}")


class Tiramisu(Product):
    
    meal2 = "Tiramisu";

    def __init__(self, meal2=meal2):
        self.meal2 = meal2
 
    def cook(self):
        print(f"Italian dessert prepared: {self.meal2}")


class DuckALOrange(Product):

    meal1 = "Duck À L'Orange";

    def __init__(self, meal1=meal1):
        self.meal1 = meal1
    
    def cook(self):
        print(f"French main course prepared: {self.meal1}")


class CremeBrulee(Product):

    meal2 = "Crème brûlée";

    def __init__(self, meal2=meal2):
        self.meal2 = meal2
    
    def cook(self):
        print(f"French dessert prepared: {self.meal2}")


class Factory(ABC):

    @abstractmethod
    def get_dish(type_of_meal):
        pass


class ItalianDishesFactory(Factory):
    
    def __init__(self, type_of_meal=0):
        self.type_of_meal = type_of_meal

    def get_dish(type_of_meal):

        if type_of_meal == 'main':
            return FettuccineAlfredo()
        
        if type_of_meal == 'dessert':
            return Tiramisu()


class FrenchDishesFactory(Factory):
    
    def __init__(self, type_of_meal=0):
        self.type_of_meal = type_of_meal

    def get_dish(type_of_meal):

        if type_of_meal == 'main':
            return DuckALOrange()
        if type_of_meal == 'dessert':
            return CremeBrulee()


class FactoryProducer:

    factory1 = 'italian';
    factory2 = 'french';

    def __init__(self, type_of_factory=0, factory1=factory1,  factory2=factory2 ):
        self.type_of_factory = type_of_factory

    def get_factory(self, type_of_factory):
        if type_of_factory == self.factory1:
            return ItalianDishesFactory

        if type_of_factory == self.factory2:
            return FrenchDishesFactory


### tests SS
fp = FactoryProducer()
fac = fp.get_factory("italian")

### set1
main_dish = fac.get_dish("main")
main_dish.cook()

### set 2
dessert = fac.get_dish("dessert")
dessert.cook()

### set 3
fac1 = fp.get_factory("french")
main_dish = fac1.get_dish("main")
main_dish.cook()

### set 4
dessert = fac1.get_dish("dessert")
dessert.cook()