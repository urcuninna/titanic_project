# Limpieza de datos 

import pandas as pd

def limpiar_datos(df: pd.DataFrame) -> pd.DataFrame:
    # copiar el DataFrame original para evitar modificarlo directamente
    df_limpio = df.copy()

    # eliminar columnas innecesarias
    df_limpio = df_limpio.drop(columns=['Cabin', 'Ticket'])

    # imputar valores faltantes en la columna 'Age' con la mediana
    df_limpio['Age'] = df_limpio['Age'].fillna(df_limpio['Age'].median())

    #imputar valores faltantes en la columna 'Embarked' con la moda
    df_limpio['Embarked'] = df_limpio['Embarked'].fillna(df_limpio['Embarked'].mode()[0])

    return df_limpio
