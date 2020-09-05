#  Author: Shakeb Siddiqui sms8508@psu.edu
# Collaborator:
grade1 = input("Enter your course 1 letter grade: ")
credit1 = input("Enter your course 1 credit: ")
credit = float(credit1)

if grade1 == ("A"):
  course1gpa=float(4.0)
  print (f"Grade point for course 1 is {course1gpa}")
elif grade1 == ("A-"):
  print (f"Grade point for course 1 is {float(3.67)}")
elif grade1 == ("B+"):
  print (f"Grade point for course 1 is {float(3.33)}")
elif grade1 == ("B-"):
  print (f"Grade point for course 1 is {float(2.67)}")
elif grade1 == ("C+"):
  print (f"Grade point for course 1 is {float(2.330)}")
elif grade1 == ("C"):
  print (f"Grade point for course 1 is {float(2.0)}")
elif grade1 == ("D"):
  print (f"Grade point for course 1 is {float(1.0)}")
elif grade1 == ("F"):
  print (f"Grade point for course 1 is {float(0.0)}")
else:
  print(f"Grade point for course 1 is {float(0.0)}")


grade2 = input("Enter your course 2 letter grade: ")
credit2 = input("Enter your course 2 credit: ")
credit2 = float(credit2)

if grade2 == ("A"):
  print (f"Grade point for course 2 is: {float(4.0)}")
elif grade2 == ("A-"):
  print (f"Grade point for course 2 is {float(3.67)}")
elif grade2 == ("B+"):
  print (f"Grade point for course 2 is {float(3.33)}")
elif  grade2 == ("B"):
  print (f"Grade point for course 2 is {float(3.0)}")
elif grade2 == ("B-"):
  print (f"Grade point for course 2 is {float(2.67)}")
elif grade2 == ("C+"):
  print (f"Grade point for course 2 is {float(2.33)}")
elif grade2 == ("C"):
  print (f"Grade point for course 2 is {float(2.0)}")
elif grade2 == ("D"):
  print (f"Grade point for course 2 is {float(1.0)}")
elif grade2 == ("F"):
  print (f"Grade point for course 2 is {float(0.0)}")
else:
  print(f"Grade point for course 2 is {float(0.0)}")

grade3 = input("Enter your course 3 letter grade: ")
credit3 = input("Enter your course 3 credit: ")
credit3 = float(credit3)

if grade3 == ("A"):
  print (f"Grade point for course 3 is: {float(4.0)}")
elif grade3 == ("A-"):
  print (f"Grade point for course 3 is {float(3.67)}")
elif grade3 == ("B+"):
  print (f"Grade point for course 3 is {float(3.0)}")
elif grade3 == ("B-"):
  print (f"Grade point for course 3 is {float(2.67)}")
elif grade3 == ("C+"):
  print (f"Grade point for course 3 is {float(2.33)}")
elif grade3 == ("C"):
  print (f"Grade point for course 3 is {float(2.00)}")
elif grade3 == ("D"):
  print (f"Grade point for course 3 is {float(1.00)}")
elif grade3 == ("F"):
  print (f"Grade point for course 3 is {float(0.0)}")
else:
  print(f"Grade point for course 3 is {float(0.0)}")

GPA = ((course1gpa * credit1) + (grade2 * credit2) + (grade3 * credit3)) / ((credit1 + credit2 + credit3)) 
print(f"Your GPA is: {GPA}")