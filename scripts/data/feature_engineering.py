# Feature Engineering
import pandas as pd
import numpy as np

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer

# Creación de variables nuevas

def crear_features(df):

    df = df.copy()
    
    # Title
    df["Title"] = df["Name"].str.extract(" ([A-Za-z]+)\.", expand=False)
    
    rare_titles = ["Lady", "Countess", "Capt", "Col", "Don", "Dr",
                   "Major", "Rev", "Sir", "Jonkheer", "Dona"]
    
    df["Title"] = df["Title"].replace(rare_titles, "Rare")
    df["Title"] = df["Title"].replace({
        "Mlle": "Miss",
        "Ms": "Miss",
        "Mme": "Mrs"
    })
    
    # Family size
    df["family_size"] = df["SibSp"] + df["Parch"] + 1
    
    # Agrupación de family size 
    def agrupar_family(size):
        if size == 1:
            return "solo"
        elif 2 <= size <= 4:
            return "pequena"
        else:
            return "grande"
    
    df["Family_group"] = df["family_size"].apply(agrupar_family)
    
    return df

# Selección de variables

def seleccionar_features():
    features = ["Pclass", "Sex", "Title", "Age", "Family_group", "Embarked"]
    return features

# Definir tipos de variables

def obtener_feature_types():
    num_cols = ["Age"]
    ordinal_cols = ["Pclass"]
    cat_cols = ["Sex", "Title", "Family_group", "Embarked" ]
    
    return num_cols, ordinal_cols, cat_cols

# Construcción de pipelines de transformación

def transformaciones():
    
    num_cols, ordinal_cols, cat_cols = obtener_feature_types()
    
    # Pipeline numérico sin escalado porque funciono mejor en la exploración
    num_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median"))
    ])

    # Pipeline categórico
    cat_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ])
    
    # ColumnTransformer
    preprocessor = ColumnTransformer([
        ("num", num_pipeline, num_cols),
        ("ordinal", "passthrough", ordinal_cols),
        ("cat", cat_pipeline, cat_cols)
    ])
    
    return preprocessor

# 5. FUNCIÓN PRINCIPAL


def preparar_df(df):
    
    # Crear features
    df = crear_features(df)
    
    # Seleccionar variables
    features = seleccionar_features()
    X = df[features]
    y = df["Survived"]
    
    # Construir preprocessor
    preprocessor = transformaciones()
    
    return X, y, preprocessor