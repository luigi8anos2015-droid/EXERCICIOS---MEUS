pedido1 = input('pedidos feitos (separados por vírgulas): ').split(",")

print(f'pedidos feitos {pedido1}')
retirar = input('que item deseja retirar da sua lista? : ')
if retirar in pedido1:
    pedido1.remove(retirar)
    print(f'pedidos atualizados: {pedido1}')
else:
    print('Item não encontrado na lista.')
