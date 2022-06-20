from enum import IntEnum
from caixa_orquestrador import OrquestradorCaixas
from cliente import Cliente

class ComandosAgencia(IntEnum):
    FINALIZA = 0
    ATENDE_CLIENTE = 1
    FINALIZA_ATENDIMENTO = 2
    TIRA_DO_AR = 3
    COLOCA_NO_AR = 4

class Agencia:
    def __init__(self, orquestrador : OrquestradorCaixas) -> None:
        self.orquestrador = orquestrador

    @property
    def __lista_de_comandos(self) -> str:
        return """
Insira o código da próxima operação:
1 - Atende novo cliente
2 - Finaliza atendimento
3 - Tira caixa do ar
4 - Coloca caixa no ar
0 - Finaliza expediente
"""

    def __entrada_cliente(self) -> Cliente:
        nome_cliente = input("Insira o nome do cliente:\n")
        while nome_cliente == "":
            nome_cliente = input("Favor inserir um nome válido:\n")

        return Cliente(nome=nome_cliente)
    
    def __entrada_caixa(self) -> int:
        num_caixa = int(input("Insira o numero da caixa:\n"))
        while not self.orquestrador.caixa_valido(num_caixa=num_caixa):
            num_caixa = int(input("Favor inserir um caixa válido:\n"))
        
        return num_caixa

    def atende_cliente(self) -> None:
        cliente = self.__entrada_cliente()
        resposta = self.orquestrador.atende_cliente(cliente=cliente)
        print(resposta[1])
    
    def finaliza_atendimento(self) -> None:
        num_caixa = self.__entrada_caixa()
        resposta = self.orquestrador.termina_atendimento(num_caixa=num_caixa)
        print(resposta[1])

    def tira_caixa_do_ar(self) -> None:
        num_caixa = self.__entrada_caixa()
        resposta = self.orquestrador.tira_caixa_do_ar(num_caixa=num_caixa)
        print(resposta[1])
    
    def coloca_caixa_no_ar(self) -> None:
        num_caixa = self.__entrada_caixa()
        resposta = self.orquestrador.coloca_caixa_no_ar(num_caixa=num_caixa)
        print(resposta[1])
        
    def executa(self) -> None:
        while(True):
            comando = int(input(self.__lista_de_comandos))

            if(comando == ComandosAgencia.ATENDE_CLIENTE):
                self.atende_cliente()
            elif(comando == ComandosAgencia.FINALIZA_ATENDIMENTO):
                self.finaliza_atendimento()
            elif(comando == ComandosAgencia.TIRA_DO_AR):
                self.tira_caixa_do_ar()
            elif(comando == ComandosAgencia.COLOCA_NO_AR):
                self.coloca_caixa_no_ar()
            elif(comando == ComandosAgencia.FINALIZA):
                break


