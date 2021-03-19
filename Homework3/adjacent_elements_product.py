numbers = input("Input numbers: ")

n = ([int(i) for i in numbers.split()])
sums = ([n[i] * n[i + 1] for i in range(len(n) - 1)])

max_product = max(sums)
print(max_product)
