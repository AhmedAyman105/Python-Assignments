# 01 

def remove_chars(name) :
    return name[1:-1]

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

cleaned_list = map(remove_chars,friends_map)
for i in cleaned_list :
  print(i)

print("=" * 50)

for i in map(lambda name :name[1:-1] ,friends_map) :
  print(i)

# 02 
friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

def get_names(name) :
  return name.endswith("m")

names = filter(get_names,friends_filter)
for name in names :
  print(name)


for name in filter(lambda name : name.endswith("m"),friends_filter) :
  print(name)

# 03 
nums = [2, 4, 6, 2]

def multiplyAll(num1,num2):
  return num1 * num2
from functools import reduce

result = reduce(multiplyAll,nums)

print(result)


result2 = reduce(lambda num1,num2 : num1*num2 , nums)

print(result2)

# 04 
skills = reversed(("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript"))
indexedSkills = enumerate(skills,50)
for i , s in (indexedSkills) :
  if type(s) != int :
    print(f"{i} - {s}")

# Second Solution 

def removeNumbers(itrable):
  return type(itrable) != int

cleaned = enumerate(filter(removeNumbers,skills),50)

for i , s in cleaned : 
  print(f"{i} - {s}")

