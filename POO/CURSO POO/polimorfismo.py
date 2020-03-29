#la habilidad de tomar varias formas
#cambiar el comportamiento de una superclase para adaptarlo
#solo es definir el cambio en las clases

class Persona:
    def __init__(self,nombre):
        self.nombre=nombre

    def avanza(self):
        print('Ando caminando')

class Ciclista(Persona):
    def __init__(self,nombre):
        super().__init__(nombre)

    def avanza(self):#tiene que tener los mismos parametros
        print('Ando moviendome en mi bicicleta')


def main():
    persona= Persona('David')
    persona.avanza()

    ciclista=Ciclista('Luis')
    ciclista.avanza()

if __name__== '__main__': #si el archivo se ejecuta desde la terminal
    main()
