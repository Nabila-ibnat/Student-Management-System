import os
from student import Student
from grades import calculate_grade
from utils import print_line, print_header

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "Data")
DATA_FILE = os.path.join(DATA_DIR, "students.txt")


def load_students():
    students = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    if len(parts) == 3:
                        students.append(Student(parts[0], parts[1], parts[2]))
    return students


def save_students(students):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(DATA_FILE, "w") as f:
        for s in students:
            f.write(f"{s}\n")


def add_student():
    print_header("ADD STUDENT")
    name = input("Enter Student Name  : ").strip()
    age = input("Enter Student Age   : ").strip()
    marks = input("Enter Student Marks : ").strip()

    students = load_students()
    students.append(Student(name, age, marks))
    save_students(students)

    print("\nStudent Added Successfully!")
    print_line()


def view_students():
    print_header("STUDENT LIST")
    students = load_students()

    if not students:
        print("No students found.")
        print_line()
        return

    print(f"{'Name':<20} {'Age':<10} {'Marks':<10} {'Grade'}")
    print_line()

    for s in students:
        grade = calculate_grade(s.marks)
        print(f"{s.name:<20} {s.age:<10} {s.marks:<10} {grade}")

    print_line()
    print(f"Total Students: {len(students)}")
    print_line()


def search_student():
    print_header("SEARCH STUDENT")
    search_name = input("Enter Student Name: ").strip().lower()

    students = load_students()
    found = [s for s in students if search_name in s.name.lower()]

    if found:
        for s in found:
            print("\nStudent Found!")
            print_line()
            print(f"Name  : {s.name}")
            print(f"Age   : {s.age}")
            print(f"Marks : {s.marks}")
            print(f"Grade : {calculate_grade(s.marks)}")
            print_line()
    else:
        print("Student Not Found!")
        print_line()


def update_student():
    print_header("UPDATE STUDENT")
    search_name = input("Enter Student Name: ").strip().lower()

    students = load_students()
    updated = False

    for i, s in enumerate(students):
        if s.name.lower() == search_name:
            print("\nCurrent Information")
            print_line()
            print(f"Name  : {s.name}")
            print(f"Age   : {s.age}")
            print(f"Marks : {s.marks}")

            new_name = input("\nEnter New Name  : ").strip()
            new_age = input("Enter New Age   : ").strip()
            new_marks = input("Enter New Marks : ").strip()

            students[i] = Student(new_name, new_age, new_marks)
            save_students(students)
            print("\nStudent Updated Successfully!")
            print_line()
            updated = True
            break

    if not updated:
        print("Student Not Found!")
        print_line()


def delete_student():
    print_header("DELETE STUDENT")
    search_name = input("Enter Student Name: ").strip().lower()

    students = load_students()
    new_list = [s for s in students if s.name.lower() != search_name]

    if len(new_list) < len(students):
        save_students(new_list)
        print("Student Deleted Successfully!")
    else:
        print("Student Not Found!")

    print_line()
