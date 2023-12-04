from db.db_connect import Connectserver
from flask import *

app = Flask(__name__)   # cria a aplcação

server = Connectserver(host='127.0.0.1', user='root', password='', port='3306')  # conecta com o banco de dados (já criado no arquivo createdb.py)

login = False
produtos_carrinho = {}
nomes = []
names = server.select('hometreasures', 'PRODUTOS', ['NOME'])
for result in names:
    produtos_carrinho[result[0]] = 0


@app.route('/')     # página inicial, quando o usuário ainda não está logado
def aux_index():
    infos_produtos = obter_infos_produtos()
    return render_template('aux_index.html', infos_produtos = infos_produtos)

@app.route('/index')   # página quando o usuário está logado
def index():
    infos_produtos = obter_infos_produtos()
    return render_template('index.html', infos_produtos = infos_produtos, nome=nome)


@app.route('/entrar')   # abre o formulário para login
def entrar():
    return render_template('login.html')


@app.route('/get-login-info', methods=['POST'])     # verifica as informações do login
def process_login():

    if request.method == 'POST':

        inserted_email = request.form['email']
        inserted_password = request.form['password']
        result = server.select('hometreasures', 'CLIENTES', ['EMAIL_LOGIN', 'SENHA', 'NOME'], f""" EMAIL_LOGIN = '{inserted_email}' """)  # lista de tuplas com os registros que têm esse email

        if len(result) > 0:     # verifica se o email existe na tabela clientes

            global email_login
            global password
            global nome
            email_login = result[0][0]
            password = result[0][1]
            nome = result[0][2]

            if password == inserted_password:
                global login
                login = True
                return redirect(url_for('index'))   # abre a home já logado
            
            else:
                mensagem = 'Senha incorreta.'
        
        else:
            mensagem = 'Email não existe no banco de dados.'
        
        return render_template('login.html', message=mensagem)
        
        
    

@app.route('/cadastrar')    # abre o formulário de cadastro
def cadastrar():
    return render_template('cadastro.html')
    

@app.route('/get-register-info', methods=['POST'])  # pega as informações do cadastro e armazena no banco de dados
def process_register():

    if request.method == 'POST':

        name = request.form['name']

        data_aux = list(request.form['birth_date'])
        ano = data_aux[6] + data_aux[7] + data_aux[8] + data_aux[9]
        mes = data_aux[3] + data_aux[4]
        dia = data_aux[0] + data_aux[1]
        data_nasc = f'{ano}-{mes}-{dia}'    # mini-algoritmo para deixar a data de nascimento no formato AAAA-MM-DD

        cpf = request.form['cpf'].replace('.', '').replace('-', '')     # retira os pontos e o traço

        gender = request.form['sex']
        if gender == 'Masculino':
            gender = 'M'
        else:
            gender = 'F'

        estado_civil = request.form['estadocivil']
        nacionality = request.form['nacionality']
        contact_email = request.form['contact-email']

        phone = request.form['phone-number'].replace(' ', '').replace('(', '').replace(')', '').replace('-', '')    # retira o espaço vazio, os parênteses e o traço

        cep = request.form['cep'].replace('-', '')      # retira o traço
        state = request.form['state']
        city = request.form['city']
        street = request.form['street']
        street_number = request.form['number']
        logradouro = street + ", " + street_number
        complement = request.form['complement']
        login_email = request.form['login-email']

        password = request.form['password']
        confirm_password = request.form['confirm-password']

        if password != confirm_password:
            message = 'Erro. As senhas não coincidem.'
            return render_template('cadastro.html', mensagem=message)   # se as senhas não forem iguais, o cadastro reinicia e uma mensagem aparece avisando que as senhas não coincidem
        
        else:

            result_email = server.select('hometreasures', 'CLIENTES', '*', f""" EMAIL_LOGIN = '{login_email}' """)
            result_cpf = server.select('hometreasures', 'CLIENTES', '*', f""" CPF = '{cpf}' """)

            if len(result_email) > 0:
                message = 'Email já existe no banco de dados.'
                return render_template('cadastro.html', mensagem=message)
            
            elif len(result_cpf) > 0:
                message = 'CPF já existe no banco de dados.'
                return render_template('cadastro.html', mensagem=message)
            
            else:
                result = server.insert('hometreasures', 'CLIENTES', ['NOME', 'DATA_NASC', 'CPF', 'GENERO', 'ESTADO_CIVIL', 'NACIONALIDADE', 'EMAIL_CONTATO', 'TELEFONE', 'CEP', 'ESTADO', 'CIDADE', 'LOGRADOURO', 'COMPLEMENTO', 'EMAIL_LOGIN', 'SENHA'], (f'{name}', f'{data_nasc}', f'{cpf}', f'{gender}', f'{estado_civil}', f'{nacionality}', f'{contact_email}', phone, f'{cep}', f'{state}', f'{city}', f'{logradouro}', f'{complement}', f'{login_email}', f'{password}'))     # adiciona o novo cadastro ao banco de dados
                if result[0]:
                    return redirect(url_for('entrar'))   # renderiza a página de login
                else:
                    message = f'Desculpe, não foi possível completar seu cadastro. Revise as informações inseridas e tente novamente. Código do erro: {result[1]}'
                    return render_template('cadastro.html', mensagem = message)
            
