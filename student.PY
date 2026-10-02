# ===============================================
# STUDENT MANAGEMENT SYSTEM IS MADE BY  ARIF !!!
# ===============================================

students = []

def add_student():
    print("\n----- Add Student -----")

    sid = input("Enter Student ID: ")

    
    for student in students:
        if student["id"] == sid:
            print("Student ID already exists!")
            return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "id": sid,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    print("\n----- Student List -----")

    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:
        print("--------------------------")
        print("ID     :", student["id"])
        print("Name   :", student["name"])
        print("Age    :", student["age"])
        print("Course :", student["course"])
    print("--------------------------")



def search_student():
    print("\n----- Search Student -----")

    sid = input("Enter Student ID: ")

    for student in students:
        if student["id"] == sid:
            print("\nStudent Found")
            print("--------------------------")
            print("ID     :", student["id"])
            print("Name   :", student["name"])
            print("Age    :", student["age"])
            print("Course :", student["course"])
            return

    print("Student not found.")



def update_student():
    print("\n----- Update Student -----")

    sid = input("Enter Student ID: ")

    for student in students:
        if student["id"] == sid:
            print("Student Found!")

            student["name"] = input("Enter New Name: ")
            student["age"] = input("Enter New Age: ")
            student["course"] = input("Enter New Course: ")

            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():
    print("\n----- Delete Student -----")

    sid = input("Enter Student ID: ")

    for student in students:
        if student["id"] == sid:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")



def menu():

    while True:

        print("\n==============================")
        print(" STUDENT MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Chole jaow ")

        choice = input("\nEnter your choice: ")

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
            print("\nThank you for using Student Management System.")
            break

        else:
            print("Not found Students detels!Please try again.")


menu()