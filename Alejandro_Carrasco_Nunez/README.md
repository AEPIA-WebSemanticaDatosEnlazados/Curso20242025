
# Memoria Trabajo Web Semántica y Datos Enlazados

- **Asignatura:** Web Semántica y Datos Enlazados
- **Máster:** MÁSTER UNIVERSITARIO EN INVESTIGACIÓN EN INTELIGENCIA ARTIFICIAL
- **Autor:** Alejandro Carrasco Núñez

## Índice

- [1. Introducción](#1-introducción)
- [2. Proceso de transformación](#2-proceso-de-transformación)
  - [2.1. Selección de la fuente de datos](#21-selección-de-la-fuente-de-datos)
  - [2.2. Análisis de los datos](#22-análisis-de-los-datos)


## 1. Introducción

En esta memoria se describe el proyecto para la asignatura "Web Semántica y Datos Enlazados," que ha consistido en la transformación de un conjunto de datos de origen, en CSV, a datos enlazados.

Se ha tratado un dataset que contenía una población de vehículos eléctricos, obtenidos del portal de datos abiertos del gobierno de EE.UU. (Data.gov).

## 2. Proceso de transformación

### 2.1. Selección de la fuente de datos
Se ha escogido el conjunto de datos sobre la **población de vehículos eléctricos**, publicado en [el portal de datos abiertos del gobierno de EE.UU. (Data.gov)](https://catalog.data.gov/dataset/electric-vehicle-population-data). Este conjunto de datos proporciona información detallada sobre los vehículos eléctricos registrados, incluyendo características como el tipo de vehículo, el fabricante, el modelo, el año de fabricación y la ubicación geográfica.

El conjunto de datos está disponible en el portal de **Data.gov**, que es una iniciativa del gobierno de EE.UU. para proporcionar acceso a datos públicos. Los distintos conjuntos de datos disponibles en la página están disponibles para su uso y distribución bajo licencias abiertas.
El conjunto de datos elegido incluye información sobre miles de vehículos eléctricos registrados en diferentes regiones. Por eso, dichos datos se actualizan periódicamente.

El dataset fue descargado en formato CSV, desde la página web. Dicho archivo tiene un tamaño de 55.74 MB.

### 2.2. Análisis de los datos
Mediante la herramienta **OpenRefine**, aprendida durante el curso, se han analizado los datos contenidos en el archivo CSV.

Se creó un proyecto de nombre “**Electric Vehicle Population Data Proyect**” y se importó el CSV. El resultado fue una tabla de datos compuesta por 235.692 filas, siendo cada fila el registro de un vehículo eléctrico.

En las siguientes imágenes se pueden ver una parte de los registros y sus valores para cada columna.

![Datos 1 OpenRefine](./images/openrefine1.png)

![Datos 2 OpenRefine](./images/openrefine2.PNG)

En total para cada registro hay **18 columnas** (atributos), que son las siguientes:

*	**VIN (1-10)**: Campo de tipo texto que representa la matrícula del vehículo. Es única para cada vehículo, por ejemplo, 5YJ3E1EBXK.
*	**County**: Campo de tipo texto que representa el condado donde se ubica el vehículo. Hay 212 valores, por ejemplo, King.
*	**City**: Campo de tipo texto que representa la ciudad donde se ubica el vehículo. Hay 788 valores, por ejemplo, Seattle.
*	**Stat**e: Campo de tipo texto que representa el estado donde se ubica el vehículo. Hay 48 valores, por ejemplo, WA.
*	**Postal Code**: Campo de tipo texto que representa el código postal, formado por un conjunto de dígitos, por ejemplo, 98178.
*	**Model Year**: Campo de tipo entero que representa el año del modelo. Su rango de valores comprende del 2000 al 2025.
*	**Make**: Campo de tipo texto que representa el fabricante. Hay 46 valores, por ejemplo, TESLA.
*	**Model**: Campo de tipo texto que representa el fabricante. Hay 171 valores, por ejemplo, MODEL 3.
*	**Electric Vehicle Type**: Campo de tipo texto que representa el tipo de vehículo eléctrico. Hay 2 valores: Battery Electric Vehicle (BEV) y Plug-in Hybrid Electric Vehicle (PHEV).
*	**Clean Alternative Fuel Vehicle (CAFV) Eligibility**: Campo de tipo texto que representa la eligibilidad de combustible alternativo para el vehículo. Hay 3 valores, por ejemplo, “Clean Alternative Fuel Vehicle Eligible”, “Eligibility unknown as battery range has not been researched” y “Not eligible due to low battery range”.
*	**Electric Range**: Campo de tipo entero que representa el rango eléctrico. El rango comprende de 0 a 337.
*	**Base MSRP**: Campo de tipo entero que representa el precio base del vehículo. El rango comprende de 0 a 845000.
*	**Legislative District**: Campo de tipo entero que representa el distrito legislativo. El rango comprende de 1 a 49.
*	**DOL Vehicle ID**: Campo de tipo texto que representa el id de cada vehículo. Es una ristra única de 9 dígitos aunque se ha mantenido como cadena de texto.
*	**Vehicle Location**: Campo de texto que representa la localización geográfica del vehículo. La representación viene dada por defecto por el CSV, y se representa de la siguiente manera: POINT (coordenadaX coordenadaY), que en un ejemplo real se vería: POINT (-122.23825 47.49461). Para este campo se ha realizado una transformación con el fin de separar las coordenadas x e y.
*	**Electric Utility**: Campo de tipo texto que representa la empresa de electricidad. Hay 76 valores.
*	**2020 Census Tract**: Campo de tipo entero que representa el tramo censal. Su rango va de 1 billón a 57 billones.

A los campos que se han considerado de tipo entero se les ha aplicado la transformación de celdas a tipo “**Number**”.

Por otro lado, para verificar los rangos y número de valores que cada campo puede tomar se han empleado distintas **Facets**. Se han generado tanto Facets de tipo “**Text**” para las cadenas, como “**Numeric**” para los campos de tipo entero. Algunas de esas Facets se pueden visualizar en las siguientes imágenes.

![Facets OpenRefine](./images/openrefinefacets.PNG)     ![Facets2 OpenRefine](./images/openrefinefacets2.PNG)

Para el campo **Vehicle Location** se ha aplicado una transformación. Se han generado dos columnas nuevas (**Coordinate X**, **Coordinate Y**) para separar las dos coordenadas que contiene la ubicación. Se han creado mediante la opción **Add column based on this column**, utilizando dos expresiones regulares **GREL** para extraer cada valor.
El uso de las expresiones se muestra en las siguientes imágenes.

![Regular expression 1 OpenRefine](./images/openrefinecoordinatex.PNG)     ![Regular expression 2 OpenRefine](./images/openrefinecoordinatey.PNG)

Las dos columnas nuevas siguen siendo de tipo texto, por lo que se ha aplicado una transformación a tipo numérico.

![Transformed Point OpenRefine](./images/openrefinetransformedpoint.PNG)

**Licencia de los datos** El sitio web indica que el conjunto de datos se encuentra bajo la licencia **[Open Data Commons Open Database License (ODbL) 1.0](https://opendatacommons.org/licenses/odbl/1-0/)**. Esta licencia permite al usuario compartir, modificar y utilizar la base de datos, siempre que se cumpla lo siguiente:

*	Se debe dar crédito al publicador de este conjunto de datos, indicando un enlace a la licencia y si se han realizado cambios; además, cualquier redistribución de la base de datos debe realizarse bajo la misma licencia ODbL 1.0 (condición de **share-alike**).

Es importante destacar que la licencia se aplica tanto a los datos en sí como a la estructura de la base de datos, de modo que cualquier extracción o combinación que identifique la fuente original está sujeta a los términos de la licencia.

Dado que el CSV original está bajo la licenci ODbL 1.0, para la transformación a datos enlazados se debe mantener la **misma licencia**. De esta forma se cumple con las condiciones de atribución y de share-alike que se establecen. Esto implica que, aunque se haya cambiado el formato y la estructura (de CSV a datos enlazados), los términos de la licencia deben seguir siendo los mismos, y cualquier base de datos derivada o modificación futura se hará bajo ODbL 1.0.

### 2.3. Estrategia de nombrado
Se considera el dominio **http://catalog.data.gov/** para la consulta de los datos. Dada la naturaleza de nuestro conjunto de datos y su contenido se adoptarán las siguientes convenciones:

*	**Términos ontológicos**:
    *	Usaremos el hash (**#**) como separador para los términos de la ontología.
      *	Ruta para términos ontológicos: **http://catalog.data.gov/ontology/ElectricVehicle#**
      *	Patrón para términos ontológicos: **http://catalog.data.gov/ontology/ElectricVehicle#<term>**
*	**Individuos**:
    *	Usaremos la barra (/) para recuperar los datos de manera individual o en grupo.
      *	Ruta para individuos: **http://catalog.data.gov/resource**
      *	Patrón para individuos: **http://catalog.data.gov/resource/<resource_type>/<id>**
Ejemplos de URIs generadas:
*	Términos ontológicos: **http://catalog.data.gov/ontology/ElectricVehicle#electricVehicleType**
*	Individuos (por ejemplo vehículos): **http://catalog.data.gov/resource/Vehicle/5YJ3E1EBXK**
