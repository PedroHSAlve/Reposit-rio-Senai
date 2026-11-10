while True:
    print("====== Calculadora ======")
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    print("Escolha a operação que desejar:")
    print("1- Soma")
    print("2- Subtração")
    print("3- Multiplicação")
    print("4- Divisão")
    opção = int(input(" Digite a opção desejada: "))
    if opção == 1:
        result = num1 + num2
        print(f"O resultado da soma é: {result}")
    elif opção == 2: 
        result = num1 - num2
        print(f"O resultado da subtração é: {result}")
    elif opção == 3: 
        result = num1 * num2
        print(f"O resultado da multiplicação é: {result}")
    elif opção == 4: 
        result = num1 / num2
        print(f"O resultado da divisão é: {result}")
    else:
        print("Opção inválida ! Tente novamente.")
        
    resp = input("Deseja continuar? (s/n): ")
    if resp == "s":
        continue
    if resp == "n":
        print("Obrigado por utilizar a calculadora !")
        print("Até a próxima !")
                
        
    break       
        
     