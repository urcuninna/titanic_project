'''Este módulo contiene la función cargar_raw que se encarga de cargar un archivo CSV desde la carpeta `data/raw` y devolverlo como un DataFrame de pandas.'''

import pandas as pd
from pathlib import Path


def cargar_raw (filename: str) -> pd.DataFrame: 

    ruta_proyecto= Path(__file__).resolve().parents[2]
    ruta_datos = ruta_proyecto / "data" / "raw" / filename

    df = pd.read_csv(ruta_datos)

    return df

'''Filename = titaninc_dataset.csv; con str se indica que la entrada es una cadena de texto, mientras con pd.DataFrame se indica que la función devuelve un DataFrame de pandas.
_file_= titanic_project/src/data/load_data.py; Path lo convierte en un objeto tipo ruta, y resolve lo convierte en una ruta absoluta; parents[2] sube dos niveles en la jerarquía de carpetas hasta llegar a la raiz y asi se obtiene la ruta de este archivo load_data.py.
finalmente se construye la ruta completa del archivo csv usando el operador/ 
'''