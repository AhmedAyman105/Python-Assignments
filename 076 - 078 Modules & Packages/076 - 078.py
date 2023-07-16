# 01 
import random

print(f"Random Number Between 10 And 50 => {random.randint(10,51)}")
print(f"Random Even Number Between 2 And 10 => {random.randrange(2,11,2)}")
print(f"Random Odd Number Between 1 And 9 => {random.randrange(1,10,2)}")

# 02 
import sys

sys.path.append(r"F:\30.Elzero web school\Python 2023\Mastering Python\000 - Assignmens\076 - 078 Modules & Packages\Python")

import my_mod

print(my_mod.say_hello("Ahmed"))
print(my_mod.say_welcome("Ahmed"))

# 03 
from my_mod import say_hello

print(say_hello("Ahmed"))

# 04 
from my_mod import say_hello as  new_welcome
print(new_welcome("Ahmed"))

