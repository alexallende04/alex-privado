"""Carga las atenciones del hospital desde los archivos CSV de data/."""

import csv
from pathlib import Path

from atencion import AtencionFarmacia, AtencionMedica
from hospital import Hospital
from paciente import Paciente

DIRECTORIO_DATOS = Path(__file__).parent / "data"
ARCHIVO_PACIENTES = DIRECTORIO_DATOS / "pacientes.csv"
ARCHIVO_MEDICAS = DIRECTORIO_DATOS / "atenciones_medicas.csv"
ARCHIVO_FARMACIA = DIRECTORIO_DATOS / "atenciones_farmacia.csv"


def leerCsv(ruta: Path) -> list[dict]:
    with open(ruta, newline="", encoding="utf-8") as archivo:
        return list(csv.DictReader(archivo))


def aBooleano(valor: str) -> bool:
    return valor.strip().lower() in ("true", "1", "si", "sí")


def cargarPacientes(ruta: Path = ARCHIVO_PACIENTES) -> dict[int, Paciente]:
    """Devuelve los pacientes indexados por el codigo de la atencion medica
    con la que se realizo la atencion."""
    pacientes: dict[int, Paciente] = {}
    for fila in leerCsv(ruta):
        codigoAtencion = int(fila["codigo_atencion"])
        pacientes[codigoAtencion] = Paciente(
            nombre=fila["nombre"],
            sintoma=int(fila["sintoma"]),
            habitual=aBooleano(fila["habitual"]),
        )
    return pacientes


def cargarAtencionesMedicas(
    pacientes: dict[int, Paciente], ruta: Path = ARCHIVO_MEDICAS
) -> list[AtencionMedica]:
    atenciones = []
    for fila in leerCsv(ruta):
        codigo = int(fila["codigo"])
        paciente = pacientes.get(codigo)
        if paciente is None:
            raise ValueError(f"No hay paciente para la atencion medica {codigo}")
        atenciones.append(
            AtencionMedica(
                codigo=codigo,
                tipoDeCobro=int(fila["tipo_cobro"]),
                paciente=paciente,
                importe=float(fila["importe_consulta"]),
            )
        )
    return atenciones


def cargarAtencionesFarmacia(ruta: Path = ARCHIVO_FARMACIA) -> list[AtencionFarmacia]:
    return [
        AtencionFarmacia(
            codigo=int(fila["codigo"]),
            tipoDeCobro=int(fila["tipo_cobro"]),
            importeTotal=float(fila["importe_total"]),
            descuento=float(fila["cupon_descuento"]),
        )
        for fila in leerCsv(ruta)
    ]


def cargarHospital(razonSocial: str = "Hospital San Roque") -> Hospital:
    hospital = Hospital(razonSocial)
    pacientes = cargarPacientes()

    for atencion in cargarAtencionesMedicas(pacientes):
        hospital.addAtencion(atencion)

    for atencion in cargarAtencionesFarmacia():
        hospital.addAtencion(atencion)

    return hospital


def main() -> None:
    hospital = cargarHospital()
    medicas = hospital.atencionesMedicas()

    print(f"Hospital: {hospital.razonSocial}")
    print(f"Atenciones realizadas: {len(hospital.atencionesRealizadas)}")
    print(f"  Medicas : {len(medicas)}")
    print(f"  Farmacia: {len(hospital.atencionesRealizadas) - len(medicas)}")
    print()

    print(
        "Importe total de las consultas medicas: "
        f"${hospital.importe_total_atencion_consulta():.2f}"
    )

    minimo, maximo = 10000.0, 30000.0
    print(
        f"Importe promedio de atenciones medicas entre ${minimo:.2f} y ${maximo:.2f}: "
        f"${hospital.importe_promedio_atenciones(minimo, maximo):.2f}"
    )

    print(
        "Codigo de la primera atencion de un paciente habitual: "
        f"{hospital.codigo_primera_atencion_habitual()}"
    )
    print()

    print("Detalle de las primeras 5 atenciones de cada tipo:")
    for atencion in medicas[:5]:
        print(f"  {atencion}")
    for atencion in hospital.atencionesRealizadas[-30:][:5]:
        print(f"  {atencion}")


if __name__ == "__main__":
    main()
