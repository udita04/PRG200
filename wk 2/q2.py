marks = []
name = []

for i in range(5):
    print("Enter your name and marks ")
    name1 = input("Enter your name ")
    marks1 = int(input("Enter your marks "))

    name.append(name1)
    marks.append(marks1)

for i in range(5):
    print(name[i])
    if marks[i]>=90:
        print("Distinction")
    elif marks[i]>=75:
        print("First Division")
    elif marks[i] >=60:
        print("Second Division")
    elif marks[i] >=35:
        print("Third Division")
    else:
        print("Fail")