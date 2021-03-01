from __future__ import annotations
from abc import ABC, abstractmethod


'''
    print("\t", end ="") - tab immitation when new position
    always the first element from *args==employee
    no sets(workers could repeat), but as regards wages 
    it doesn't make sense
'''


class LeafElement:

    def __init__(self, *employee):

        self.employee = employee[0]

    def showDetails(self):
        print("\t", end="")
        print(f'{self.employee}')


class CompositeElement:

    def __init__(self, *employee):
        self.position = employee[0]
        self.children = list()

    def add(self, child):
        self.children.append(child)

    def sub(self, child):
        self.children.remove(child)

    def showDetails(self):

        print(f'{self.position}')
        for child in self.children:
            print("\t", end="")
            child.showDetails()


"""main method"""

if __name__ == "__main__":

    topLevelMenu = CompositeElement("GeneralManager")
    subMenuItem1 = CompositeElement("Manager1")
    subMenuItem2 = CompositeElement("Manager2")
    subMenuItem11 = LeafElement("Developer11")
    subMenuItem12 = LeafElement("Developer12")
    subMenuItem21 = LeafElement("Developer21")
    subMenuItem22 = LeafElement("Developer22")
    subMenuItem1.add(subMenuItem11)
    subMenuItem1.add(subMenuItem12)
    subMenuItem2.add(subMenuItem22)
    subMenuItem2.add(subMenuItem22)

    topLevelMenu.add(subMenuItem1)
    topLevelMenu.add(subMenuItem2)
    topLevelMenu.showDetails()
