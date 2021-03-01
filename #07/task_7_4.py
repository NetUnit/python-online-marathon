from __future__ import annotations
from abc import ABC, abstractmethod
import time


'''
    ### ver1
    According to the task condition:
    subclasess possess 2 operations:
    so that in my solution: launch() and 
    wash() appeared. 
'''


# Subsystem1 == class
class Washing:

    def lauch(self):
        return 'Washing is: Ready!'

    def wash(self):
        return 'Washing...'


# Subsystem2 == class
class Rinsing:

    def lauch(self):
        return 'Rinsing is: Ready!'

    def rinse(self):
        return 'Rinsing...'


# Subsystem3 == class
class Spinning:

    def lauch(self):
        return 'Spinning is: Ready!'

    def spin(self):
        return 'Spinning...'


# Facade
# depecting the whole info through one message
class WashingMachine:

    def __init__(self, subsystem1=0, subsystem2=0, subsystem3=0):

        self._subsystem1 = subsystem1 or Washing()
        self._subsystem2 = subsystem2 or Spinning()
        self._subsystem3 = subsystem3 or Rinsing()

    # start washing - by_default
    def startWashing(self):

        results = []

        results.append("Facade initializes starting of washing:")
        results.append(self._subsystem1.lauch())
        results.append(self._subsystem2.lauch())
        results.append(self._subsystem3.lauch())

        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.wash())
        results.append(self._subsystem3.rinse())
        results.append(self._subsystem2.spin())

        print('\n'.join(results))


if __name__ == "__main__":

    washingMachine = WashingMachine()
    washingMachine.startWashing()


'''
    The comprehensive version that has timing and 
    follow the rules of subclassing: as client 
    might interfere into the process of washing 
    either stop it: client_code() function

    NOTE: Timing added here and setup different
    procedures into a timelimit.
    May add inquiry() option into every step 
    of washing.
'''


# '''Facade'''
# depecting the whole info through separate
# messages within the time
class WashingMachine:

    def __init__(self, subsystem1: Washing, subsystem2: Spinning, subsystem3:  Rinsing):

        self._subsystem1 = subsystem1 or Washing()
        self._subsystem2 = subsystem2 or Spinning()
        self._subsystem3 = subsystem3 or Rinsing()

    # start washing - by_default
    def start_washing(self):

        results = []

        # washing section
        results.append(self._subsystem1.lauch())
        results.append(self._subsystem1.wash())

        # spinning section
        results.append(self._subsystem2.lauch())
        results.append(self._subsystem2.spin())

        # rinsing section
        results.append(self._subsystem3.lauch())
        results.append(self._subsystem3.rinse())

        # return '\n'.join(results)
        return 'Washing process has just finished'

# Subsystem1 == class


class Washing:

    def lauch(self):
        print('Washing is: Ready!')
        return ''

    def wash(self):
        timing = 0
        print('The washing has started: ')
        while timing < 5:
            time.sleep(0.5)
            timing += 1
            print(timing)

        return 'Washing is over'

# Subsystem2 == class


class Spinning:

    def lauch(self):
        print('Spinning is: Ready!')
        return ''

    def spin(self):
        timing = 0
        print('The spinning has started: ')
        while timing < 5:
            time.sleep(0.5)
            timing += 1
            print(timing)

        return 'Spinning is over'

# Subsystem3 == class


class Rinsing:

    def lauch(self):
        return ''

    def rinse(self):
        timing = 0
        print('The rinsing has started: ')
        while timing < 5:
            time.sleep(0.5)
            timing += 1
            print(timing)

        return 'Rinsing is over'


def client_code(facade: WashingMachine):

    print(facade.start_washing(), end="")


if __name__ == "__main__":
    # The client code may have some of the subsystem's objects already created.
    # In this case, it might be worthwhile to initialize the Facade with these
    # objects instead of letting the Facade create new instances.
    subsystem1 = Washing()
    subsystem2 = Spinning()
    subsystem3 = Rinsing()
    facade = WashingMachine(subsystem1, subsystem2, subsystem3)
    client_code(facade)
