
from User import User
from DB import DataBase

user_obj = User("Satyam", 23, "satyam@gmail.com")
user_db = DataBase("root", "userdb", "root")

user_obj.showInfo()
user_db.saveToDB(user_obj)