#Módulos
import requests
import ast
from datetime import datetime

#Obtener fechas
d=datetime.today()
fechayhora = d.strftime("%d/%m/%Y - %I:%M:%S%p")

#Inicializamos la variables
indice_menu = 0
monedas_dict = {}
monedas_aceptadas = ["BTC","ETH","XRP"]
codigos_aceptados = ["11111","22222","33333","44444","55555","66666"]


#Recibir Cantidad
def recibir_cnt():
    moneda_recibir = ""
    while not moneda_recibir in monedas_aceptadas:
        print("")
        moneda_recibir = input("Ingrese el símbolo de la moneda a recibir: ")
    monto_recibir = float(input("Ingrese monto a recibir en $USD: "))
    codigo_remitente = ""
    while not codigo_remitente in codigos_aceptados:
        codigo_remitente = input("Ingrese código de Remitente: ")
    
    #Cargar Balance de Cuenta
    ruta_balance = open("balance_cuenta.txt","r")
    balance_general = ast.literal_eval(ruta_balance.read())
    ruta_balance.close()
    
    #API de Coin Market Cap
    headers = {  'Accepts': 'application/json',  'X-CMC_PRO_API_KEY':  "API_Key"}
    parametros = {'symbol': moneda_recibir}
    data = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest",headers=headers,params=parametros).json()
    cotizacion = data["data"][moneda_recibir]["quote"]["USD"]["price"]
    
    #Cálculos
    balance_actual = balance_general[moneda_recibir]
    balance_actual = round(balance_actual + (monto_recibir/cotizacion),2)
    balance_general[moneda_recibir] = balance_actual
    
    #Guardar Nuevo Balance
    ruta_balance = open("balance_cuenta.txt","w")
    ruta_balance.write(str(balance_general))
    ruta_balance.close()
    
    #Guardar Transacción
    hist_trans = open("historico_transacciones.txt","a")
    hist_trans.write("\n"+fechayhora+" -   "+moneda_recibir+"   -  "+str(monto_recibir)+"  -  "+str(codigo_remitente)+"  -  Crédito")
    hist_trans.close()
    
    #Confirmación
    print("")
    print("Transacción Realizada con Éxito.")
    confirmacion = input("Presione Enter para Continuar...")


#Transferir Monto
def transf_cnt():
    moneda_transfer = ""
    while not moneda_transfer in monedas_aceptadas:
        print("")
        moneda_transfer = input("Ingrese el símbolo de la moneda a transferir: ")
    monto_transfer = float(input("Ingrese monto a transferir en $USD: "))
    codigo_receptor = ""
    while not codigo_receptor in codigos_aceptados:
        codigo_receptor = input("Ingrese Código de Receptor: ")
    
    #Cargar Balance de Cuenta
    ruta_balance = open("balance_cuenta.txt","r")
    balance_general = ast.literal_eval(ruta_balance.read())
    ruta_balance.close()
    
    #API de Coin Market Cap
    headers = {  'Accepts': 'application/json',  'X-CMC_PRO_API_KEY':  "API_Key"}
    parametros = {'symbol': moneda_transfer}
    data = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest",headers=headers,params=parametros).json()
    cotizacion = data["data"][moneda_transfer]["quote"]["USD"]["price"]
    
    #Cálculos
    balance_actual = balance_general[moneda_transfer]
    balance_actual = round(balance_actual - (monto_transfer/cotizacion),2)
    
    if balance_actual < 0:
        print("")
        print("No tiene fondos suficientes para realizar esta transferencia.")
        print("Revise el balance de la cuenta con la opción #3 y vuelva a intentarlo.")
        print("")
    else:
        balance_general[moneda_transfer] = balance_actual
    
    #Guardar Nuevo Balance
        ruta_balance = open("balance_cuenta.txt","w")
        ruta_balance.write(str(balance_general))
        ruta_balance.close()
    
    #Guardar Transacción
        hist_trans = open("historico_transacciones.txt","a")
        hist_trans.write("\n"+fechayhora+" -   "+moneda_transfer+"   -  "+str(monto_transfer)+"  -  "+str(codigo_receptor)+"  -  Débito")
        hist_trans.close()
    
    #Confirmación
        print("")
        print("Transacción Realizada con Éxito.")
        confirmacion = input("Presione Enter para Continuar...")
    
#Balance Moneda
def balance_moneda():
    consultar_moneda = ""
    while not consultar_moneda in monedas_aceptadas:
        print("")
        consultar_moneda = input("Ingrese el símbolo de la moneda que desea consultar: ")
        
