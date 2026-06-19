# Practice exercises for Student Management System

# Exercise 1: Print student info
def print_student_info(name, age, marks):
    print(f"Name: {name}, Age: {age}, Marks: {marks}")

# Exercise 2: Check if a student passes (marks >= 40)
def is_pass(marks):
    return float(marks) >= 40

# Exercise 3: Calculate average marks from a list
def average_marks(marks_list):
    if not marks_list:
        return 0
    return sum(marks_list) / len(marks_list)


# --- Run exercises ---
if __name__ == "__main__":
    print_student_info("John", 20, 85)
    print("Pass:", is_pass(85))
    print("Average:", average_marks([85, 78, 91]))
