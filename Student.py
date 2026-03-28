# Student Management System

students = {}

def add_student():
    name = input("Enter student name: ")
    
    # marks dictionary
    marks = {}
    subjects = set()
    
    n = int(input("How many subjects? "))
    
    for i in range(n):
        sub = input("Enter subject name: ")
        subjects.add(sub)   # set (no duplicates)
        
        mark = int(input(f"Enter marks for {sub}: "))
        marks[sub] = mark   # dictionary
    
    students[name] = {
        "subjects": subjects,
        "marks": marks
    }
    
    print("✅ Student added successfully!\n")


def display_students():
    for name, data in students.items():
        print(f"\n👤 Name: {name}")
        print("📚 Subjects:", data["subjects"])
        print("📊 Marks:", data["marks"])


def search_student():
    name = input("Enter student name to search: ")
    
    if name in students:
        print("\n✅ Found!")
        print("Subjects:", students[name]["subjects"])
        print("Marks:", students[name]["marks"])
    else:
        print("❌ Student not found")


def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice")


# Run program
menu()