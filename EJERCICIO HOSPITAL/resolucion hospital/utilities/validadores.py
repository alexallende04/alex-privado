__all__ = ["Validador"]


class Validador:

    @staticmethod
    def esFlotante(numero: float) -> float:
        if isinstance(numero, bool) or not isinstance(numero, (int, float)):
            raise ValueError("Error debe ser un numero flotante")
        return float(numero)

    @staticmethod
    def esEntero(numero: int) -> int:
        if isinstance(numero, bool) or type(numero) != int:
            raise ValueError("Error debe ser un numero entero")
        return numero

    @staticmethod
    def esFlotantePositivo(numero: float) -> float:
        numero = Validador.esFlotante(numero)
        if numero < 0:
            raise ValueError("Error debe ser un numero flotante positivo")
        return numero

    @staticmethod
    def esEnteroPositivo(numero: int) -> int:
        if Validador.esEntero(numero) < 0:
            raise ValueError("Error debe ser un numero entero positivo")
        return numero

    @staticmethod
    def esCadenaNoVacia(cadena: str) -> str:
        if type(cadena) != str or not cadena.strip():
            raise ValueError("Error debe ser una cadena no vacia")
        return cadena.strip()
