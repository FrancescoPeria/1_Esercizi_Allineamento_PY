# TIPO PRIMITIVO
s = 'mamma'
def change_stringa(a):
    # a è variabile locale che esiste solo nella funzione
    print('Indirizzo della variabile locale a: ', id(a), ' - valore di a: ', a)
    a = a + 'modifica'
    print('Indirizzo della variabile locale a: ', id(a), ' - valore di a: ', a)

print('Indirizzo di s prima della funzione: ', id(s), ' - valore di a: ', s)
change_stringa(s)
print('Indirizzo di s dopo la funzione: ', id(s), 'valore di a: ', s)
print(' ')

# TIPO NON PRIMITIVO MODIFICA CON APPEND
l = ['mamma', 1, 4.6]
def change_lista(a):
    # a è variabile locale che esiste solo nella funzione
    a.append('modificata')
    print('Indirizzo della variabile locale a: ', id(a), 'valore di a: ', a)

print('Indirizzo di l prima della funzione: ', id(l), ' - valore di l: ', l)
change_lista(l)
print('Indirizzo di l dopo la funzione: ', id(l), ' - valore di l: ', l)
print(' ')

# TIPO NON PRIMITIVO RIASSEGNAMENTO
l = ['mamma', 1, 4.6]
def change_lista(a):
    # a è variabile locale che esiste solo nella funzione
    a = ['nonna', 0, -3.4]
    print('Indirizzo della variabile locale a: ', id(a), 'valore di a: ', a)


print('Indirizzo di l prima della funzione: ', id(l), ' - valore di l: ', l)
change_lista(l)
print('Indirizzo di l dopo la funzione: ', id(l), ' - valore di l: ', l)



def ref_demo(x):
    print("x=", x, "id=", id(x))
    x = 42

L1 = ['A', 1]
print(id(L1))
L1 = L1.append('modifica')
print(L1)
print(id(L1))
L2 = L1
print(id(L2))