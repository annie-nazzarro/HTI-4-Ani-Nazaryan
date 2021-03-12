n = int(input("Input the number you love "))
factorial_number = 1
if n == 0:
    print(1)
elif n < 0:
    print("Hey, negative numbers do not have factorial ")
else:
    for i in range(1, n + 1):
        factorial_number = factorial_number * i
    print(factorial_number)
