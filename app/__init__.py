from db.db_connect import Connectserver

server = Connectserver('127.0.0.1', 'root', '', '3306')

server.insert('hometreasures', 'FORNECEDORES', ['NOME', 'ENDERECO', 'EMAIL', 'TELEFONE'], ('MadeiraMadeira', 'R. Mal. Deodoro, 717 - Centro, Curitiba - PR, 80010-010', 'madeiramadeira@email.com', '08000800099'))

server.insert('hometreasures', 'PRODUTOS', ['NOME', 'DESCRICAO', 'LINK_IMAGEM', 'PRECO', 'ESTOQUE', 'COD_FORNECEDOR'], ('Mesa de Jantar 6 Lugares 1,60m Tampo MDF e Vidro Pés Madeira Maciça Tangará CabeCasa MadeiraMadeira Caramelo/Off White', 'A mesa Tangará, é a escolha perfeita para ambientes elegantes e sofisticados. Sendo uma peça extremamente funcional, ela proporciona todo conforto necessário sem abdicar do estilo e beleza. Possui os pés em madeira Tauari, com tampo em MDF e vidro com bordas chanfradas e acabamento em laca, resistente e elegante.', 'https://product-hub-prd.madeiramadeira.com.br/810295/images/810295_1.jpg?width=500&canvas=1:1&bg-color=FFF', 1500.79, 30, 5))