student_count = int(input())
students = []

for _ in range(student_count):
    students.append(input().split())

students.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])
