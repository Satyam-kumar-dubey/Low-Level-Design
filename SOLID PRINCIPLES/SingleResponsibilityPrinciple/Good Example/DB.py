
from User import User

class DataBase:
    
    def __init__(self, user, db, password) -> None:
        self.user = user
        self.db = db
        self.password = password
        
    def saveToDB(self, user:User) -> None:
        print(f"{user.name} is getting saved in the {self.db}")
        
    def deleteFromDB(self, user:User) -> None:
        print(f"{user.name} is getting deleted from the {self.db}")
        
        