from abc import ABC, abstractmethod

class Planta(ABC):
    def __init__(self, nome_comum, nome_cientifico):
        self._nome_comum = nome_comum
        self._nome_cientifico = nome_cientifico

    @property
    def nome_comum(self):
        return self._nome_comum

    @property
    def nome_cientifico(self):
        return self._nome_cientifico

    @abstractmethod
    def reproduzir(self):
        pass

    def exibir_ficha_tecnica(self):
        print(f"--- Ficha Técnica: {self.nome_comum} ---")
        print(f"Nome Científico: {self.nome_cientifico}")