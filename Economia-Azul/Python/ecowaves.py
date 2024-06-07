# participantes
# Laura (RM: 558843) | Maria Eduarda (RM: 558832) | Vínicius Saes (RM: 554456)

# importações
import os
import re
from datetime import datetime

# 1º função de validação - valida se o e-mail está nos conformes

def verifica_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(regex, email):
        return True
    else:
        return False
    
# 2° função de validação - verifica se a senha está nos conformes
def verifica_senha(senha: str) -> bool:
    retorno = False
     # Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        print("A senha deve ter no mínimo 8 caracteres, um caractere especial e uma letra maíuscula")
        return False
    
    # Verifica se a senha tem pelo menos um caractere especial
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
        print("A senha deve ter no mínimo 8 caracteres, um caractere especial e uma letra maíuscula")
        return False
    
    # Verifica se a senha tem pelo menos uma letra maiúscula
    if not re.search(r'[A-Z]', senha):
        print("A senha deve ter no mínimo 8 caracteres, um caractere especial e uma letra maíuscula")
        return False
    
    # Se passou por todas as verificações, a senha é válida
    return True

# 3° função de validação - verifica se alguns dados estão corretamente (nome-> só letras | cnpj -> só n°s e 14 caracteres)
def verifica_dados(tipo, dado):
    retorno = False
    if tipo == "nome":
        regex = r'^[a-zA-Z\s]+$'  # apenas letras e espaços
    # elif tipo == "nome":
    #     regex = r'^[a-zA-Z\s]+$'  # apenas letras e espaços
    else:
        return False
    
    return re.match(regex, dado) is not None

# 4° função de validação - verifica se formato do CNPJ está correto
def validar_cnpj(cnpj):
    # Expressão regular para validar o formato do CNPJ
    cnpj_regex = r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$'
    
    if re.match(cnpj_regex, cnpj):
        return True
    else:
        return False
    
# 5° função de validação - valida se uma data está correta
def validar_data(data_str):
    try:
        data = datetime.strptime(data_str, '%d/%m/%Y')
        return data
    except ValueError:
        return None
    
# 6° função de validação - valida se o horário está correto
def validar_horario(horario_str):
    try:
        horario_inicio, horario_fim = horario_str.split(" - ")
        inicio = datetime.strptime(horario_inicio, '%H:%M').time()
        fim = datetime.strptime(horario_fim, '%H:%M').time()
        if inicio >= fim:
            print("Horário inválido. O horário de início deve ser antes do horário de fim.")
            return None
        return horario_str
    except ValueError:
        return None
    
# 7° função de validação - valida se o usuário já foi cadastrado pelo e-mail digitado
def verificar_usuario_por_email(lista_usuarios, email):
    for usuario in lista_usuarios:
        if usuario.get('email') == email:
            return True
    return False
    
# Listas para armazenar os diferentes tipos de usuários
voluntarios = [{'id': 1, 'nome': 'Saes', 'email': 'saes@fiap.com', 'senha': 'RM554456$', 'tipo': 'voluntario'}]

ongs = [{'id': 1, 'nome': 'ONG Oceana', 'email': 'oceana@ong.com', 'senha': 'Dpx101894$', 'cnpj': '14.780.332/0001-31', 'descricao': 'Ong de preservação dos oceanos', 'tipo': 'ong'}]

parceiros = []

atividades = [{'id_atividade': 1, 'nome_atividade': 'Limpeza de praia', 'data_atividade': '08/09/2024', 'descricao_atividade': 'Fazer limpeza da praia de Bertioga e remoção de microplásticos na área costeira, atividade acompanhada de Guia.', 'vagas': 10, 'local': 'Bertioga - SP', 'horario': '09:00 - 11:00', 'id_ong': 1}, {'id_atividade': 2, 'nome_atividade': 'Limpeza SubAquatica', 'data_atividade': '11/10/2024', 'descricao_atividade': 'Mergulho acompanhado de um Guia para remoção de lixos, entulhos e detritos do mar.', 'vagas': 15, 'local': 'Fernando de Noronha', 'horario': '09:00 - 13:00', 'id_ong': 1}]

inscritos = []

