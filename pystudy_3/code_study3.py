def print_3_times():
    print("Wa! Sans!")
    print("Wa! Sans!")
    print("Wa! Sans!")


print_3_times()


def calc_add(a, b):
    print(a + b)
    return


calc_add(1, 3)


def rev(lst):
    v = []

    for element in lst:
        v.insert(0, element)

    return v


list1 = [1, 2, 3, 4, 5, 6]
list2 = rev(list1)

print(list2)
