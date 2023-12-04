import mysql.connector

connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            port='3306',
        )
cursor = connection.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS HOMETREASURES')
cursor.execute('USE HOMETREASURES')

suppliers_table = """
        CREATE TABLE IF NOT EXISTS FORNECEDORES(
            COD_FORNECEDOR INT AUTO_INCREMENT PRIMARY KEY,
            NOME VARCHAR(250) NOT NULL,
            ENDERECO VARCHAR(300),
            EMAIL VARCHAR(250),
            TELEFONE VARCHAR(20)
        )
        """

products_table = """
        CREATE TABLE IF NOT EXISTS PRODUTOS(
            COD_PRODUTO INT AUTO_INCREMENT PRIMARY KEY,
            NOME VARCHAR(250) NOT NULL,
            DESCRICAO TEXT,
            LINK_IMAGEM TEXT,
            PRECO DECIMAL NOT NULL,
            ESTOQUE INT,
            COD_FORNECEDOR INT,
            FOREIGN KEY (COD_FORNECEDOR) REFERENCES FORNECEDORES(COD_FORNECEDOR)
        )
        """

clients_table = """
        CREATE TABLE IF NOT EXISTS CLIENTES(
            COD_CLIENTE INT AUTO_INCREMENT PRIMARY KEY,
            NOME VARCHAR(250),
            DATA_NASC DATE,
            CPF VARCHAR(11),
            GENERO CHAR(1),
            ESTADO_CIVIL VARCHAR(20),
            NACIONALIDADE VARCHAR(30),
            EMAIL_CONTATO VARCHAR(200),
            TELEFONE BIGINT,
            CEP VARCHAR(8),
            ESTADO VARCHAR(50),
            CIDADE VARCHAR(80),
            LOGRADOURO VARCHAR(200),
            COMPLEMENTO VARCHAR(200),
            EMAIL_LOGIN VARCHAR(200),
            SENHA VARCHAR(50)
        )
        """

orders_table = """
        CREATE TABLE IF NOT EXISTS PEDIDOS(
            COD_PEDIDO INT AUTO_INCREMENT PRIMARY KEY,
            COD_CLIENTE INT,
            STATUS VARCHAR(40),
            DATA DATE,
            FOREIGN KEY (COD_CLIENTE) REFERENCES CLIENTES(COD_CLIENTE)
        )
        """

orders_items_table = """
        CREATE TABLE IF NOT EXISTS ITENS_PEDIDO(
            COD_ITEM INT AUTO_INCREMENT PRIMARY KEY,
            COD_PEDIDO INT,
            COD_PRODUTO INT,
            QUANTIDADE INT,
            FOREIGN KEY (COD_PEDIDO) REFERENCES PEDIDOS(COD_PEDIDO),
            FOREIGN KEY (COD_PRODUTO) REFERENCES PRODUTOS(COD_PRODUTO)
        )   
        """

cursor.execute(suppliers_table)
cursor.execute(products_table)
cursor.execute(clients_table)
cursor.execute(orders_table)
cursor.execute(orders_items_table)

cursor.close()
connection.commit()
connection.close()