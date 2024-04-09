
def gerar_gray_(n_bits):
    assert n_bits > 0, "O número de bits deve ser maior que zero"
    gray_codigos = [0]
    while len(gray_codigos) < 2**n_bits:
        novos_gray_codigos = []
        for i in range(1, len(gray_codigos)+1):
            novos_gray_codigos.append(gray_codigos[i-1] ^ (i & gray_codigos[i-1]))
        gray_codigos += novos_gray_codigos
    print(gray_codigos[1:])
    return gray_codigos[1:]