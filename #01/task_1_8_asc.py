def studying_hours(a):

    asc = 0
    desc = 1
    for i in range(len(a) - 1):
        if a[i] <= a[i + 1]:
            desc += 1
        else:
            if desc > asc:
                asc = desc
            desc = 1
    return max(desc, asc)

# checkslit
a = [6, 20, 160, 420, 550] # asc
b = a[::-1] # desc
print(order([1, 7, 0, 4, 8, 1])) #rand




