def print_3_times():
    print("Wa! Sans!")
    print("Wa! Sans!")
    print("Wa! Sans!")


print_3_times()


def calcAdd(a, b):
    print(a + b)
    return


calcAdd(1, 3)
calcAdd(3, 4)


def rev(lst):
    v = []

    for element in lst:
        v.insert(0, element)

    return v


list1 = [1, 2, 3, 4, 5, 6]
list2 = rev(list1)

print(list2)


def calcMulti(c, d):
    print(c * d)
    return


calcMulti(4, 5)
calcMulti(6, 7)
