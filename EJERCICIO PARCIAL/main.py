from solucion import Viaje,ViajeInterurbano,ViajeUrbano

def leerViajes(archivo):
    viajes = []
    with open(archivo,encoding="utf-8") as f:
        next(f)
        for linea in f:
            cadenas = linea.strip().split(",")
            tipo, codigo, conductor, destino, pasajeros, precio_base = cadenas

            codigo = int(codigo)
            pasajeros = int(pasajeros)
            precio_base = float(precio_base)
            
            if tipo == "1":
                viajes.append(ViajeUrbano(codigo, conductor, destino, pasajeros, precio_base))

            elif tipo == "2":
                viajes.append(ViajeInterurbano(codigo, conductor, destino, pasajeros, precio_base))
        
    return viajes

def main():
    viajes = leerViajes("viajes.csv")
    
    #---------------------------punto 1 -----------------------------------
    for v in viajes:
        print(f"Viaje:  {v.codigo} | Destino: {v.destino} | Importe: {v.importe_recaudado():.2f}" )
    
    #---------------------------punto 2 -----------------------------------
    recaudacion_total = sum(f.importe_recaudado() for f in viajes)
        
    print(f"La recaudacion total es: {(recaudacion_total):.2f}")
    
    #--------------------------punto 3 ------------------------------------
    pasajeros_por_destino = {}
    for v in viajes:
        if v.destino in pasajeros_por_destino:
            pasajeros_por_destino[v.destino] = pasajeros_por_destino[v.destino] + v.pasajeros
        else:
            pasajeros_por_destino[v.destino] = v.pasajeros
    print (pasajeros_por_destino)
    #--------------------------punto 4 ------------------------------------
    v_max = viajes[0]
    for f in viajes:
        if f.pasajeros > v_max.pasajeros:
            v_max = f
    print(f"El viaje con mayor cartidad de pasajeros es: {v_max.codigo} | {v_max.destino} | {v_max.pasajeros}")
           
            
if __name__ == "__main__":
    main()
