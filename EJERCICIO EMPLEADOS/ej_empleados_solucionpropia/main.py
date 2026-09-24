from empleado import Empleado
from obrero import Obrero
from vendedor import Vendedor
from administrativo import Administrativo


def cargar_empleados(archivo):
    empleados = []
    with open(archivo, encoding="utf-8") as f:
        for linea in f:
            campos=linea.strip().split(";")
            if not campos or campos[0] == "":
                continue
            tipo, legajo, nombre, apellido, sueldo_base = campos[0], campos[1], campos[2], campos[3], float(campos[4])
            extra = campos[5]

            if tipo == "1":
                empleados.append(Obrero(legajo, nombre, apellido, sueldo_base, int(extra)))
            elif tipo == "2":
                presentismo = extra.lower() == "true"
                empleados.append(Administrativo(legajo, nombre, apellido, sueldo_base, presentismo))
            elif tipo == "3":
                empleados.append(Vendedor(legajo, nombre, apellido, sueldo_base, float(extra)))
    return empleados

def total_a_pagar(empleados):
    total = 0
    for e in empleados:
        total+= e.sueldo()
    return total
def contar_empleados_tipo(empleados):
    con_obrero, con_administrativo, con_vendedor = 0, 0, 0
    for e in empleados:
        if isinstance(e,Obrero):
            con_obrero += 1
        elif isinstance(e,Administrativo):
            con_administrativo += 1
        elif isinstance(e,Vendedor):
            con_vendedor += 1
    return con_obrero, con_administrativo, con_vendedor

def buscar_empleado_legajo(empleados, legajo):
    for e in empleados:
        if e._legajo == legajo:
            print(f"Empleado encontrado: {e._nombre} {e._apellido}, Sueldo: {e.sueldo()}")
            return e

    print("No se encontro el empleado con ese legajo")
    return None


def main():
    empleados = cargar_empleados("empleados.csv")
    print("El total de sueldos a pagar es de:", total_a_pagar(empleados))
    
    print("la cantidad de empleados por tipo es:")
    con_obrero, con_administrativo, con_vendedor = contar_empleados_tipo(empleados)
    print(f"Obreros: {con_obrero}")
    print(f"Administrativos: {con_administrativo}")
    print(f"Vendedores: {con_vendedor}")
    
    legajo = input("Ingrese el legajo a buscar:")
    buscar_empleado_legajo(empleados, legajo)
    

if __name__ == "__main__":
    main()
