#permisos para hacer cambios

class CasillaDeVotacion:
    def __init__ (self, identificador, pais):#pais es arreglo con coidades
        self._identificador = identificador
        self._pais = pais
        self._region = None

    @property  #decorador que define que una funcion es una propiedad
    def region(self):
        return self._region

    @region.setter
    def set_region(self, region):#para modificar region
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(f"La region {region} no es valida para {self._pais}")


casilla = CasillaDeVotacion(123, ['Ciudad de Mexico', 'Morelos'])
print(casilla.region)
casilla.set_region = 'Ciudad de Mexico'
print(casilla.region)