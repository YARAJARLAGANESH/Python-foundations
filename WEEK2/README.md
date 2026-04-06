# Where in My second Week:
i learned about classes, methods(types) ,private attributes inheritance, dunder methods 
csv file reading, writing ,loading and working of csv 

The task of second week is 

Build a Student class with name, grades, GPA calculation method
Extend Student into a CollegeStudent subclass with department
Write a CSV reader that loads student data and prints formatted report
Override __str__ and __repr__ in both classes

The Sturcture of My Task

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
      
3. Usage

Relationship:
CollegeStudent IS-A Student (Inheritance)
