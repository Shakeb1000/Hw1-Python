# Author: Shakeb Siddiqui sms8508@psu.edu
# Collaborator: Eric Byjoo ezb5481@psu.edu

grade1 = input("Enter your course 1 letter grade: ")
credit1 = input("Enter your course 1 credit: ")
credit1 = float(credit1)

if grade1 == ("A"):
  course1gp=float(4.0)
  print (f"Grade point for course 1 is: {course1gp}")
elif grade1 == ("A-"):
  course1gp=float(3.67)
  print (f"Grade point for course 1 is: {course1gp}")
elif grade1 == ("B+"):
  course1gp=float(3.33)
  print (f"Grade point for course 1 is: {course1gp}")
elif grade1 == ("B"):
  course1gp=float(3.0)
  print (f"Grade point for course 1 is: {course1gp}")
elif grade1 == ("B-"):
  course1gp=float(2.67)
  print (f"Grade point for course 1 is: {course1gp}")
elif grade1 == ("C+"):
  course1gp=float(2.330)
  print (f"Grade point for course 1 is: {course1gp}")
elif grade1 == ("C"):
  course1gp=float(2.0)
  print (f"Grade point for course 1 is: {course1gp}")
elif grade1 == ("D"):
  course1gp=float(1.0)
  print (f"Grade point for course 1 is: {course1gp}")
elif grade1 == ("F"):
  course1gp=float(0.0)
  print (f"Grade point for course 1 is: {course1gp}")
else:
  course1gp=float(0.0)
  print(f"Grade point for course 1 is: {course1gp}")


grade2 = input("Enter your course 2 letter grade: ")
credit2 = input("Enter your course 2 credit: ")
credit2 = float(credit2)

if grade2 == ("A"):
  course2gp = float(4.0)
  print (f"Grade point for course 2 is: {course2gp}")
elif grade2 == ("A-"):
  course2gp=float(3.67)
  print (f"Grade point for course 2 is: {course2gp}")
elif grade2 == ("B+"):
  course2gp=float(3.33)
  print (f"Grade point for course 2 is: {course2gp}")
elif  grade2 == ("B"):
  course2gp =float(3.0)
  print (f"Grade point for course 2 is: {course2gp}")
elif grade2 == ("B-"):
  course2gp=float(2.67)
  print (f"Grade point for course 2 is: {course2gp}")
elif grade2 == ("C+"):
  course2gp =float(2.33)
  print (f"Grade point for course 2 is: {course2gp}")
elif grade2 == ("C"):
  course2gp=float(2.0)
  print (f"Grade point for course 2 is: {course2gp}")
elif grade2 == ("D"):
  course2gp=float(1.0)
  print (f"Grade point for course 2 is: {course2gp}")
elif grade2 == ("F"):
  course2gp=float(0.0)
  print (f"Grade point for course 2 is: {course2gp}")
else:
  course2gp=float(0.0)
  print(f"Grade point for course 2 is: {course2gp}")

grade3 = input("Enter your course 3 letter grade: ")
credit3 = input("Enter your course 3 credit: ")
credit3 = float(credit3)

if grade3 == ("A"):
  course3gp=float(4.0)
  print (f"Grade point for course 3 is: {course3gp}")
elif grade3 == ("A-"):
  course3gp=float(3.67)
  print (f"Grade point for course 3 is: {course3gp}")
elif grade3 == ("B+"):
  course3gp=float(3.0)
  print (f"Grade point for course 3 is: {course3gp}")
elif grade3 == ("B-"):
  course3gp=float(2.67)
  print (f"Grade point for course 3 is: {course3gp}")
elif grade3 == ("C+"):
  course3gp=float(2.33)
  print (f"Grade point for course 3 is: {course3gp}")
elif grade3 == ("C"):
  course3gp=float(2.00)
  print (f"Grade point for course 3 is: {course3gp}")
elif grade3 == ("D"):
  course3gp=float(1.00)
  print (f"Grade point for course 3 is: {course3gp}")
elif grade3 == ("F"):
  course3gp=float(0.0)
  print (f"Grade point for course 3 is: {course3gp}")
else:
  course3gp=float(0.0)
  print(f"Grade point for course 3 is: {course3gp}")

GPA = ((course1gp * credit1) + (course2gp * credit2) + (course3gp * credit3)) / ((credit1 + credit2 + credit3)) 
print(f"Your GPA is: {GPA}")