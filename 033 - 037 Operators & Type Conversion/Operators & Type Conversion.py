# 01 
print(bool(True))
print(bool(100))
print(bool([1]))
print(bool(100>50))

print(bool(None))
print(bool(0))
print(bool([]))
print(bool({}))

# 02
html = 80
css = 60
javascript = 70


print(bool(html > 50 and css > 50 and javascript > 50))


# 03 
num_one = 10
num_two = 20
num = 20

print(num > num_one or num > num_two)
print(num > num_one and num > num_two)

# 04 
num_one = 10 
num_two = 20

result = num_one + num_two
print(result)

result **= 3
print(result)

print(result%26000)
print(result%26000/5)
print(type(str(result%26000/5)))