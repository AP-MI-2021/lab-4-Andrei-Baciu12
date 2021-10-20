def main():
    stop = False
    while not stop:
        print("""
            1 -> Citeste lista
            2 -> Afiseaza parte intreaga a tuturor numerelelor din lista
            3 ->  Afiseaza numerele care apartin unui interval dat
            4 -> Afisarea tuturor numerelelor a carui parte fractionara este divizor al partii intregi
            5 -> Afisarea listei cu proprietatea 5
            x -> Exit
        """)
        optiune = input("Alegeti optiunea: ")
        if optiune == '1':
            lista = citeste_lista()
            print(lista)
        elif optiune == 'x':
            stop = True
        elif optiune == '2':
            lista_intregi = gaseste_intreg(lista)
            print(lista_intregi)
        elif optiune == '3':
            n1 = float(input("dati un element: "))
            n2 = float(input("dati un element mai mare ca n1: "))
            lista = citeste_lista()
            lista3 = gaseste_numere_care_apartin_intrevalului(lista, n1, n2)
            print(lista3)
        elif optiune == '4':
            lista4 = gaseste_numere_care_au_parte_intreaga_divizor_al_partii_zecimale(lista)
            print(lista4)

def citeste_lista():
    """
    Functia citeste niste numere introduse si afisa o lista cu acele numere
    :return: o lista
    """
    result_list = []
    string_lista = input("Dati lista: ")
    string_elemente = string_lista.split(sep=" ")
    for string_element in string_elemente:
        element = float(string_element)
        result_list.append(element)
    return result_list





def extract_fractionar(numar):
    return str(numar).split('.')[1]

def gaseste_numere_care_apartin_intrevalului(lista, n1, n2):
    """
    Functia gaseste numere care se afla intre doua numere date de la tastatura
    :param lista: o lista de numere reale
    :param n1: un numar dat, mai mic ca n2
    :param n2: un numar dat,  mai mare ca n1
    :return: lista de numere care se afla intre n1 si n2
    """
    result_list = []
    for element in lista:
        if element > n1 and element < n2:
            result_list.append(element)
    return result_list
def test_gaseste_numere_care_apartin_intrevalului():
    assert gaseste_numere_care_apartin_intrevalului([1, 2, 3, 4, 5], 2, 6) == [3, 4, 5]
test_gaseste_numere_care_apartin_intrevalului()

def gaseste_intreg(lista):
    """
    Functia gaseste partea intrega a numerelor din lista
    :param lista: o lista de float uri
    :return: lista cu numere intregi
    """
    res = []
    for c in lista:
        i, d = divmod(c, 1)
        res.append(i)
    return res
def test_gaseste_intregi():
    assert gaseste_intreg([2, 3, 4, 5, 53]) == [2, 3, 4, 5, 53]
    assert gaseste_intreg([1, 2, 3, 45]) == [1, 2, 3, 45]

test_gaseste_intregi()
def gaseste_numere_care_au_parte_intreaga_divizor_al_partii_zecimale(lista):
    list = []
    for b in lista:
        i,d = divmod(b, 1)
        if d % i == 0:
            list.append(b)
    return list


main()
