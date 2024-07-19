class Model:
    def __init__(self):
        self.users = []

    def add_user(self, nome, email, senha):
        self.users.append({"nome": nome, "email": email, "senha": senha})
    
    def check_login(self, email, senha):
        for user in self.users:
            if user["email"] == email and user["senha"] == senha:
                return True
        return False

