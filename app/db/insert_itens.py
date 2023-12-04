import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port='3306',
    database="HomeTreasures"
)
cursor = connection.cursor()

suppliers = """
    INSERT INTO FORNECEDORES (NOME, ENDERECO, EMAIL, TELEFONE)
    VALUES
    ('Faro Atadado', 'Rua Piauí, 1500. Uberlândia, MG', 'faroatacado@email.com', 34999151001),
    ('Fornecedor 2', 'Avenida B, 456', 'fornecedor2@email.com', '9876543210'),
    ('Fornecedor 3', 'Rua C, 789', 'fornecedor3@email.com', '5555555555'),
    ('Fornecedor 4', 'Avenida D, 101', 'fornecedor4@email.com', '9999999999'),
    ('MadeiraMadeira', 'R. Mal. Deodoro, 717 - Centro, Curitiba - PR, 80010-010', 'madeiramadeira@email.com', '08000800099')
"""

products = """
    INSERT INTO PRODUTOS (NOME, DESCRICAO, LINK_IMAGEM, PRECO, ESTOQUE, COD_FORNECEDOR)
    VALUES
    ('Armário Sofia 1 porta', 'Com ele você não terá mais problemas com a organização do seu lar, suas prateleiras espaçosas são ótimas para você guardar sapatos e roupas, possuí  1 Porta de giro, 3 Gavetas e Nichos abertos.', 'https://product-hub-prd.madeiramadeira.com.br/711955/images/4412d5e9-e6cc-4058-a33c-0d8931221741jequitiba1644263185200zoom.jpg?width=700&canvas=1:1&bg-color=FFF',  200.00, 50, 1),
    ('Cama Athenas Solteiro', 'Se você está em busca de uma noite revigorante de sono, vai se apaixonar pela Cama Athenas. Confeccionada com materiais de qualidade e resistência, ela terá uma vida útil muito mais longa e ainda ajudará a decorar seu dormitório com graça e charme.', 'https://atacadotropicalmoveis.com.br/wp-content/uploads/2021/08/Cama-Athenas-Solt.jpg', 599.90, 30, 2),
    ('Cadeira Slin Eiffel', 'Além de funcional e super confortável, a cadeira Slim Eiffel irá completar a decoração da sua casa! Perfeita para sala de jantar, cozinha ou home office, possui o assento profundo e as costas ergonômicas para manter você sempre confortável!', 'https://atacadotropicalmoveis.com.br/wp-content/uploads/2019/07/38309722_1GG.jpg', 107.80, 80, 3),
    ('Estofado Berlim 2,50 metros', 'Pilow com assento de 8 cm espuma de D 28. Espuma do pilow do braço D 26. Encosto e rineira em fibra mista. Molas Bonel. Tecido veludinho', 'https://crmagazineexpress.com.br/wp-content/uploads/2020/09/Sof%C3%A1-Retr%C3%A1til-Reclin%C3%A1vel-Berlim-2.50m-Veludo-Cinza-814-e1598642685284.jpg', 670.30, 20, 4),
    ('Mesa de Jantar 6 Lugares 1,60m', 'A mesa Tangará, é a escolha perfeita para ambientes elegantes e sofisticados. Sendo uma peça extremamente funcional, ela proporciona todo conforto necessário sem abdicar do estilo e beleza. Possui os pés em madeira Tauari, com tampo em MDF e vidro com bordas chanfradas e acabamento em laca, resistente e elegante.', 'https://product-hub-prd.madeiramadeira.com.br/810295/images/810295_1.jpg?width=500&canvas=1:1&bg-color=FFF', 1500.79, 30, 5)
"""

