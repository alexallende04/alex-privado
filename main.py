from alquileres import Bicicleta,Moto
def cargar_alquileres(archivo):
    alquileres = []
    with open(archivo,encoding="utf-8") as f:
        next(f)
        for l in f:
            campos = l.strip().split("|")
            tipo,codigo,cliente,monto_base,extra = campos
            
            codigo = int(codigo)
            monto_base = float(monto_base.replace(",","."))
            tipo = int(tipo)
        
            if tipo == 1:
                alquileres.append(Bicicleta(codigo,cliente,monto_base,int(extra)))
            elif tipo == 2:
                incluye_casco = extra == "SI"
                alquileres.append(Moto(codigo,cliente,monto_base,incluye_casco))
    return alquileres
        


alquileres = cargar_alquileres("alquileres.csv")
for a in alquileres:
    print(f"{a.codigo} - {a.cliente} - importe a cobrar: {a.importeAcobrar()}")       