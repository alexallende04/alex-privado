from utilities import Validador

# Exports
__all__ = ["Paciente"]


class Paciente:
    # Sintomas del enunciado: 1 corazon, 2 pulmon, 3 otras
    SINTOMAS = {1: "corazon", 2: "pulmon", 3: "otras"}

    def __init__(self, nombre: str, sintoma: int, habitual: bool = False) -> None:
        self._nombre = Validador.esCadenaNoVacia(nombre)
        self._sintoma = self._validarSintoma(sintoma)
        self._habitual = self._validarHabitual(habitual)

    @staticmethod
    def _validarSintoma(sintoma: int) -> int:
        if Validador.esEntero(sintoma) not in Paciente.SINTOMAS:
            raise ValueError("Error el sintoma debe ser 1, 2 o 3")
        return sintoma

    @staticmethod
    def _validarHabitual(habitual: bool) -> bool:
        if not isinstance(habitual, bool):
            raise ValueError("Error habitual debe ser un booleano")
        return habitual

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str) -> None:

        self._nombre = Validador.esCadenaNoVacia(nombre)

    @property
    def sintoma(self) -> int:
        return self._sintoma

    @sintoma.setter
    def sintoma(self, sintoma: int) -> None:
        self._sintoma = self._validarSintoma(sintoma)

    @property
    def habitual(self) -> bool:
        return self._habitual

    @habitual.setter
    def habitual(self, habitual: bool) -> None:
        self._habitual = self._validarHabitual(habitual)

    def __str__(self) -> str:
        return (
            f"Paciente: {self.nombre} - Sintoma: {self.SINTOMAS[self.sintoma]} - "
            f"Habitual: {'si' if self.habitual else 'no'}"
        )


if __name__ == "__main__":
    persona = Paciente("Huenu", 1, True)

    print(persona)
