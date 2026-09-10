"""import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)

print("Status Code:", response.status_code)
print("Response:")
data = response.json()

print("Task ID:", data["id"])
print("Title:", data["title"])
print("Completed:", data["completed"])

#multiple get
import requests

url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

print("\nTotal Records:", len(data))

print("\nFirst 5 Tasks:")

for task in data[:5]:
    print("ID:", task["id"])
    print("Title:", task["title"])
    print("Completed:", task["completed"])
    print("--------------------")

    #mini project
    print("\nJob Data:")

for task in data[:5]:
    job_id = task["id"]
    job_title = task["title"]

    print("Job ID:", job_id)
    print("Job Title:", job_title)
    print("--------------------")


#
import requests
def get_jobs():
    url = "https://jsonplaceholder.typicode.com/todos"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as error:
        print("API request failed:", error)
        return []
def filter_jobs(jobs, keyword):
    matched_jobs = []

    for job in jobs:
        if keyword.lower() in job["title"].lower():
            matched_jobs.append(job)

    return matched_jobs

jobs = get_jobs()
ai_jobs = filter_jobs(jobs, "qui")

print("\nFiltered Jobs:")

for job in ai_jobs[:5]:
    print("Job ID:", job["id"])
    print("Job Title:", job["title"])
    print("--------------------")

print("Total Records:", len(jobs))

print("\nJob Data:")

for job in jobs[:5]:
    job_id = job["id"]
    job_title = job["title"]

    print("Job ID:", job_id)
    print("Job Title:", job_title)
    print("--------------------")

    #post
    import requests

url = "https://jsonplaceholder.typicode.com/posts"

candidate = {
    "name": "Kusuma",
    "skills": ["Python", "AI"],
    "experience": 0
}

response = requests.post(url, json=candidate)

print("Status Code:", response.status_code)
print("Response:", response.json())"""

import requests


# ==============================
# DAY 5 - API
# JOB DATA COLLECTOR
# ==============================


# 1. Get job data from API
def get_jobs():
    url = "https://jsonplaceholder.typicode.com/todos"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as error:
        print("API request failed:", error)
        return []


# 2. Filter jobs by keyword
def filter_jobs(jobs, keyword):
    matched_jobs = []

    for job in jobs:
        if keyword.lower() in job["title"].lower():
            matched_jobs.append(job)

    return matched_jobs


# 3. Display jobs
def display_jobs(jobs):
    for job in jobs:
        print("Job ID:", job["id"])
        print("Job Title:", job["title"])
        print("--------------------")


# ==============================
# MAIN PROGRAM
# ==============================

jobs = get_jobs()

print("===== JOB DATA COLLECTOR =====")

print("\nTotal Records:", len(jobs))


# Display first 5 jobs
print("\nFirst 5 Jobs:")

display_jobs(jobs[:5])


# Filter jobs
filtered_jobs = filter_jobs(jobs, "qui")

print("\nFiltered Jobs:")

display_jobs(filtered_jobs[:5])