# 01 
my_nums = [15, 81, 5, 17, 20, 21, 13]
x=1
for number in my_nums : 
    if number % 5 == 0:
        print(f"{x} _ {number}")
        x+=1
else :
    print("All Numbers Printed")

# 02 
myRange = range(1,21)

for n in myRange :
  print(f"{str(n).zfill(2)}")
else:
  print("All Numbers Printed")

# 03
# Input
my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}

degress = {
  "A" : "100",
  "B" : "80",
  "C" : "40",
  "D" : "20"
}

c=0
for key , value in my_ranks.items() :
    print(f"My Rank in {key} Is {value} And This Equal {degress[value]} Points")
    c = int(degress[value]) + c
else :
  print(f"Total Points is: {c}")

# 04 
# Input
students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}

print("------------------------------")
f=0
for main_key , main_value in students.items() :
  print(f"-- Student Name => {main_key}")
  for child_key , child_value in main_value.items() :
    print(f"- {child_key} => {degress[child_value]} ")
    f = int(degress[child_value]) + f
  print(f"total points for {main_key} is {f}")
  f=0
  print("------------------------------")



