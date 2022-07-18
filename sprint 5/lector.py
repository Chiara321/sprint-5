import json
import os
import webbrowser

f = open('Reporte.html','w')

html_template = 

path, _ = os.path.split(os.path.abspath(__file__))

with open(path+'/eventos_classic.json') as file:
    data = json.load(file)
    
print(type(data))

for transacciones in data["transacciones"]:
    print('')
    print('Estado: ', transacciones["estado"])
    print('Tipo: ', transacciones["tipo"])
    print('Número de cuenta : ', transacciones["cuentaNumero"])
    print('Cupo diario restante: ', transacciones["cupoDiarioRestante"])
    print('Monto: ', transacciones["monto"])
    print('Fecha: ', transacciones["fecha"])
    print('Numero de transacción: ', transacciones["numero"])
    print('Saldo: ', transacciones["saldoEnCuenta"])
    print('Tarjetas de crédito: ', transacciones["totalTarjetasDeCreditoActualmente"])
    print('Chequeras: ', transacciones["totalChequerasActualmente"])
    print('')
    
f.write(html_template)
f.close()

webbrowser.open_new_tab('Reporte.html')
    