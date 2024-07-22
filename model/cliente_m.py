
import tkinter as tk
from tkinter import messagebox
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
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        except mariadb.Error as e:
            print(f"Erro ao inserir cliente: {e}")
            messagebox.showerror("Erro", "Erro ao cadastrar cliente!")

    def registrar_compra(self, cliente_id, camiseta, quantidade):
        cursor = self.conn.cursor()
        try:
            cursor.execute('INSERT INTO compras (cliente_id, camiseta, quantidade) VALUES (%s, %s, %s)', (cliente_id, camiseta, quantidade))
            self.conn.commit()
            return True
        except mariadb.connector.Error as e:
            print(f"Erro ao registrar compra: {e}")
            return False
        
    def selecionar_clientes(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM clientes')
        return cursor.fetchall()

    def fechar_conexao(self):
        self.conn.close()

    def historico_compras(self, cliente_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT camiseta, quantidade FROM compras WHERE cliente_id = %s', (cliente_id,))
        return cursor.fetchall()

    def fechar_conexao(self):
        self.conn.close()


