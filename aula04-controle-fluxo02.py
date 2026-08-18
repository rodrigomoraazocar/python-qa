resultado_testes=["passou","passou","falhou","passou","bloqueado","passou","falhou","falhou"]
count=0
for indice, resultado in enumerate(resultado_testes):
    if resultado =="falhou":
        count=count +1
        print(f"❌ Teste {indice} falhou - investigar")
        if count >= 3:
            print("🛑 Muitas falhas, abortando suite")
            break
    elif resultado=="bloqueado":
        print(f"⏭️ Teste {indice} bloqueado, pulando")
        continue
    elif resultado =="passou":
        print(f"✅ Teste {indice} passou")
