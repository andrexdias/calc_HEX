
def gray_code(n):
    
    """Criador da tabela de N Gray

    Returns:
        gray: Ira mandar print com a tabela
    """

    gray = ['0', '1']

    for i in range(2, n + 1):
        gray = gray + gray[::-1]

        for j in range(0, 1 << (i - 1)):
            gray[j] = '0' + gray[j]

        for j in range(1 << (i - 1), 1 << i):
            gray[j] = '1' + gray[j]

    return gray
