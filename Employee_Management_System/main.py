import csv
import os

EMPLOYEE_FILE = "employees.csv"
CANDIDATE_FILE = "candidates.csv"
ATTENDANCE_FILE = "attendance.csv"

# ==========================
# FILE INITIALIZATION
# ==========================

def initialize_files():
    files = {
        EMPLOYEE_FILE: ["ID", "Name", "Department", "Skills", "Salary", "Experience"],
        CANDIDATE_FILE: ["Name", "Email", "Skills", "JobRole", "MatchScore", "Status"],
        ATTENDANCE_FILE: ["EmployeeID", "Date", "Status"]
    }

    for file, header in files.items():
        if not os.path.exists(file):
            with open(file, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(header)

# ==========================
# EMPLOYEE MANAGEMENT
# ==========================

def add_employee():
    emp_id = input("Employee ID: ")

    with open(EMPLOYEE_FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0 and row[0] == emp_id:
                print("Employee ID already exists!")
                return

    name = input("Name: ")
    dept = input("Department: ")
    skills = input("Skills: ")
    salary = input("Salary: ")
    exp = input("Experience: ")

    with open(EMPLOYEE_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([emp_id, name, dept, skills, salary, exp])

    print("Employee Added Successfully!")

def view_employees():
    with open(EMPLOYEE_FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def search_employee():
    emp_id = input("Enter Employee ID: ")

    with open(EMPLOYEE_FILE, "r") as f:
        reader = csv.reader(f)
        found = False

        for row in reader:
            if len(row) > 0 and row[0] == emp_id:
                print(row)
                found = True

        if not found:
            print("Employee Not Found")

def delete_employee():
    emp_id = input("Employee ID to Delete: ")

    rows = []

    with open(EMPLOYEE_FILE, "r") as f:
        reader = csv.reader(f)

        for row in reader:
            if len(row) > 0 and row[0] != emp_id:
                rows.append(row)

    with open(EMPLOYEE_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print("Employee Deleted Successfully!")

# ==========================
# AI SKILL MATCHING
# ==========================

def calculate_match(candidate_skills, required_skills):
    candidate = set(candidate_skills.lower().split(","))
    required = set(required_skills.lower().split(","))

    matched = len(candidate.intersection(required))
    score = (matched / len(required)) * 100

    return round(score, 2)

# ==========================
# INTERVIEW QUESTIONS
# ==========================

def generate_questions(role):

    questions = {
        "python developer": [
            "What is OOP?",
            "Explain decorators.",
            "What is REST API?"
        ],
        "frontend developer": [
            "What is React?",
            "Difference between let and var?",
            "Explain DOM."
        ]
    }

    role = role.lower()

    if role in questions:
        print("\nInterview Questions:")
        for q in questions[role]:
            print("-", q)
    else:
        print("General Questions:")
        print("- Tell me about yourself")
        print("- Why should we hire you?")

# ==========================
# CANDIDATE SYSTEM
# ==========================

def register_candidate():

    name = input("Name: ")
    email = input("Email: ")
    skills = input("Skills (comma separated): ")
    role = input("Job Role: ")

    required = input("Required Skills (comma separated): ")

    score = calculate_match(skills, required)

    status = "Shortlisted" if score >= 60 else "Rejected"

    with open(CANDIDATE_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, email, skills, role, score, status])

    print("Candidate Registered!")
    print("Match Score:", score)
    print("Status:", status)

    generate_questions(role)

def view_candidates():

    with open(CANDIDATE_FILE, "r") as f:
        reader = csv.reader(f)

        for row in reader:
            print(row)

# ==========================
# RANKING SYSTEM
# ==========================

def rank_candidates():

    candidates = []

    with open(CANDIDATE_FILE, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            candidates.append(row)

    candidates.sort(
        key=lambda x: float(x["MatchScore"]),
        reverse=True
    )

    print("\nTop Candidates")

    rank = 1

    for c in candidates:
        print(rank, c["Name"], c["MatchScore"])
        rank += 1

# ==========================
# ATTENDANCE SYSTEM
# ==========================

def mark_attendance():

    emp_id = input("Employee ID: ")
    date = input("Date (DD-MM-YYYY): ")
    status = input("Present/Absent: ")

    with open(ATTENDANCE_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([emp_id, date, status])

    print("Attendance Recorded!")

def attendance_history():

    with open(ATTENDANCE_FILE, "r") as f:
        reader = csv.reader(f)

        for row in reader:
            print(row)

# ==========================
# REPORTS
# ==========================

def generate_reports():

    emp_count = sum(1 for _ in open(EMPLOYEE_FILE)) - 1
    cand_count = sum(1 for _ in open(CANDIDATE_FILE)) - 1

    print("\n===== REPORT =====")
    print("Total Employees:", emp_count)
    print("Total Candidates:", cand_count)

# ==========================
# MENU
# ==========================

def menu():

    initialize_files()

    while True:

        print("\n===== AI EMPLOYEE MANAGEMENT SYSTEM =====")

        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Delete Employee")
        print("5. Register Candidate")
        print("6. View Candidates")
        print("7. Rank Candidates")
        print("8. Mark Attendance")
        print("9. Attendance History")
        print("10. Generate Report")
        print("11. Exit")

        choice = input("Enter Choice: ")

        try:

            if choice == "1":
                add_employee()

            elif choice == "2":
                view_employees()

            elif choice == "3":
                search_employee()

            elif choice == "4":
                delete_employee()

            elif choice == "5":
                register_candidate()

            elif choice == "6":
                view_candidates()

            elif choice == "7":
                rank_candidates()

            elif choice == "8":
                mark_attendance()

            elif choice == "9":
                attendance_history()

            elif choice == "10":
                generate_reports()

            elif choice == "11":
                print("Thank You")
                break

            else:
                print("Invalid Choice")

        except Exception as e:
            print("Error:", e)

menu()