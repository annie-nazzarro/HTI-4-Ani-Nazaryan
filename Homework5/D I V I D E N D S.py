numbers = [12, 24, 42, "test", "True", 43, 34, "a", 72]
n = int(input("Input any number "))
for i in filter(lambda x: isinstance(x, int) and x % n == 0, numbers):
    print(i)
