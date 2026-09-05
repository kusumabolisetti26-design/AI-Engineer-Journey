#variables &datatypes
name = "Kusuma"
age = 20
cgpa = 8.9
is_student = True

print(name)
print(age)
print(cgpa)
print(is_student)

#List
skills = ["Python", "Java", "SQL", "Docker"]

print("First skill:", skills[0])
print("Last skill:", skills[-1])

skills.append("AWS")

print("Updated skills:", skills)
print("Number of skills:", len(skills))

#Dictionary
candidate = {
    "name": "Kusuma",
    "skills": ["Python", "Java", "SQL"],
    "experience": 1
}

print("Name:", candidate["name"])
print("Skills:", candidate["skills"])
print("Experience:", candidate["experience"])

candidate["location"] = "India"
candidate["experience"] = 2

print("Updated Candidate:", candidate)

#sets
candidate_skills = {"Python", "Java", "SQL", "Docker"}
required_skills = {"Python", "SQL", "AWS", "Docker"}

matched = candidate_skills & required_skills
missing = required_skills - candidate_skills

print("Matched skills:", matched)
print("Missing skills:", missing)

#if-else
experience=2
if experience>=2:
    print("Experienced")
else:
    print("Beginner")


#for loop
skills=["python","java","c++","aws"]
for skill in skills:
    print("i know",skill)


required_skills = ["python", "java", "sql", "aws"]
candidate_skills = ["python", "java", "c++"]
match=0
missing=0
for skill in required_skills:
    if skill in candidate_skills:
        match+=1
    else:
        missing+=1
matchper=(match/len(required_skills))*100
print(matchper)

#mini project
required_skills=["java","aws","docker","fastapts","python"]
candidate_skills=["python","sql","docker","java"]
matched=[]
missing=[]
for skill in required_skills:
    if skill in candidate_skills:
        matched.append(skill)
    else:
        missing.append(skill)
matchper=(len(matched)/len(required_skills))*100
print("=========Resume Analyser=======")
print("\nmatched")
for skill in matched:
    print("/",skill)
print("\nmissed")  
for skill in missing:
    print("x",skill)
print(f"\nMatch Score: {matchper:.0f}%")

#while
skills = ["python", "java", "sql", "aws"]

i = 0

while i < len(skills):
    print(skills[i])
    i += 1
#while
required_skills = ["python", "java", "sql", "aws"]
candidate_skills = ["python", "java", "c++"]
i=0
while i<len(required_skills):
    if required_skills[i] in candidate_skills:
        print(required_skills[i],"-->matched")
    else:
        print(required_skills[i],"-->missing")
    i+=1

#mini project using while
required_skills=["java","aws","docker","fastapts","python"]
candidate_skills=["python","sql","docker","java"]
matched=[]
missing=[]
i=0
while i<len(required_skills):
    if required_skills[i] in candidate_skills:
        matched.append(required_skills[i])
    else:
        missing.append(required_skills[i])
    i+=1
matchper=(len(matched)/len(required_skills))*100
print("=========Resume Analyser=======")
print("\nmatched")
for skill in matched:
    print("/",skill)
print("\nmissed")  
for skill in missing:
    print("x",skill)
print(f"\nMatch Score: {matchper:.0f}%")


# ==============================
# DAY 2 - PYTHON FUNCTIONS
# ==============================

# Functions
def dog():
    print("cat")

dog()


# Functions with Parameters
def student(name, age):
    print("student name:", name)
    print("student age:", age)

student("kusuma", 19)
student("jaeshu", 20)


# Return
def calculate_score(matched, total):
    return (matched / total) * 100

score = calculate_score(3, 5)
print(score)


# Parameters with Default Values
def job_role(role="AI Engineer"):
    print("my job role is", role)

job_role()
job_role("ML Engineer")


# Variable Scope
def student():
    student_name = "Kusuma"
    print(student_name)

student()


# List Comprehension
skills = ["python", "java", "sql", "docker"]

upper = [skill.upper() for skill in skills]

print(upper)


# List Comprehension + If
skills = ["python", "java", "sql", "docker", "aws"]

new_list = [skill for skill in skills if len(skill) > 4]

print(new_list)


# Functions + Comprehension + If
def filter_skills(skills):
    result = [skill for skill in skills if len(skill) > 4]
    return result


skills = ["python", "java", "sql", "docker", "aws"]

result = filter_skills(skills)

print(result)


# ==============================
# RESUME SKILL ANALYZER
# ==============================

required_skills = ["python", "java", "sql", "aws", "docker"]

candidate_skills = ["python", "java", "docker"]


# Find Matched Skills
def find_matched_skills(required_skills, candidate_skills):
    matched = []

    for skill in required_skills:
        if skill in candidate_skills:
            matched.append(skill)

    return matched


matched = find_matched_skills(required_skills, candidate_skills)

print("Matched Skills:", matched)


# Find Missing Skills
def find_missing_skills(required_skills, candidate_skills):
    missing = []

    for skill in required_skills:
        if skill not in candidate_skills:
            missing.append(skill)

    return missing


missing = find_missing_skills(required_skills, candidate_skills)

print("Missing Skills:", missing)


# Calculate Match Score
def calculate_match_score(matched_skills, required_skills):
    percentage = (len(matched_skills) / len(required_skills)) * 100
    return percentage


score = calculate_match_score(matched, required_skills)

print("Match Score:", score)


# Display Report
def display_report(matched, missing, score):
    print("===== RESUME SKILL ANALYZER =====")

    print("\nMatched Skills:")
    for skill in matched:
        print("✓", skill)

    print("\nMissing Skills:")
    for skill in missing:
        print("✗", skill)

    print(f"\nMatch Score: {score:.0f}%")


display_report(matched, missing, score)