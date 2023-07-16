# 01 
num = int(input("Enter The number").strip())

t = type(num) == int
c = 0
if num < 5 and t == True :
    print("The number you entered is less than 5")
elif num > 5 and t == True :
    while num > 0 :
        num -= 1
        if num == 0 :
            print("Number 0 Is Not Larger Than 0")
        elif num == 6:
            continue
        else :
            print(f"The num is {num}")
            c +=1
print(f"{c} Numbers Printed  Successfully.")

# 02 
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
a= 0
b=1
x =0
while a < len(friends) : 
    if friends[a] == friends[a].capitalize():
        print(f"#{b} {friends[a]}")
        b += 1
        a += 1
    else :
        x += 1
        a+=1
print(f"number of neglected names is {x}")

# # 03 
# # Code
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills:
    print(skills.pop(0))


# 04 
my_friends = []
max_friends = 4
a = 0
while a < max_friends:
    name = input("Enter The Name You Want To Add To The List : ").strip()
    if name == name.upper() :
        print("InValid Name")

    elif name == name.lower() :
        my_friends.append(name.capitalize())
        print(f"The First Letter From {name} Which is {name:.1s} is Capitalized")
        a+= 1
        print(f"The Name {name} Is Added Successfully , {max_friends - a} friends left")
    
    elif name == name.title() :
        my_friends.append(name)
        a+=1
        print(f"The Name {name} Is Added Successfully , {max_friends - a} friends left")
else :
    print("The List Is Full")


print(my_friends)

