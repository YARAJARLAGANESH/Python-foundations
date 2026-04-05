
# Create a class named Student with attributes name and marks. 
import csv


class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = []
        self.update_marks(marks)  # Validate on entry

    def _validate_marks(self, marks):
        """Central validation method - single source of truth for mark validation."""
        if not isinstance(marks, list):
            raise ValueError("Marks must be a list.")
        for mark in marks:
            if not isinstance(mark, (int, float)):
                raise ValueError(f"Invalid mark type: {mark}. All marks must be int or float.")
            if mark < 0 or mark > 100:
                raise ValueError(f"Mark {mark} is out of range. Must be between 0 and 100.")

    def update_marks(self, marks):
        """Update marks with validation. Accepts a list."""
        self._validate_marks(marks)
        self._marks = marks
        return self._marks

    @property
    def marks(self):
        """Read-only access to marks as a tuple (immutable copy)."""
        return tuple(self._marks)

    def gpa(self):
        """Calculate and return the GPA of the student based on the marks."""
        if not self._marks:
            return 0.0
        grade_points = []
        for mark in self._marks:
            if mark >= 90:
                grade_points.append(10.0)
            elif mark >= 80:
                grade_points.append(9.0)
            elif mark >= 70:
                grade_points.append(8.0)
            elif mark >= 60:
                grade_points.append(7.0)
            elif mark >= 50:
                grade_points.append(6.0)
            elif mark >= 40:
                grade_points.append(5.0)
            else:
                grade_points.append(0.0)
        return sum(grade_points) / len(grade_points)

    def get_info(self):
        """Return student information as a dictionary."""
        return {
            'name': self.name,
            'marks': self.marks,
            'gpa': self.gpa()
        }
    def __str__(self):
        return f"Student: {self.name}, GPA: {self.gpa()}"

    def __repr__(self):
        return f"Student info : {self.get_info()}"
    
# Create a subclass named CollegeStudent that inherits from Student and has an additional attribute department. Override the gpa method to include a bonus of 0.5 for students in the AIML department.
class CollegeStudent(Student):
    def __init__(self, name, marks, department):
        super().__init__(name, marks)
        if not isinstance(department, str) or not department.strip():
            raise ValueError("Department must be a non-empty string.")
        self.department = department.strip()

    def gpa(self):
        """Override gpa to include bonus for AIML department."""
        base_gpa = super().gpa()
        if self.department.lower() == "aiml":
            return min(10.0, base_gpa + 0.5)
        return base_gpa
    
    def __str__(self):
        return super().__str__() + f", Department: {self.department}"
    
    def __repr__(self):
        return super().__repr__() + f" Department: {self.department}"

# Usage
try:
    college_student1 = CollegeStudent("Ganesh", [80, 90, 88], "AIML")
    college_student1.get_info()
    
    student1 = Student("ravi", [82, 85, 91])
    student1.get_info()
    
  
    
    # This will raise a ValueError - invalid marks
    print("\nAttempting to create student with invalid marks...")
    college_student2 = CollegeStudent("Ravi", [65, 'A', -6], "AIML")
    college_student2.get_info()
except ValueError as e:
    print(f"Error: {e}")

# Create valid student and update marks
print("\nCreating student with valid marks...")
college_student2 = CollegeStudent("Ravi", [65, 75, 85], "AIML")
college_student2.get_info()

college_student2.update_marks([89, 92, 85])
print(f"\nUpdated GPA for {college_student2.name}: {college_student2.gpa()}")

print(student1.__repr__())
print(student1.__str__() )
print(college_student1.__repr__())
print(college_student1.__str__())
