# TIPI PRIMITIVI
a = 12
print('Indirizzo dell\'int a in memoria: ', id(a), ' - valore di a: ', a)
b = 12.5
print('Indirizzo del float b in memoria: ', id(b), ' - valore di b: ', b)
c = 'casa'
print('Indirizzo della string in memoria: ', id(c), ' - valore di c: ', c)
print('')

# TIPI PRIMITIVI: PASSAGGIO A VALORE DURANTE ASSEGNAMENTO
a1 = a
print('Indirizzo dell\'int a1 in memoria dopo assegnamento a1 = a: ', id(a1), ' - valore di a1: ', a1)
b1 = b
print('Indirizzo del float b1 in memoria dopo assegnamento b1 = b: ', id(b1), ' - valore di a1: ', b1)
c1 = c
print('Indirizzo della string c1 in memoria dopo assegnamento c1 = c: ', id(c1), ' - valore di a1: ', c1)
print('')

# TIPI PRIMITIVI: MODIFICA DOPO ASSEGNAMENTO
a1 = 1
print('Indirizzo dell\'int a in memoria dopo riassegnamento di a1: ', id(a), ' - valore di a: ', a)
print('Indirizzo dell\'int a1 in memoria dopo riassegnamento di a1: ', id(a1), ' - valore di a1: ', a1)
b1 = 1.5
print('Indirizzo del float b in memoria dopo riassegnamento b1: ', id(b), ' - valore di b: ', b)
print('Indirizzo del float b1 in memoria dopo riassegnamento b1: ', id(b1), ' - valore di b1: ', b1)
c1 = 'mamma'
print('Indirizzo della string c in memoria dopo riassegnamento di c1: ', id(c), ' - valore di c: ', c)
print('Indirizzo della string c1 in memoria dopo riassegnamento di c1: ', id(c1), ' - valore di c1: ', c1)
print('')

# TIPI NON PRIMITIVI - IMMUTABLE
t = (1, 'casa', 1.6)
print('Indirizzo della tupla t: ', id(t), ' - valore di t: ', t)

t1 = t
print('Indirizzo della tupla t1 dopo assegnamento t1 = t: ', id(t1), ' - valore di t1: ', t1)
print('Indirizzo della tupla t dopo assegnamento t1 = t: ', id(t), ' - valore di t: ', t)

t1 = ('mamma', 2, 8.6)
print('Indirizzo della tupla t1 dopo riassegnamento a t1: ', id(t1), ' - valore di t1: ', t1)
print('Indirizzo della tupla t dopo riassegnamento a t1: ', id(t), ' - valore di t: ', t)
print('')

# TIPI NON PRIMITIVI - MUTABLE
l = [1, 'casa', 1.6]
print('Indirizzo della lista l: ', id(l), ' - valore di l: ', l)

l1 = l
l2 = l
print('Indirizzo della lista l1 dopo assegnamento l1 = l: ', id(l1), ' - valore di l1: ', l1)
print('Indirizzo della lista l2 dopo assegnamento l2 = l: ', id(l2), ' - valore di l2: ', l2)
print('Indirizzo della lista l dopo assegnamento l1 = l: ', id(l), ' - valore di l: ', l)
print('Indirizzo della lista l dopo assegnamento l2 = l: ', id(l), ' - valore di l: ', l)

l1 = ['mamma', 2, 8.6]
print('Indirizzo della lista l1 dopo riassegnamento a l1: ', id(l1), ' - valore di l1: ', l1)
print('Indirizzo della lista l dopo riassegnamento a l1: ', id(l),' - valore di l: ', l)
print('Indirizzo della lista l2 dopo riassegnamento a l1: ', id(l2),' - valore di l: ', l2)

l2.append('babbo')
print('Indirizzo della lista l2 dopo modifica a l2: ', id(l2), ' - valore di l2: ', l2)
print('Indirizzo della lista l1 dopo modifica a l2: ', id(l1), ' - valore di l1: ', l1)
print('Indirizzo della lista l dopo modifica a l2: ', id(l), ' - valore di l: ', l)

