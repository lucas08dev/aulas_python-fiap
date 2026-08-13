endpoints = ["/login", "/produtos", "/pedidos"]


status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
]

def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299

def erros_seguidos(codigos_http):
    for i in range(len(codigos_http) - 1):
        codigo_atual = codigos_http[i]
        prox_codigo = codigos_http[i + 1]

        if not eh_sucesso(codigo_atual) and eh_sucesso(prox_codigo):
            return True

    return False

def analisar_endpoint(codigos_http):
    qtd_de_sucesso = 0

    for codigo in codigos_http:
        if eh_sucesso(codigo):
            qtd_de_sucesso += 1

    qtd_req = len(codigos_http)
    qtd_erros = qtd_req - qtd_de_sucesso

    percentual_sucesso = (qtd_de_sucesso / qtd_req ) * 100

    tem_erros_seguidos = erros_seguidos(codigos_http)

    if tem_erros_seguidos:
        classificacao = "CRÍTICO"

    elif percentual_sucesso >= 80:
        classificacao = "ESTÁVEL"

    else:
        classificacao = "INSTÁVEL"

    return (qtd_de_sucesso, qtd_erros, percentual_sucesso, classificacao)

maior_qtd_erros = -1
endpoint_maior_erro = ""


for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    codigos_endpoint = status[i]

    sucessos, erros, percentual, classificacao = analisar_endpoint(codigos_endpoint)

    print(f"Endpoint: {nome_endpoint}")
    print(f"Códigos HTTP: {codigos_endpoint}")
    print(f"Sucessos: {sucessos}")
    print(f"Erros: {erros}")
    print(f"% de sucesso: {percentual:.1f}%")
    print(f"Classificação: {classificacao}")
    print("-" * 30)
    print()

    if erros > maior_qtd_erros:
        maior_qtd_erros = erros
        endpoint_maior_erro = nome_endpoint

    elif erros == maior_qtd_erros:
        endpoint_maior_erro += " " + nome_endpoint

print(f"Endpoiint(s) com + erros: {endpoint_maior_erro} com {maior_qtd_erros} erros")
