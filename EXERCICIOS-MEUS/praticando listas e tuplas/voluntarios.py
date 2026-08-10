voluntarios = []

while True:
    nome = input(f'Digite o nome do voluntário {len(voluntarios)+1} (ou sair para encerrar): ')
    
    if nome.lower() == 'sair':
        break
    
    if nome.lower() in [v.lower() for v in voluntarios]:
        print(f'"{nome}" já foi cadastrado! Digite um nome diferente.')
        continue
    
    voluntarios.append(nome)

print(f'\nOs voluntários são: {voluntarios}')