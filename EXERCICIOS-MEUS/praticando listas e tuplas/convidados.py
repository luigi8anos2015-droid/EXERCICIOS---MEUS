convidados= ['ana', 'bia' , 'carlos']

novos_convidados=input('digite o nome do novo convidado: ')
convidados_posicao= int(input('digite a posição que deseja adicionar o convidado: '))

convidados.insert(convidados_posicao, novos_convidados)
print(f'Lista de convidados atualizada: {convidados}')