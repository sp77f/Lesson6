class User:
    def __init__(self, id,name, access_level ):
        self.name = name
        self._id = id
        self.__access_level = "user"

    def get_info(self):
        print("User info: ", self.name, self._id, self.__access_level)
    def set_name (self, name):
        self.name = name
class Admin(User):
    def __init__(self, id, name, access_level):
        super().__init__(id, name, access_level)
        self.__access_level = "admin"
    def get_info(self):
        print("Admin info: ", self.name, self._id, self.__access_level)
    def _add_user(user):
        if user in users:
            print("Такой пользователь уже есть")
        else:
            users.append(user)
            print(f"Пользователь {user.name} добавлен")

    def __delete_user(user):
        if user in users:
            users.remove(user)
            print(f"Пользователь {user.name} удален")
        else:
            print("User does not exist")
    def _confirm_delete(user):
        print(f"Вы уверены что хотите удалить пользователя {user.name}? (y/n)")
        answer = input()
        if answer == "y":
            Admin.__delete_user(user)
        else:
            print("Действие отменено")
users=[]
users.append(User(1, "Piter", "user1"))
users.append(User(2, "John", "user1"))
users.append(User(3, "Abram", "user1"))
print("Текущий список пользователей: ")
for user in users:
    user.get_info()
new_user = User(4, "Mark", "user4")
Admin._add_user(new_user)
print("Обновленный список пользователей: ")
for user in users:
    user.get_info()
admin = Admin(1, "Johnny", "admin1")
admin.get_info()
Admin._confirm_delete(users[1])
print("Обновленный список пользователей: ")
for user in users:
    user.get_info()