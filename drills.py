
#student_heights = [180, 124, 165, 173, 189, 169, 146]
#total_height = 0
#total_students = 0
#for h in student_heights:
#    total_height += h
#    total_students += 1
#average_height = int(total_height / total_students)
#print(average_height)

for i in range(1,101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)