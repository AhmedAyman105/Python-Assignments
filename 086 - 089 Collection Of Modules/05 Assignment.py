''' This Module Used To Correct pylint'''
# 05

myFriends = ["Ahmed", "Osama", "Sayed"]


def say_hello(some_peoples) -> list:
    ''' This Function Used To Correct pylint'''
    for someone in some_peoples:
        print(f"Hello {someone}")

say_hello(myFriends)
