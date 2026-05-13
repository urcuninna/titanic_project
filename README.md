# Análisis Predictivo de Supervivencia — Titanic Dataset

Por: Erika Yesid Pinchao Rosero (urcuninna)

Fecha: Mayo 2026

Herramientas: Python, Scikit-learn, Pandas, Matplotlib, Seaborn, Power BI, Markdown.

## Objetivo del Proyecto (Business Task)

Construir un modelo predictivo capaz de estimar la probabilidad de supervivencia de un pasajero a partir de sus características demográficas y sociales.

## Preguntas clave
¿Qué factores estuvieron más relacionados con la supervivencia?

¿Qué perfiles tenían mayores probabilidades de sobrevivir?

¿Qué tan bien puede un modelo de machine learning predecir nuevos casos?

## Tarea analítica

Construir un modelo predictivo que permita estimar la probabilidad de supervivencia de un pasajero en función de sus características.

## Fuentes de Datos

Fuente: Titanic Dataset — Kaggle / OpenML.

Periodo histórico: Viaje inaugural del RMS Titanic (1912).

## Variables principales:

Sexo
Edad
Clase del pasajero
Tarifa
Puerto de embarque
Información familiar

## Variable objetivo:

Survived

## Procesamiento y Limpieza (Data Wrangling)

Volumen: 891 registros procesados.

Limpieza:

- tratamiento de valores nulos
- validación de tipos de datos
- eliminación de inconsistencias
- transformación de variables categóricas

## Ingeniería de Variables (Feature Engineering):

- agrupación de títulos sociales (Mr, Mrs, Master, Rare)
- creación de tamaño familiar (FamilySize)
- agrupación de estructuras familiares
- escalamiento de variables numéricas
- encoding de variables categóricas

## Calidad:

- validación de consistencia
- evaluación de distribución de variables
- análisis exploratorio previo al modelado

## Análisis Exploratorio (EDA)

El análisis exploratorio permitió identificar patrones demográficos y sociales fuertemente relacionados con la supervivencia.

Las mujeres presentaron tasas de supervivencia considerablemente superiores a las de los hombres, consolidándose como una de las variables más influyentes dentro del análisis.

La clase social mostró una relación importante con la supervivencia. Los pasajeros de primera clase presentaron mayores probabilidades de sobrevivir frente a pasajeros de clases inferiores, sugiriendo diferencias relacionadas con acceso, ubicación y recursos durante la evacuación.

Los perfiles infantiles también mostraron mayores niveles de supervivencia, especialmente aquellos identificados mediante títulos sociales asociados a niños (Master).

La estructura familiar reveló patrones relevantes. Los pasajeros pertenecientes a familias pequeñas mostraron mejores resultados frente a pasajeros completamente solos o familias numerosas, las cuales parecían enfrentar mayores dificultades de evacuación y movilidad.

El puerto de embarque mostró ligeras diferencias entre perfiles de supervivencia, aunque con menor impacto comparado con variables sociales y demográficas.

## Modelado Predictivo (Machine Learning)

### Modelos evaluados:

- Logistic Regression
- Random Forest
- Gradient Boosting

### Metodología:

- train/test split
- validación cruzada estratificada
- optimización de threshold
- evaluación mediante F1-score y AUC

### Resultados del Modelo

La Regresión Logística presentó el mejor equilibrio entre desempeño, estabilidad e interpretabilidad.

Métricas obtenidas:

F1-score: ~0.79
AUC: ~0.87

Aunque modelos basados en árboles como Random Forest y Gradient Boosting mostraron resultados competitivos, la Regresión Logística logró una mejor capacidad de generalización sobre las variables construidas durante el feature engineering.

## Principales Hallazgos del Modelo

El modelo identificó que variables sociales y demográficas tuvieron una influencia significativa sobre la supervivencia.

Factores con impacto positivo:

- perfiles femeninos
- niños (Master)
- clases sociales altas
- familias pequeñas

Factores con impacto negativo:

- hombres adultos (Mr)
- familias numerosas
- clases sociales bajas

La interpretación de coeficientes permitió transformar el modelo predictivo en insights explicativos sobre el comportamiento de supervivencia de los pasajeros.

## Conclusiones

El proyecto permitió construir un modelo predictivo funcional capaz de estimar probabilidades de supervivencia a partir de características de los pasajeros.

El feature engineering tuvo un impacto importante sobre el rendimiento del modelo, especialmente mediante la representación de relaciones familiares y perfiles sociales.

La Regresión Logística no solo presentó el mejor desempeño general, sino también una mayor interpretabilidad frente a otros modelos evaluados.

Finalmente, el análisis evidenció cómo variables sociales y demográficas pueden influir significativamente en eventos de emergencia y cómo el machine learning puede utilizarse tanto para predicción como para generación de conocimiento a partir de datos históricos.