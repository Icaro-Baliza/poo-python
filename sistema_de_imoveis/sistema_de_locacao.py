from endereco import Endereco
from imovel import Imovel
from proprietario import Proprietario

lista_proprietarios: list[Proprietario] = []
lista_imoveis: list[Imovel] = []

def cadastrar_proprietario():
    nome = input("Digite o nome do proprietario: ")
    cpf = input("Digite o cpf do proprietario: ")
    identidade = input("Digite a identidade do proprietario: ")
    endereco = cadastrar_endereco()
    proprietario = Proprietario(nome, cpf, identidade, endereco)
    return proprietario

def cadastrar_imovel():
    iptu = input("Digite o iptu do imovel: ")
    tipo = input("Digite o tipo do imovel: ")
    utilizacao = input("Digite a utilizacao do imovel: ")
    rua = input("Digite a rua: ")
    numero = input("Digite o numero: ")
    cep = input("Digite o cep: ")
    estado = input("Digite o estado: ")
    cidade = input("Digite a cidade: ")
    imovel = Imovel(iptu, tipo, utilizacao, rua, numero, cep, estado, cidade)
    return imovel

def cadastrar_endereco():
    rua = input("Digite a rua: ")
    numero = input("Digite o numero: ")
    cep = input("Digite o cep: ")
    estado = input("Digite o estado: ")
    cidade = input("Digite a cidade: ")
    endereco = Endereco(rua, numero, cep, estado, cidade)
    return endereco

def associar_imovel_proprietario(p: int, imovel: Imovel):
    if lista_proprietarios[p].adiciona_imovel(imovel):
        print("Imovel associado com sucesso")
    else:
        print("Erro ao associar (imovel ja associado ou endereço do imovel igual ao do proprietario)")

def busca_proprietario():
        cpf=input("Digite o cpf do proprietario: ")
        for i in range(len(lista_proprietarios)):
            if lista_proprietarios[i].get_cpf() == cpf:
                return i
        else:
            print("Proprietario não encontrado")
            return -1


while True:
    print("\nEscolha a operação que deseja fazer")
    print("\n1 - Cadastrar proprietário")
    print("2 - Cadastrar imóvel")
    print("3- Associar imovel a proprietario")
    print("4- Alugar imovel")
    print("5- Bloquear imovel")
    print("6- Listar imoveis de um proprietario por tipo")
    print("7- Atualizar endereço do proprietario")
    print("0 - Sair\n")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 0:
        print("Saindo do sistema...")
        break
    if opcao == 1:
        lista_proprietarios.append(cadastrar_proprietario())
    elif opcao == 2:
        lista_imoveis.append(cadastrar_imovel())
    elif opcao == 3:
        cpf = input("Digite o cpf do proprietario: ")
        for i in range(len(lista_proprietarios)):
            if lista_proprietarios[i].get_cpf() == cpf:
                a=i
                break
        else:
            print("Proprietario não encontrado")
            continue
        print("Digite o endereço do imovel")
        endereco = cadastrar_endereco()
        for i in range(len(lista_imoveis)):
            if lista_imoveis[i].get_endereco() == endereco:
                imovel = lista_imoveis[i]
                break
        else:
            print("Imovel não encontrado")
            continue
        associar_imovel_proprietario(a, imovel)

    elif opcao == 4:
        i = busca_proprietario()
        if i == -1:
            continue
        print("Digite o endereço do imovel")
        endereco = cadastrar_endereco()
        if lista_proprietarios[i].busca_imovel(endereco)==False:
            print("Imovel não encontrado")
            continue
        else:
            dia= input("Digite o dia: ")
            dia = int(dia)
            mes= input("Digite o mes: ")
            mes=int(mes)
            ano= input("Digite o ano: ")
            ano = int(ano)
            lista_proprietarios[i].busca_imovel(endereco).get_agenda().alugar(dia, mes, ano)

    elif opcao == 5:
        i = busca_proprietario()
        if i == -1:
            continue
        print("Digite o endereço do imovel")
        endereco = cadastrar_endereco()
        if lista_proprietarios[i].busca_imovel(endereco)==False:
            print("Imovel não encontrado")
            continue
        else:
            dia= input("Digite o dia: ")
            dia = int(dia)
            mes= input("Digite o mes: ")
            mes=int(mes)
            ano= input("Digite o ano: ")
            ano = int(ano)
            lista_proprietarios[i].busca_imovel(endereco).get_agenda().bloquear(dia, mes, ano)

    elif opcao == 6:
        i = busca_proprietario()
        if i == -1:
            continue
        tipo = input("Digite o tipo do imovel: ")
        lista_proprietarios[i].listar_imoveis_por_tipo(tipo)

    elif opcao == 7:
        i = busca_proprietario()
        if i == -1:
            continue
        print("Digite o novo endereco do proprietario")
        rua = input("Digite a rua: ")
        numero = input("Digite o numero: ")
        cep = input("Digite o cep: ")
        verifica = input("Deseja mudar estado e cidade? (s/n): ")
        if verifica == "s":
            estado = input("Digite o estado: ")
            cidade = input("Digite a cidade: ")
            lista_proprietarios[i].atualiza_endereco(rua, numero, cep, estado, cidade)
        else:
            lista_proprietarios[i].atualiza_endereco(rua, numero, cep)
