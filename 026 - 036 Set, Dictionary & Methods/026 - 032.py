# 01
myList = [1,2,3,3,4,5,1]
unique_list = list(set(myList))
print(unique_list)
print(type(unique_list))
print(unique_list[0:len(unique_list)-1])
print(unique_list[:-1])

# 02 
nums = {1,2,3}
let = {"A","B","C"}
print(nums.union(let))
print(nums|let)
nums.update(["A","B","C"])
print(nums)

# 03
my_set = {1, 2, 3}
letters = {"A", "B", "C"}

print(my_set)
my_set.clear()
print(my_set)

my_set.add("A")
my_set.add("B")
print(my_set)

my_set.discard("C")
print(my_set)

# 04 
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

print(set_one.issubset(set_two))

# 05 
mySkills = { 
    "One" : {
        "name" : "HTML",
        "Progress" : "50%"
    },
    "Two" : {
        "name" : "CSS",
        "Progress" : "60%"
    },
    "Three" : {
        "name" : "Python",
        "Progress" : "70%"
    }
}
# One
print (mySkills["One"]["name"] + " Progress Is " + mySkills["One"]["Progress"])
print ("{:s} Progress Is {:s} ".format(mySkills["One"]["name"] ,mySkills["One"]["Progress"]))

# Two 
print (mySkills["Two"]["name"] + " Progress Is " + mySkills["Two"]["Progress"])
print ("{:s} Progress Is {:s} ".format(mySkills["Two"]["name"] ,mySkills["Two"]["Progress"]))

# Three
print (mySkills["Three"]["name"] + " Progress Is " + mySkills["Three"]["Progress"])
print ("{:s} Progress Is {:s} ".format(mySkills["Three"]["name"] ,mySkills["Three"]["Progress"]))

mySkills["Four"] = {
    "name" : "AI",
    "Progress" : "40%"
}

print(mySkills)

# Four
print (mySkills["Four"]["name"] + " Progress Is " + mySkills["Four"]["Progress"])
print ("{:s} Progress Is {:s} ".format(mySkills["Four"]["name"] ,mySkills["Four"]["Progress"]))