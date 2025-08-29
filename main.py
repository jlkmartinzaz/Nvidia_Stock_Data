<<<<<<< HEAD
from NvidiaExtract import NvidiaExtract

response=NvidiaExtract("csv")
response.querries()
print(response1.response)
=======
from Extract.NvidiaExtract import extract_data
from Transform.NvidiaTransform import transform_data
from Load.NvidiaLoad import load_data

if __name__ == "__main__":
    print(" Iniciando proceso ETL de Nvidia")
    extract_data()
    transform_data()
    load_data()
    print("Proceso ETL finalizado")

>>>>>>> feature/etl-nvidia
