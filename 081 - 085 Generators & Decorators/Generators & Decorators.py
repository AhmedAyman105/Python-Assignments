# 01
def reverse_string(my_string):
  for i in my_string[-1::-1]:
    yield i

for c in reverse_string("Elzero") :
  print(c)

print(reverse_string("Elzero"))


# 02 

def myDecorator(func) :

  def nestedDecorator() :

    print("Sugar Added From Decorators")

    func()

    print("####################")

  return nestedDecorator

@myDecorator
def make_tea():
  print("Tea Created")

@myDecorator
def make_coffe():
  print("Coffe Created")


make_tea()
make_coffe()