class Alquiler:
    def __init__(self,codigo,cliente,monto_base):
        self.codigo = codigo
        self.cliente = cliente
        self.monto_base = monto_base
    
    def importeAcobrar(self):
        pass

class Bicicleta(Alquiler):
    def __init__(self,codigo,cliente,monto_base,horas):
        super().__init__(codigo,cliente,monto_base)
        self.horas = horas
    def importeAcobrar(self):
        return self.monto_base * self.horas
    
class Moto(Alquiler):
    def __init__(self,codigo,cliente,monto_base,incluye_casco):
        super().__init__(codigo,cliente,monto_base)
        self.incluye_casco = incluye_casco
    
    def importeAcobrar(self):
            if self.incluye_casco:
                monto = self.monto_base + 500
                return monto
            else:
                return self.monto_base
                
            