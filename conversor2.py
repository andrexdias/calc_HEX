# O Python tem funções para conversão de bases como o decimal e hexadecimal
def converter_base(numero, base_origem, base_destino):
    numero_decimal = int(numero, base_origem)
    if base_destino == 10:
        resultado = str(numero_decimal) 
    elif base_destino == 2:
        resultado = bin(numero_decimal).replace("0b", "")
    elif base_destino == 16:
        resultado = hex(numero_decimal).replace("0x", "")
    else:
        resultado = "Base de destino não suportada."
    print(f"O número {numero} na base {base_origem} é {resultado} na base {base_destino}.")