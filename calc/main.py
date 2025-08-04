import calculator
import os

def cleanTerminal():
    print('\n' * 100)

i = 0
while True:

    if i != 0:
        cleanTerminal()
    i = i+1
    print("1 para adicao "
          "\n2 para subtracao"
          "\n3 para multiplicacao"
          "\n4 para divisao")
    case = input()

    a = int(input())

    b = int(input())

    cleanTerminal()
    print(calculator.calculator(a, b, case))
    input("enter para continuar")
