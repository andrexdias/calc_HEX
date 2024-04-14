def converter_base(n, base_origem, base_destino):
    # Dicionário para mapear dígitos hexadecimais
    hex_map = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    # Converter o número para a base 10
    num_dec = 0
    for i, digito in enumerate(reversed(str(n))):
        num_dec += int(digito) * (base_origem ** i)

    # Converter o número da base 10 para a base de destino
    num_base_destino = ''
    while num_dec > 0:
        digito = num_dec % base_destino
        if 10 <= digito <= 15:
            digito = hex_map[digito]
        num_base_destino = str(digito) + num_base_destino
        num_dec //= base_destino

    return num_base_destino

