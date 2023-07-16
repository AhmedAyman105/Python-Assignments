# 01 

class Game : 
    
    def __init__(self,name,developer,year,price) -> None:
        
        self.name = name
        self.developer = developer
        self.year = year
        self.price = price
    def price_in_pounds(self):
        return self.price * 15.6


game_one = Game("Ys", "Falcom", 2010, 50)

print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(f"Price In Egypt Is {game_one.price_in_pounds()}", end="")

# 02 
class User:

      def __init__(self,fname,sname,age,gender) -> None:
          
          self.fname = fname
          self.sname = sname
          self.age = age 
          self.gender = gender
      
      def full_details(self) : 
          
          if self.gender == "Male" :

              return f"Hello Mr {self.fname} {self.sname:.1s}. [{str(40 - self.age).zfill(2)}] Years To Reach 40"
          
          elif self.gender == "Female" :
              
              return f"Hello Mrs {self.fname} {self.sname:.1s}. [{str(40 - self.age).zfill(2)}] Years To Reach 40"


user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details()) # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details()) # Hello Mrs Eman O. [15] Years To Reach 40


# 03 

class Message:
    
    @staticmethod
    def print_message():
        return "Hello From Class Message"

print(Message.print_message())

# Output
# Hello From Class Message

# 04 

class Games:
    
    def __init__(self,args) -> None:

        self.game = args

    
    def show_games(self) :
        
        if self.game.__class__ is str :
            
            print(f"I Have One Game Called \"{self.game}\"")
        
        elif self.game.__class__ is list :
            
            print("I Have Many Games:")

            for x in self.game :
                
                print(f"-- {x}")
        if self.game.__class__ is int :
            
            print(f"I Have {self.game} Game.")


my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)


my_game.show_games()
my_games_names.show_games()
my_games_count.show_games()


# 05 

# Main Class
class Members:

  def __init__(self, n, p):

    self.name = n

    self.permission = p

  def show_info(self):

    return f"Your Name Is {self.name} And You Are {self.permission}"

class Admins(Members) :
    
    def __init__(self, n, p):
      
      super().__init__(n,p)

class Moderators(Members) :
    
    def __init__(self, n, p) :
      
      Members.__init__(self,n,p)

# Create Moderators Class Here

member_one = Admins("Osama", "Admin")
member_two = Moderators("Ahmed", "Moderator")

print(member_one.show_info())
# Output
# Your Name Is Osama And You Are Admin

print(member_two.show_info())
# Output
# Your Name Is Ahmed And You Are Moderator

# 06 

class A:

  def __init__(self, one):

    self.one = one

class B:

  def __init__(self, two):

    self.two = two

class C:

  def __init__(self, three):

    self.three = three

class Text(A,B,C) :

    def __init__(self, one , two , three):
        A.__init__(self,one)
        B.__init__(self,two)
        C.__init__(self,three)

    def show_name(self) : 
        
        return f"The Name Is {self.one}{self.two}{self.three}"

the_name = Text("El", "ze", "ro")

print(the_name.show_name())

# Ouput
# The Name Is Elzero