# 2° função - solicita ao voluntario os dados necessários, depois os adiciona em um dicionário
def cadastrar_voluntario():
    print("\nCadastro:")
    nome = input("Nome: ")
    while not verifica_dados("nome", nome):
        print("Nome inválido. Tente novamente.")
        nome = input("Nome: ")

    email = input("E-mail: ")
    while not verifica_email(email):
        print("E-mail inválido. Tente novamente. (exemplo@domain.com)")
        email = input("E-mail: ")
    while verificar_usuario_por_email(voluntarios, email):
        print("Esse e-mail já está cadastrado em nosso sistema.")
        email = input("E-mail: ")
        while not verifica_email(email):
            print("E-mail inválido. Tente novamente. (exemplo@domain.com)")
            email = input("E-mail: ")

    while True:
        senha = input("Senha:  ")
        if verifica_senha(senha):
            break

    id = len(voluntarios) + 1
    voluntario = {
        "id": id,
        "nome": nome,
        "email": email,
        "senha": senha,
        "tipo": "voluntario"
    }

    # Adicionar o nova voluntario à lista de voluntarios
    voluntarios.append(voluntario)
    
    os.system("cls")
    print(f"\nSeja bem-vindo, {nome}!!! Cadastro realizado com sucesso! Por favor, faça login para continuar.\n")

# 3° função - solicita a ONG os dados necessários, depois os adiciona em um dicionário
def cadastrar_ong():
    print("\nCadastro:")
    nome = input("Razão Social: ")
    while not verifica_dados("nome", nome):
        print("Razão Social inválida. Tente novamente.")
        nome = input("Razão Social: ")

    email = input("E-mail: ")
    while not verifica_email(email):
        print("E-mail inválido. Tente novamente. (exemplo@domain.com)")
        email = input("E-mail: ")

    while True:
        senha = input("Senha:  ")
        if verifica_senha(senha):
            break

    cnpj = input("CNPJ: ")
    while not validar_cnpj(cnpj):
        print("CNPJ inválido. Tente novamente. (XX. XXX. XXX/0001-XX)")
        cnpj = input("CNPJ: ") 

    descricao = input("Descrição: ")

    id = len(ongs) + 1
    nova_ong = {
        "id": id,
        "nome": nome,
        "email": email,
        "senha": senha,
        "cnpj": cnpj,
        "descricao": descricao,
        "tipo": "ong"
    }

    # Adicionar a nova ONG à lista de ONGS
    ongs.append(nova_ong)
    
    os.system("cls")
    print(f"\nSeja bem-vindo, {nome}!!! Cadastro realizado com sucesso! Por favor, faça login para continuar.\n")

# 4° função - solicita ao parceiro (hospedagens) os dados necessários, depois os adiciona em um dicionário
def cadastrar_parceiro():
    print("\nCadastro:")

    nome = input("Razão Social: ")
    while not verifica_dados("nome", nome):
        print("Razão Social inválida. Tente novamente.")
        nome = input("Razão Social: ")

    email = input("E-mail: ")
    while not verifica_email(email):
        print("E-mail inválido. Tente novamente. (exemplo@domain.com)")
        email = input("E-mail: ")

    while True:
        senha = input("Senha:  ")
        if verifica_senha(senha):
            break

    id = len(parceiros) + 1

    novo_parceiro = {
        "id": id,
        "nome": nome,
        "email": email,
        "senha": senha,
        "tipo": "parceiro"
    }
    # Adicionar o novo parceiro à lista de parceiros
    parceiros.append(novo_parceiro)

    os.system("cls")
    print(f"\nSeja bem-vindo, {nome}!!! Cadastro realizado com sucesso! Por favor, faça login para continuar.\n")

def login(tipo):
    print("\nDigite suas credenciais")
    email_login = input("E-mail: ")
    senha_login = input("Senha: ")
    if not email_login == "" and not senha_login == "":
        if tipo == "1":
            for usuario in voluntarios:
                if usuario["email"] == email_login and usuario["senha"] == senha_login:
                    return usuario
        elif tipo == "2":
            for usuario in ongs:
                if usuario["email"] == email_login and usuario["senha"] == senha_login:
                    return usuario
        elif tipo == "3":
            for usuario in parceiros:
                if usuario["email"] == email_login and usuario["senha"] == senha_login:
                    return usuario
    return None

