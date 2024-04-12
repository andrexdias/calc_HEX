def converter_base(numero, base_destino):
    """
    Converte um número de uma base para outra e imprime o resultado.

    Args:
        numero (str): O número a ser convertido (como string).
        base_destino (int): A base de destino (2 para binário, 10 para decimal, 16 para hexadecimal).
    """
    try:
        # Converte o número para decimal
        decimal = int(numero, base_destino)

        # Converte o decimal para a base de destino
        if base_destino == 2:
            resultado = bin(decimal)[2:]  # Remove o prefixo "0b" do binário
        elif base_destino == 16:
            resultado = hex(decimal)[2:]  # Remove o prefixo "0x" do hexadecimal
        else:
            resultado = str(decimal)

        print(f"Resultado na base {base_destino}: {resultado}")
    except ValueError:
        print("Erro: Número inválido ou base não suportada.")

