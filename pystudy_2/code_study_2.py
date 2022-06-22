list_a = ["Internet", 'Explorer', 'Dies']
print(list_a[0])

list_b = ["파이참"]
print(list_b[0])

list_1 = [1, 2, 3]
print(list_1 + [4])

list_2 = [1, 2, 3, 4]
list_2.insert(1, 3)
list_2.extend([5, 6, 7, 8])
list_2.remove(8)
list_2.pop(3)

list_3 = ["W", "a", "!", "S", "a", "n", "s"]
for element in list_3:
    print(element)

if 9 in list_2:
    print("값을 찾았습니다.")
else:
    print("값이 존재하지 않습니다.")

str_list = ["W", "a", "!", "S", "a", "n", "s"]
del str_list[2]
print(str_list)

list_i = []
for list_i in range(1, 100, 2):
    print(list_i)

