from empleado import Empleado

class Administrativo(Empleado):
    def __init__(self, legajo, nombre, apellido,sueldo_base,presentismo):
        super().__init__(legajo,nombre,apellido,sueldo_base)
        self._presentismo = presentismo
    
    def sueldo(self):
        if self._presentismo == True:
            sueldo_neto = self._sueldo_base + (self._sueldo_base * 0.13)
        else:
            sueldo_neto = self._sueldo_base
        
        return sueldo_neto