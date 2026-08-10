notas=[]
for i in range(5):
    nota = float(input(f'Digite a nota {i+1}: '))
    notas.append(nota)
    notas.sort()
print(f'As notas em ordem crescente são: {notas}')