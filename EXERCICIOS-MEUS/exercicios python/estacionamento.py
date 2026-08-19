horas_ficadas=float(input('digite quantas horas voce ficou fora: '))

if horas_ficadas <= 1:
    valor=6
else:
    horas_extras=horas_ficadas - 1
    valor=6 + (3+horas_extras)

if valor >= 40:
    valor=40

print(f'o total a pagar sera {valor:.2f}')