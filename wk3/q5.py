def average_score(*marks):
    total = sum(marks)
    average = total / len(marks)
    return average


print(average_score(70, 80, 90))
print(average_score(60, 75, 85, 95))