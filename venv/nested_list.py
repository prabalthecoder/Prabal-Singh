if __name__ == '__main__':
    n = int(input())
student = []
marks = []

for i in range(n):
    student.append(input())
    marks.append(input())
marks_list = list(zip(student, marks))
grades = {}

for j in range(0, n):
    grades[marks_list[j][0]] = marks_list[j][1]
sorted_marks = sorted(set(grades.values()))
match = sorted_marks[1]

result = []
for name in grades.keys():
    if grades[name] == match:
        result.append(name)
for k in result:
    print(k)