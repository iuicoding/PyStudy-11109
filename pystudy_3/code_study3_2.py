def print_n_times(n, *value):
    for i in range(n):
        for value in value:
            print(value)


print_n_times(2, "Wa!", "Sans!")
