#Ultima modificacion 21/06/22
#Codigo utilizado para calcular la huella de carbono de la lap.
#Realizado por Abraham Ortiz Castro, Jesús Alejandro Gómez Bautista
# Ulises Hernández Hernández, Alan Iván Flores Juárez

#Se importan las librerias.
import pyrebase
import psutil
import wmi
import time

# Se inicializan variables para calcular promedio de la huella de carbono.
cont = 0
promedioHC = 0
suma = 0

#Se pone la información de la base de datos
config = {
  "apiKey": "AIzaSyBbuUlvoFJ3S6HQrB7NT3GtvKE4IRBcdkw",
  "authDomain": "carbon-footprint-856d0.firebaseapp.com",
  "databaseURL": "https://carbon-footprint-856d0-default-rtdb.firebaseio.com",
  "projectId": "carbon-footprint-856d0",
  "storageBucket": "carbon-footprint-856d0.appspot.com",
  "messagingSenderId": "558213562155",
  "appId": "1:558213562155:web:05da045a6cd89d78d14f6e",
  "measurementId": "G-0GHHHQ93Y4"
}

#crea la autenticacioon
firebase = pyrebase.initialize_app(config)
#se accesa a la base de datos en Firebase
db = firebase.database()
factor_emision = {}


#Función para obtener la energía de la laptop que consume en Wats
def obtener_consumo_energia_laptop():
    try:
        # Crear una instancia de la clase WMI para acceder a la información del sistema
        w = wmi.WMI(namespace="root\\WMI")

        # Obtener el consumo de energía en vatios
        power_info = w.ExecQuery("SELECT * FROM BatteryStatus")[0]
        #Se convierte a W
        consumo_energia = power_info.DischargeRate / 1000

        return consumo_energia

    except:
        pass

    return -1  # No se pudo obtener el consumo de energía

# Función que calcula la huella de carbono
# Parametro el consumo de energía y el factor de emisión
# Regresa la huella de carbono
def calcular_huella_carbono(consumo_energia, factor_emision):
    # Calcula la huella de carbono de la laptop
    huella_carbono = consumo_energia * factor_emision
    return huella_carbono


#Se modifican las variables que nos sean las de la laptop
#Tiene como parametro el factor de emision
def modificar_datos(factor):

    #Se inicia con la lectura de datos
    all_users = db.child("T-Systems").get()
    #Se checan todos los usuarios de la base de datos
    for users in all_users.each():
        # Guarda el valor de numero en una variable
        if (users.key() == "W_Aire"):
            #Se suma el voltaje para calcular la huella de carbono
            suma_carbono = users.val()
            # Calcula la huella de carbono
            huella_carbono = round(calcular_huella_carbono(users.val(), factor), 2)
            # Imprime el resultado
            db.child("T-Systems").update({"H_Aire": huella_carbono})


        elif (users.key() == "W_Focos"):
            #Se suma el voltaje para calcular la huella de carbono
            suma_carbono += users.val()
            # Calcula la huella de carbono
            huella_carbono = round(calcular_huella_carbono(users.val(), factor), 2)
            # Imprime el resultado
            db.child("T-Systems").update({"H_Focos": huella_carbono})

        elif (users.key() == "W_Laptop"):
            #Se suma el voltaje para calcular la huella de carbono
            suma_carbono += users.val()
            # Calcula la huella de carbono
            huella_carbono = round(calcular_huella_carbono(users.val(), factor), 2)
            # Imprime el resultado
            db.child("T-Systems").update({"H_Laptop": huella_carbono})

        elif (users.key() == "W_Microondas"):
            #Se suma el voltaje para calcular la huella de carbono
            suma_carbono += users.val()
            # Calcula la huella de carbono
            huella_carbono = round(calcular_huella_carbono(users.val(), factor), 2)
            # Imprime el resultado
            db.child("T-Systems").update({"H_Micro": huella_carbono})

        elif (users.key() == "W_Refri"):
            #Se suma el voltaje para calcular la huella de carbono
            suma_carbono += users.val()
            # Calcula la huella de carbono
            huella_carbono = round(calcular_huella_carbono(users.val(), factor), 2)
            # Imprime el resultado
            db.child("T-Systems").update({"H_Refri": huella_carbono})

        elif (users.key() == "W_Tv"):
            #Se suma el voltaje para calcular la huella de carbono
            suma_carbono += users.val()
            # Calcula la huella de carbono
            huella_carbono = round(calcular_huella_carbono(users.val(), factor), 2)
            # Imprime el resultado
            db.child("T-Systems").update({"H_Tv": huella_carbono})

    return suma_carbono


def main():
    global promedioHC , cont, suma
    # Datos de consumo de energía de la laptop (en kilovatios)
    consumo_energia_laptop = round(obtener_consumo_energia_laptop(),2)
    db.child("T-Systems").update({"W_Laptop": consumo_energia_laptop})

    # Factor de emisión de carbono (en kgCO2e/kWh)
    factor_emision = 0.435  # Reemplaza con el factor de emisión de tu fuente de energía
    #Se coloca en la base de datos
    db.child("T-Systems").update({"FactorEmision": factor_emision})

    sumaEnergia = modificar_datos(factor_emision)

    # Calcula la huella de carbono de la laptop
    huella_carbono_laptop = round(calcular_huella_carbono(consumo_energia_laptop, factor_emision),2)

    #Se coloca en la base de datos
    db.child("T-Systems").update({"H_Laptop": huella_carbono_laptop})

    #Suma de la huella de carbono
    total = round((huella_carbono_laptop + sumaEnergia) , 2 )
    #Se coloca en la base de datos
    db.child("T-Systems").update({"TotalHC": total})

    # Promedio huella de carbono (se espera que se inicialize el programa cada cierto tiempo)
    if promedioHC == 0:
        suma = total
        promedioHC = total
        cont = 1

    else:
        cont += 1
        #Se saca el promedio de todos los valores
        suma = suma + total
        promedioHC = round(suma/cont , 2)

    #Se coloca en la base de datos
    db.child("T-Systems").update({"PromedioHC": promedioHC})

    #Se declara el tipo de usuario y se sube en la base de datos
    if promedioHC < 60:
        db.child("T-Systems").update({"TipodeUsuario": "Bajo"})
    elif promedioHC < 70:
        db.child("T-Systems").update({"TipodeUsuario": "Medio"})
    else:
        db.child("T-Systems").update({"TipodeUsuario": "Alto"})

#Se core main

if __name__ == '__main__':

    while(1):
        main()
        time.sleep(3)
