Nota: trabajo en proceso y no finalizado

# Trabajo final Web semántica y datos enlazados
## Ana Chacón Tanarro. Curso 2024-2025
- [1. Introducción](#1-introducción)
- [2. Proceso de transformación](#2-proceso-de-transformación)
  - [2.1. Selección de la fuente de datos](#21-selección-de-la-fuente-de-datos)
  - [2.2. Licencia](#22-licencia)
  - [2.3. Análisis de datos](#22-análisis-de-datos)

## 1. Introducción

Este trabajo se centra en transformar y crear un conjunto de datos enlazados a partir de la selección de un conjunto de datos publicado por el Instituto Nacional de Estadística (INE) y crear una aplicación que consiga mostrar los datos de manera sencilla.

## 2. Proceso de transformación
### 2.1. Preparación y análisis de datos
#### 2.1.1. Selección de la fuente de datos y acceso

Este trabajo se centra principalmente en la obtención y transformación de un conjunto de datos que represente el censo de la población española con la distribución de la población por edades y municipios. Los requisitos principales han sido:
- Que la fuente de datos fuese una institución pública, por asegurar la calidad de los datos. También se priorizaba que ésta fuese la generadora y propietaria de los datos.
- Que los datos estuviesen lo más actualizados posible.
- Que los datos estuviesen disponibles y bien estructurados. 

Así, se ha seleccionado como conjunto de datos el censo anual de población a nivel municipal, desagregado por sexo y edad (año a año) elaborado y publicado por el Instituto Nacional de Estadística (INE) el 19 de diciembre de 2024. El censo anual de población es una operación estadística que se publica siempre a finales de cada año ofreciendo las cifras oficiales y características demográficas de la población española a 1 de enero del mismo año. Así, los datos escogidos recogen información de la población residente en España a 1 de enero de cada año censado y se actualizan anualmente. Se pueden obtener los datos desde el siguiente enlace: [Censo anual, resultados por municipios](https://www.ine.es/dynt3/inebase/es/index.htm?padre=11555&capsel=11532). 

En particular, los datos provienen de la tabla [68542 - Población por sexo y edad (año a año)](https://www.ine.es/jaxiT3/dlgExport.htm?t=68542&L=0), la cual se descarga automáticamente en formato csv. Se comprueba que los datos descargados están bien estructurados y contienen la información mínima exigida: población censada por municipio y edad.

#### 2.1.2. Licencia

Como el propio INE informa en su [página web](https://www.ine.es/dyngs/AYU/index.htm?cid=125), la licencia de uso general es la Creative Commons Reconocimiento 4.0 [(CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.es). Esta licencia permite compartir (copiar y redistribuir el material en cualquier medio o formato para cualquier propósito) y adaptar (remezclar, transformar y construir a partir del material para cualquier propósito), siempre dando crédito de manera adecuada, brindando un enlace a la licencia e indicando si se han realizado cambios. 

Respecto a este último punto, el INE también indica lo siguiente: 
- La cita puede realizarse de la siguiente manera:* **Fuente: Sitio web del INE: www.ine.es** si no se realiza ningún tratamiento de los datos o bien: **Elaboración propia con datos extraídos del sitio web del INE: www.ine.es** en caso de que se realice tratamiento de los datos*
- Debe mencionarse la fecha de la última actualización de la información.
- No se debe indicar, insinuar o sugerir que el INE participa, patrocina o apoya la reutilización de la información.
- La utilización de los datos se realizará bajo la responsabilidad y riesgo del usuario, y el INE no se hace responsable de su uso. 
- Los agentes reutilizadores se hallan sometidos a la normativa aplicable en materia de reutilización de la información del sector público, incluyendo el régimen sancionador previsto en el artículo 11 de la Ley 37/2007, de 16 de noviembre, sobre reutilización de la información del sector público.

Debido a que la transformación de los datos no va a suponer una agregación de valor sustancial al conjunto de datos original, se mantiene la misma licencia para cumplir con la licencia de los datos originales. 

#### 2.1.3. Análisis de datos

A continuación, se muestra el proceso seguido para el análisis y procesamiento de los datos en [OpenRefine](https://openrefine.org/). 

Para cargar los datos en OpenRefine, se ha tenido que aumentar la memoria RAM dedidaca al software que venía por defecto a 8 GBs, debido al tamaño del conjunto de datos (716.4 MBs). Una vez cargado el proyecto, los datos tienen la siguiente apariencia:
![Previsualización de los datos](figs/swld_view_data.png)

Existen 10.018.440 filas, indicando los valores de población censada dependiendo del valor de otras 6 variables. Así, el conjunto de datos presenta 7 columnas:
- Total Nacional: esta columna solo presenta un valor, "Total Nacional". Se presenta en formato texto. 
- Provincias: desagrega los datos de población censada por provincias. La información que se da en esta tabla es el código de provincia seguido del nombre. Ejemplo: "01 Araba/Álava". Esta columna está vacía para los valores totales nacionales a nivel España como conjunto. Se presenta en formato texto. 
- Municipios: desagrega la información por municipio. Sigue la misma estructura que la anterior, se compone de un código identificativo del municipio y el nombre de éste. Ejemplo: "01001 Alegría-Dulantzi". También presenta valores vacíos cuando los valores de población se refieren a los totales nacionales o totales a nivel provincia. Se presenta en formato texto.  
- Sexo: desagrega la información entre "Hombres", "Mujeres" y "Total". Se presenta en formato texto. 
- Edad: desagrega la información entre "Todas las edades" y año por año (de 0 a 99 años y más de 100, como por ejemplo "0 años"). Se presenta en formato texto. 
- Periodo: Referido al año de referencia (desde 2021 a 2024). Se ha transformado a formato de fecha. 
- Total: valor de la población censada. Se ha transformado a formato de número y los valores van de 0 a 48.619.695.
![Facetas](figs/facets.png)
No se encuentran valores fuera de rango o erróneos.

Por facilitar la interpretación de los datos, se ha sustituido el valor "Total Nacional" por "España" y se ha renombrado dicha columna a "País", de tal manera que existe una jerarquía entre las columnas País, Provincias y Municipios. 

### 2.2. Estrategia de nombrado

Lo primero que se debe elegir, es el uso de # o /. Debido a que tenemos muchos datos y son modulares, se usará / para nuestros datos. Por otro lado, se usará # para la ontología, ya que se puede acceder a todos los términos del vocabulario de una sola vez. 

Asumiendo que tenemos control sobre el dominio datos.ine.es, tendríamos la siguiente estructura:
- Dominio: http://datos.ine.es/
- Ruta para los términos ontológicos: http://datos.ine.es/vocab#
  - Patrón para términos ontológicos: http://datos.ine.es/vocab#<term>
- Ruta para los individuos: http://datos.ine.es/resources/
  - Patrón para individuos:  http://datos.ine.es/resources/<resource>

Vamos a usar como base la ontología de [Data Cube](https://www.w3.org/TR/vocab-data-cube/), ya que está específicamente diseñada para la publicación de datos multidimensionales, como los estadísticos, utilizando el estándar W3C RDF y basándose en el modelo de información SDMX 2.0, estándar ISO para el intercambio de datos y metadatos estadísticos. Extenderemos la ontología con aquellos elementos específicos de nuestro conjunto de datos. 
