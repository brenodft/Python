courses = []
with open("courses.csv", "r" ,encoding="utf-8") as file:
    for line in file:
        name, category = line.rstrip().split(",")
        course = {}
        course["name"] = name
        course["category"] = category
        courses.append(course)
print(courses)

def get_language(course):
    return course["name"]
def get_category(course):
    return course["category"]

for course in sorted(courses, key = get_language, reverse=False):
    print(f"{course['name']} -{course['category']}")