def converter_base(numero_e, base_origem, base_destino):
    """Conversor

    Args:
        numero_e (_número_): é o número que será convertido pela base escolhida
        base_origem (base de origem): É  base do numero que ira ser convertido, base hexadecimal, decimal ou binario
        base_destino (base de destino): É a base que deseja ser convertida, base hexadecimal ou decimal ou binaria

    Returns:
        num_base_destino: é já o número convertido pela base desejada
    """
    hex_map = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    num_dec = 0
    for i, digito in enumerate(reversed(str(numero_e))):
        num_dec += int(digito) * (base_origem ** i)

    num_base_destino = ''
    while num_dec > 0:
        digito = num_dec % base_destino
        if 10 <= digito <= 15:
            digito = hex_map[digito]
        num_base_destino = str(digito) + num_base_destino
        num_dec //= base_destino

    return num_base_destino

