class Endereco:
    def __init__(self, rua: str, numero: str, cep: str, estado: str, cidade: str) -> None:
        self.__rua = rua
        self.__numero = numero
        self.__cep = cep
        self.__estado = estado
        self.__cidade = cidade

    def __eq__(self, endereco: object) -> bool:
        return endereco.get_rua() == self.__rua and endereco.get_numero() == self.__numero and endereco.get_cep() == self.__cep and endereco.get_estado() == self.__estado and endereco.get_cidade() == self.__cidade

    def __str__(self) -> str:
        return f"Endereco: {self.__rua}, {self.__numero}, cep: {self.__cep}, {self.__estado}, {self.__cidade}"

    def get_rua(self) -> str:
        return self.__rua
    
    def get_numero(self) -> str:
        return self.__numero
    
    def get_cep(self) -> str:
        return self.__cep
    
    def get_estado(self) -> str:
        return self.__estado
    
    def get_cidade(self) -> str:
        return self.__cidade

    def set_rua(self, rua: str) -> None:
        self.__rua = rua
    
    def set_numero(self, numero: str) -> None:
        self.__numero = numero
    
    def set_cep(self, cep: str) -> None:
        self.__cep = cep
    
    def set_estado(self, estado: str) -> None:
        self.__estado = estado
    
    def set_cidade(self, cidade: str) -> None:
        self.__cidade = cidade