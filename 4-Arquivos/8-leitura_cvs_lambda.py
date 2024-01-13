courses = []
with open("courses.csv", "r" ,encoding="utf-8") as file:
    for line in file:
        name, category = line.rstrip().split(",")
        course = {}
        course["name"] = name
        course["category"] = category
        courses.append(course)
print(courses)


for course in sorted(courses, key = lambda course: course["name"], reverse=False):
    print(f"{course['name']} -{course['category']}")