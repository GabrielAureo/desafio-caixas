class Cliente:
    def __init__(self, nome : str) -> None:
        self.nome = nome
    
    def __str__(self) -> str:
        return self.nome