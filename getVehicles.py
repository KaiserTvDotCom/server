
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from collections import OrderedDict


cred = credentials.Certificate("key.json")
cnf = {
    "databaseURL": "https://gtasos-e45f6.firebaseio.com",
}
fb = firebase_admin.initialize_app(cred, cnf)


vehiculosTotales = db.reference('Empresarial/Vehiculos')
vehiculos = vehiculosTotales.get()


def getVehicles(empresa):

    nombreURL = db.reference('Empresarial/Empresas/' + empresa + '/Data/nombre')
    nombre= nombreURL.get()
    # EmpresaID Periferico -MpDKWPlPfY3CNSTQgx1
    vehicles = db.reference('/Empresarial/Empresas/' + empresa + '/Vehiculos/active')
    activeVehicles = vehicles.get()

    matchingVehicles = {}

    # Iterar a través de las llaves de vehiculos
    for key in vehiculos:
        # Verificar si la llave está en activeVehicles
        if key in activeVehicles:
            # Agregar el valor correspondiente de vehiculos a matchingVehicles
            matchingVehicles[key] = vehiculos[key]

    micros = {}
    lastVehicle = 0
    idVehicles = []
    for vehiculo, items in matchingVehicles.items():
        for item, values in items.items():

            if item == 'data':
                for key, valores in values.items():
                    if key == 'clase':
                        lastVehicle = valores

            if item == 'micro':

                idVehicles.append(vehiculo)
                for actives, imeis in values.items():
                    micros[lastVehicle] = imeis

                lastVehicle = 0

    for key in micros:
        micros[key] = set(filter(lambda x: x != 0, micros[key].keys()))

    return micros, idVehicles,nombre


