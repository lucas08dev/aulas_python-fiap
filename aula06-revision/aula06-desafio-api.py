endpoints = ["Login", "Produtos", "Pedidos"]

status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500]
]


def analisar(requisicoes):
    sucessos = 0
    erros = 0
    erros_seguidos = False
    contador = 0

    for valor in requisicoes:
        if 200 <= valor <= 299:
            sucessos += 1
            contador = 0
        else:
            erros += 1
            contador += 1
            if contador == 2:
                erros_seguidos = True

    porcentagem = (sucessos / len(requisicoes)) * 100
    return porcentagem, erros, erros_seguidos

for i in range(len(endpoints)):
    porcentagem, erros, erros_seguidos = analisar(status[i])
    print(f"Endpoint: {endpoints[i]}")
    print(f"Taxa de sucesso: {porcentagem}%")
    print()

endpoint_menos_eficiente = None
maior_erro = -1

for i in range(len(endpoints)):
    porcentagem, erros, erros_seguidos = analisar(status[i])
    if erros > maior_erro:
        maior_erro = erros
        endpoint_menos_eficiente = endpoints[i]

print(f"Endpoint com mais erros: {endpoint_menos_eficiente} com ({maior_erro} erros)")
print()

for i in range(len(endpoints)):
    porcentagem, erros, erros_seguidos = analisar(status[i])
    print(f"{endpoints[i]} teve dois erros seguidos? {erros_seguidos}")
print()

print("RESULTADO DE OPERAÇÕES:")
for i in range(len(endpoints)):
    porcentagem, erros, erros_seguidos = analisar(status[i])

    if erros_seguidos:
        classificacao = "Crítico"
    elif porcentagem >= 80:
        classificacao = "Instável" if porcentagem < 80 else "Estável"
        classificacao = "Estável"
    else:
        classificacao = "Instável"

    print(f"{endpoints[i]}: {classificacao}")