# FUNÇÕES DA ONG
def cadastrar_atividade(atividades, id_ong):
    while True:
        nome_atividade = input("\nNome da atividade: ").strip()

        # Validação da data
        while True:
            data_atividade = input("Data da atividade (dd/mm/aaaa): ").strip()
            data = validar_data(data_atividade)
            if data:
                ano = data.year
                mes = data.month
                ano_atual = datetime.now().year
                mes_atual = datetime.now().month
                
                if ano < ano_atual:
                    print("Ano inválido. O ano já passou.")
                elif ano == ano_atual and mes < mes_atual:
                    print("Mês inválido. O mês já passou.")
                elif ano > ano_atual + 2:
                    print("Ano inválido. A data está muito distante. (Só estamos aceitando atividades até o ano de 2026, por enquanto)")
                else:
                    break
            else:
                print("Data inválida. Por favor, insira uma data no formato dd/mm/aaaa.")

        descricao_atividade = input("Descrição da atividade: ").strip()
        local = input("Local da atividade: ").strip()

        while True:
            vagas = input("Número de vagas: ").strip()
            if vagas.isnumeric():
                vagas = int(vagas)  # Converter para inteiro
                if vagas == 0:
                    print("0 vagas? Adicione alguma vaga, por favor")
                else:
                    break
            else:
                print("ERRO! Digite um número, por favor!")
        
        # Validação do horário
        while True:
            horario = input("Horário da atividade (hh:mm - hh:mm): ").strip()
            if validar_horario(horario):
                break
            else:
                print("Horário inválido. Por favor, insira no formato hh:mm - hh:mm.")
        
        
        # Gerar um ID único para a atividade
        id_atividade = len(atividades) + 1
        
        # Adicionar a atividade ao dicionário de atividades
        nova_atividade = {
            "id_atividade": id_atividade,
            "nome_atividade": nome_atividade,
            "data_atividade": data_atividade,
            "descricao_atividade": descricao_atividade,
            "vagas": vagas,
            "local": local,
            "horario": horario,
            "id_ong": id_ong
        }
        
         # Adicionar a nova atividade à lista de atividades
        atividades.append(nova_atividade)

        # Perguntar se deseja adicionar outra atividade
        continuar = input("Deseja cadastrar outra atividade? (s/n): ").strip().lower()
        if continuar != 's':
            print("")
            break


def visualizar_atividade(atividades, id_ong):
    # Filtrar atividades pela ID da ONG
    atividades_filtradas = [atividade for atividade in atividades if atividade["id_ong"] == id_ong]
    
    # Verificar se há atividades para a ONG especificada
    if not atividades_filtradas:
        print("Não há atividades disponíveis no momento.")
        return
    
    # Exibir as atividades filtradas
    for i, atividade in enumerate(atividades_filtradas):
        print(f"{i + 1}. Atividade: (ID: {atividade['id_atividade']}) {atividade['nome_atividade']}, "
              f"Descrição: {atividade['descricao_atividade']}, Data: {atividade['data_atividade']}, "
              f"Local: {atividade['local']}, Horário: {atividade['horario']}, Vagas: {atividade['vagas']}")

def exibir_perfil_ong(ongs, id_ong):
    # Percorrer a lista de ONGs para encontrar a ONG com o ID especificado
    for ong in ongs:
        if ong["id"] == id_ong:
            # Exibir os detalhes da ONG
            print(f"Seu perfil, {ong['nome']} (ID: {ong['id']}):")
            print(f"CNPJ: {ong['cnpj']} | Descrição: {ong['descricao']} | E-mail: {ong['email']}")
            return

    # Se nenhuma ONG for encontrada com o ID especificado
    print("ONG não encontrada.")

#FUNÇÕES DO VOLUNTÁRIO
# def visualizar_atividadesUsuario(atividades):
#     for i, atividade in enumerate(atividades):
#         print(f"{i + 1}. Atividade: (ID: {atividade['id_atividade']}) {atividade['nome_atividade']}, (OFERECIDA PELA ONG: {atividade[id_ong]}) "
#               f"Descrição: {atividade['descricao_atividade']}, Data: {atividade['data_atividade']}, "
#               f"Local: {atividade['local']}, Horário: {atividade['horario']}, Vagas: {atividade['vagas']}")
def visualizar_atividadesUsuario(atividades):
    if not atividades:
        print("Não há atividades disponíveis no momento.")
        return

    for i, atividade in enumerate(atividades):
        print(f"{i + 1}. Atividade: (ID: {atividade['id_atividade']}) {atividade['nome_atividade']}, (OFERECIDA PELA ONG: {atividade['id_ong']}) "
              f"Descrição: {atividade['descricao_atividade']}, Data: {atividade['data_atividade']}, "
              f"Local: {atividade['local']}, Horário: {atividade['horario']}, Vagas: {atividade['vagas']}")
    inscrever_atividade(opcaoUser)


#FUNÇÃO PARA USUÁRIO SE CADASTRAR EM UMA ATIVIDADE
def inscrever_atividade(id_voluntario):
    print("\nAtividades Disponíveis:")
    for atividade in atividades:
        print(f"{atividade['id_atividade']} - {atividade['nome_atividade']}: {atividade['descricao_atividade']}")

    id_atividade = input("\nInsira o ID da atividade que deseja se inscrever: ")
    id_atividade = int(id_atividade)

    # Verifica se o ID da atividade é válido
    if id_atividade not in [atividade['id_atividade'] for atividade in atividades]:
        print("ID de atividade inválido.")
        return

    # Verifica se o voluntário já está inscrito na atividade
    for atividade in atividades:
        if atividade['id_atividade'] == id_atividade and id_voluntario in inscritos:
            print("Você já está inscrito nesta atividade.")
            return

    # Inscreve o voluntário na atividade
    for atividade in atividades:
        if atividade['id_atividade'] == id_atividade:
            inscritos.append(id_voluntario)
            print("Inscrição realizada com sucesso.")
            return

