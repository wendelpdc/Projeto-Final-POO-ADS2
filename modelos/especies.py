from modelos.tipos import PlantaSemFlor, PlantaComFlor

class Briofita(PlantaSemFlor):
    def exibir_ficha_tecnica(self):
        super().exibir_ficha_tecnica()
        print("Classificação: Briófita (Sem flores, sem sementes, sem vasos)")
        print(f"Reprodução: {self.reproduzir()}")
        print("Estrutura: Avascular (transporte por difusão).")

class Pteridofita(PlantaSemFlor):
    def exibir_ficha_tecnica(self):
        super().exibir_ficha_tecnica()
        print("Classificação: Pteridófita (Sem flores, sem sementes, com vasos)")
        print(f"Reprodução: {self.reproduzir()}")
        print("Estrutura: Vascular (possui xilema e floema).")

class Gimnosperma(PlantaComFlor):
    def __init__(self, nome_comum, nome_cientifico):
        super().__init__(nome_comum, nome_cientifico, tipo_semente="Nua")

    def exibir_ficha_tecnica(self):
        super().exibir_ficha_tecnica()
        print("Classificação: Gimnosperma (Com flores/cones, sem frutos)")
        print(f"Reprodução: {self.reproduzir()} - Sementes nuas.")

class Angiosperma(PlantaComFlor):
    def __init__(self, nome_comum, nome_cientifico, tipo_cotiledone):
        super().__init__(nome_comum, nome_cientifico, tipo_semente="Protegida")
        self.tipo_cotiledone = tipo_cotiledone

    def exibir_ficha_tecnica(self):
        super().exibir_ficha_tecnica()
        print(f"Classificação: Angiosperma ({self.tipo_cotiledone})")
        print(f"Reprodução: {self.reproduzir()} - Protegida por fruto.")