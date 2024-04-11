TC, TF, TK = 0, 0, 0

while True:
    opcao = int(
        input(
            "Digite uma opção e prima Enter: \n   (9) para conversão de Celsius em Fahrenheit \nou (8) para conversão de Fahrenheit em Celsius \nou (7) para conversão de Celsius em Kelvin \nou (6) para conversão de Kelvin em Celsius \nou (5) para conversão de Fahrenheit em Kelvin \nou (4) para conversão de Kelvin em Fahrenheit \nou digite (0) para sair: "
        )
    )
    print()
    if opcao == 9:
        TC = float(input("Digite o valor em Celsius: "))
        TF = (9 * TC / 5) + 32
        print(f"{round(TC,2)} C = {round(TF,2)} F")
    elif opcao == 8:
        TF = float(input("Digite o valor em Fahrenheit: "))
        TC = (TF - 32) * 5 / 9
        print(f"{round(TF,2)} F = {round(TC,2)} C")
    elif opcao == 7:
        TC = float(input("Digite o valor em Celsius: "))
        TK = TC + 273
        print(f"{round(TC,2)} C = {round(TK,2)} K")
    elif opcao == 6:
        TK = float(input("Digite o valor em Kelvin: "))
        TC = TK - 273
        print(f"{round(TK,2)} K = {round(TC,2)} C")
    elif opcao == 5:
        TF = float(input("Digite o valor em Fahreheit: "))
        TK = (5 / 9) * (TF - 32) + 273
        print(f"{round(TF,2)} F = {round(TK,2)} K")
    elif opcao == 4:
        TK = float(input("Digite o valor em Kelvin: "))
        TF = (9 / 5) * (TK - 273) + 32
        print(f"{round(TK,2)} K = {round(TF,2)} F")

    else:
        break

    print()

