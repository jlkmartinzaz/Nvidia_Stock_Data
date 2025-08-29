import pandas as pd
from Config.config import RAW_DATA_PATH, TRANSFORMED_FILE_PATH

def transform_data():
    print("Transformando datos...")
    df = pd.read_csv(RAW_DATA_PATH)

    # Ejemplo de transformaciones:
    df = df.dropna()  # elimina filas con valores nulos
    df["Date"] = pd.to_datetime(df["Date"])  # convierte fechas
    df = df.sort_values("Date")  # ordena por fecha

    df.to_csv(TRANSFORMED_FILE_PATH, index=False)
    print(f"Datos transformados guardados en {TRANSFORMED_FILE_PATH}")

if __name__ == "__main__":
    transform_data()

