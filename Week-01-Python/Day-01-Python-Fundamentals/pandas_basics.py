import pandas as pd
data = {
    "Name": ["Kusuma", "Meghana", "Madhavi"],
    "Age": [20, 20, 21],
    "Skill": ["Python", "Java", "AI"]
}
df = pd.DataFrame(data)
print(df)

print("\nNames:")
print(df["Name"])

print("\nSkills:")
print(df["Skill"])
print("\nStudents above age 20:")
print(df[df["Age"] > 20])

print("\n===== CSV DATA =====")

students = pd.read_csv(
    "Week-01-Python/Day-01-Python-Fundamentals/students.csv"
)

print(students)
print("\nStudents with Python skill:")

python_students = students[students["skill"] == "Python"]

print(python_students)

print("\nStudents sorted by age:")

sorted_students = students.sort_values("age")

print(sorted_students)
print("\nStudents sorted by age (descending):")

sorted_students = students.sort_values("age", ascending=False)

print(sorted_students)
print("\nMissing values:")
print(students.isnull().sum())

print("\n===== SKILL ANALYSIS =====")

job_data = pd.DataFrame({
    "Name": ["Kusuma", "Meghana", "Madhavi", "Rahul", "Anil"],
    "Skill": ["Python", "Java", "Python", "Python", "Java"],
    "Salary": [60000, 50000, 70000, 65000, 55000]
})

print(job_data)

print("\nAverage salary by skill:")

salary_by_skill = job_data.groupby("Skill")["Salary"].mean()

print(salary_by_skill)

print("\n===== JOB DATASET ANALYZER =====")

print("\nTotal candidates:", len(job_data))

print("\nHighest salary:")
print(job_data["Salary"].max())

print("\nAverage salary:")
print(job_data["Salary"].mean())

print("\nPython candidates:")
print(job_data[job_data["Skill"] == "Python"])

print("\nAverage salary by skill:")
print(job_data.groupby("Skill")["Salary"].mean())