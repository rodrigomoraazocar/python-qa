[["""
Aula 02 - Listas
================================
Conteúdo:
- Listas: coleção ordenada de valores (equivalente a ArrayList)

Exemplos de sintaxe:
    lista = [item1, item2, item3]
    lista.append(item4)          # adiciona no final
"""

navegadores = ["Chrome", "Firefox", "Edge"]     # cria a lista com 3 itens (posições 0, 1, 2)
print(navegadores)                              # mostra a lista completa: ['Chrome', 'Firefox', 'Edge']
print(navegadores[0])                           # mostra só o item da posição 0: 'Chrome'

navegadores.append("Opera")                     # adiciona 'Opera' no final da lista
print(navegadores)                              # ['Chrome', 'Firefox', 'Edge', 'Opera']

navegadores.remove("Opera")                      # remove 'Opera' pelo VALOR (não pela posição)
print(navegadores)                              # volta a ser: ['Chrome', 'Firefox', 'Edge']

print(navegadores.pop(0))                       # remove o item da posição 0 ('Chrome') E imprime ele
                                                 # depois desse pop, a lista vira: ['Firefox', 'Edge']

navegadores.insert(1, "Chromium")               # insere 'Chromium' NA posição 1, empurrando o resto pra frente
                                                 # lista agora: ['Firefox', 'Chromium', 'Edge']

if "Firefox" in navegadores:                    # checa se 'Firefox' existe na lista (True ou False)
    posicao = navegadores.index("Firefox")      # se existir, pega a posição onde ele está
    print("Firefox está na lista na posicao", posicao)
else:
    print("Firefox não está na lista")

print(navegadores)                              # mostra o estado atual da lista
navegadores.append("Opera Mini")                # adiciona 'Opera Mini' no final
print(navegadores)                              # mostra a lista final, com 'Opera Mini' incluído
