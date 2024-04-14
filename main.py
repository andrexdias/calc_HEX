import tabela_gray # Chamar arquivo Python para a tabela de gray
import conversor # Chamar arquivo Conversor para conversão de bases
import op_ar # Chamar arquivo op_ar para operações aritméticas em diferentes bases
# Optei por chamar todos os arquivos individualmente para não extender nem poluir o código!


print("Seja bem vindo ao programa de calculos!\n")  # Mensagem de Introdução

print("Escolha a opção:") # menu
print("[1] - Criação da Tabela de Grays de n Bits")
print("[2] - onversão entre Sistemas Numéricos")
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

if escolha == 1: 
    num_bits = int(input("Insira o número de bits que deseja para criar a tabela: \n"))
    tabela_gray.gerar_e_imprimir_tabela_gray(num_bits) 

elif escolha == 2:
    print("Vamos fazer a conversão! \n")
    numero = input("Por favor, insira o número que deseja converter: \n") # Número para conversão
    print("""Guia de Bases:
Para usar a calculadora é preciso inserir as bases de origens e de destino. Essas bases são:
Base Binário: 2
Base Decimal: 10
Base Hexadecimal: 16""") # Guias das baases
    base_origem = int(input("Insira a base do número que deseja converter:")) # Pedir a base de origiem
    while base_origem != 2 and base_origem != 10 and base_origem != 16: # Checker de base de origem e pedir base de origem se for errada se digitar errado
        print("Por favor, insira 2, 10 ou 16.")
        base_origem = int(input("Insira a base do número que deseja:")) #
    base_destino = int(input("Insira a base do destino:")) # Pedir base de destino
    while base_destino != 2 and base_destino != 10 and base_destino != 16: # Checker de base de destino e pedir base de destino se estiver errada!
        print("Por favor, insira 2, 10 ou 16. ")
        base_destino = int(input("Insira a base do destino do número que deseja:")) 
    conversor.converter_base(numero, base_origem, base_destino) # Função para conversão!
        
    
    
elif escolha == 3:
    print("Operações Aritmétricas!")

elif escolha == 4:
    print("Seja bem vindo ao painel de ajuda!")
