
# Memoria Trabajo Web Semántica y Datos Enlazados

- **Asignatura:** Web Semántica y Datos Enlazados
- **Máster:** MÁSTER UNIVERSITARIO EN INVESTIGACIÓN EN INTELIGENCIA ARTIFICIAL
- **Autor:** Alejandro Carrasco Núñez

## Índice

- [1. Introducción](#1-introducción)
- [2. Proceso de transformación](#2-proceso-de-transformación)
  - [2.1. Selección de la fuente de datos](#21-selección-de-la-fuente-de-datos)
  - [2.2. Análisis de los datos](#22-análisis-de-los-datos)
  - [2.3. Estrategia de nombrado](#23-estrategia-de-nombrado)
  - [2.4. Desarrollo del vocabulario](#24-desarrollo-del-vocabulario)
  - [2.5. Desarrollo de la ontología](#25-desarrollo-de-la-ontología)


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

### 2.4. Desarrollo del vocabulario
Se han definido requisitos funcionales y no funcionales mediante preguntas de competencia:

**Requisitos Funcionales**:
*	Pregunta de competencia 1:
    *	Pregunta: ¿Cómo puede un usuario obtener información detallada de un vehículo específico?
    *	Respuesta: El usuario puede utilizar la matrícula (VIN) para obtener un vehículo específico, y toda su información asociada.
*	Pregunta de competencia 2:
    * Pregunta: ¿Por qué campos se puede filtrar los vehículos eléctricos?
    * Respuesta: Se puede filtrar los vehículos por fabricante, modelo, tipo de vehículo, año del modelo, rango eléctrico, precio base, distrito legislativo, ID del vehículo, eligibilidad CAFV, estado, ciudad, condado, código postal, ubicación, empresa de electricidad y tramo censal.

**Requisitos no Funcionales**:
* Pregunta de competencia 1:
  * Pregunta: ¿Qué herramientas y extensiones se utilizarán para trabajar con el esqueleto RDF?
  * Respuesta: Utilizar OpenRefine y extensiones que permitan trabajar con el esqueleto RDF, facilitando la transformación y limpieza de datos.

**Extracción de términos**:
*	VIN: Número de Identificación del Vehículo, una matrícula única para cada vehículo.
*	County: Condado donde se ubica el vehículo.
*	City: Ciudad donde se ubica el vehículo.
*	State: Estado donde se ubica el vehículo.
*	Postal Code: Código postal del área donde se ubica el vehículo.
*	Model Year: Año del modelo del vehículo.
*	Make: Fabricante del vehículo.
*	Model: Modelo del vehículo.
*	Electric Vehicle Type: Tipo de vehículo eléctrico (BEV o PHEV).
*	CAFV Eligibility: Eligibilidad del vehículo para combustible alternativo limpio.
*	Electric Range: Rango eléctrico del vehículo.
*	Base MSRP: Precio base del vehículo.
*	Legislative District: Distrito legislativo donde se ubica el vehículo.
*	DOL Vehicle ID: Identificación del vehículo en el Departamento de Licencias.
*	Vehicle Location (coordinate x, coordinate y): Localización geográfica.
*	Electric Utility: Empresa de electricidad que suministra energía al vehículo.
*	2020 Census Tract: Tramo censal del año 2020.

**Conceptualización**: La representación de las clases con sus atributos y las relaciones entre ellas, se muestra en el siguiente diagrama conceptual (realizado mediante la herramienta draw.io).

![Diagrama Conceptual](./images/conceptualizacion.png)

**Búsqueda de ontologías**: Se ha hecho una búsqueda de ontologías publicadas relativas al dominio de vehículos eléctricos o en su defecto, se ha generalizado a vehículos. Se ha empleado la herramienta de búsqueda **[LOV](https://lov.linkeddata.es/dataset/lov/)**. Algunas ontologías encontradas han sido:

* **[Ontología Schema de vehículo](https://schema.org/Vehicle)**: Ofrece muchas propiedades adecuadas a las clases y atributos definidos en el modelado.
* **[Ontología foaf](http://xmlns.com/foaf/spec/)**: Empleada para propiedades no encontradas en la ontología anterior.
* **[Ontología geo](http://www.w3.org/2003/01/geo/)**: Empleada para la propiedad de localización geográfica (representa coordenadas).

Como resultado se muestra la siguiente tabla. En ella se asocia una ontología a cada elemento del glosario de términos, y se añade el concepto que se usará en la implementación.  

| Término | Ontología | Concepto |
|--------------|--------------|--------------|
| VIN | https://schema.org/vehicleIdentificationNumber | schema:vehicleIdentificationNumber |
| County | https://schema.org/Place | schema:Place |
| City | https://schema.org/City | schema:City |
| State | https://schema.org/State | schema:State |
| Postal Code | https://schema.org/postalCode | schema:postalCode |
| Model Year | https://schema.org/vehicleModelDate | schema:vehicleModelDate |
| Make | http://xmlns.com/foaf/spec/#term_maker | foaf:term_maker |
| Model | https://schema.org/model | schema:model |
| Electric Vehicle Type | https://schema.org/vehicleTransmission | schema:vehicleTransmission |
| CAFV Eligibility | https://schema.org/fuelType | schema:fuelType |
| Electric Range | https://schema.org/fuelCapacity | schema:fuelCapacity |
| Base MSRP | https://schema.org/price | schema:price |
| Legislative District | https://schema.org/Observation | schema:Observation |
| DOL Vehicle ID | https://schema.org/productID | schema:productID |
| Vehicle Location | http://www.w3.org/2003/01/geo/wgs84_pos#Point | geo:Point |
| Electric Utility | https://schema.org/Place | schema:Place |
| 2020 Census Tract | https://schema.org/Observation | schema:Observation |

### 2.5. Desarrollo de la ontología
Para implementar la ontología se ha empleado la herramienta OpenRefine (al igual que en los apartados anteriores), y la extensión **rdf-transform**. Dado que la versión más actualizada de OpenRefine no dispone de esa extensión, se ha descargado por separado de un [repositorio](https://github.com/AtesComp/rdf-transform) disponible desde la documentación de OpenRefine.

Se ha definido el esqueleto rdf siguiendo lo aprendido en los vídeos téoricos de la asignatura y teniendo como base el modelo conceptual implementado. En la URI base de RDF se ha definido la ruta para individuos indicada en la estrategia de nombrado.

![RDF Header](./images/uriresourcesopenrefine.PNG)

La raíz del esquema rdf será la clase **Vehicle** identificada con su **VIN** y a partir de la cual, se han creado tanto propiedades individuales como referencias a otras clases (por ej. **County**, **City**,...).
