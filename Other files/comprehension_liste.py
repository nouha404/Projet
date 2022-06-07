nombres = [1, 21, 5, 44, 4 , 9, 5, 83, 29, 31, 25, 38]
nombre_pairs = [i  for i in nombres if i % 2 == 0 ] #retorune i dans nombres paire si i % 2 = 0
print(nombre_pairs)

# nombre positif
nombres2 = range(-10, 10)
nombre_positif = [i for i in nombres2 if i > 0]
print(nombre_positif)


#double du tableau
nombre3 = range(1,101)
double = [i* 2 for i in nombre3]
print(double)

