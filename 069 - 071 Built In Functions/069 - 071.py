# 01
values = (0, 1, 2)

if any(values):

  my_var = 0

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

  print("Good")

else:

  print("Bad")

# Good

# 02 
v = 40

my_range = list(range(v))

print(sum(my_range, v) + pow(v, v, v))  # 820

for x in range(820):
  if sum(list(range(x+1))) == 820 :
    print(x)

# 03

n = 20  # 20 21 22

l = list(range(n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

  print("Good")

# Output => Good
for x in range(1,100):
  if round(sum(list(range(x)))/x) == 10 :
    print(x)
    



# 04 

def my_all(iterable) :
  y=0
  for i in iterable :
      if bool(i) :
        y+= 1
  if y == len(iterable) :
    return True
  else:
    return False



def my_any(iterable) :
  x =0
  for i in iterable:
    if bool(i):
      x +=1
  if x >= 1:
    return True
  else:
    return False



values = (0, 0, 1)

print(my_all(values))
print(my_any(values))

def my_min(iterable) :
  k = iterable[0]
  for i in iterable :
    if i < k:
      k = i 
  return k

def my_max(iterable) :
  k = iterable[0]
  for i in iterable :
    if i > k:
      k = i 
  return k

x = [2,3,5,6,1]
y = (2,3,5,6,1)
print(my_min(x))
print(my_max(x))
print(my_max(y))
print(my_min(y))