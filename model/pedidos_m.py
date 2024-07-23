


import mariadb
import sys

class ClienteModel:
    def __init__(self, db_name='sarah_hassen_cardoso', user='sarah_hassen_cardoso', password='12345', host='localhost', port=3306):
        try:
            self.conn = mariadb.connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database=db_name
            )
        except mariadb.Error as e:
            print(f"Erro de conexão ao MariaDB: {e}")
            sys.exit(1)
       
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pedidos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                cliente_id INT,
                itens TEXT,
                valor_total DECIMAL(10, 2),
                forma_pagamento VARCHAR(50),
                endereco_entrega VARCHAR(200),
                tipo_entrega VARCHAR(50)
            )
        ''')
        self.conn.commit()

    def inserir_pedido(self, cliente_id, itens, valor_total, forma_pagamento, endereco_entrega, tipo_entrega):
        cursor = self.conn.cursor()
        try:
            cursor.execute('INSERT INTO pedidos (cliente_id, itens, valor_total, forma_pagamento, endereco_entrega, tipo_entrega) VALUES (%s, %s, %s, %s, %s, %s)',
                           (cliente_id, itens, valor_total, forma_pagamento, endereco_entrega, tipo_entrega))
            self.conn.commit()
            return True
        except mariadb.Error as e:
            print(f"Erro ao inserir pedido: {e}")
            return False

    def fechar_conexao(self):
        self.conn.close()