# 01
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0])
print(friends.pop(0))
print(friends[-5])
print(friends[-1])
print(friends.pop(-1))
print(friends[4])

# 02 
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[::2])
print(friends[1::2])

# 03 
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[1:4])
print(friends[3:5])

# 04 
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends[3:5] = "Elzero" , "Elzero"
print(friends)

# 05
friends = ["Osama", "Ahmed", "Sayed"]
friends.append("Nasser")
friends.insert(0,"eska")
print(friends)

# 06 
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
friends[0:2] = []
friends.remove("Salem")
print(friends)

# 07
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

friends.extend(employees)
friends.extend(school)
print(friends)

# 08 
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)

# 09 
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(friends))


# 10 
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[-1][0])
print(technologies[-1][-1])