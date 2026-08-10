produtos=['arroz','feijao','macarrao']

item=input('digite um item e caso ele nao esteja na lista irei te informar: ')
if item in produtos:
    print('o item esta na lista, nao se preocupe')
else:
    print(f'o item {item} nao esta na lista, deve ser comprado')

print(produtos)
