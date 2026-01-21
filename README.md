# Sistema de Catalogação Botânica - ONG BioBrasil

> **Projeto Final de POO (ADS 2025.2)** > Sistema em Python para catalogação e classificação taxonômica de plantas, simulando uma demanda real para ONGs.

## 📋 Sobre o Projeto
Este software foi desenvolvido para solucionar o problema de identificação e classificação de espécies vegetais da **ONG BioBrasil**. Diferente de um cadastro simples, o sistema utiliza um algoritmo de decisão baseado em características biológicas (presença de flores, vasos, sementes e frutos) para determinar automaticamente a classe taxonômica correta:

* **Briófitas** (ex: Musgos)
* **Pteridófitas** (ex: Samambaias)
* **Gimnospermas** (ex: Pinheiros)
* **Angiospermas** (ex: Fruteiras)

## 🚀 Tecnologias e Arquitetura
O projeto foi estruturado em **Pacotes Python** para separar a interface da regra de negócios, aplicando rigorosamente os 4 pilares da Orientação a Objetos:

* **Abstração:** Uso da classe base abstrata `Planta` como contrato.
* **Encapsulamento:** Atributos protegidos (`_nome`) acessados via *Properties*.
* **Herança:** Hierarquia de classes multinível (`Planta` -> `PlantaComFlor` -> `Angiosperma`).
* **Polimorfismo:** Método `exibir_ficha_tecnica()` com comportamento único para cada espécie.

## 📂 Estrutura do Projeto
```text
Projeto-Final-POO-ADS2/
│
├── main.py                  # Ponto de entrada (Execução)
├── modelos/                 # [PACOTE] Regras de Negócio
│   ├── base.py              # Classe Abstrata
│   ├── tipos.py             # Categorias Intermediárias
│   └── especies.py          # Classes Concretas (Briófita, etc.)
│
└── sistema/                 # [PACOTE] Interface de Usuário
    └── interface.py         # Menu Interativo (CLI)