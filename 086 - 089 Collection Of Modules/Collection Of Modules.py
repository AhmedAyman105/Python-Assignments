# 01 
my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

for data in zip(my_list, my_tuple):
  my_data.extend(data)
final_string = "".join(my_data).capitalize()

print(final_string)

print(my_data)

# 02 
my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
  if type(item1) != int:
    my_data.extend(item1)
final_string = "".join(my_data).capitalize()

print(final_string)

# 03 
from PIL import Image

my_image = Image.open(r"F:\30.Elzero web school\Python 2023\Mastering Python\000 - Assignmens\086 - 089 Collection Of Modules\elzero-pillow.png")

# The box take upper left corner and lower left corner
box_L = (400,0,800,400) # L
box_O = (800,400,1200,800) # O
box_E = (0,400,400,800) # E
box = (0,0,1200,400)
cropped_image1 = my_image.crop(box_L)
cropped_image2 = my_image.crop(box_O)
cropped_image3 = my_image.crop(box_E)
cropped_image4 = my_image.crop(box)

cropped_image1.show() # L
cropped_image2.show() # O
cropped_image3.show() # O

gray_l = cropped_image1.convert("L")
gray_l.show()
gray_l.save(r"F:\30.Elzero web school\Python 2023\Mastering Python\000 - Assignmens\086 - 089 Collection Of Modules\L.png","png")

cropped_image4.show()
gray_2 = cropped_image4.convert("L")
rotated = gray_2.rotate(180)
rotated.show()
rotated.save(r"F:\30.Elzero web school\Python 2023\Mastering Python\000 - Assignmens\086 - 089 Collection Of Modules\rotated.png","png")


# 04 
# Write Function With Help To Get The Output

def say_hello_to(someone) :
    '''
    parameter(someone) => Person Name
    Function To Say Hello To Anyone
    '''
    return f"hello {someone}"

print(say_hello_to("Osama")) 

print(say_hello_to.__doc__)

