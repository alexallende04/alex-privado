import pytest
from solucion import Viaje,ViajeUrbano,ViajeInterurbano
def test_urbano():
 x=ViajeUrbano(1,"Ana","Cordoba",10,2000); assert isinstance(x,Viaje); assert x.importe_recaudado()==pytest.approx(20000)
def test_interurbano():
 x=ViajeInterurbano(2,"Juan","Alta Gracia",10,2000); assert isinstance(x,Viaje); assert x.importe_recaudado()==pytest.approx(22000)
