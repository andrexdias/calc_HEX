def operacao_aritmetica(num1, num2, base1, base2, operacao, base_final):
    def converter_base(numero, base):
        return int(numero, base)

    if operacao == 'soma':
        resultado1 = converter_base(num1, base1) + converter_base(num2, base2)
    elif operacao == 'subtracao':
        resultado1 = converter_base(num1, base1) - converter_base(num2, base2)
    else:
        return "Operação não suportada."

    if base_final == 2:  # binário
        resultado_final = ''
        while resultado1:
            resultado_final = str(resultado1 % 2) + resultado_final
            resultado1 //= 2
    elif base_final == 10:  # decimal  
        resultado_final = resultado1
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