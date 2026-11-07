
class User:
    
    def __int__(self, name:str, email:str) -> None:
        self.name = name
        self.age = self
        self.email = email
    
    def showInfo(self) -> None:
        print(f"Your name is {self.name} and your age is {self.age}")
    
    def isAdult(self) -> bool:
        return self.age >= 18
    
    def SaveToDB(self):
        print(f"{self.name} is getting Saved to the DataBase")
        
    def deleteUser(self):
        print(f"{self.name} is getting deleted from the DataBase")
        
        
user1 = User()
user1.name = "Satyam"
user1.age = 23
user1.email = "satyam@gmail.com"

user1.showInfo()
print(user1.isAdult())
user1.SaveToDB()
user1.deleteUser()


## This is not a good code as there are many reason to make changes in the User class