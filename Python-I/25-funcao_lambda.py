power = lambda num: num**2
pair = lambda x: x%2 == 0
divNum = lambda x,y: x/y
reverse = lambda s: s[::-1]

print(power(5))
print(power(9))

print(pair(4))
print(pair(5))

print(divNum(4,2))
print(divNum(6,7))

print(reverse("Python"))
print(reverse("Javascript"))