from typing import Tuple, Union
from caixa import CaixaStatus, Caixa
from cliente import Cliente

class OrquestradorCaixas:
    def __init__(self, caixas: list[Caixa]) -> None:
        self.caixas: list[Caixa] = caixas
        self.fila_de_espera: list[Cliente] = []

    @property
    def clientes_esperando(self):
        return len(self.fila_de_espera) > 0

    def caixa_valido(self, num_caixa: int):
        return num_caixa > 0 and num_caixa < len(self.caixas)

    def __get_caixa_livre(self) -> Union[int, bool]:
        return next(
            (caixa for caixa in self.caixas if caixa.status == CaixaStatus.LIVRE), False)

    def atende_cliente(self, cliente: Cliente) -> Tuple[bool, str]:
        caixa_livre = self.__get_caixa_livre()
        if(caixa_livre):
            return caixa_livre.atende_cliente(cliente=cliente)
        else:
            self.fila_de_espera.append(cliente)
            return False, "Ocupado"

    def termina_atendimento(self, num_caixa: int) -> Tuple[bool, str]:
        if(not self.caixa_valido(num_caixa=num_caixa)):
            return False, "Número inválido de caixa"

        resposta = self.caixas[num_caixa - 1].termina_atendimento()

        if(resposta[0] and self.clientes_esperando):
            proximo_cliente = self.fila_de_espera.pop(0)
            self.atende_cliente(proximo_cliente)

        return resposta

    def tira_caixa_do_ar(self, num_caixa: int) -> Tuple[bool, str]:
        if(not self.caixa_valido(num_caixa=num_caixa)):
            return False, "Número inválido de caixa"

        resposta = self.caixas[num_caixa - 1].tira_do_ar()
        return resposta

    def coloca_caixa_no_ar(self, num_caixa: int) -> Tuple[bool, str]:
        if(not self.caixa_valido(num_caixa=num_caixa)):
            return False, "Número inválido de caixa"

        resposta = self.caixas[num_caixa - 1].coloca_no_ar()
        return resposta
