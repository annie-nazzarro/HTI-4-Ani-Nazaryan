numbers = [i for i in input("Input dividends ").split()]
n = int(input("Input any number "))
for i in filter(lambda x: x.isnumeric() and int(x) % n == 0, numbers):
    print(i, end=" ")
