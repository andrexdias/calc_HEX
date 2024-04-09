import tabela_gray


print("Seja bem vindo ao programa de calculos!\n")

print("Escolha a opção:")
print("[1] - Criação da Tabela de Grays de n Bits")
print("[2] - onversão entre Sistemas Numéricos")
print("[3] - Operações aritméticas em diferentes bases")
print("[4] - Ajudas \n")

escolha = int(input("Insira a sua opção:"))

while escolha > 4:
    print("Opção inválida!")
    print("Por favor insira novamente!\n")
    print("Escolha a opção:")
    print("[1] - Criação da Tabela de Grays de n Bits")
    print("[2] - onversão entre Sistemas Numéricos")
    print("[3] - Operações aritméticas em diferentes bases")
    print("[4] - Ajudas \n")
    escolha = int(input("Insira a opção:\n"))

if escolha == 1:
    n_bits = int(input("Insira o número de bits que deseja para criar a tabela: \n"))
    tabela_gray.gerar_gray_(n_bits)
    

elif escolha == 2:
    print("Vamos fazer a conversão!")
    
elif escolha == 3:
    print("Operações Aritmétricas!")

elif escolha == 4:
    print("Seja bem vindo ao painel de ajuda!")
