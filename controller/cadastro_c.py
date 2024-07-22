
from view.cadastro_v import CadastroView
from model.model import Model
from view.login_v import LoginView

class CadastroController:
    def __init__(self,parent, view:CadastroView, model:Model):
        self.view = view
        self.model = model
        self.view.botao_ir_para_login.config(command=lambda:parent.switch_frame(LoginView))