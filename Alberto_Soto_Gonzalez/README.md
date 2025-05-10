# Proyecto de Transformación de Datos Cinematográficos a la Web Semántica

## Información del Proyecto
- **Título:** Transformación de Datos de IMDB a Datos Enlazados
- **Asignatura:** Web Semántica y Datos Enlazados
- **Programa:** Máster en Investigación en Inteligencia Artificial
- **Autor:** Alberto Soto Gonzalez

## Índice

- [1. Introducción](#1-introducción)
- [2. Proceso de transformación](#2-proceso-de-transformación)
  - [2.1. Selección de la fuente de datos](#21-selección-de-la-fuente-de-datos)
  - [2.2. Análisis de los datos](#22-análisis-de-los-datos)
  - [2.3. Estrategia de nombrado](#23-estrategia-de-nombrado)
  - [2.4. Desarrollo del vocabulario](#24-desarrollo-del-vocabulario)
  - [2.5. Desarrollo de la ontología](#25-desarrollo-de-la-ontología)
  - [2.6. Enlazado](#26-enlazado)
- [3. Aplicación y explotación](#3-aplicación-y-explotación)

## 1. Introducción

Este proyecto se centra en la transformación de un conjunto de datos cinematográficos a formato de datos enlazados, siguiendo los principios y metodologías de la Web Semántica. El objetivo principal es crear una representación semántica rica de las 1000 producciones audiovisuales más destacadas según IMDB, permitiendo su integración en la Web de Datos.

## 2. Proceso de transformación

### 2.1. Selección de la fuente de datos

La fuente principal de datos para este proyecto es el dataset [IMDB Top 1000 Movies and TV Shows](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows), disponible en la plataforma Kaggle. Este conjunto de datos se encuentra bajo la licencia [CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/), lo que permite su uso, modificación y distribución sin restricciones.

El dataset fue creado a partir de la información pública disponible en Internet Movie Database (IMDB), una de las bases de datos cinematográficas más completas y utilizadas a nivel mundial. La selección de las 1000 producciones se basa en su calificación y popularidad en la plataforma, lo que garantiza que estamos trabajando con un conjunto de datos que representa lo más destacado del cine y la televisión.

Esta selección se basa en varios factores clave:
- **Riqueza de información:** El dataset contiene datos detallados sobre películas y series, incluyendo información técnica, artística y comercial
- **Estructura relacional:** Presenta múltiples conexiones entre entidades (películas, directores, actores), lo que facilita la creación de relaciones semánticas
- **Actualidad:** Los datos representan el panorama cinematográfico actual, con producciones desde los inicios del cine hasta la actualidad
- **Accesibilidad:** Disponible en formato CSV, facilitando su procesamiento y transformación
- **Licencia permisiva:** La licencia CC0 permite su uso sin restricciones, ideal para proyectos académicos y de investigación
- **Calidad de datos:** La información proviene de IMDB, una fuente confiable y constantemente actualizada
- **Potencial semántico:** La naturaleza interconectada de los datos cinematográficos permite crear una red rica de relaciones semánticas

El dataset incluye producciones de diversos géneros, épocas y países, lo que proporciona una visión amplia y diversa del panorama cinematográfico. Esta diversidad es especialmente valiosa para la creación de una ontología que pueda representar adecuadamente las diferentes facetas del mundo del cine y la televisión. 

### 2.2. Análisis de los datos

El conjunto de datos, con un tamaño aproximado de 1.2 MB, contiene 1000 registros de producciones audiovisuales. Cada registro está compuesto por 16 columnas que contienen información detallada sobre cada producción:

1. **Poster_Link**: URL que enlaza con la imagen del póster oficial de la película o serie. Este enlace permite acceder a la imagen promocional de alta calidad de cada producción.

2. **Series_Title**: Título oficial de la película o serie. Este campo contiene el nombre completo de la producción tal como aparece en IMDB.

3. **Released_Year**: Año de lanzamiento de la producción. Este campo numérico indica el año en que la película o serie fue estrenada oficialmente.

4. **Certificate**: Clasificación por edades o certificación de la producción (por ejemplo, PG-13, R, TV-MA). Este campo indica las restricciones de edad recomendadas para el contenido.

5. **Runtime**: Duración total de la producción en minutos. Este campo numérico representa la longitud exacta de la película o episodio.

6. **Genre**: Géneros cinematográficos de la producción, separados por comas. Una producción puede pertenecer a múltiples géneros (por ejemplo, "Action, Adventure, Sci-Fi").

7. **IMDB_Rating**: Calificación promedio en IMDB, en una escala de 0 a 10. Este valor se calcula a partir de las votaciones de los usuarios de la plataforma.

8. **Overview**: Sinopsis o resumen del argumento de la producción. Este campo de texto proporciona una descripción concisa de la trama.

9. **Meta_score**: Puntuación de Metacritic, en una escala de 0 a 100. Este valor representa la evaluación crítica agregada de la producción.

10. **Director**: Nombre del director principal de la producción. Este campo identifica al responsable de la dirección de la película o serie.

11. **Star1, Star2, Star3, Star4**: Nombres de los cuatro actores principales de la producción, ordenados por relevancia en el reparto. Estos campos identifican a los intérpretes más destacados.

12. **No_of_Votes**: Número total de votos recibidos en IMDB. Este campo numérico indica la cantidad de usuarios que han calificado la producción.

13. **Gross**: Ingresos brutos de la producción en dólares. Este campo numérico representa la recaudación total en taquilla.

A continuación se muestra una vista previa de los datos en OpenRefine, donde se pueden observar las diferentes columnas y sus valores:

![Vista previa de datos en OpenRefine](./img/openrefine-data-preview.png)