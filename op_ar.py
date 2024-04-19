def converter_base1(num1, base1):
    """Conversor do Numero 1

    Args:
        num1 (Número 1): É o primeiro número que ira ser consertido para decimal
        base1 (Base 01): É a base 01 do primeiro numero que ira ser convertido para decimal

    Returns:
        resultado1: É o primeiro número já em decimal
    """
    resultado1 = 0
    num1 = str(num1)
    for digito in num1:
        resultado1 = resultado1 * base1
        if '0' <= digito <= '9':
            resultado1 += ord(digito) - ord('0')
        elif 'A' <= digito <= 'F':
            resultado1 += ord(digito) - ord('A') + 10
        elif 'a' <= digito <= 'f':
            resultado1 += ord(digito) - ord('a') + 10
    return resultado1

def converter_base2(num2, base2):
    """Conversor do Numero 2

    Args:
        num1 (Número 2): É o segundo número que ira ser consertido para decimal
        base1 (Base 2): É a base do segundo numero que ira ser convertido para decimal

    Returns:
        resultado2: É o segundo número já em decimal
    """
    resultado2 = 0
    num2 = str(num2)
    for digito in num2:
        resultado2 = resultado2 * base2
        if '0' <= digito <= '9':
            resultado2 += ord(digito) - ord('0')
        elif 'A' <= digito <= 'F':
            resultado2 += ord(digito) - ord('A') + 10
        elif 'a' <= digito <= 'f':
            resultado2 += ord(digito) - ord('a') + 10
    return resultado2

def som(resultado1, resultado2):
    """Soma dos números

    Args:
        resultado1 (numero 1 decimal): É  conversão do numero que está como str para int
        resultado2 (numero 2 decimal): É  conversão do numero que está como str para int

    Returns:
        soma: É a soma dos numeros
    """
    resultado1 = int(resultado1)
    resultado2 = int(resultado2)
    soma = resultado1 + resultado2
    return soma

def sub(resultado1, resultado2):
    """Subtração dos números

    Args:
        resultado1 (numero 1 decimal): É  conversão do numero que está como str para int
        resultado2 (numero 2 decimal): É  conversão do numero que está como str para int

    Returns:
        subtracao: É a subtracao dos numeros
    """
    resultado1 = int(resultado1)
    resultado2 = int(resultado2)
    if resultado1 < resultado2:
        subtracao = resultado2 - resultado1
    if resultado1 >= resultado2:
        subtracao = resultado1 - resultado2
    return subtracao

def soma_operacao_aritmetica(soma, base_final):
    """conversão para base final da soma

    Args:
        soma (Soma): É o resultado da soma da função anterior
        base_final (Base Final): É a base final que ira converter a soma

    Returns:
        print: É o resultado impresso na consola da soma já convertida na base desejada pelo utilizador
    """

    if base_final == 2:  # Binario
        resultado_final_s = ""
        while soma:
            resultado_final_s = str(soma % 2) + resultado_final_s
            soma //= 2
    elif base_final == 10:  # decimal
        resultado_final_s = soma
    elif base_final == 16:  # hexadecimal
        hex_map = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        resultado_final = ''
        while soma:
            digito = soma % 16
            if digito in hex_map:
                resultado_final_s = hex_map[digito] + resultado_final_s
            else:
                resultado_final_s = str(digito) + resultado_final_s
            resultado1 //= 16
    else:
        return "Base final não suportada."

    print(f"O resultado da soma na base {base_final} é: {resultado_final_s}")
    
def subn_operacao_aritmetica(subtracao, base_final):
    """conversão para base final da subtração

    Args:
        subtracao (Subtração): É o resultado da subtração da função anterior
        base_final (Base Final): É a base final que ira converter a subtração

    Returns:
        print: É o resultado impresso na consola da soma já convertida na base desejada pelo utilizador
    """
    if base_final == 2:  # Binario
        resultado_final_sub = ''
        while subtracao:
            resultado_final_sub = str(subtracao % 2) + resultado_final_sub
            subtracao //= 2
    elif base_final == 10:  # decimal
        resultado_final_sub = subtracao
    elif base_final == 16:  # hexadecimal
        hex_map = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        resultado_final_sub = ''
        while subtracao:
            digito = subtracao % 16
            if digito in hex_map:
                resultado_final_sub = hex_map[digito] + resultado_final_sub
            else:
                resultado_final_sub = str(digito) + resultado_final_sub
            resultado_final_sub //= 16
    else:
        return "Base final não suportada."

    print(f"O resultado da subtração na base {base_final} é: {resultado_final_sub}")