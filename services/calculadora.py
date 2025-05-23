class Calculadora:
    def __init__(self, valor_imovel: float, percentual_entrada: float, anos_contrato: int):
        self.valor_imovel = valor_imovel
        self.percentual_entrada = percentual_entrada
        self.anos_contrato = anos_contrato

    def calcular_valor_entrada(self) -> float:
        return self.valor_imovel * (self.percentual_entrada / 100)

    def calcular_valor_financiar(self) -> float:
        entrada = self.calcular_valor_entrada()
        return self.valor_imovel - entrada

    def calcular_guardar_contrato(self) -> float:
        return self.valor_imovel * 0.15

    def calcular_valor_mensal_guardar(self) -> float:
        total_guardar = self.calcular_guardar_contrato()
        meses = self.anos_contrato * 12
        return total_guardar / meses if meses else 0
