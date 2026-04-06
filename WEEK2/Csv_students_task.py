import csv

from Week2_Tasks import CollegeStudent
def parse_marks(marks_str):
    """Convert '80,90,88' → [80, 90, 88]"""
    return [float(m.strip()) for m in marks_str.split(",")]

def load_students_from_csv(filename):
    """Load students from a CSV file and return a list of CollegeStudent objects."""
    students = []
    with open(filename, mode = 'r' )as file:
        reader = csv.DictReader(file)

        for row in reader:
            try: 
                name = row['name']
                marks = parse_marks(row['marks'])
                department = row['department']
                student = CollegeStudent(name, marks, department)
                students.append(student)
            except ValueError as e:
                print(f"Skipping invalid row {row}: {e}")

    return students
        
def print_report(students):
    print("\n ======== STUDENT REPORT =======")

    for student in students:
        info = student.get_info()

        print(f"name      :{info['name']}")
        print(f"Marks      :{info['marks']}")
        print(f"GPA     :{info['gpa']}")

    if isinstance(student, CollegeStudent):
            print(f"Department : {student.department}")
        
    print("-" * 30)
    
students = load_students_from_csv("students.csv")
print_report(students)