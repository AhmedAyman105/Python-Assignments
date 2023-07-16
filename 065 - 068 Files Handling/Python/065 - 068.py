n=0
for i in range (1,51) :
    if i == 25 :
      myfile = open(rf"C:\Users\Ahmed Ayman\Desktop\Python\special-txt.txt","w")
      myfile.write(f"Elzero web school => {i}\n")
      myfile.close()
      n +=1
    else:
      myfile = open(rf"C:\Users\Ahmed Ayman\Desktop\Python\txt{i}.txt","w")
      myfile.write(f"Elzero web school => {i}\n")
      myfile.close()
      n +=1

import os 

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())                # folder that contain the file 
print(os.path.abspath(__file__))  # assign.py path 
print(os.path.dirname(__file__))  # folder that contain the file
print(os.path.basename(__file__)) # file name 
print(n)


###################################################################

# 02 

myfile = open(r"C:\Users\Ahmed Ayman\Desktop\Python\txt1.txt","a")
myfile.write("Appended => Elzero Web School\n"*50)
myfile.close()


# 03 

myfile = open(r"F:\30.Elzero web school\Python 2023\Mastering Python\000 - Assignmens\065 - 068 Files Handling\Python\txt1.txt","r")
myList= myfile.readlines()
print(myList)
print(f"The Number Of lines is => {len(myList)}")


x=0
for i in range(0,len(myList)) :
    for j in myList[i] :
      if j !=" " :
        x+=1
    x -=1 

print(x) # number of letters
x=0

for i in range(0,len(myList)) :
    for j in myList[i] :
      if j == " " :
        x+=1
    x+=1
print(x)
x=0
for i in range(0,len(myList)) :
    for j in myList[i] :
      if j == "l" :
        x+=1
print(x)

for i in range((n-9),51) :
  os.remove(fr"C:\Users\Ahmed Ayman\Desktop\Python\txt{i}.txt")