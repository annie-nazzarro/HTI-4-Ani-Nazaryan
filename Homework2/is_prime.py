number = int(input("Input the number to check whether it's a prime or not "))
isprime = True
if number <= 1:
    isprime = False
else:
    for i in range(2, number):

        if number % i == 0:
            isprime = False
            break
if isprime:
    print("Yes")
else:
    print("NO")
