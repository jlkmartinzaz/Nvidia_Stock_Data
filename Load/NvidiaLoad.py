import pandas as pd
from sqlalchemy import create_engine
from Config.config import DB_USER, DB_HOST, DB_PORT, DB_NAME, TABLE_NAME, TRANSFORMED_FILE_PATH
import getpass

def load_data():
    print("Introduce la contraseña de la base de datos: ")
    password = getpass.getpass()

    DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    print(" Cargando datos a PostgreSQL...")
    df = pd.read_csv(TRANSFORMED_FILE_PATH)

    engine = create_engine(DATABASE_URL)
    df.to_sql(TABLE_NAME, engine, if_exists="replace", index=False)

    print(f" Datos cargados en la tabla {TABLE_NAME}")

if __name__ == "__main__":
    load_data()

