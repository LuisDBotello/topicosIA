from Tienda import Tienda
import requests
import json, random, math
from pathlib import Path

def crearMatrizCostos(tiendas):

    #conseguir costos
    ruta_matriz = Path(__file__).resolve().parent / "matriz_distancias.json"
    if ruta_matriz.exists():
        with open(ruta_matriz, "r", encoding="utf-8") as archivo:
            matriz = json.load(archivo)
    else:
        matriz = llamarAosrm(tiendas)
        with open(ruta_matriz, "w", encoding="utf-8") as archivo:
            json.dump(matriz, archivo, indent=4)    

    #pasar de metros a km
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] is not None:
                matriz[i][j] /= 1000
    
    return matriz

def llamarAosrm(tiendas):
    request = ""
    for tienda in tiendas:
        if(request == ""):
            request = tienda.ubicacion
        else:
            request = request + ";" + tienda.ubicacion

    url = "https://router.project-osrm.org/table/v1/driving/" + request + "?annotations=distance"

    #conseguir el costo entre los puntos registrados 
    matriz = []
    respuesta = requests.get(url, timeout=30)
    if respuesta.status_code == 200:
        datos = respuesta.json()

        if datos["code"] == "Ok":
            matriz = datos["distances"]
        else:
            print("Error de OSRM:", datos["code"])
    else:
        print(respuesta.text)

    return matriz

def generarSolucionInicialSimple(arreglo):
    return arreglo



def swapRandom(arreglo):
    implicados = random.randint(2, len(arreglo)-1)

    inicio = random.randint(1, len(arreglo) - implicados)
    fin = inicio + implicados

    arreglo[inicio:fin] = arreglo[inicio:fin][::-1]

    return arreglo    

def generarVecinoAleatorio(solucionActual):
    solucionCandidata = swapRandom(solucionActual)
    return solucionCandidata


def costo(matriz, solucion):
    total = 0.0
    for i in range(len(solucion) - 1):
        total += matriz[solucion[i].id - 1][solucion[i + 1].id - 1]
    total += matriz[solucion[-1].id - 1][solucion[0].id - 1]  # regreso al origen
    return total
      

def imprimirEdo(solucion):
    estado = " -> ".join(f"{tienda.id}: {tienda.nombre}" for tienda in solucion)
    print(f"Estado actual de la solución: {estado}")
#main

tiendas = list()
tiendas.append(Tienda(1, "Soriana Barrancos",          "-107.42554676939416,24.7478797295238"))
tiendas.append(Tienda(2, "Soriana Hiper Abastos",      "-107.37083831550379,24.771080889546653"))
tiendas.append(Tienda(3, "Soriana La Campiña",         "-107.36491998671882,24.817470202992013"))
tiendas.append(Tienda(4, "Soriana Zapata",             "-107.42373302359326,24.79047876680318"))
tiendas.append(Tienda(5, "Soriana Tres Ríos",          "-107.39780712678498,24.835783370363277"))
tiendas.append(Tienda(6, "Walmart Isla Musala",        "-107.37053648378415,24.826498737354484"))
tiendas.append(Tienda(7, "Walmart Mexico 68",          "-107.39499917843953,24.779229226368944"))
tiendas.append(Tienda(8, "Walmart UAdeO",              "-107.43732890925116,24.812025295138323"))
tiendas.append(Tienda(9, "Walmart Tres Ríos",          "-107.40925294555574,24.815169842144716"))

matrizCostos = crearMatrizCostos(tiendas)

solucionActual = generarSolucionInicialSimple(tiendas)
costoActual = costo(matrizCostos, solucionActual)

T = 10 #un promedio es que el delta empeore la solucion inicial un 20%, por eso 10
temperaturaFinal = 0.01
alpha = 0.96

mejor, costoMejor = solucionActual[:], costoActual
while (T > temperaturaFinal):
    for i in range(10):
        solucionCandidata = generarVecinoAleatorio(solucionActual.copy())
        costoCandidata = costo(matrizCostos, solucionCandidata)
        delta = costoCandidata - costoActual

        if delta < 0 or random.random() < math.exp(-delta / T):
            solucionActual, costoActual = solucionCandidata, costoCandidata
            if costoActual < costoMejor:
                mejor, costoMejor = solucionActual[:], costoActual
    print(costo(matrizCostos, solucionActual))
    T *= alpha

for i in mejor:
    print(i.nombre)
print("Costo")
print(costoMejor)


