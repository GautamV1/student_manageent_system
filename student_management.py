students = []

def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    subject = input("Enter subject: ")
    student = (name, age, subject)
    students.append(student)
    print("Student added!\n")

def view_students():  # fixed function name
    if not students:
        print("No students to show.\n")
        return
    for i, student in enumerate(students, 1):  # fixed 'students' instead of 'student'
        print(f"{i}. Name: {student[0]}, Age: {student[1]}, Subject: {student[2]}\n")

def search_student():
    name = input("Enter name to search: ")
    found = False
    for student in students:
        if student[0].lower() == name.lower():
            print(f"Found: Name: {student[0]}, Age: {student[1]}, Subject: {student[2]}\n")
            found = True
            break
    if not found:  # moved outside the loop
        print("Student not found.\n")

# Main menu loop
while True:
    print("1. Add student")
    print("2. View all students")
    print("3. Search student")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()  # fixed function name
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.\n")

input("Press Enter to close...")