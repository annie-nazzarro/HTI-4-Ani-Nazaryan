n = int(input("Input the number of students "))

students = [int(i) for i in input("Input grades they get ").split()]
diff = max(students) * n - sum(students)
print(diff)

