Class Design:

1. Student
   - Attributes:
     - name (str)
     - _marks (list, protected)
   - Methods:
     - update_marks()
     - _validate_marks()
     - marks (property)
     - gpa()
     - get_info()
     - __str__()
     - __repr__()

2. CollegeStudent (inherits Student)
   - Additional Attribute:
     - department (str)
   - Overridden Methods:
     - gpa()
     - __str__()
     - __repr__()

Relationship:
CollegeStudent IS-A Student (Inheritance)
