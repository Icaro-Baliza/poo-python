from datetime import datetime, timedelta

class Agenda:
    def __init__(self):
        self.__bloqueado = []
        self.__alugado= []

    def alugar(self, dia: datetime, mes: datetime, ano:datetime) -> bool:
        data = datetime(ano, mes, dia)
        if data not in self.__alugado and data not in self.__bloqueado:
            self.__alugado.append(data)
            return True
        else:
            return False
    
    def bloquear(self, dia: datetime, mes: datetime, ano:datetime) -> bool:
        data = datetime(ano, mes, dia)
        if data not in self.__bloqueado and data not in self.__alugado:
            self.__bloqueado.append(data)
            return True
        else:
            return False