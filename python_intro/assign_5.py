class Admin:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def assign_role(self, user, role):
        user.set_role(role)

    def get_user_info(self, user):
        print(user.get_user_info())


class User:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email
        self.__role = None

    def set_role(self, role):
        self.__role = role

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_name(self):
        return self.__role

    def get_user_info(self):
        return f'Name: {self.__name}\n Email: {self.__email}\n Role: {self.__role}'

class Instructor(User):
    def __init__(self, name, email, expertise):
        super().__init__(name, email)
        self.__expertise = expertise

    def get_expertise(self):
        self.__expertise = expertise

    def get_user_info(self):
        userInfo = super().get_user_info()
        return f"{userInfo}\nExpertise: {self.__expertise}\n"

class Learner(User):
    def __init__(self, name, email, path):
        super().__init__(name, email)
        self.__path = path

    def get_path(self):
        self.__path = path

    def get_user_info(self):
        userInfo = super().get_user_info()
        return f"{userInfo}\nStream: {self.__path}\n"
