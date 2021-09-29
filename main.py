import sys
table = [
    {
        "letra": ["A", "J"],
        "valor": 1
    },
    {
        "letra": ["B", "K", "S"],
        "valor": 2
    },
    {
        "letra": ["C", "L", "T"],
        "valor": 3
    },
    {
        "letra": ["D", "M", "U"],
        "valor": 4
    },
    {
        "letra": ["E", "N", "V"],
        "valor": 5
    },
    {
        "letra": ["F", "O", "W"],
        "valor": 6
    },
    {
        "letra": ["G", "P", "X"],
        "valor": 7
    },
    {
        "letra": ["H", "Q", "Y"],
        "valor": 8
    },
    {
        "letra": ["I", "R", "Z"],
        "valor": 9
    },
]


def parseToNumber(c):
    if c.isdigit():
        return str(c)
    else:
        for item in table:
            for letra in item["letra"]:
                if c == letra:
                    return str(item["valor"])


def rutinaCalc(ref):
    ref = list(reversed(ref))
    contador = 0
    total = 0
    for item in ref:
        pivote = 0
        if contador % 2 == 0:
            pivote = str(int(item) * 2)
            if len(pivote) == 2:
                pivote = str(int(pivote[0]) + int(pivote[1]))
            total += int(pivote)
        else:
            pivote = str(int(item) * 1)
            if len(pivote) == 2:
                pivote = str(int(pivote[0]) + int(pivote[1]))
            total += int(pivote)
        contador += 1
    print("Total: " + str(total))
    new_ref = str(total)[len(str(total)) - 1]
    return 10 - int(new_ref)


def modulo10(ref):
    print("M10 - HSBC")
    print("Cliente:" + ref)
    ref = ref.upper()
    numerica = ""
    for item in ref:
        numerica += str(parseToNumber(item))
    print("Numerica: " + numerica)
    digito_verificador = rutinaCalc(str(numerica))    
    print("Verificador: " + str(digito_verificador))
    if digito_verificador == 10:
        digito_verificador = 0
    return str(ref) + str(digito_verificador)


if __name__ == '__main__':
    # Ingresar la clave del cliente
    # 03850
    referencia = modulo10('001834')
    print("Referencia: " + referencia)
