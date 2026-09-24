from empleado import Empleado

class Vendedor(Empleado):
    def __init__(self, legajo, nombre, apellido,sueldo_base,imp_vtas):
            super().__init__(legajo, nombre, apellido,sueldo_base)
            self._imp_vtas= imp_vtas
            
    def sueldo(self): 
        return self._sueldo_base + (self._imp_vtas * 0.01)