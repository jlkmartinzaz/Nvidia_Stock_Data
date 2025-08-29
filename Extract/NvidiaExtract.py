import pandas as pd
from Config.config import RAW_DATA_PATH

def extract_data():
    print(f" Extrayendo datos desde {RAW_DATA_PATH}...")
    df = pd.read_csv(RAW_DATA_PATH)
    print(" Datos extraídos correctamente")
    return df

if __name__ == "__main__":
    df = extract_data()
    print(df.head())

