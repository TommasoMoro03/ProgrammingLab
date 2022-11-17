values = []

def sum_csv(file_name):
    somma = 0.0
    my_file = open(file_name, 'r')
    for line in my_file:
        elements = line.split(',')
        if elements[0] != 'Date':
            mese = elements[0]
            valore = float(elements[1])
            somma = somma + valore
    return somma

print('somma: {}'.format(sum_csv('shampoo_sales.csv')))