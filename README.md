# Procesador de Transacciones Financieras

Este proyecto tiene como objetivo procesar un archivo CSV que contiene transacciones financieras para calcular el balance final, identificar las transacciones de mayor monto y contar el número de transacciones de crédito y débito. Es una herramienta útil para analizar datos financieros de manera rápida y precisa.

## Instrucciones de Ejecución

Asegúrate de tener instalado Python 3.x en tu sistema. Además, este proyecto depende de la biblioteca `pandas`. Para instalar las dependencias necesarias, ejecuta el siguiente comando:

`pip install -r requirements.txt`

## Ejecución del Programa

Para ejecutar el programa, utiliza el siguiente comando en la terminal:

`python app.py`

Donde es la ruta al archivo CSV que deseas procesar. Por ejemplo:

`python app.py data.csv`

**Nota:** Se ha proporcionado un archivo de ejemplo llamado `data.csv` que puedes usar para probar el programa. Este archivo contiene datos de transacciones ficticias con las columnas `id`, `tipo` y `monto`.  
  
Si deseas usar un archivo propio o diferente, asegúrate de que esté incluido en la carpeta del proyecto.

## Enfoque y Solución

### Lógica Implementada: Validación de Entrada

El programa verifica que se haya proporcionado un archivo CSV como argumento. Si el archivo no existe o no contiene las columnas requeridas (`id`, `tipo`, `monto`), se muestra un mensaje de error y el programa termina.

### Cálculo del Balance Final

Se recorre cada transacción del archivo CSV:

*   Si el tipo de transacción es `Crédito`, se suma el monto al balance final.
*   Si el tipo de transacción es `Débito`, se resta el monto del balance final.

### Identificación de Transacciones de Mayor Monto

Se calcula el valor máximo de las transacciones. Luego, se identifican todas las transacciones que coinciden con este valor máximo y se registran sus IDs.

### Conteo de Transacciones

Se cuenta cuántas transacciones son de tipo `Crédito` y cuántas son de tipo `Débito`.

### Salida del Programa

El programa genera un reporte con:

*   El balance final.
*   Las transacciones de mayor monto.
*   El conteo de transacciones por tipo.

## Estructura del Proyecto

*   `app.py`: Script principal que procesa el archivo CSV.
*   `data.csv`: Archivo CSV de ejemplo para pruebas.
*   `requirements.txt`: Lista de dependencias necesarias (`pandas`).
*   `README.md`: Documentación del proyecto.