print("Seja bem vindo ao programa de calculos!\n")  

print("Escolha a opção:") # menu
print("[1] - Criação da Tabela de Grays de n Bits")
print("[2] - Conversão entre Sistemas Numéricos")
print("[3] - Operações aritméticas em diferentes bases")
print("[4] - Ajudas \n")

escolha = int(input("Insira a sua opção:")) # Pedido de escolha ao utilizador 

while escolha > 4: # Se caso o utilizador escolher uma opção errada ira encaminhar para escolher uma opção correta
    """
    Menu de escolha
    """
    print("Opção inválida!")
    print("Por favor insira novamente!\n")
    print("Escolha a opção:")
    print("[1] - Criação da Tabela de Grays de n Bits")
    print("[2] - Conversão entre Sistemas Numéricos")
    print("[3] - Operações aritméticas em diferentes bases")
    print("[4] - Ajudas \n")
    escolha = int(input("Insira a opção:\n"))

if escolha == 1:  # Escolha da criação de tabela de Gray de N Bits 
    """Menu de escolha 01"""
    import tabela_gray # Importar arquivo da função da tabela de gray 
    n = int(input("Insira o número de bits:")) # Introdução do número de bits
    gray = tabela_gray.gray_code(n) # Chamar a função
    for code in gray: # Chamar o codigo no gray para dar print
        print(code)
    

elif escolha == 2:
    """Menu de escolha 02"""
    import conversor
    print("Vamos fazer a conversão! \n")
    numero_e = input("Por favor, insira o número que deseja converter: \n") # Número para conversão
    print("""   Guia de Bases:
                Para usar a calculadora é preciso inserir as bases de origens e de destino. Essas bases são:
                    Base Binário: 2
                    Base Decimal: 10
                    Base Hexadecimal: 16""") # Guias das bases
    base_origem = int(input("Insira a base do número do número que escreveu:")) # Pedir a base de origiem
    while base_origem != 2 and base_origem != 10 and base_origem != 16: # Checker de base de origem e pedir base de origem se for errada
        print("Por favor, insira 2, 10 ou 16.")
        base_origem = int(input("Insira a base do número que deseja:")) #
    base_destino = int(input("Insira a base do destino:")) # Pedir base de destino
    while base_destino != 2 and base_destino != 10 and base_destino != 16: # Checker de base de destino e pedir base de destino se estiver errada!
        print("Por favor, insira 2, 10 ou 16. ")
        base_destino = int(input("Insira a base do destino do número que deseja:")) 
    resultado = conversor.converter_base(numero_e, base_origem, base_destino)
    print(f"O número {numero_e} na base {base_origem} é {resultado} na base {base_destino}.")
    
elif escolha == 3:
    """Menu de escolha 03"""
    print("Operações Aritmétricas!")
    print("""   Guia de Bases:
                Para usar a calculadora é preciso inserir as bases de origens e de destino. Essas bases são:
                    Base Binário: 2
                    Base Decimal: 10
                    Base Hexadecimal: 16""") # Guias das bases
    import op_ar # Importar o arquivo
    num1 = int(input("Insira o primeiro numero da conta:"))
    base1 = int(input("Insira a base que estão os números que acabou de registrar:"))
    while base1 != 2 and base1 != 10 and base1 != 16: # Checker de base e pedir base do numero 1 se for errada
        print("Por favor, insira 2, 10 ou 16.")
        base1 = int(input("Insira a base que deseja para o número 1:"))
    resultado1 = op_ar.converter_base1(num1, base1)
    num2 = int(input("Insira o segundo numero da conta:"))
    base2 = int(input("Insira a base dos números que acabou de registrar:"))
    while base2 != 2 and base2 != 10 and base2 != 16: #Checker de base do numero 2
        print("Por favor, insira 2, 10 ou 16")
        base2 = int(int("Insira a base do 2º número:"))
    resultado2 = op_ar.converter_base2(num2, base2)
    base_final = int(input("Insira a base que deseja no final:"))
    while base_final != 2 and base_final != 10 and base_final != 16: #Checker de base final
        print("Por favor insira 2 para bases binárias, 10 para bases decimais e 16 para bases hexadecimais")
        base_final = str("Insira a base final:")
    soma = op_ar.som(resultado1, resultado2)
    subtracao = op_ar.sub(resultado1, resultado2)
    op_ar.soma_operacao_aritmetica(soma, base_final)
    op_ar.subn_operacao_aritmetica(subtracao, base_final)
        
elif escolha == 4: # Ajuda
    """Menu de Ajuda 04"""
    print(""" Olá, seja bem vindo!
          Na opção 1 consegue criar uma tabela de Gray com n bits personalizado!
          Na opção 2 consegue converter qualquer número para bin, hex, dec.
          Na opção 3 consegue calcular tanto hax, bin, dec, permitindo tendo bases diferentes para os calculos fazendo já a conversão!
          Este código foi elaborado por André Dias, Rodrigo Soares, Tómas Silva e Guilherme Nunes!
          """)
