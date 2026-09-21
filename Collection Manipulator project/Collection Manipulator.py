# Collection Manipulator

students = []

print("<<<< Welcome To Student Record Manager >>>>")

while True:

    print("\nSelect an option:")
    print("a. Add student")
    print("b. Display all students")
    print("c. Update student information")
    print("d. Delete student")
    print("e. Display subjects stored")
    print("f. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "a":

        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        subjects = input("Enter Subjects: ")

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "subjects": subjects
        }

        students.append(student)

        print("Student Added Successfully")

    # Display All Students
    elif choice == "b":

        if len(students) == 0:
            print("No Student Found")

        else:
            print("\n--- Display All Students ---")

            for s in students:
                print("Student ID:", s["id"])
                print("Name:", s["name"])
                print("Age:", s["age"])
                print("Subjects:", s["subjects"])
                print()

    # Update Student
    elif choice == "c":

        student_id = input("Enter Student ID: ")

        found = False

        for s in students:
            if s["id"] == student_id:

                s["age"] = input("Enter New Age: ")
                s["subjects"] = input("Enter New Subjects: ")

                print("Student Updated Successfully")
                found = True
                break

        if found == False:
            print("Student Not Found")

    # Delete Student
    elif choice == "d":

        student_id = input("Enter Student ID: ")

        found = False

        for i in range(len(students)):
            if students[i]["id"] == student_id:

                del students[i]

                print("Student Deleted Successfully")
                found = True
                break

        if found == False:
            print("Student Not Found")

    # Display Subjects
    elif choice == "e":

        print("\nStored Subjects:")

        for s in students:
            print(s["subjects"])

    # Exit
    elif choice == "f":

        print("Thank You!")
        break

    else:
        print("Invalid Choice")





#------------- Output --------------```


# <<<< Welcome To Student Record Manager >>>>

# Select an option:
# a. Add student
# b. Display all students
# c. Update student information
# d. Delete student
# e. Display subjects stored
# f. Exit

# Enter your choice: a

# Enter Student ID: 101
# Enter Name: Alice
# Enter Age: 20
# Enter Subjects: Math,Science,English

# Student Added Successfully


# Select an option:
# a. Add student
# b. Display all students
# c. Update student information
# d. Delete student
# e. Display subjects stored
# f. Exit

# Enter your choice: a

# Enter Student ID: 102
# Enter Name: Raj
# Enter Age: 21
# Enter Subjects: Python,C++

# Student Added Successfully


# Select an option:
# a. Add student
# b. Display all students
# c. Update student information
# d. Delete student
# e. Display subjects stored
# f. Exit

# Enter your choice: b

# --- Display All Students ---

# Student ID: 101
# Name: Alice
# Age: 20
# Subjects: Math,Science,English

# Student ID: 102
# Name: Raj
# Age: 21
# Subjects: Python,C++


# Select an option:
# a. Add student
# b. Display all students
# c. Update student information
# d. Delete student
# e. Display subjects stored
# f. Exit

# Enter your choice: c

# Enter Student ID: 101
# Enter New Age: 22
# Enter New Subjects: Math,Python

# Student Updated Successfully


# Select an option:
# a. Add student
# b. Display all students
# c. Update student information
# d. Delete student
# e. Display subjects stored
# f. Exit

# Enter your choice: b

# --- Display All Students ---

# Student ID: 101
# Name: Alice
# Age: 22
# Subjects: Math,Python

# Student ID: 102
# Name: Raj
# Age: 21
# Subjects: Python,C++


# Select an option:
# a. Add student
# b. Display all students
# c. Update student information
# d. Delete student
# e. Display subjects stored
# f. Exit

# Enter your choice: e

# Stored Subjects:
# Math,Python
# Python,C++


# Select an option:
# a. Add student
# b. Display all students
# c. Update student information
# d. Delete student
# e. Display subjects stored
# f. Exit

# Enter your choice: d

# Enter Student ID: 102

# Student Deleted Successfully


# Select an option:
# a. Add student
# b. Display all students
# c. Update student information
# d. Delete student
# e. Display subjects stored
# f. Exit

# Enter your choice: b

# --- Display All Students ---

# Student ID: 101
# Name: Alice
# Age: 22
# Subjects: Math,Python


# Select an option:
# a. Add student
# b. Display all students
# c. Update student information
# d. Delete student
# e. Display subjects stored
# f. Exit

# Enter your choice: f

# Thank You!