#Cargar Balance de Cuenta
    ruta_balance = open("balance_cuenta.txt","r")
    balance_general = ast.literal_eval(ruta_balance.read())
    ruta_balance.close()
    
#API de Coin Market Cap
    headers = {  'Accepts': 'application/json',  'X-CMC_PRO_API_KEY':  "API_Key"}
    parametros = {'symbol': consultar_moneda}
    data = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest",headers=headers,params=parametros).json()
    cotizacion = data["data"][consultar_moneda]["quote"]["USD"]["price"]

#Cálculos
    moneda_balance = balance_general[consultar_moneda]
    moneda_usd = round(moneda_balance*cotizacion,2)
    
#Impresión de Información    
    print("")
    print("El balance de la Moneda",consultar_moneda,"es: ")
    print(moneda_balance)
    print("")
    print("El balance de la Moneda",consultar_moneda,"en $USD es: ")
    print(moneda_usd)
    print("")
    confirmacion = input("Presione Enter para Continuar...")
    print("")
    
    
#Balance General
def balance_general():
#Cargar Balance de Cuenta
    ruta_balance = open("balance_cuenta.txt","r")
    balance_general = ast.literal_eval(ruta_balance.read())
    ruta_balance.close()
    
#API de Coin Market Cap
    headers = {  'Accepts': 'application/json',  'X-CMC_PRO_API_KEY':  "API_Key"}
    parametros = {'symbol': "BTC"}
    data = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest",headers=headers,params=parametros).json()
    cotizacion_btc = float(data["data"]["BTC"]["quote"]["USD"]["price"])
    headers = {  'Accepts': 'application/json',  'X-CMC_PRO_API_KEY':  "API_Key"}
    parametros = {'symbol': "ETH"}
    data = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest",headers=headers,params=parametros).json()
    cotizacion_eth = float(data["data"]["ETH"]["quote"]["USD"]["price"])
    headers = {  'Accepts': 'application/json',  'X-CMC_PRO_API_KEY':  "API_Key"}
    parametros = {'symbol': "XRP"}
    data = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest",headers=headers,params=parametros).json()
    cotizacion_xrp = float(data["data"]["XRP"]["quote"]["USD"]["price"])
    
    #Impresión
    print("")
    print("El balance General de su cuenta es: ")
    print("")
    print("Moneda BTC:",balance_general["BTC"],"  -  $USD:",round(balance_general["BTC"]*cotizacion_btc,2))
    print("")
    print("Moneda ETH:",balance_general["ETH"],"  -  $USD:",round(balance_general["ETH"]*cotizacion_eth,2))
    print("")
    print("Moneda XRP:",balance_general["XRP"],"  -  $USD:",round(balance_general["XRP"]*cotizacion_xrp,2))
    print("")
    print("Su balance total en $USD es de:",round(balance_general["BTC"] * cotizacion_btc + balance_general["ETH"] * cotizacion_eth + balance_general["XRP"] * cotizacion_xrp,2))
    print("")
    confirmacion = input("Presione Enter para Continuar...")
    print("")
    
    
    
#Histórico de Transacciones
def historico_transacciones():
    print("")
    print("Histórico de Transacciones: ")
    print("")
    hist_trans = open("historico_transacciones.txt","r")
    print(hist_trans.read())
    hist_trans.close()
    print("")
    confirmacion = input("Presione Enter para Continuar...")
    print("")
  

#Menú
while indice_menu != "6":
    
    print("")
    print("Seleciones de la siguiente lista, que tarea desea realizar, Ingrese el Número del Menú:")
    print("")
    print("1. Recibir Transferencia")
    print("2. Transferir Criptomoneda")
    print("3. Obtener Balance de una Criptomoneda en USD")
    print("4. Obtener Balance Total de la Cuenta")
    print("5. Revisar Histórico de Transferencia")
    print("6. Salir de Billetera Digital")
    print("")
    indice_menu = input("Que tarea desea realizar? ")
    
    #Selección de Tarea a Realizar
    if indice_menu == "1":
        recibir_cnt()
    elif indice_menu == "2":
        transf_cnt()
    elif indice_menu == "3":
        balance_moneda()
    elif indice_menu == "4":
        balance_general()
    elif indice_menu == "5":
        historico_transacciones()
    elif indice_menu == "6":
        print("")
        print("Gracias por usar su Billetera Digital")
        print("")
    else:
        print("")
        print("Número de Menú Incorrecto, Inténtelo Nuevamente...")
            
    
    

    


