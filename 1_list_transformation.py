#Task 1: Sort grades in descending order

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

print('Sorting grades in descending order')
grades.sort(reverse = True)
print(grades)

#Task 2: Calculate the average grade and display it

total = sum(grades)
average = (total / len(grades))

print(average)

#Task 3 Replace any grade below 80 with the value Failed

grades[7] = 'Failed'
grades[8] = 'Failed'
grades[9] = 'Failed'
print(grades)