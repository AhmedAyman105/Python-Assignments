# 01
num = input("Add Your Number ")


if len(num) > 0 and len(num) != 1 :
    raise IndexError("Only One Character Allowed")
elif num == "0" :
    raise ValueError("Number Must Be Larger Than 0")
elif num.isalpha() :
  raise Exception("Only Numbers Allowed")


# 02
LETTER = input("Add Letter From A to Z")

try : 
  if len(LETTER) >= 2 :
    raise IndexError
  elif LETTER.isalpha() == False :
    raise ValueError
  
except IndexError:
  print("You Must Write One Character Only")

except ValueError :
  print("The Letter Not In A - Z")

else:
  print(f"You Typed {LETTER}")

# 03 
def calculate(num1, num2) -> int:
  return num1 + num2

print(calculate(20, 30))
print(152 - 94)