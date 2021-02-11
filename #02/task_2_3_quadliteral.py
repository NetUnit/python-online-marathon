import re


'''
    The string defining the points of the quadrilateral has the next form: "#LB1:1#RB4:1#LT1:3#RT4:3"

    LB - Left Bottom point
    LT - Left Top point
    RT - Right Top point
    RB - Right Bottom point
    numbers after letters are the coordinates of a point.
    Write a function figure_perimetr() that calculates the perimeter of a quadrilateral

    The formula for calculating the distance between points: 

    dist = sqrt(sum(zip((x2-x1)**2 + (y2 - y1)**2))))

'''


def figure_perimetr(test):

    p1 = [int(i) for i in (
        ' '.join(re.compile(r'([L]{1}[B]{1}\d\S\d)').findall(test)))[2:5:2]]
    p2 = [int(i) for i in (
        ' '.join(re.compile(r'([L]{1}[T]{1}\d\S\d)').findall(test)))[2:5:2]]
    p3 = [int(i) for i in (
        ' '.join(re.compile(r'([R]{1}[T]{1}\d\S\d)').findall(test)))[2:5:2]]
    p4 = [int(i) for i in (
        ' '.join(re.compile(r'([R]{1}[B]{1}\d\S\d)').findall(test)))[2:5:2]]

    l1 = (sum([abs(a - b) ** 2 for a, b in zip(p1, p2)])) ** 0.5
    l2 = (sum([abs(a - b) ** 2 for a, b in zip(p2, p3)])) ** 0.5
    l3 = (sum([abs(a - b) ** 2 for a, b in zip(p3, p4)])) ** 0.5
    l4 = (sum([abs(a - b) ** 2 for a, b in zip(p4, p1)])) ** 0.5

    return 'A perimeter is: {}'.format(sum(tuple((l1, l2, l3, l4))))


# test = "#LB1:1#RB4:1#LT1:3#RT4:3"
test = "#LB0:1#RB5:1#LT4:5#RT8:3"
print(figure_perimetr(test))
