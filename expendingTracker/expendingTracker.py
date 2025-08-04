def adicionarGasto(gastos):
    data = input("Data (DD/MM/AAAA): ")
    nome =input("Nome do gasto: ")
    valor = float(input("Gasto em R$"))
    descricao = input("descricao: ")

    novo_gasto = {
        "data": data,
        "nome": nome,
        "valor": valor,
        "descricao": descricao
    }

    gastos.append(novo_gasto)

def listarGastos(gastos):
   print(gastos)
def calcularTotalDeGasto(gastos):
    print("")


