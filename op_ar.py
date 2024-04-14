def soma_subtracao_base_n(base, num1, num2):

    if base == 'bin':
        num1_dec = int(num1, 2)
        num2_dec = int(num2, 2)
    elif base == 'dec':
        num1_dec = int(num1)
        num2_dec = int(num2)
    else: 
        num1_dec = int(num1, 16)
        num2_dec = int(num2, 16)

    soma = num1_dec + num2_dec
    subtracao = num1_dec - num2_dec
    
    if base == 'bin':
        soma_base_n = bin(soma)[2:]
        subtracao_base_n = bin(subtracao)[2:]
    elif base == 'dec':
        soma_base_n = str(soma)
        subtracao_base_n = str(subtracao)
    else:
        soma_base_n = hex(soma)[2:]
        subtracao_base_n = hex(subtracao)[2:]

    print(f"A soma de {num1} e {num2} na base {base} é: {soma_base_n}")
    print(f"A subtração de {num1} e {num2} na base {base} é: {subtracao_base_n}")

