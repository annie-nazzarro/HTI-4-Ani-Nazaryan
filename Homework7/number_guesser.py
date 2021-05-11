# we assume lower bound is 0
# upper bound is 1000
min = int(input("Enter Lower bound:  "))
max = int(input("Enter Upper bound:  "))
for i in range(1, 11):
    middle = int((max + min) / 2)
    print("My number is " + str(i) + " : " + str(middle))
    guess_status = input()

    while guess_status not in {"-1", "1", "0"}:
        print("Your input can only be: -1, 1 or 0")
        guess_status = input()
    if guess_status == "-1":
        max = middle
    elif guess_status == "1":
        min = middle
    else:
        print(f"I guessed in {i} steps!")
        break
else:
    print("I could not guess in 10 steps!  You are a liar")
