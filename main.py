from operations import *


def main():
    while True:
        print("\n" + "=" * 50)
        print("STUDENT MANAGEMENT SYSTEM".center(50))
        print("=" * 50)
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("=" * 50)

        choice = input("Enter Choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("=" * 50)
            print("      Thank You For Using")
            print("   STUDENT MANAGEMENT SYSTEM")
            print("  Program Closed Successfully!")
            print("=" * 50)
            break
        else:
            print("Invalid Choice! Please enter 1-6.")


if __name__ == "__main__":
    main()
