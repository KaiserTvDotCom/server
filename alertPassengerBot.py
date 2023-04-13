import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import datetime
import time
import telebot

key={
  "type": "service_account",
  "project_id": "gtasos-e45f6",
  "private_key_id": "807e8a7e97f64fffda5a49b1cdbe3b7ae2c1f8dc",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDYTF7qcYXcrioh\nMBFZbYnhMTvs002/UuBRvNHMAxOPW0sHEijBX/iRms4IOBOJLnWYGYGSGPabKd+G\nYGzsXCkdrfqepc7rpzb2zY2lzQijBD3m+qcUsqODkdQ0UOIN5wfnvkZ9wpDurjUZ\nP9bC2lWvs66NTlocGh6W6yQ+VbkDWjCYOzXXwMyJrT0QitYWIpIJmQw48f4UHSUG\nctKWMRzuABFozQX9eWCNwpGih3bDVgqbY9k/w9SKv3UvfOl6goMAED9wHsxOcoJt\nwJZuTZdrUYsPPugDToHiV2LQvGflfYSSRCMz15s4/NFVZ+bpAJAAbSnBqv25WMw2\n14FTv/vhAgMBAAECggEAU1OslzXvw3HnMgziCikcXoBInTZUM9o6J9MNocInpWke\nsNUqlUCjMnjIWbs8r3MSA2wEEiQC0QjjH1IDdFUW0+PD8p1e50Ludkr/ADpKUv7d\n2B+FAYDGZHfoH9VvGLsBvSH85xLvIbxEIXuKAVv6eatHmhFuvnfDhBGHT2pX0bWW\nLKem3uG186Hpy68qVbXNh07rNNzo0ggP6O0eR9DxlWDMKIK6zw+2iZy1Y8SIDYU0\nY0UBmOd0kqkHBwTmKhF6T0AXKTROSMiw9bvr3s6O1SpdGPxKloYl+jDsjM9X77jG\nf39/JWirZ3s4vRb6eoMVZtvJ0/3uL7fp2ucpJyDxNwKBgQDzbWH3JP0BzQqsddTh\n9SRX0AmY3+ukyBV/oM9IGPCgyR/UEH2gTrF2sa8R+/qZPTukyzUjT/xVwDGmHkX5\nQaxqgeM4/98EP1E/2hEdEQf2F7MIa+iN7uc4gINjRvDEio5HCqEPZlf9fvTDIhcQ\nyPzU4DYZ6qzFqlc8Y0QJhR05ywKBgQDjeElg8cwDBLVzXFZY06GnxvfOsAlovDNZ\nMqqsDqBbJX7jh7lg2Sd2lD1TFQb6gzIMns24tfKLEv7UBR0cY/lP0ox0fveWZ4wx\n8EQ0vLJYgwPMHxJ7SfAxFti9uDnRWQ0uL5HFy2bGpMHcmruLicKQg8JETKKlcsi0\nAvVUd7kbgwKBgB6WcQfoGu6eAChZig12i0GJf5s5D9gd2C24XDN4Bsx9WUWBaPe6\ny6vZeeEto3ib7CGx8xRj2ZZA1zxDc5F1gh/EAHRKGpDjD+eRFDNtz21J3xJA1PD4\nww8jft77rAdWTbh5inFv78CHsmPOpc1TJAnvvnyVM26HD/0jkAoOMvTvAoGBAJ3I\nKwX+0udpFb/eVdqpeaFaRzvsKaqnmOqPVYmhX6O5n4mN9I10M4ZyDxOZK00LQeU1\nJjewpXvIglBo96dgxWeUAW8xPuXqD3n4UidOmFsDDdhB2V0BjYVPdqoqpphLL/RQ\ndMoBa9nwILS38803kmkRq+gaTFt9AjCzOJ8NqK2nAoGBAKa2qTpLOy7U23OZSCcu\nrbpgwnXqzcpNAJOVDlVpbALkl98AtlAaE9EfIrcM7Qp2+ZQ2sPmvEXzNKwKSFoT7\nrIzLfhBcdpfNCmDDXZ138lhwlRV3z0TrxbGW1GfptMKBjVuz0Hha1fmTv3j9r7mp\nMNGh994NxicA6BUxYHV1z4wD\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-zowhs@gtasos-e45f6.iam.gserviceaccount.com",
  "client_id": "118003823458500827145",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-zowhs%40gtasos-e45f6.iam.gserviceaccount.com"
}


