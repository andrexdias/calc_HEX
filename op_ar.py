def converter_base1(num1, base1):
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
    resultado1 = int(resultado1)
    resultado2 = int(resultado2)
    soma = resultado1 + resultado2
    return soma

def sub(resultado1, resultado2):
    resultado1 = int(resultado1)
    resultado2 = int(resultado2)
    if resultado1 < resultado2:
        subtracao = resultado2 - resultado1
    if resultado1 > resultado2:
        subtracao = resultado1 - resultado2
    return subtracao


def operacao_aritmetica(operacao, base_final):

    if base_final == 2:  # binário
        resultado_final = ''
        while resultado1:
            resultado_final = str(resultado1 % 2) + resultado_final
            resultado1 //= 2
    elif base_final == 16:  # hexadecimal
        hex_map = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        resultado_final = ''
        while resultado1:
            digito = resultado1 % 16
            if digito in hex_map:
                resultado_final = hex_map[digito] + resultado_final
            else:
                resultado_final = str(digito) + resultado_final
            resultado1 //= 16
    else:
        return "Base final não suportada."

    print(f"O resultado da {operacao} na base {base_final} é: {resultado_final}")