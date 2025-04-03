import pandas as pd
import sys

#Verificación de que se haya proporcionado un archivo CSV
if len(sys.argv) != 2:
    print("Necesitas proporcionar un archivo CSV")
    sys.exit(1)

#Obtener el nombre del archivo CSV desde los argumentos de la línea de comandos
archivo_csv = sys.argv[1]

#Declaración de Variables
balanceFinal = 0
conteoCredito = 0
conteoDebito = 0

#Lectura del archivo CSV
try:
    data = pd.read_csv(archivo_csv, sep=";")
except FileNotFoundError:
    print(f"El archivo '{archivo_csv}' no fue encontrado.")
    sys.exit(1)

#Extraccion las columas a usar
ids = data.get('id').values
tipos = data.get('tipo').values
transacciones = data.get('monto').values

#Obtención del valor de la mayor transacción
montoMaximo = max(transacciones)
mayoresTransacciones = []  # Lista para almacenar los IDs de las transacciones con el monto máximo en caso tengamos mas de 1

#Bucle para cálculo del balance y conteo de transacciones
for i in range(len(ids)):
    # Determinar si es crédito o débito
    if tipos[i].capitalize() == 'Credito':
        balanceFinal += transacciones[i]
        conteoCredito += 1
    elif tipos[i].capitalize() == "Debito":
        balanceFinal -= transacciones[i]
        conteoDebito += 1

    # Guardar los IDs de las transacciones con el monto máximo
    if transacciones[i] == montoMaximo:
        mayoresTransacciones.append(ids[i])

#Muestra de resultados
print("")
print("Reporte de Transacciones")
print("---------------------------------------------")
print(f"Balance Final: {balanceFinal}")
print(f"Transacción(es) de Mayor Monto: ID {', '.join(map(str, mayoresTransacciones))} - {montoMaximo}")
print(f"Conteo de transacciones: Crédito: {conteoCredito} Débito: {conteoDebito}")
print("")