import pandas as pd

RAW_DATA_PATH = "data/Nvidia.csv"

def extract_data():
    df = pd.read_csv(RAW_DATA_PATH)
    print("Datos extraídos correctamente")
    return df

