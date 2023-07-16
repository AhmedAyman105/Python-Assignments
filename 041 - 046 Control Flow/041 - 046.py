# 01
num1 = int(input("Enter The First Number : ").strip())
num2 = int(input("Enter The Second Number : ").strip())
Operation = input("Enter Type Of Operation [ + - * /  % ]").strip()

if Operation == "+" :
    
    print(f"The Sum is {num1 + num2}")

elif Operation == "-" :
    
    print(f"The Subtraction is {num1 - num2}")

elif Operation == "*" :
    
    print(f"The Multiplication is {num1 * num2}")

elif Operation == "/" :

    print(f"The Division  is {num1 / num2}")

elif Operation == "%" :

    print(f"The Modelus  is {num1 % num2}")


# 02 

age = 15 

print("App Is Suitable For You" if age > 16 else "App Is Not Suitable For You")


# 03
age = int(input("Enter Your Age Please : ").strip())

print(f"Months {age * 12}")
print(f"Weeks {age * 12 * 4}")
print(f"Days {age * 12 * 4 * 7}")
print(f"Hours {age * 12 * 4 * 7 *24 }")
print(f"Minutes  {(age * 12 * 4 * 7 *24 *60) }")
print(f"Seconds  {(age * 12 * 4 * 7 *24 *60*60) }")


# 04 

countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

Country = input("Enter Your Country Please : ").strip().capitalize()

if Country in countries : 
    print(f"Your Country Eligible For Discount And The Price After Discount Is ${price - discount}")

else :
    print(f"Your Country Not Eligible For Discount And The Price  Is ${price}")