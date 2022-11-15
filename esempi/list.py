def sum_list(lista):
    risultato = 0;
    for item in lista:
        risultato = risultato + item
    return risultato


lista = [1,2,3,4,5,6]
stampa = sum_list(lista)
print('somma: {}'.format(stampa))