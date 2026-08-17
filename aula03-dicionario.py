"""
Aula 03 - Dicionários
================================
Conteúdo:
- Dicionários: pares chave-valor (equivalente a HashMap)
- Como criar, acessar e modificar valores por chave

Exemplos de sintaxe:
    dicionario = {"chave": "valor"}
    dicionario["chave"]              # acessa o valor
    dicionario["nova_chave"] = "x"   # adiciona/atualiza uma chave
"""

usuario_teste = {                              # cria o dicionário com 3 pares chave-valor
    "email": "michaeljackson@mj.com",
    "password": "Test123",
    "active": True
}

print(usuario_teste)                            # mostra o dicionário inteiro
print(usuario_teste["email"])                   # acessa direto pela chave "email"
print("O e-mail do Michael Jackson é : ", usuario_teste["email"])  # combina texto fixo com o valor

usuario_teste["active"] = False                 # ATUALIZA o valor da chave "active" (já existia)
usuario_teste["telefone"] = "9999-0000-8888-7777-4444-1111-3333"   # ADICIONA uma chave nova, "telefone" não existia antes
print(usuario_teste)                            # mostra o dicionário já com "telefone" incluído

usuario_teste["telefone"] = "000-111-333-444-555"  # SOBRESCREVE "telefone" (a chave já existia, então não duplica)

print(usuario_teste.get("password"))            # .get() busca "password" com segurança — existe, então retorna o valor normal
print(usuario_teste.get("telefone"))            # mesma coisa, "telefone" existe, retorna o valor atual

print(usuario_teste.get("cpf", "não informado")) # "cpf" NÃO existe no dicionário
                                                  # .get() não quebra o script (diferente de usuario_teste["cpf"], que daria KeyError)
                                                  # como passamos um segundo argumento, retorna "não informado" em vez de None


resposta_api = {
    "usuario": {
        "email": "qa@empresa.com",
        "endereco": {
            "cidade": "Blumenau"
        }
    }
}
print(resposta_api["usuario"]["email"])
print(resposta_api["usuario"]["endereco"]["cidade"])
