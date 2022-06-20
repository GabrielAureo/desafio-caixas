class CaixaResposta:
    def __init__(self, sucesso : bool, mensagem : str) -> None:
        self.sucesso = sucesso
        self.mensagem = mensagem