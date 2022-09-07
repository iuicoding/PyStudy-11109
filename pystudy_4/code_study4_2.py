list_input_a = ["438", "43", "534", "와 샌즈", "341"]

list_number = []
for item in list_input_a:
    try:
        int(item)
        list_number.append(item)
    except:
        pass


print("{} 내부에 있는 숫자는".format(list_input_a))
print("{}입니다.".format(list_number))
