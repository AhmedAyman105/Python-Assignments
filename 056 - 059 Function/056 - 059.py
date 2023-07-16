# 01
def calculate(n1,n2,t="+") :
    if t == "+" or t.lower().startswith("a") :
        print(n1+n2)
    elif t == "-" or  t.lower().startswith("s"):
        print(n1-n2)
    elif t == "*" or t.lower().startswith("m"):
        print(n1*n2)
    else :
        print("Wrong Operator")

calculate(10, 20) # 30
calculate(10, 20, "AdD") # 30
calculate(10, 20, "a") # 30
calculate(10, 20, "A") # 30

calculate(10, 20, "S") # -10
calculate(10, 20, "subTRACT") # -10

calculate(10, 20, "Multiply") # 200
calculate(10, 20, "m") # 200


def calculate(n1,n2,t="+") :
    if t == "+" or t.lower().startswith("a") :
        return(n1+n2)
    elif t == "-" or  t.lower().startswith("s"):
        return(n1-n2)
    elif t == "*" or t.lower().startswith("m"):
        return(n1*n2)
    else :
        print("Wrong Operator")

print(calculate(10, 20)) # 30
print(calculate(10, 20, "AdD")) # 30
print(calculate(10, 20, "a")) # 30
print(calculate(10, 20, "A")) # 30

print(calculate(10, 20, "S")) # -10
print(calculate(10, 20, "subTRACT")) # -10

print(calculate(10, 20, "Multiply")) # 200
print(calculate(10, 20, "m")) # 200

# 02 
def addition(*Numbers) :
    sum=0
    for  number in Numbers : 
        if number == 10 :
            continue
        elif number == 5 :
            sum = sum - number 
        else :
            sum = sum + number
    return sum

# Tests
print(addition(10, 20, 30, 10, 15)) # 65
print(addition(10, 20, 30, 10, 15, 5, 100)) # 160


# 03 

def show_skills(name,*skills) :
    if skills == () :
        print(f"Hello {name} You Have No Skills To Show")
    else :
        print(f"Hello {name} your skills is:")
        for skill in skills : 
            print(f"- {skill}")
        
show_skills("Ahmed","HTML","CSS","JS","Python")
show_skills("Ahmed")

# 04 

def say_hello(name="Unknown",age="Unknown",country="Unknown") :
    return f"hello {name} Your Age Is {age} And Your Country Is {country}"

print(say_hello("Osama", 38, "Egypt"))
print(say_hello())

