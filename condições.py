# Exemplo de condições

print('Formulário pra entrar no clã LDG') # Essa linha irá dizer na tela "Formulário pra entrar no clã LDG"

dupe = str(input('Você conhece algum dupe da 1.12.2? ')).upper().strip() # Irá perguntar se você conhece algum dupe.
funcionando = str(input('Ele está funcionando? ')).upper().strip()
if dupe == ('SIM'): # Traduzindo ao pé da letra: Se o input acima for respondido com "Sim," ou "Yes", irá passar para a próxima "fase"
    if funcionando == ('SIM'):  
        print('ok')
    print('Muito bem!')
else:
    print('Tudo bem. Isso não e essencial.')

          
