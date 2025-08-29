import requests 
import pandas as pd 
import numpy as np 
class NvidiaExtract:
 def __init__(self,csv_path):
  self.csv=csv_path
 def querries(self):
  data=pd.read_csv(self.csv)
 def response(self):
  return data.head(5)
=======
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


