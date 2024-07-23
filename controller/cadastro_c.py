
from view.cadastro_v import CadastroView
from model.model import Model
from view.login_v import LoginView
import  tkinter as tk
class CadastroController:
    def __init__(self,parent, view:CadastroView, model:Model):
        self.view = view
        self.model = model
        self.view.botao_cadastrar.config(command=self.cadastrar_usuario)

    def cadastrar_usuario(self):
        nome = self.view.get_nome()
        email = self.view.get_email()
        senha = self.view.get_senha()
        
        if nome and email and senha.isdigit():
            # Tentativa de cadastrar o usuário
            try:
                self.model.cadastrar_usuario(nome, email, senha)
            except Exception as e:
                # Tratamento de exceções específicas
                print(f'Erro ao cadastrar usuaário: {e}')
                # Exibir uma mensagem de erro para o usuário na interface
                self.view.mostrar_mensagem_erro("Erro ao cadastrar usuário.")
            else:
                # Limpar campos de entrada e atualizar lista de usuários após cadastro bem-sucedido
                self.view.nome_entry.delete(0, tk.END)
                self.view.email_entry.delete(0, tk.END)
                self.view.senha_entry.delete(0, tk.END)
                self.view.cadastrar_listbox.delete(0, tk.END)
                self.carregar_usuarios()
        else:
             # Lidar com o caso em que a validação dos dados falha
             self.view.mostrar_mensagem_erro("Por favor, preencha todos os campos corretamente.")


    def carregar_usuarios(self):

        usuarios= self.model.selecionar_usuarios()
        for usuario in usuarios:
            self.view.adicionar_usuario_lista(usuario) 

