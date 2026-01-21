import os
from modelos.especies import Briofita, Pteridofita, Gimnosperma, Angiosperma

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_planta(catalogo):
    limpar_tela()
    print("--- MÓDULO DE CADASTRO ---")
    nome = input("Nome comum: ")
    cientifico = input("Nome científico: ")
    
    print("\n[Assistente de Classificação Taxonômica]")
    if input("Possui flores e sementes? (s/n): ").lower() == 'n':
        if input("Possui vasos condutores? (s/n): ").lower() == 'n':
            nova = Briofita(nome, cientifico)
        else:
            nova = Pteridofita(nome, cientifico)
    else:
        if input("Possui frutos protegendo a semente? (s/n): ").lower() == 'n':
            nova = Gimnosperma(nome, cientifico)
        else:
            tipo = input("Tipo (Monocotiledônea / Dicotiledônea): ")
            nova = Angiosperma(nome, cientifico, tipo)
    
    catalogo.append(nova)
    print(f"\nSucesso: {nome} classificada como {type(nova).__name__}.")
    input("Enter para continuar...")

def exibir_relatorio(catalogo):
    limpar_tela()
    print(f"=== RELATÓRIO ({len(catalogo)} espécimes) ===\n")
    for planta in catalogo:
        planta.exibir_ficha_tecnica()
        print("-" * 40)
    input("\nEnter para voltar...")

def executar_menu():
    catalogo = []
    while True:
        limpar_tela()
        print("=== SISTEMA ONG BIO BRASIL v2.0 ===")
        print("1. Nova Catalogação")
        print("2. Ver Relatório")
        print("3. Sair")
        
        op = input("Opção: ")
        if op == '1': cadastrar_planta(catalogo)
        elif op == '2': exibir_relatorio(catalogo)
        elif op == '3': break