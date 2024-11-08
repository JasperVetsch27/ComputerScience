# 1

students = {}

for i in range(5):
    student = input("What is the name of the student\n>")
    grade = input("What is the grade of the student\n>")
    students[student] = grade

for p, t in students.items():
    print(p + ": " +  t)

# 2

student = {"name": "Alice", "age": 16, "grade": "A"}

for key, value in student.items():
    print(key + " " + str(value))

# 3

student["grade"] = "A+"

print(student)

