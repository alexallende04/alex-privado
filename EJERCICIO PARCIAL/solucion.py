class Viaje():
    def __init__(self, codigo, conductor, destino, pasajeros, precio_base):
        self.codigo = codigo
        self.conductor = conductor
        self.destino = destino
        self.pasajeros = pasajeros
        self.precio_base = precio_base
    
    def importe_recaudado(self):
        pass




class ViajeUrbano(Viaje):
    
    def importe_recaudado(self):
        return self.pasajeros * self.precio_base
    
class ViajeInterurbano(Viaje):
    
    def importe_recaudado(self):
        return self.pasajeros * self.precio_base * 1.10
    