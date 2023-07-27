from endereco import Endereco
from agenda import Agenda

class Imovel:
    """
    """

    def __init__(self, iptu: float, tipo: str, utilizacao: str, rua: str, numero: str, cep: str, estado="BA", cidade="Salvador") -> None:
        self.__iptu = iptu
        self.__tipo = tipo
        self.__utilizacao = utilizacao
        self.__endereco = Endereco(rua, numero, cep, estado, cidade)
        self.__agenda = Agenda()

    def __eq__(self, imovel) -> bool:
        if isinstance(imovel, Imovel):
            return self.__endereco == imovel.get_endereco()
        else:
            return False
    
    def __str__(self) -> str:
        return f"Iptu:{self.__iptu},\nTipo:{self.__tipo},\nUtilizacao:{self.__utilizacao},\nEndereco: {self.__endereco}"

    def get_endereco(self) -> Endereco:
        return self.__endereco
    
    def get_tipo(self) -> str:
        return self.__tipo
    
    def get_agenda(self) -> Agenda:
        return self.__agenda
