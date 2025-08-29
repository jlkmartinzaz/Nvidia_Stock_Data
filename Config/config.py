import os

# Directorios de datos
RAW_DATA_PATH = os.path.join("data", "Nvidia.csv")
TRANSFORMED_FILE_PATH = os.path.join("data", "transformed_stock_data.csv")

# Configuración de la base de datos PostgreSQL
# Nota: el password se pedirá al usuario en NvidiaLoad.py
DB_USER = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "nvidia_db"

TABLE_NAME = "nvidia_stock"

