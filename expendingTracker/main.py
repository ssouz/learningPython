import expendingTracker
import json


gastos = []


with open('gastos.json', 'r') as file:
    gastos = json.load(file)

while True:
    print("\n=== Sistema de Gastos ===")
    print("1. Adicionar novo gasto")
    print("2. Listar todos os gastos")
    print("3. Calcular total dos gastos")
    print("4. Sair do sistema")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
       expendingTracker.adicionarGasto(gastos)
       with open('gastos.json', 'w') as file:
           json.dump(gastos, file, indent=4)
    elif opcao == "2":
       expendingTracker.listarGastos(gastos)
    elif opcao == "3":
     expendingTracker.calcularTotalDeGasto(gastos)

    elif opcao == "4":
        print("\nSistema encerrado!")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")




    input("\nPressione Enter para continuar...")