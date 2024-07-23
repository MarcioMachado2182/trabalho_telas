
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
            CREATE TABLE IF NOT EXISTS clientes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                cpf VARCHAR(20) UNIQUE,
                email VARCHAR(100)
            )
        ''')
        self.conn.commit()

    def inserir_cliente(self, nome, cpf, email):
        cursor = self.conn.cursor()
        try:
            cursor.execute('INSERT INTO clientes (nome, cpf, email) VALUES (?, ?, ?)', (nome, cpf, email))
            self.conn.commit()
            return True
        except mariadb.Error as e:
            print(f"Erro ao inserir cliente: {e}")
            return False

    def inserir_pedido(self, cliente_id, items, valor_total, forma_pagamento, endereco_entrega, metodo_entrega):
        cursor = self.conn.cursor()
        try:
            cursor.execute('INSERT INTO pedidos (cliente_id, items, valor_total, forma_pagamento, endereco_entrega, metodo_entrega) VALUES (%s, %s, %s, %s, %s, %s)',
                           (cliente_id, items, valor_total, forma_pagamento, endereco_entrega, metodo_entrega))
            self.conn.commit()
            return True
        except mariadb.Error as e:
            print(f"Erro ao inserir pedido: {e}")
            return False
        
    def selecionar_clientes(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM clientes')
        return cursor.fetchall()

    def historico_compras(self, cliente_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT items, valor_total FROM pedidos WHERE cliente_id = %s', (cliente_id,))
        return cursor.fetchall()

    def fechar_conexao(self):
        self.conn.close()


