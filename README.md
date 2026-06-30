# 🎓 Student Record Management System (Python Mini Project)

A beginner-level Python console application built as part of the **AI/ML Internship 2026 Lab Manual**, covering concept

No external libraries or advanced topics (no AI/search algorithms) are used — this is a pure Python fundamentals project.

## 📌 Features

1. **Add Student** – take name, roll number, and marks as input, store as a dictionary
2. **View All Students** – display all records in a neat table using a loop
3. **Search Student by Roll No** – linear search through the list with `break`
4. **Class Statistics** – highest, lowest, and average marks using `max()`, `min()`, `sum()`
5. **Bonus: Word Frequency Tool** – counts how often each word appears in a sentence (dictionary practice)
6. **Exit** – cleanly ends the program loop

---

## 🛠️ Concepts Used

| Concept | Where it's used |
|---|---|
| Variables & f-strings | Throughout (printing records, statistics) |
| `input()` & type conversion | `add_student()`, `search_student()` |
| String methods (`.strip()`, `.title()`, `.lower()`, `.split()`) | `add_student()`, `word_frequency_demo()` |
| if / elif / else | `calculate_grade()`, `main()` |
| for loop | `view_all_students()`, `search_student()`, `word_frequency_demo()` |
| while loop | `main()` menu loop |
| break / continue | `search_student()`, `main()` |
| Lists | `students` list, `all_marks` list |
| Tuples | `GRADE_SCALE` |
| Dictionaries | Each student record, `frequency` dictionary |
| Functions with return values | `calculate_grade()` |
| Functions with default parameters | `calculate_grade(marks, scale=GRADE_SCALE)` |

---

## ▶️ How to Run

1. Make sure Python 3 is installed:
   ```bash
   python3 --version
   ```
2. Clone this repository or download the file.
3. Run the program:
   ```bash
   python3 student_record_system.py
   ```
4. Follow the on-screen menu (enter numbers 1–6).

---

## 📂 Project Structure

```
student-record-system/
│
├── student_record_system.py   # Main program
└── README.md                  # Project documentation
```

---

## 🚀 Future Improvements (Not part of this submission)

- Save/load records to a file (CSV/JSON)
- Use classes (OOP) once Module covers it
- Add a simple GUI

---

## 👤 Author

Built as a beginner Python mini project for the AI/ML Internship Lab (Modules 1–4).
