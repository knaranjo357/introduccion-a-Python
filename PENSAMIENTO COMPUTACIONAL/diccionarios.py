#no tienen orden
#{}
#mutables
#iterables

my_dic={
    'David':35,
    'Erika':22,
    'luis':19,
}

my_dic['David']

my_dic.get('Juan',30) #si no existe nos devuelve 30

my_dic.get('Erika',30) #devuelve 22 por que existe

my_dic['David']=10 #cambiamos el valor de David

my_dic['Pedro']=70 #creamos pedro

del my_dic['Pedro'] #eliminamos pedro


########iterar llaves

for llave in my_dic.keys():
    print(llave)

######iterar valor

for valor in my_dic.values():
    print(valor)

for llave,valor in my_dic.items():
    print(llave, valor)

'David' in my_dic #True
'kk' in my_dic #False

