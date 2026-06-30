"""
Student Record Management System
---------------------------------
A beginner-friendly mini project built using only:
    Module 1 -> Variables, Input/Output, Strings
    Module 2 -> If-Else, Loops, Break/Continue
    Module 3 -> Lists, Tuples, Dictionaries
    Module 4 -> Functions (default params, return values)

This console app lets a user add students, view records, search,
calculate grades, and see simple class statistics.
"""

# ---------------------------------------------------------
# MODULE 3: Data Structures
# A list of dictionaries is used to store all student records.
# Each dictionary holds the details of one student (key-value pairs).
# ---------------------------------------------------------
students = []

# A tuple is used for fixed data that should never change.
GRADE_SCALE = ("A", "B", "C", "D", "F")


# ---------------------------------------------------------
# MODULE 4: Functions
# ---------------------------------------------------------

def calculate_grade(marks, scale=GRADE_SCALE):
    """
    Returns a letter grade based on marks.
    Demonstrates a function with a default parameter.
    """
    if marks >= 90:
        return scale[0]      # A
    elif marks >= 75:
        return scale[1]      # B
    elif marks >= 60:
        return scale[2]      # C
    elif marks >= 40:
        return scale[3]      # D
    else:
        return scale[4]      # F


def add_student():
    """
    Module 1: takes user input (string + numeric conversion)
    Module 3: stores the new record as a dictionary inside the list
    """
    name = input("Enter student name: ").strip().title()
    roll_no = input("Enter roll number: ").strip()
    marks = float(input("Enter marks (out of 100): "))

    grade = calculate_grade(marks)

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "grade": grade
    }

    students.append(student)
    print(f"\n✅ Student '{name}' added successfully with Grade {grade}!\n")


def view_all_students():
    """
    Module 2: uses a for loop to go through the list of dictionaries
    """
    if not students:
        print("\nNo student records found yet.\n")
        return

    print("\n" + "-" * 50)
    print(f"{'Roll No':<10}{'Name':<20}{'Marks':<10}{'Grade':<5}")
    print("-" * 50)

    for s in students:
        print(f"{s['roll_no']:<10}{s['name']:<20}{s['marks']:<10}{s['grade']:<5}")

    print("-" * 50 + "\n")


def search_student():
    """
    Module 2: loop + if-else + break
    Searches a student by roll number.
    """
    roll_no = input("Enter roll number to search: ").strip()

    found = False
    for s in students:
        if s["roll_no"] == roll_no:
            print(f"\n🔎 Found: {s['name']} | Marks: {s['marks']} | Grade: {s['grade']}\n")
            found = True
            break   # stop looping once found

    if not found:
        print("\n❌ No student found with that roll number.\n")


def class_statistics():
    """
    Module 3 + Module 4: works on a list of numbers (marks)
    using built-in functions max(), min(), sum(), len()
    """
    if not students:
        print("\nNo data available for statistics.\n")
        return

    all_marks = [s["marks"] for s in students]   # building a list from dictionaries

    highest = max(all_marks)
    lowest = min(all_marks)
    average = sum(all_marks) / len(all_marks)

    print("\n📊 Class Statistics")
    print(f"Total Students : {len(students)}")
    print(f"Highest Marks  : {highest}")
    print(f"Lowest Marks   : {lowest}")
    print(f"Average Marks  : {average:.2f}\n")


def word_frequency_demo():
    """
    Extra Module 1+3 demo: string processing + dictionary counting
    (based on the word-frequency task style from Module 3)
    """
    sentence = input("Enter a sentence to analyze: ")
    words = sentence.lower().split()

    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    print("\nWord Frequency:")
    for word, count in frequency.items():
        print(f"  {word} -> {count}")
    print()


def show_menu():
    """
    Module 1: print formatted text (menu)
    """
    print("=" * 50)
    print("     STUDENT RECORD MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Roll No")
    print("4. Show Class Statistics")
    print("5. Word Frequency Tool (Bonus)")
    print("6. Exit")
    print("=" * 50)


def main():
    """
    Module 2: while loop runs the program menu until the user exits
    """
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            class_statistics()
        elif choice == "5":
            word_frequency_demo()
        elif choice == "6":
            print("\nThank you for using the Student Record System. Goodbye! 👋")
            break          # exits the while loop
        else:
            print("\n⚠️ Invalid choice. Please enter a number between 1 and 6.\n")
            continue       # goes back to the top of the loop


# Standard Python entry point
if __name__ == "__main__":
    main()
