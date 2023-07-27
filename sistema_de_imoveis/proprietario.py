from endereco import Endereco
from imovel import Imovel

class Proprietario():
    """
    
    """

    def __init__(self, nome: str, cpf: str, identidade: str, endereco: Endereco) -> None:
        self.__nome = nome
        self.__cpf = cpf
        self.__identidade = identidade
        self.__endereco = endereco
        self.__imoveis: list[Imovel] = []

    def __str__(self) -> str:
        return f"Proprietario: {self.__nome}, {self.__cpf}, {self.__identidade}, {self.__endereco}"

    def atualiza_endereco(self, rua: str, numero: str, cep: str, estado='', cidade='') -> None:
        self.__endereco.set_rua(rua)
        self.__endereco.set_numero(numero)
        self.__endereco.set_cep(cep)
        if estado!='':
            self.__endereco.set_estado(estado)
        if cidade!='':
            self.__endereco.set_cidade(cidade)
        
    def adiciona_imovel(self, imovel: Imovel) -> bool:
        if imovel.get_endereco() == self.__endereco:
            return False
        elif imovel in self.__imoveis:
            return False
        else:
            self.__imoveis.append(imovel)
            return True
        
    def remove_imovel(self, imovel: Imovel) -> bool:
        if imovel in self.__imoveis:
            self.__imoveis.remove(imovel)
            return True
        else:
            return False
    
    def listar_imoveis_por_tipo(self, tipo: str) -> None:
        print(f"\nImoveis do tipo {tipo}:")
        for i in range(len(self.__imoveis)-1):
            print(f"Imovel {i+1}:")
            if self.__imoveis[i].get_tipo() == tipo:
                print(self.__imoveis[i]+'\n')
        print(f"Imovel {len(self.__imoveis)}:")        
        print(self.__imoveis[-1])

    def listar_imoveis(self) -> None:
        if len(self.__imoveis)> 0:
            for i in range(len(self.__imoveis)-1):
                print(self.__imoveis[i]+',')
            print(self.__imoveis[-1])
        else:
            print("Não há imoveis cadastrados")

    def get_cpf(self) -> str:
        return self.__cpf
    
    def busca_imovel(self, endereco: Endereco):
        for i in range(len(self.__imoveis)):
            if self.__imoveis[i].get_endereco() == endereco:
                return self.__imoveis[i]
        else:
            return None
        