cred = credentials.Certificate(key)
cnf = {
    "databaseURL": "https://gtasos-e45f6.firebaseio.com",
}
fb = firebase_admin.initialize_app(cred, cnf)

#limitePasajes
limitePasajes=70
#lista de chats
listaChats=['1995718936']

#Lista de empresas
listaEmpresas=['-MpDKWPlPfY3CNSTQgx1','-MUB-3ENmgqhkimA7JXF']

bot = telebot.TeleBot("5757432534:AAFus6QaW9a7IqIIdieAxbLGsVBuCd9z5WQ", parse_mode=None)
maxQuery=72
@bot.message_handler(commands=["last"])

def sendLast(message):

    text = message.text
    # Separar el número de horas del comando
    try:
        hours = text.split()[1]
    except:
        hours=1
    hours=int(hours)
    print('hours:', hours)
    if hours <=0 or hours==None :
          hours=1
          bot.send_message(message.chat.id,'consultando la ultima hora')
    elif hours> maxQuery:
          hours=maxQuery
          bot.send_message(message.chat.id,'maxima consulta ' +str(maxQuery) +' horas')
    
          
    today = datetime.datetime.today()
    # Fecha de inicio a las 12:00 AM


    # Fecha de fin al momento de ejecutar el script
    endPoint = datetime.datetime.now()
    endPoint = int(endPoint.timestamp())
    startPoint = endPoint - hours * 3600

    """
    #Ruta para pasajes
    print('Establezca puntos de inicio y fin. Epoch entero y de diez digitos')
    startPoint=input('epoch de Inicio: ')
    if(len(startPoint)==10 and startPoint.isdigit):
        print('startPoint OK')
    else:
        print('bad startPoint')
        exit()
    endPoint=input('epoch de Fin: ')
    if(len(endPoint)==10 and endPoint.isdigit):
        
        print('endPoint OK')
        if(endPoint<=startPoint):
            print('endPoint menor que startPoint')
            exit()
    else:
        print('bad endPoint')
        exit()
    """

    startPoint=int(startPoint)
    endPoint=int(endPoint)

    errorConteos=False

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


    for empresa in listaEmpresas:
            
            dataVehicles=getVehicles(empresa)
            listaVehiculos=dataVehicles[0]
            nombre=dataVehicles[2]
            print('EMPEZO RUTA: ',nombre)
            for vehiculo,imeis in listaVehiculos.items():
            
                    subidaCounter=0
                    bajadaCounter=0
                    bloqueoCounter=0
                    
                    for imei in imeis:
                            ref = db.reference('/Pasaje/' + str(imei)).order_by_child('epoch').start_at(startPoint).end_at(endPoint)
                            barra1=ref.get()

                            for keys,valores in barra1.items():
                                    for valor,key in valores.items():
                                            if(valor=='type'):
                                                    
                                                    if(key=='Subida'):
                                                            subidaCounter+=1
                                                    if(key=='Bajada'):
                                                            bajadaCounter+=1
                                                    if(key=='Bloqueo'):
                                                            bloqueoCounter+=1
                                    
                    print('Conteos en unidad:',vehiculo)
                    print('Conteo de subidas',subidaCounter)
                    print('Conteo de Bajadas',bajadaCounter)
                    print('Conteo de Bloqueos',bloqueoCounter)

                    if(abs(subidaCounter-bajadaCounter)<limitePasajes):
                            print('Conteos correctos')
                    else:
                            
                            mensajeUnificado = ('\n' +
                            'Conteo de subidas: ' + str(subidaCounter) + '\n' +
                            'Conteo de bajadas: ' + str(bajadaCounter) + '\n' +
                            'Conteo de bloqueos: ' + str(bloqueoCounter) + '\n')
                            bot.send_message(message.chat.id,nombre +'\n' +'conteos incorrectos en Unidad:'+ vehiculo   + mensajeUnificado)
                            errorConteos=True

            print('TERMINO RUTA: ',nombre)

    if not errorConteos:
            bot.send_message(message.chat.id,'Conteos en rutas OK')


@bot.message_handler(commands='ping')
def ping(message):
      bot.send_message(message.chat.id,'pong')

@bot.message_handler(commands='help')
def ping(message):
      bot.send_message(message.chat.id,'escribe /last *numero de horas a consultar* \n escribe /ping para pingear el bot')
      
bot.polling()
    