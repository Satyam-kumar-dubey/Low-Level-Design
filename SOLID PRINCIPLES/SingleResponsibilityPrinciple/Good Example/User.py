
class User:
    
    def __init__(self, name:str ,age:int , email:str):
        self.name = name
        self.age = age
        self.email = email
        
    def showInfo(self)-> None:
        print(f"Your name is {self.name} and your are {self.age} years old")
        
    def isAdult(self) -> bool:
        return self.age >= 18
    
    
## Here the user class contains code only related to the user not anything else