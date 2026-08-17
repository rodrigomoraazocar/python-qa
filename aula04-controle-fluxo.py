"""
Aula 04 - Controle de Fluxo (if / for / while)
================================================
Conteúdo:
- if / elif / else
- for: percorrendo listas e dicionários
- while: repetição condicional
- Indentação define o bloco (obrigatório, diferente de Java)

Exemplos de sintaxe:
    for item in lista:
        print(item)

    for indice, item in enumerate(lista):
        print(indice, item)
"""

lista_navegadores = ["Chrome", "Firefox", "Edge"]   # lista com 3 navegadores (posições 0, 1, 2)

# --- if / else dentro do for: decide algo diferente para cada item ---
for navegador in lista_navegadores:
    if navegador == "Edge":
        print(f"Pulando {navegador}, ainda nao suportado")
    else:
        print(f"Testando em: {navegador}")

print()  # linha em branco só para separar visualmente as duas partes

# --- acessando por posição (índice), sem loop ---
print("Navegadores suportados:", lista_navegadores[0], ",", lista_navegadores[1], ",", lista_navegadores[2])

# --- mesma coisa, mas com posição + valor juntos, usando enumerate() ---
for indice, navegador in enumerate(lista_navegadores):
    print(f"Posição {indice}: {navegador}")

# --- testando um navegador que NÃO está na lista ---
navegador_teste = "Safari"
if navegador_teste in lista_navegadores:
    print(f"{navegador_teste} está na lista de suportados")
else:
    print(f"{navegador_teste} não está na lista de suportados")
