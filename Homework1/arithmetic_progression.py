first_number = int(input("Please, input the first number of arithmetic progression:" + " "))
second_number = int(input("Please, input the second number of arithmetic progression:" + " "))
N = int(input("Please, input which term of arithmetic progression you want to find:" + " "))
# an=a1+(n−1)d
d = second_number - first_number
N_th_term = first_number + (N - 1) * d
print(N_th_term)
