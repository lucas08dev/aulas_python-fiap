eng2sp = dict()
print(eng2sp)

eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {
    'one': 'uno', 
    'two': 'dos',
    'three': 'tres'
}

print(eng2sp)
print(eng2sp['two']) # Acessar chave

print('dos' in eng2sp)

valores = eng2sp.values()
print('uno' in valores) # Acessar valores


print()

def count_letters(s):
    d = dict() # Dicionário vazio
    for c in s: # Cada caracter na string
        if c not in d: # Se não houver a letra no dicionario add e vai pro prox
            d[c] = 1

        else:
            d[c] += 1 # Senão, adiciona mais um a letra que ja possui

    return d

dict_count = count_letters("ovo")
print(dict_count)



