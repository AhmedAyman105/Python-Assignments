# 01 
import datetime , pyfiglet , termcolor

theDate = datetime.datetime(2000,10,5)
now = datetime.datetime.now()

print(f"Days From 2000-10-5 To 2023-05-14 Is => {(now - theDate).days} Days")

print(termcolor.colored(pyfiglet.figlet_format("Elzero Web School"),"red"))

# 02 
x = datetime.datetime.now()

print(x.strftime("%Y-%m-%d"))
print(x.strftime("%B %d, %Y"))
print(x.strftime("%d - %B - %Y"))
print(x.strftime("%d / %B / %y"))
print(x.strftime("%d / %b / %Y"))
print(x.strftime("%a, %d %B %Y"))