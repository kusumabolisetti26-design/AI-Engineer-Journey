import numpy as np
numbers = np.array([10, 20, 30, 40, 50])
print(numbers)
print("Shape:", numbers.shape)

numbers = np.array([10, 20, 30, 40, 50])

print("First:", numbers[0])
print("Third:", numbers[2])
print("Last:", numbers[4])
print("First 3:", numbers[0:3])
print("Middle:", numbers[1:4])
print("Multiply by 2:", numbers * 2)
print("Add 10:", numbers + 10)
print("Square:", numbers ** 2)

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\nMatrix:")
print(matrix)

print("Shape:", matrix.shape)
print("First row:", matrix[0])
print("First row, second column:", matrix[0, 1])
print("Second row, third column:", matrix[1, 2])
print("\nStatistics:")
print("Sum:", numbers.sum())
print("Mean:", numbers.mean())
print("Maximum:", numbers.max())
print("Minimum:", numbers.min())

print("\nFirst column:")
print(matrix[:, 0])

print("\nFirst row:")
print(matrix[0, :])


marks = np.array([78, 85, 92, 67, 88, 95, 72, 81])

print("\n===== NUMERICAL DATA ANALYZER =====")

print("Marks:", marks)
print("Average:", marks.mean())
print("Highest:", marks.max())
print("Lowest:", marks.min())
print("Total:", marks.sum())

passed = marks[marks >= 75]

print("\nStudents scoring 75 or above:")
print(passed)

print("Number of students:", len(passed))
failed = marks[marks < 75]

print("\nStudents scoring below 75:")
print(failed)

print("Number of failed students:", len(failed))
pass_percentage = (len(passed) / len(marks)) * 100

print("\nPass Percentage:", pass_percentage, "%")