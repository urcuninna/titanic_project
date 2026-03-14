load_data.py
clean_data.py
feature_engineering.py
train_model.py

Muchos scripts no se ejecutan solos, sino que son importados como módulos.

Ejemplo:

clean_data.py
def remove_duplicates(df):
    return df.drop_duplicates()

Luego en otro script:

from clean_data import remove_duplicates

Esto es arquitectura profesional de proyectos.

El script más importante muchas veces es uno que corre todo el pipeline:

run_pipeline.py

Ejemplo:

from data.load_data import load_data
from data.clean_data import clean_data
from features.build_features import build_features

df = load_data()
df = clean_data(df)
df = build_features(df)

Esto permite ejecutar todo con:

python run_pipeline.py