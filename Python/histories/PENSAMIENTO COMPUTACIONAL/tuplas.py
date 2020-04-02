#son inmutables NO se pueden modificar
#pueden contener cualquier tipo de valor pueden ser mezcladas
#pueden devolver varios valores en una funcion

#my_tuple(1) ----esto es un entero necesita la coma
#my_tuple(1,)----tupla

my_tuple1 = (1, 'dos', True)
my_tuple2 = (2, 'tres',False)
my_tuple2 += my_tuple1 #esta reasignando

print(my_tuple2) #(2, 'tres', False, 1, 'dos', True)


a, b, c =my_tuple1  #a=1 #b='dos' #c=True

def cualquierfuncion(n,m):
    l=n
    k=m
    return(n,m)

x,y=cualquierfuncion(1,2)

print(x,y)

