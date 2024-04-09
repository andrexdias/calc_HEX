def gerar_e_imprimir_tabela_gray(num_bits: int) -> None:
    """
    Função para gerar e imprimir uma tabela de códigos Gray com um número especificado de bits.

    :param num_bits: Número de bits no código Gray
    :return: None
    """
    def gerar_codigo_gray(num_bits: int) -> list:
        """
        Função para gerar uma tabela de códigos Gray com um número especificado de bits.

        :param num_bits: Número de bits no código Gray
        :return: Lista de códigos Gray como inteiros
        """
        if num_bits <= 0:
            return []
        elif num_bits == 1:
            return [0, 1]

        # Gera os códigos Gray para n-1 bits
        codigos_gray = gerar_codigo_gray(num_bits - 1)

        # Adiciona os bits faltantes aos códigos Gray gerados anteriormente
        codigos_gray_reversos = codigos_gray[::-1]  # Reverte a lista de códigos Gray
        for i in range(len(codigos_gray)):
            codigos_gray.append(codigos_gray[i] | (codigos_gray_reversos[i] << 1))

        return codigos_gray

    def imprimir_tabela_gray(codigos_gray: list) -> None:
        """
        Função para imprimir a tabela de códigos Gray em formato tabular.

        :param codigos_gray: Lista de códigos Gray como inteiros
        :return: None
        """
        tamanho_codigo = len(bin(max(codigos_gray))) - 2
        print(f"Tabela de Códigos Gray (tamanho: {tamanho_codigo}):")
        print(" " * 4 + "| " + " ".join(f"{i:0{tamanho_codigo}b}" for i in range(len(codigos_gray))))
        print("-" * 4 + "+" + "-" * (tamanho_codigo * len(codigos_gray)))

        for i, codigo in enumerate(codigos_gray):
            print(f"{i:4d} | {codigo:0{tamanho_codigo}b}")

    # Gera e imprime a tabela de códigos Gray
    codigos_gray = gerar_codigo_gray(num_bits)
    imprimir_tabela_gray(codigos_gray)
