import re


'''
    As input data, you have a list of strings.

    Write a method double_string() for counting the number of strings from the list, 
    represented in the form of the concatenation of two strings from this arguments  list.

'''


def double_string(data):

    # spliting items half-to-half order
    lst = []
    for i in data:
        x = i[0:int(len(i)/2)]  # qwer
        y = i[int(len(i)/2):]  # aaaa
        lst.append(x)
        lst.append(y)

    # defining similarities with original list
    lst2 = []
    for i in lst:
        if not i in data:
            pass
        else:
            lst2.append(i)

    return int(len(lst2)/2)


data2 = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qweraaaa']
print(double_string(data))


