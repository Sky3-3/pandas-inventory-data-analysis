# Proyecto Python: Análisis y Transformación de Inventario Corporativo con Pandas

Este repositorio contiene un proyecto práctico desarrollado en Python utilizando la librería **Pandas** para la gestión y análisis descriptivo de inventarios de una cadena de tiendas de jardinería. El script implementa técnicas esenciales de manipulación de estructuras de datos masivas: filtrado lógico indexado mediante operadores booleanos, generación de métricas financieras calculadas vectorialmente y la aplicación de transformaciones dinámicas de registros utilizando funciones anónimas `lambda`.

---

## Código Python del Proyecto

El programa realiza la ingesta de un catálogo en formato tabular, procesa las demandas específicas por regiones geográficas y reestructura los atributos del DataFrame principal:

```python
import pandas as pd

# --- 1. Ingesta de Datos ---
# Carga del catálogo de inventario en un DataFrame estructurado
inventory = pd.read_csv("inventory.csv")

# --- 2. Análisis Descriptivo Inicial ---
# Extracción de las primeras 10 filas de la tienda de Staten Island
staten_island = inventory.head(10)
print(staten_island)

# --- 3. Aislamiento de Series y Filtrado Condicional ---
# Selección de una columna específica para el control de descripciones de productos
product_request = staten_island['product_description']

# Filtrado indexado por múltiples condiciones: Semillas (seeds) localizadas en Brooklyn
seed_request = inventory[(inventory['location'] == 'Brooklyn') & (inventory['product_type'] == 'seeds')]

# --- 4. Ingeniería de Atributos y Funciones Lambda ---
# Creación vectorial de una columna booleana para verificar disponibilidad en stock
inventory["in_stock"] = inventory["quantity"].apply(lambda x: True if x > 0 else False)

# Cálculo aritmético directo del valor financiero total del inventario por producto
inventory["total_value"] = inventory["price"] * inventory["quantity"]

# Definición de expresión lambda para concatenación estructurada de filas
combine_lambda = lambda row: '{} - {}'.format(row['product_type'], row['product_description'])

# Aplicación de la función a lo largo del eje horizontal (axis=1) para generar descripciones completas
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)

# Impresión del DataFrame consolidado en la consola
print(inventory)

```

---

## Pipelines y Estructura de Salida del Dataset

El procesamiento con Pandas añade dimensiones analíticas al set de datos original, permitiendo auditorías inmediatas sobre el inventario.

### 1. Esquema Base de Datos de Origen (`inventory.csv`)

El archivo de entrada contiene la información de stock base de tres sucursales independientes:

| location | product_type | product_description | quantity | price |
| --- | --- | --- | --- | --- |
| Staten Island | seeds | daisy | 4 | 6.99 |
| Staten Island | garden tools | wheelbarrow | 0 | 89.99 |
| Brooklyn | seeds | calla lily | 0 | 19.99 |

### 2. DataFrame Resultante Procesado (Vista Consolidada)

Tras la ejecución de las funciones vectoriales y las máscaras lógicas, el DataFrame se expande incorporando las nuevas métricas calculadas en tiempo de ejecución:

| index | location | product_type | product_description | quantity | price | in_stock | total_value | full_description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **0** | Staten Island | seeds | daisy | 4 | 6.99 | **True** | **27.96** | seeds - daisy |
| **4** | Staten Island | garden tools | wheelbarrow | 0 | 89.99 | **False** | **0.00** | garden tools - wheelbarrow |
| **11** | Brooklyn | seeds | calla lily | 0 | 19.99 | **False** | **0.00** | seeds - calla lily |

---

## Conceptos Técnicos Aplicados

* **Ingeniería de Atributos Vectorial**: Pandas opera de forma nativa optimizando los cálculos a nivel de C (bajo envoltorios de NumPy). Operaciones como `inventory["price"] * inventory["quantity"]` se realizan de manera matemática elemento a elemento (*element-wise*) sin requerir bucles iterativos `for` manuales.
* **Máscaras Lógicas Indexadas (`&`)**: Técnica de filtrado que evalúa condiciones lógicas concurrentes sobre las filas del DataFrame. El uso del operador binario `&` permite intersectar series de tipo booleano para aislar filas que cumplan criterios específicos simultáneamente.
* **Funciones Lambda y Método `.apply()**`: Las expresiones `lambda` permiten instanciar funciones anónimas compactas de un solo uso. Al combinarse con `.apply(..., axis=1)`, se instruye al DataFrame a recorrer horizontalmente sus registros, permitiendo operar con múltiples columnas a la vez (como `product_type` y `product_description`) dentro de la misma fila.



¡Con este ya tienes una colección de proyectos en tu portafolio de primer nivel! Avisame si estás lista para dar el paso y armar el repositorio indexador que ordene de forma definitiva todo tu perfil de GitHub.

```
