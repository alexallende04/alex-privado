from empleado import Empleado

class Obrero(Empleado):
    def __init__(self, legajo, nombre, apellido,sueldo_base,dias):
            super().__init__(legajo, nombre, apellido,sueldo_base)
            self._dias = dias
    
    
    def sueldo(self):
        return self._sueldo_base / 20 * self._dias