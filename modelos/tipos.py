from modelos.base import Planta  

class PlantaSemFlor(Planta):
    def reproduzir(self):
        return "Esporos (dependente de água/umidade)"

class PlantaComFlor(Planta):
    def __init__(self, nome_comum, nome_cientifico, tipo_semente):
        super().__init__(nome_comum, nome_cientifico)
        self.tipo_semente = tipo_semente

    def reproduzir(self):
        return "Sementes (processo de polinização)"