courses = []

with open('courses.csv','r', encoding = 'utf-8') as file:
    for line in file:
        courses.append(line.rstrip())


for course in sorted(courses):
    print(course)
