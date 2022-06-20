from agencia import Agencia
from caixa_orquestrador import OrquestradorCaixas
from caixa import Caixa
from config import NUM_CAIXAS


def main():
    agencia = Agencia(
        orquestrador= OrquestradorCaixas(
            caixas = [Caixa(i) for i in range(NUM_CAIXAS)]
        )
    )

    agencia.executa()

if __name__ == "__main__":
    main()