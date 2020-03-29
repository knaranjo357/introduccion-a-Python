#es mutable
#tener cuidado por que puede crear bugs

my_list= [1, 2, 3]

my_list[0] # 1
my_list[1:] # [2, 3]

my_list.append(5) #[1, 2, 3, 5]

my_list[0]='a' #['a', 2, 3,5]

my_list.pop() #defec remove last element

for element in my_list:
    print(element)

#a
#2
#3


a=[1,2,3]
b=a

id(a)
id(b)

#asignamos el mismo nombre pero la
#direccion es la misma
#si hago cambios en alguna se aplica en todas


#################################

a=[1,2,3]
b=a

c=list(a) #clono la lista y serian 2 diferentes
d= a[::] #otra forma de clonar

#list comprehension
    #aplica operaciones a los valores de una secuencia
    #tambien se puede filtrar

my_list=list(range(100))
doble = [i*2 for i in my_list] #le aplica a todos


