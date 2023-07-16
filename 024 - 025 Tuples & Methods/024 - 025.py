# 1 
name = "Ahmed" 
print(name)
print(type(name))

# 2 
friends = ("Osama", "Ahmed", "Sayed")

friends=list(friends)
friends[0] = "Elzero"
friends = tuple(friends)
print(type(friends))
print(len(friends))
print(friends)

# 3 
nums = (1, 2, 3)
letters = ("A", "B", "C")
c = nums + letters
print(f"nums_and_letters_one = {c}")

# 4 
my_tuple = (1, 2, 3, 4)
a , b ,_ , c = my_tuple
print(a)
print(b)
print(c)
