# Análisis de Vuelos en Argentina: Impacto de Feriados Largos 🇦🇷

## Descripción del Proyecto 📝

Este proyecto de análisis de datos explora la actividad de vuelos en Argentina, centrándose en el impacto de los feriados largos. El objetivo es identificar patrones de viaje, analizar el comportamiento de la demanda en días festivos y extraer conclusiones significativas que puedan ser de valor para el sector aerocomercial.

El análisis sigue una metodología de ciencia de datos, dividida en tres capas principales:
* **Capa Bronce 🥉:** Carga y limpieza inicial de los datos.
* **Capa Plata 🥈:** Normalización de los datos y creación de una base de datos relacional para el análisis.
* **Capa Oro 🥇:** Análisis exploratorio, visualizaciones y pruebas de hipótesis para responder a preguntas de negocio.

---

## Análisis y Hallazgos Principales 📈

En la **Capa de Oro**, se realizaron los siguientes análisis y se obtuvieron las siguientes conclusiones:

### 1. **Comparación de Vuelos: Feriados vs. Días Normales**

Se determinó que la actividad de vuelos, incluyendo el número de pasajeros y la ocupación promedio, es mayor en los días de feriado largo. . Un análisis de distribución mediante un `boxplot` mostró que la variabilidad en la cantidad de vuelos es diferente entre ambos tipos de días, sugiriendo una demanda más predecible durante los feriados. .

### 2. **Rutas y Destinos Populares en Feriados**

El análisis reveló que la demanda en feriados se concentra en los principales centros turísticos del país.

* **Gráfico de Torta:** La Ciudad Autónoma de Buenos Aires se destaca como el principal destino de vuelos durante los feriados, seguida por los destinos internacionales.
* **Gráfico de Barras Horizontales:** El análisis de las 10 rutas más populares confirmó que los vuelos con origen en la Ciudad de Buenos Aires y destino a provincias turísticas como Misiones y Mendoza son los más transitados.

### 3. **Análisis de Estacionalidad Mensual**

Se identificó la estacionalidad en la actividad de vuelos, con picos de demanda en los meses de verano (enero), invierno (julio) y fin de año (diciembre). . Este análisis provee un contexto adicional a la demanda generada por los feriados largos.

---


## Cómo Ejecutar el Proyecto ⚙️

1.  **Clonar el repositorio:**
    `git clone https://docs.github.com/es/get-started/using-git/getting-changes-from-a-remote-repository`
2.  **Instalar las dependencias:**
    `pip install -r requirements.txt`
3.  **Ejecutar los notebooks:**
    Ejecuta los notebooks en orden (bronce, plata, oro) para replicar el análisis completo.
    * _notebook_bronze.ipynb_: Realiza la ingesta y limpieza.
    * _notebook_silver.ipynb_: Normaliza los datos y crea la base de datos `analisis_vuelos.db`.
    * _notebook_gold.ipynb_: Ejecuta las consultas y genera las visualizaciones y conclusiones.

---

## Tecnologías y Librerías

* **Python**
* **Pandas:** Manipulación y análisis de datos.
* **SQLite3:** Gestión de la base de datos.
* **Matplotlib & Seaborn:** Visualizaciones.
* **SciPy:** Pruebas estadísticas.