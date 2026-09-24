# Imports
from abc import ABC, abstractmethod

from paciente import Paciente
from utilities import Validador

# Exports
__all__ = ["Atencion", "AtencionMedica", "AtencionFarmacia"]


class Atencion(ABC):
    # Tipos de cobro del enunciado: 1 efectivo, 2 tarjeta de credito
    TIPOS_DE_COBRO = {1: "efectivo", 2: "tarjeta de credito"}

    def __init__(self, codigo: int, tipoDeCobro: int) -> None:
        self._codigo = Validador.esEnteroPositivo(codigo)
        self._tipoDeCobro = self._validarTipoDeCobro(tipoDeCobro)

    @staticmethod
    def _validarTipoDeCobro(tipoDeCobro: int) -> int:
        if Validador.esEntero(tipoDeCobro) not in Atencion.TIPOS_DE_COBRO:
            raise ValueError("Error el tipo de cobro debe ser 1 o 2")
        return tipoDeCobro

    @property
    def codigo(self) -> int:
        return self._codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self._codigo = Validador.esEnteroPositivo(codigo)

    @property
    def tipoDeCobro(self) -> int:
        return self._tipoDeCobro

    @tipoDeCobro.setter
    def tipoDeCobro(self, tipoDeCobro: int) -> None:
        self._tipoDeCobro = self._validarTipoDeCobro(tipoDeCobro)

    @abstractmethod
    def importeACobrar(self) -> float:
        pass

    def __str__(self) -> str:
        return (
            f"Atencion {self.codigo} - "
            f"Cobro: {self.TIPOS_DE_COBRO[self.tipoDeCobro]} - "
            f"Importe a cobrar: ${self.importeACobrar():.2f}"
        )


class AtencionMedica(Atencion):
    def __init__(
        self, codigo: int, tipoDeCobro: int, paciente: Paciente, importe: float
    ) -> None:
        super().__init__(codigo, tipoDeCobro)
        self._paciente = self._validarPaciente(paciente)
        self._importe = Validador.esFlotantePositivo(importe)

    @staticmethod
    def _validarPaciente(paciente: Paciente) -> Paciente:
        if not isinstance(paciente, Paciente):
            raise ValueError("Error el valor ingresado no corresponde a un paciente")
        return paciente

    @property
    def paciente(self) -> Paciente:
        return self._paciente

    @paciente.setter
    def paciente(self, paciente: Paciente):
        self._paciente = self._validarPaciente(paciente)

    @property
    def importe(self) -> float:
        return self._importe

    @importe.setter
    def importe(self, importe: float):
        self._importe = Validador.esFlotantePositivo(importe)

    def importeACobrar(self) -> float:
        valor = self.importe
        if self.paciente.habitual:
            valor = valor * 0.75
        match self.tipoDeCobro:
            case 1:
                valor = valor * 0.9
            case 2:
                valor = valor * 1.2
        return valor

    def esPacienteHabitual(self) -> bool:
        return self.paciente.habitual

    def __str__(self) -> str:
        return (
            f"Atencion Medica {self.codigo} - "
            f"Cobro: {self.TIPOS_DE_COBRO[self.tipoDeCobro]} - "
            f"Consulta: ${self.importe:.2f} - {self.paciente} - "
            f"Importe a cobrar: ${self.importeACobrar():.2f}"
        )


class AtencionFarmacia(Atencion):
    def __init__(
        self,
        codigo: int,
        tipoDeCobro: int,
        importeTotal: float,
        descuento: float,
    ) -> None:
        super().__init__(codigo, tipoDeCobro)
        self._importeTotal = Validador.esFlotantePositivo(importeTotal)
        self._descuento = Validador.esFlotantePositivo(descuento)

    @property
    def importeTotal(self) -> float:
        return self._importeTotal

    @importeTotal.setter
    def importeTotal(self, importeTotal: float) -> None:
        self._importeTotal = Validador.esFlotantePositivo(importeTotal)

    @property
    def descuento(self) -> float:
        return self._descuento

    @descuento.setter
    def descuento(self, descuento: float) -> None:
        self._descuento = Validador.esFlotantePositivo(descuento)

    def importeACobrar(self) -> float:
        # El cupon es un monto fijo a restar; si es 0 no se aplica descuento.
        valor = max(self.importeTotal - self.descuento, 0.0)
        match self.tipoDeCobro:
            case 1:
                valor = valor * 0.95
            case 2:
                valor = valor * 1.3
        return valor

    def __str__(self) -> str:
        return (
            f"Atencion Farmacia {self.codigo} - "
            f"Cobro: {self.TIPOS_DE_COBRO[self.tipoDeCobro]} - "
            f"Medicamentos: ${self.importeTotal:.2f} - Cupon: ${self.descuento:.2f} - "
            f"Importe a cobrar: ${self.importeACobrar():.2f}"
        )


if __name__ == "__main__":
    pass
# print("Hola")
