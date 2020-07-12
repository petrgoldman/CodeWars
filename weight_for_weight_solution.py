def suma(cislo):
    suma = 0
    for i in str(cislo):
        suma += int(i)
    return suma

def order_weight(strng):
    return ' '.join(sorted(sorted(strng.split()), key = suma))