clients = """
    INSERT INTO CLIENTES (NOME, DATA_NASC, CPF, GENERO, ESTADO_CIVIL, NACIONALIDADE, EMAIL_CONTATO, TELEFONE, CEP, ESTADO, CIDADE, LOGRADOURO, COMPLEMENTO, EMAIL_LOGIN, SENHA)
    VALUES 
    ('Cliente1', '1990-01-01', '12345678901', 'M', 'Solteiro', 'Brasil', 'cliente1@email.com', '12345678901', '12345678', 'SP', 'São Paulo', 'Rua A', 'Apto 101', 'cliente1_login@email.com', 'senha1'),
    ('Cliente2', '1985-02-15', '23456789012', 'F', 'Casado', 'Brasil', 'cliente2@email.com', '23456789012', '23456789', 'RJ', 'Rio de Janeiro', 'Rua B', 'Casa 2', 'cliente2_login@email.com', 'senha2'),
    ('Cliente3', '1992-03-20', '34567890123', 'M', 'Solteiro', 'Estrangeiro', 'cliente3@email.com', '34567890123', '34567890', 'MG', 'Belo Horizonte', 'Rua C', 'Apto 303', 'cliente3_login@email.com', 'senha3'),
    ('Cliente4', '1988-04-25', '45678901234', 'F', 'Casado', 'Brasil', 'cliente4@email.com', '45678901234', '45678901', 'RS', 'Porto Alegre', 'Rua D', 'Casa 4', 'cliente4_login@email.com', 'senha4'),
    ('Cliente5', '1995-05-30', '56789012345', 'M', 'Solteiro', 'Brasil', 'cliente5@email.com', '56789012345', '56789012', 'PR', 'Curitiba', 'Rua E', 'Apto 505', 'cliente5_login@email.com', 'senha5'),
    ('Cliente6', '1980-06-10', '67890123456', 'F', 'Divorciado', 'Brasil', 'cliente6@email.com', '67890123456', '67890123', 'BA', 'Salvador', 'Rua F', 'Casa 6', 'cliente6_login@email.com', 'senha6'),
    ('Cliente7', '1998-07-15', '78901234567', 'M', 'Casado', 'Brasil', 'cliente7@email.com', '78901234567', '78901234', 'SC', 'Florianópolis', 'Rua G', 'Apto 707', 'cliente7_login@email.com', 'senha7'),
    ('Cliente8', '1983-08-20', '89012345678', 'F', 'Solteiro', 'Brasil', 'cliente8@email.com', '89012345678', '89012345', 'CE', 'Fortaleza', 'Rua H', 'Casa 8', 'cliente8_login@email.com', 'senha8'),
    ('Cliente9', '1991-09-25', '90123456789', 'M', 'Casado', 'Estrangeiro', 'cliente9@email.com', '90123456789', '90123456', 'PE', 'Recife', 'Rua I', 'Apto 909', 'cliente9_login@email.com', 'senha9'),
    ('Cliente10', '1986-10-30', '01234567890', 'F', 'Solteiro', 'Brasil', 'cliente10@email.com', '01234567890', '01234567', 'GO', 'Goiânia', 'Rua J', 'Casa 10', 'cliente10_login@email.com', 'senha10'),
    ('Matheus Strapasson', '2006-02-10', '09135052937', 'M', 'Solteiro', 'Brasil', 'matheustrapasson@gmail.com', '41996746161', '82710380', 'PR', 'Curitiba', 'Rua Howell Lewis Fry, 341', 'Bloco 2, apartamento 204', 'mathystrapa@gmail.com', '12345'),('carlos', '2006-02-10', '02135052937', 'M', 'Solteiro', 'Brasil', 'matheustrapasson@gmail.com', '41996746161', '82710380', 'PR', 'Curitiba', 'Rua Howell Lewis Fry, 341', 'Bloco 2, apartamento 204', 'carlos@gmail.com', '12345')
    
"""

orders = """
    INSERT INTO PEDIDOS (COD_CLIENTE, STATUS, DATA)
    VALUES
    (1, 'Em andamento', '2023-11-23'),
    (2, 'Concluído', '2023-11-22'),
    (3, 'Em andamento', '2023-11-21'),
    (4, 'Concluído', '2023-11-20'),
    (5, 'Em andamento', '2023-11-19'),
    (6, 'Concluído', '2023-11-18'),
    (7, 'Em andamento', '2023-11-17'),
    (8, 'Concluído', '2023-11-16'),
    (9, 'Em andamento', '2023-11-15'),
    (10, 'Concluído', '2023-11-14'),
    (1, 'Em andamento', '2023-11-13'),
    (2, 'Concluído', '2023-11-12'),
    (3, 'Em andamento', '2023-11-11'),
    (4, 'Concluído', '2023-11-10'),
    (5, 'Em andamento', '2023-11-09')
"""

orders_items = """
    INSERT INTO ITENS_PEDIDO (COD_PEDIDO, COD_PRODUTO, QUANTIDADE) VALUES
    (1, 1, 3),
    (1, 2, 2),
    (2, 3, 1),
    (1, 3, 5),
    (1, 4, 2),
    (2, 1, 4),
    (2, 2, 3),
    (3, 3, 1),
    (3, 4, 6),
    (4, 1, 2),
    (4, 2, 3),
    (5, 3, 4),
    (5, 4, 2),
    (6, 1, 3),
    (6, 2, 5),
    (7, 3, 2),
    (7, 4, 4),
    (8, 1, 6),
    (8, 2, 1),
    (9, 3, 3),
    (9, 4, 2),
    (10, 1, 4),
    (10, 2, 3),
    (11, 3, 1),
    (11, 4, 5),
    (12, 1, 2),
    (12, 2, 4),
    (13, 3, 3),
    (13, 4, 2),
    (14, 1, 4),
    (14, 2, 3),
    (15, 3, 2),
    (15, 4, 3)
"""

cursor.execute(suppliers)
cursor.execute(products)
cursor.execute(clients)
cursor.execute(orders)
cursor.execute(orders_items)

cursor.close()
connection.commit()
connection.close()