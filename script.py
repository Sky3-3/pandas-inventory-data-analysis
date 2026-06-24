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
