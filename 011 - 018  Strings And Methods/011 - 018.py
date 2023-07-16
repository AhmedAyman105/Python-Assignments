# 01 
myName = "Ahmed"
myAge = 23 
myCountry = "Egypt"

print(f"Hello '{myName}', How You Doing \\ \"\"\" Your Age Is \"{myAge}\" + And Your Country is {myCountry}")

print(f"Hello '{myName}', How You Doing \\ \"\"\" Your Age Is \"{myAge}\" ")

# 02
print(f"Hello '{myName}', How You Doing \\\n \"\"\" Your Age Is \"{myAge}\" + \n And Your Country is {myCountry}")

#03 
name = 'Elzero'
print(name[1])
print(name[2])
print(name[-1])
print(name[len(name)-1])

#04 
print(name[1:4])
print(name[0::2])
print(name[-2::-2])

#05
name = "#@#@Elzero#@#@"
print(name.strip("#@"))

#06 
num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"

print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(len(num5)))

#07
name_one = "Osama"
name_two = "Osama_Elzero"

print(name_one.rjust(20,"@"))
print(name_two.rjust(20,"@"))

#08
name_one = "OSamA"
name_two = "osaMA"

print(name_one.swapcase())
print(name_two.swapcase())

#09 
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))


#10 
name = "Elzero"
print(name.index("z"))


#11 
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3","Love",1))


#12 
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3","Love"))


#13
name = "Osama"
age = 38
country = "Egypt"
# My Name Is Osama, And My Age Is 38, And My Country Is Egypt

print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}")

