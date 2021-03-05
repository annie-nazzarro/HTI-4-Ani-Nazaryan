# we input the year and concatenate
# it to int as it is a string by default
year = int(input("Please enter your birth year:"))

# we check if year is less or equal to 0,
# then it's a mistake
if year <= 0:
    print(str("Hey,sorry, we do not have negative centuries :)"))

# else if year is less or equal to 100,
# it's first century, it'll print 1

elif year <= 100:
    print(1)

# else if  divide year by modulus, if it gets 0 as a reminder,
# then divide it by floor division
# and print the integer value of the quotient,
# otherwise add 1 to the number we get after floor division and print it
elif year % 100 == 0:
    print(year // 100)
else:
    print(year // 100 + 1)
