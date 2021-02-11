def order(a):
    count = 0
    comparison = len(a) - 1

    for i in range(comparison):
        if a[i] < a[i+1]:
            count += 1
        else:
            pass

    asc = count == comparison
    desc = count == 0

    if asc:
        return 'ascending'
    elif desc:
        return 'descending'
    else:
        return 'not sorted'

# checklists
a = [6, 20, 160, 420, 550]
b = a[::-1]

print(order(b))
