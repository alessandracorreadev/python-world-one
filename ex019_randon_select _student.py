from random import choice

s1 = input("Enter the first student`s name: ")
s2 = input("Enter the second student`s name: ")
s3 = input("Enter the third student`s name: ")
s4 = input("Enter the fourth student`s name: ")
students = [s1, s2, s3, s4]

print(f"The select student is {choice(students)}")