@app.route('/account-info')
def info_account():

    global account_info

    aux_account_info = server.select('hometreasures', 'CLIENTES', ['NOME', 'DATA_NASC', 'CPF', 'GENERO', 'ESTADO_CIVIL', 'NACIONALIDADE', 'EMAIL_CONTATO', 'TELEFONE', 'CEP', 'ESTADO', 'CIDADE', 'LOGRADOURO', 'COMPLEMENTO', 'EMAIL_LOGIN', 'SENHA'], f""" EMAIL_LOGIN = '{email_login}' """)[0]

    aux_data = str(aux_account_info[1])
    ano = aux_data[0] + aux_data[1] + aux_data[2] + aux_data[3]
    mes = aux_data[5] + aux_data[6]
    dia = aux_data[8] + aux_data[9]
    data_nasc = f'{dia}/{mes}/{ano}'

    cpf = aux_account_info[2]
    aux1 = cpf[0] + cpf[1] + cpf[2]
    aux2 = cpf[3] + cpf[4] + cpf[5]
    aux3 = cpf[6] + cpf[7] + cpf[8]
    aux4 = cpf[9] + cpf[10]
    cpf = f'{aux1}.{aux2}.{aux3}-{aux4}'

    if aux_account_info[3] == 'M':
        genero = 'Masculino'
    else:
        genero = 'Feminino'

    aux_telefone = str(aux_account_info[7])
    ddd = aux_telefone[0] + aux_telefone[1]
    aux1 = aux_telefone[2] + aux_telefone[3] + aux_telefone[4] + aux_telefone[5] + aux_telefone[6]
    aux2 = aux_telefone[7] + aux_telefone[8] + aux_telefone[9] + aux_telefone[10]
    telefone = f'({ddd}) {aux1}-{aux2}'

    account_info = {'nome': f'{aux_account_info[0]}', 'data_nasc': data_nasc, 'cpf': cpf, 'genero': genero, 'estado_civil': f'{aux_account_info[4]}', 'nacionalidade': f'{aux_account_info[5]}', 'email_contato': f'{aux_account_info[6]}', 'telefone': telefone, 'cep': f'{aux_account_info[8]}', 'estado': f'{aux_account_info[9]}', 'cidade': f'{aux_account_info[10]}', 'logradouro': f'{aux_account_info[11]}', 'complemento': f'{aux_account_info[12]}', 'email_login': f'{aux_account_info[13]}', 'senha': f'{aux_account_info[14]}'}

    return render_template('account_info.html', account_info = account_info)

@app.route('/update-account-info', methods=['POST'])
def update_account():

    if request.method == 'POST':

        nome = request.form['nome']
        email_contato = request.form['email_contato']
        telefone = request.form['telefone'].replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
        cep = request.form['cep'].replace('-', '')
        nacionalidade = request.form['nacionalidade']
        estado = request.form['estado']
        cidade = request.form['cidade']
        logradouro = request.form['logradouro']
        complemento = request.form['complemento']
        estado_civil = request.form['estado_civil']
        quer_notificacoes = request.form['quer_notificacoes']

        nova_senha = request.form['nova_senha']
        confirmar_nova_senha = request.form['confirmar_nova_senha']

        print(quer_notificacoes)

        if nova_senha != confirmar_nova_senha:
            message = 'As senhas não coincidem.'
            return render_template('account_info.html', account_info = account_info, mensagem = message)
        else:
            if nova_senha == '':
                senha_antiga = server.select('hometreasures', 'CLIENTES', ['SENHA'], f""" EMAIL_LOGIN = '{email_login}' """)[0][0]
                nova_senha = senha_antiga

            result = server.update('hometreasures', 'CLIENTES', ['NOME', 'EMAIL_CONTATO', 'TELEFONE', 'CEP', 'NACIONALIDADE', 'ESTADO', 'CIDADE', 'LOGRADOURO', 'COMPLEMENTO', 'ESTADO_CIVIL', 'SENHA'], [f'{nome}', f'{email_contato}', f'{telefone}', f'{cep}', f'{nacionalidade}', f'{estado}', f'{cidade}', f'{logradouro}', f'{complemento}', f'{estado_civil}', f'{nova_senha}'], f""" EMAIL_LOGIN = '{email_login}' """)
            if result[0]:
                sucess_message = 'Suas informações foram atualizadas com sucesso!'

                aux_account_info = server.select('hometreasures', 'CLIENTES', ['NOME', 'DATA_NASC', 'CPF', 'GENERO', 'ESTADO_CIVIL', 'NACIONALIDADE', 'EMAIL_CONTATO', 'TELEFONE', 'CEP', 'ESTADO', 'CIDADE', 'LOGRADOURO', 'COMPLEMENTO', 'EMAIL_LOGIN', 'SENHA'], f""" EMAIL_LOGIN = '{email_login}' """)[0]

                account_info = {'nome': f'{aux_account_info[0]}', 'data_nasc': f'{aux_account_info[1]}', 'cpf': f'{aux_account_info[2]}', 'genero': f'{aux_account_info[3]}', 'estado_civil': f'{aux_account_info[4]}', 'nacionalidade': f'{aux_account_info[5]}', 'email_contato': f'{aux_account_info[6]}', 'telefone': f'{aux_account_info[7]}', 'cep': f'{aux_account_info[8]}', 'estado': f'{aux_account_info[9]}', 'cidade': f'{aux_account_info[10]}', 'logradouro': f'{aux_account_info[11]}', 'complemento': f'{aux_account_info[12]}', 'email_login': f'{aux_account_info[13]}', 'senha': f'{aux_account_info[14]}'}

                return render_template('account_info.html', mensagem_sucesso = sucess_message, account_info = account_info)
            else:
                error_message = f'Desculpe, não foi possível atualizar suas informações. Revise as informações e tente novamente. Código do erro: {result[1]}'
                return render_template('account_info.html', mensagem_erro = error_message, account_info = account_info)

