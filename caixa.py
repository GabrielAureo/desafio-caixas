from enum import IntEnum
from typing import Tuple
from cliente import Cliente
from caixa_resposta import CaixaResposta


class CaixaStatus(IntEnum):
    LIVRE = 0,
    OCUPADO = 1,
    OFFLINE = 2


class Caixa:
    def __init__(self, caixa_id : int) -> None:
        self.caixa_id = caixa_id
        self.status = CaixaStatus.LIVRE
        self.cliente_atual = None
    
    @property
    def nome(self):
        return f"Caixa {self.caixa_id + 1}"

    def atende_cliente(self, cliente: Cliente) -> CaixaResposta:
        if(self.status == CaixaStatus.OCUPADO):
            return CaixaResposta(False, f"Caixa {self.nome} está ocupado.")
        elif(self.status == CaixaStatus.OFFLINE):
            return CaixaResposta(False, f"Caixa {self.nome} está offline.")
        
        self.cliente_atual = cliente
        self.status = CaixaStatus.OCUPADO

        return CaixaResposta(True, "Atendimento iniciado com sucesso.")

    def termina_atendimento(self) -> CaixaResposta:
        if(self.status == CaixaStatus.LIVRE):
            return CaixaResposta(False, f"Caixa {self.nome} não está em atendimento.")
        elif(self.status == CaixaStatus.OFFLINE):
            return CaixaResposta(False, f"Caixa {self.nome} está offline.")
        
        self.cliente_atual = None
        self.status = CaixaStatus.LIVRE

        return CaixaResposta(True, "Atendimento finalizado com sucesso.")

    def tira_do_ar(self) -> CaixaResposta:
        if(self.status == CaixaStatus.OFFLINE):
            return CaixaResposta(False, f"Caixa {self.nome} já está fora do ar.")
        elif(self.status == CaixaStatus.OCUPADO):
            return CaixaResposta(False, f"Caixa {self.nome} está em atendimento e não pode ser tirado do ar.")
        
        self.status == CaixaStatus.OFFLINE
        return CaixaResposta(True, f"Caixa {self.nome} está offline.")
    
    def coloca_no_ar(self) -> CaixaResposta:
        if(self.status != CaixaStatus.OFFLINE):
            return CaixaResposta(False, f"Caixa {self.nome} já está no ar.")

        self.status == CaixaStatus.LIVRE
        return CaixaResposta(True, f"Caixa {self.nome} está online.")


