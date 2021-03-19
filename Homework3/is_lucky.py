lucky_number = input("Enter your lucky number: ")

lucky_number = [int(i) for i in str(lucky_number)]

lucky_number_slice = len(lucky_number) // 2
islucky = True

if sum(lucky_number[:lucky_number_slice]) == sum(lucky_number[lucky_number_slice:]):
    islucky = True
else:
    islucky = False

if islucky:
    print("YES")
else:
    print("NO")