# Menu para interagir com o usuário


print("				\t\tTELA INICIAL ECOWAVES")
print("			\tQual você se encaixa -> 1 - Voluntario | 2 - ONG | 3 - Parceiros")
opcaoUser = input(" ")
while True:
    if opcaoUser == "":
        print("Você precisa digitar uma opção válida!")
        opcaoUser = input("Digite a opção desejada: ")
    elif opcaoUser == "1" or opcaoUser == "2" or opcaoUser == "3":
        break
    else:
        print("Você precisa digitar uma opção válida!")
        opcaoUser = input("Digite a opção desejada: ")

print("\nLegal! E você deseja:")
opcaoEntrada = input("[1] - cadastrar-se | [2] - Login | [3] - sair do sistema ->  ")
    
    # print("1. Cadastrar Voluntário")
    # print("2. Cadastrar ONG")
    # print("3. Cadastrar Parceiro")
    # print("4. Login")
    # print("5. Sair")
    
    # opcao = input("Escolha uma opção: ")

match(opcaoEntrada):
    case "1":
        if(opcaoUser == "1"):
            cadastrar_voluntario()
            voluntario_logado = login(opcaoUser)
            if voluntario_logado: 
                nome_usuario_logado = voluntario_logado['nome']

                os.system("cls")
                print(f"\nLogin realizado com sucesso, {nome_usuario_logado}! Você agora está logado em sua conta\n")

                while True:
                    opcao = input(f"\n0 - Sair | 1- Portal ou ChatBot | 2 - EcoVoluntariado | 3- Seu Perfil | 4- Descontos dos Parceiros\n")
                    match opcao:
                        case "0":
                            print("				\t\tAgradecemos por usar nosso sistema! Até a próxima")
                            break
                        case "1":
                            ...
                        case "2":
                            visualizar_atividadesUsuario(atividades)
                        case "3":
                            ...
                        case 4:
                            ...
            else:
                os.system("cls")
                print("\nLogin ou senha incorretos. Tente novamente.")
        elif(opcaoUser == "2"):
            cadastrar_ong()
            ong_logada = login(opcaoUser)
            if ong_logada: 
                razaosocial_ong = ong_logada['nome']
                os.system("cls")
                print(f"\nLogin realizado com sucesso, {razaosocial_ong}! Você agora está logado em sua conta\n")
                id_ong = ong_logada['id']

                while True:
                    opcao = input(f"\n0 - Sair | 1- Registrar uma Atividade | 2 - Ver suas Atividades | 3- Seu Perfil\n")

                    # opcao1 = input(f"\0 - Sair | 1- Registrar uma Atividade | 2 - Ver suas Atividades | 3- Seu Perfil\n")
                    match opcao:
                        case "0":
                            print("				\t\tAgradecemos por usar nosso sistema! Até a próxima")
                            break
                        case "1":  
                            cadastrar_atividade(atividades,id_ong)
                        case "2":
                            visualizar_atividade(atividades,id_ong)
                        case "3":
                            exibir_perfil_ong(ongs, id_ong)
                        case _:
                            print("Hmm, não existe essa opção!")
            else:
                os.system("cls")
                print("\nLogin ou senha incorretos. Tente novamente.")
                ong_logada = login(opcaoUser)
        elif(opcaoUser == "3"):
                cadastrar_parceiro()
                # print("Parceiro cadastrado")
    case "2":
        print("\nLogin:")
        usuario = login(opcaoUser)
        if usuario:
            print(f"Bem-vindo, {usuario['nome']}!")
            while True:
                    opcao = input(f"\n0 - Sair | 1- Portal ou ChatBot | 2 - EcoVoluntariado | 3- Seu Perfil | 4- Descontos dos Parceiros\n")
                    match opcao:
                        case "0":
                            print("				\t\tAgradecemos por usar nosso sistema! Até a próxima")
                            break
                        case "1":
                            ...
                        case "2":
                            visualizar_atividadesUsuario(atividades)
                            # aqui adicionar a função para o usuário se increver nas atividades
                        case "3":
                            ...
                        case 4:
                            ...
        else:
            print("Email ou senha inválidos.")
            usuario = login(opcaoUser)
    case 3:
        print("				\t\tAgradecemos por usar nosso sistema! Até a próxima")
    case _:
        print("Hmmm, não existe essa opção!")     
            