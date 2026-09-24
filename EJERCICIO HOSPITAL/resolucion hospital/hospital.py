from functools import reduce

from atencion import Atencion, AtencionMedica
from utilities import Validador

# Exports
__all__ = ["Hospital"]


class Hospital:
    def __init__(self, razonSocial: str):
        self._razonSocial = Validador.esCadenaNoVacia(razonSocial)
        self._atencionesRealizadas: list[Atencion] = []

    @property
    def razonSocial(self) -> str:
        return self._razonSocial

    @razonSocial.setter
    def razonSocial(self, razonSocial: str) -> None:
        self._razonSocial = Validador.esCadenaNoVacia(razonSocial)

    @property
    def atencionesRealizadas(self) -> list[Atencion]:
        return self._atencionesRealizadas

    @atencionesRealizadas.setter
    def atencionesRealizadas(self, atencionesRealizadas: list) -> None:
        if not isinstance(atencionesRealizadas, list) or not all(
            isinstance(atencion, Atencion) for atencion in atencionesRealizadas
        ):
            raise ValueError("Error debe ser una lista de atenciones")
        self._atencionesRealizadas = atencionesRealizadas

    def addAtencion(self, atencion: Atencion) -> None:
        if not isinstance(atencion, Atencion):
            raise ValueError("Error el valor ingresado no corresponde a una atencion")
        self._atencionesRealizadas.append(atencion)

    def atencionesMedicas(self) -> list[AtencionMedica]:
        return list(
            filter(
                lambda atencion: isinstance(atencion, AtencionMedica),
                self.atencionesRealizadas,
            )
        )

    def importe_total_atencion_consulta(self) -> float:
        """Suma de los importes de las consultas de las atenciones medicas."""
        return reduce(
            lambda acumulador, atencion: acumulador + atencion.importe,
            self.atencionesMedicas(),
            0.0,
        )

    def importe_promedio_atenciones(self, minimo: float, maximo: float) -> float:
        """Promedio de los importes a cobrar de las atenciones medicas cuyo
        importe a cobrar se encuentra entre minimo y maximo."""
        minimo = Validador.esFlotantePositivo(minimo)
        maximo = Validador.esFlotantePositivo(maximo)

        importes = list(
            map(
                lambda atencion: atencion.importeACobrar(),
                filter(
                    lambda atencion: minimo <= atencion.importeACobrar() <= maximo,
                    self.atencionesMedicas(),
                ),
            )
        )
        return sum(importes) / len(importes) if importes else 0.0

    def codigo_primera_atencion_habitual(self) -> int:
        """Codigo de la primera atencion medica de un paciente habitual, o 0."""
        for atencion in self.atencionesMedicas():
            if atencion.esPacienteHabitual():
                return atencion.codigo
        return 0

    def __str__(self) -> str:
        cadena = f"Hospital - Razon Social: {self.razonSocial}\n"
        for atencion in self.atencionesRealizadas:
            cadena += f"  {atencion}\n"
        return cadena


if __name__ == "__main__":
    pass
