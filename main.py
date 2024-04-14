"""@package docstring
Página principal do Projeto!
Este projeto foi desenvolvido no ambito da Cadeira de Ecosistemas do 1ºAno, 2ºSemestre.
"""
print("Seja bem vindo ao programa de calculos!\n")  

print("Escolha a opção:") # menu
print("[1] - Criação da Tabela de Grays de n Bits")
print("[2] - Conversão entre Sistemas Numéricos")
print("[3] - Operações aritméticas em diferentes bases")
print("[4] - Ajudas \n")

escolha = int(input("Insira a sua opção:")) # Pedido de escolha ao utilizador 

while escolha > 4: # Se caso o utilizador escolher uma opção errada ira encaminhar para escolher uma opção correta
    print("Opção inválida!")
    print("Por favor insira novamente!\n")
    print("Escolha a opção:")
    print("[1] - Criação da Tabela de Grays de n Bits")
    print("[2] - Conversão entre Sistemas Numéricos")
    print("[3] - Operações aritméticas em diferentes bases")
    print("[4] - Ajudas \n")
    escolha = int(input("Insira a opção:\n"))

if escolha == 1: # Escolha da criação de tabela de Gray de N Bits 
    import tabela_gray # Importar arquivo da função da tabela de gray 
    n = int(input("Insira o número de bits:")) # Introdução do número de bits
    gray = tabela_gray.gray_code(n) # Chamar a função
    for code in gray: # Chamar o codigo no gray para dar print
        print(code)
    

elif escolha == 2:
    import conversor2
    print("Vamos fazer a conversão! \n")
    numero = input("Por favor, insira o número que deseja converter: \n") # Número para conversão
    print("""Guia de Bases:
Para usar a calculadora é preciso inserir as bases de origens e de destino. Essas bases são:
Base Binário: 2
Base Decimal: 10
Base Hexadecimal: 16""") # Guias das bases
    base_origem = int(input("Insira a base do número que deseja converter:")) # Pedir a base de origiem
    while base_origem != 2 and base_origem != 10 and base_origem != 16: # Checker de base de origem e pedir base de origem se for errada se digitar errado
        print("Por favor, insira 2, 10 ou 16.")
        base_origem = int(input("Insira a base do número que deseja:")) #
    base_destino = int(input("Insira a base do destino:")) # Pedir base de destino
    while base_destino != 2 and base_destino != 10 and base_destino != 16: # Checker de base de destino e pedir base de destino se estiver errada!
        print("Por favor, insira 2, 10 ou 16. ")
        base_destino = int(input("Insira a base do destino do número que deseja:")) 
    conversor2.converter_base(numero, base_origem, base_destino) # Função para conversão!
    
elif escolha == 3:
    print("Operações Aritmétricas!")
    import op_ar # Importar o arquivo
    base = input("Insira a base numérica (bin, dec, hex): ") # Perguntar a base
    if base not in ['bin', 'dec', 'hex']: # Checkar se introduziu a base bem
        print("Base inválida. Deve ser 'bin', 'dec' ou 'hex'.")
        base = input("Insira a base numérica (bin, dec, hex): ")
    num1 = input(f"Insira o primeiro número na base {base}: ") # Inserir o primeiro numero
    num2 = input(f"Insira o segundo número na base {base}: ") # Inserir o segundo numero
    op_ar.soma_subtracao_base_n(base, num1, num2) #Chamar a função

elif escolha == 4: # Ajuda
    print(""" Olá, seja bem vindo!
          Este código foi elaborado por André Dias, Rodrigo Soares, Tómas Silva e Guilherme Nunes!
          """)
