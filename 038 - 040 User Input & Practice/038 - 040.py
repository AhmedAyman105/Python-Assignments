# 01
name = input("Enter The Name : ").strip().capitalize()
print(f"Hello {name}, Happy To See You Here.")

# 02 
age = int(input("Enter Your Age"))

print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You" if age < 16 else f"Hello Your Age Is {age}, All Articles Is Suitable For You")
# 03
fname = input("Enter first name") 
sname = input("Enter second name") 

print(f"Hello {fname} {sname:.1s}.")

# 04 
email = input("Enter Your Email : ").strip().lower()
e = email[:email.index("@")]
w = email[email.index("@") + 1 :email.index(".")]
tD = email[email.index(".") + 1 : ]
print(f"your user name is {e}")
print(f"your website is {w}")
print(f"you Top domain is {tD}")