my_list = [int(i) for i in input("Input numbers ").split()]

list_abs = list(map(abs, my_list))
print(list_abs)
list_abs_sum = sum(list_abs)
print(list_abs_sum)
