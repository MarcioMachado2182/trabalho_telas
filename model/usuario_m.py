class Model:
    def __init__(self):
        self.users = []

    def add_user(self, nome, email, senha, login):
        self.users.append({"nome": nome, "email": email, "senha": senha, "login": login})
    
    def check_login(self, login, senha):
        for user in self.users:
            if user["login"] == login and user["senha"] == senha:
                return True
        return False
x