@app.route('/carrinho')
def carrinho():
    infos_produtos = []
    total = 0
    for product_name, amount in produtos_carrinho.items():
        if amount != 0:
            product_link = obter_link_produto(product_name)
            product_price = server.select('hometreasures', 'PRODUTOS', ['PRECO'], f""" NOME = '{product_name}' """)[0][0]
            total_product_price = amount * product_price
            total += total_product_price
            infos_produtos.append((product_name, amount, product_link, product_price, total_product_price))

    return render_template('carrinho.html', infos_produtos = infos_produtos, lenght = len(infos_produtos), total=total)

@app.route('/adicionar-ao-carrinho/<nome_produto>')
def adicionar_produto(nome_produto):
    produtos_carrinho[nome_produto] += 1
    if login:
        return redirect(url_for('index'))
    else:
        return render_template('login.html')


@app.route('/remover-do-carrinho/<nome_produto>')
def remover_produto(nome_produto):
    if produtos_carrinho[nome_produto] != 0:
        produtos_carrinho[nome_produto] -= 1
    return redirect(url_for('index'))

@app.route('/finalizar-compra')
def finalizar_compra():

    aux_account_info = server.select('hometreasures', 'CLIENTES', ['NOME', 'DATA_NASC', 'CPF', 'GENERO', 'ESTADO_CIVIL', 'NACIONALIDADE', 'EMAIL_CONTATO', 'TELEFONE', 'CEP', 'ESTADO', 'CIDADE', 'LOGRADOURO', 'COMPLEMENTO', 'EMAIL_LOGIN', 'SENHA'], f""" EMAIL_LOGIN = '{email_login}' """)[0]
    info_endereco = [aux_account_info[8], aux_account_info[9], aux_account_info[10], aux_account_info[11], aux_account_info[12]]
    print(info_endereco)
    return render_template("finalizar_compra.html", info_endereco = info_endereco)

@app.route('/agradecimento')
def agradecimento():
    return render_template('agradecimento.html', nome=nome)


def obter_infos_produtos():
    infos_produtos = []
    select_result = server.select('hometreasures', 'PRODUTOS', ['*'])
    quantidade_produtos = len(select_result)

    print(quantidade_produtos)

    for cod in range(1, quantidade_produtos + 1):
        result = server.select('hometreasures', 'PRODUTOS', ['NOME', 'DESCRICAO', 'LINK_IMAGEM', 'PRECO'], f'COD_PRODUTO = {cod}')
        nome = result[0][0]
        descricao = result[0][1]
        link = result[0][2]
        preco = result[0][3]
        quantidade_carrinho = produtos_carrinho[nome]

        infos_produto = {'nome_produto': nome, 'descricao_produto': descricao, 'link_imagem': link, 'preco_produto': preco, 'quantidade_carrinho': quantidade_carrinho}
        infos_produtos.append(infos_produto)
    
    return infos_produtos


def obter_link_produto(produto):

    result = server.select('hometreasures', 'PRODUTOS', ['LINK_IMAGEM'], f""" NOME = '{produto}' """)
    link = result[0][0]
    return link

if __name__ == '__main__':
    app.run(debug=True)