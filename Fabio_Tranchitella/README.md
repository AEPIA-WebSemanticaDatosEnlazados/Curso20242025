# Final Project Report

- **Subject:** Semantic web and linked data
- **Master program:** Research in Artificial Intelligence
- **University:** [Universidad Internacional Menéndez Pelayo](https://www.uimp.es)
- **Author:** Fabio Tranchitella, [fabio.tranchitella@gmail.com](mailto:fabio.tranchitella@gmail.com)
- **Date:** November, 2024
- **Version:** 1.0

## Tables of contents

- [1. Introduction](#1-introduction)
- [2. Transformation process](#2-transformation-process)
  - [2.1. Selection of the data set](#21-selection-of-the-data-set)
  - [2.2. Analysis of the data set](#22-analysis-of-the-data-set)
- [9. Bibliography](#9-bibliography)

## 1. Introduction

This document describes the final project for the subject "Semantic web and linked data," part of the University Master's "Research in Artificial Intelligence" from the Universidad Internacional Menéndez Pelayo.

In particular, this project consists of the selection, transformation, preparation, and publication of a data set for the `Infant mortality rate` indicator from [The United Nations Children's Fund (UNICEF)](https://www.unicef.org), one of the agencies of the United Nations.

It also includes a sample application exposing simple REST APIs that leverage the dataset, loaded in a triplestore, to answer queries that non-technical users cannot respond to directly because of the number of records contained in the dataset.

## 2. Transformation process

### 2.1. Selection of the data set

I selected the data set containing the `Infant mortality rate` indicator published by [The United Nations Children's Fund (UNICEF)](https://www.unicef.org). The data set is available in the [UNICEF Open Data portal](https://data.unicef.org/), also known as UNICEF Data Warehouse, which publishes many freely available and distributable datasets that are part of UNICEF's Open Data initiative. It is also available in the [Humanitarian Data Exchange Hub](https://data.humdata.org), a catalog of open humanitarian data.

The full dataset with all the indicators includes 41,789 data points, each representing the `Infant mortality rate` indicator value for a given country. The indicator data is drawn from inter-agency estimates and nationally representative household surveys such as Multiple Indicator Cluster Surveys (MICS) and Demographic and Health Surveys (DHS).

I downloaded the data in CSV format, encoded in UTF-8, from the [data set's web page](https://data.humdata.org/dataset/unicef-cme-mry0) in the Humanitarian Data Exchange Hub. The uncompressed CSV file size is 8,206 KB.

The data set is available in this repository at the path [./data/CME.csv.gz](/data/CME.csv.gz).

### 2.2. Analysis of the data set

#### License of the source data set used in the project

As stated on the website, the data set is licensed under the terms of the Creative Commons Attribution-NonCommercial 3.0 IGO ([CC BY-NC 3.0 IGO](https://creativecommons.org/licenses/by-nc/3.0/igo/deed.en)) license.

As explained in the legal terms of the licenes, the user is free to share the material, including adapt and transform it. However, the user must give appropriate credit to the publisher of the data set, provide a link to the license and indicate if changes were made. Additionally, the user cannot use this data set for commercial purposes.

For more details about the legal terms of the license, please refer to the creativecommons.org website linked in the [bibliography](#9-bibliography).

#### License of the transformed linked data set resulting from the project

Given that the original license of the data set is a well-known, standard, open license, I selected the Creative Commons Attribution-NonCommercial 4.0 International ([CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)) one for the transformed and linked data. It is the same license as the one initially used by the publisher of the data set, therefore fully compatible, though a newer and updated version as suggested by the Creative Commons website.

For more details about the legal terms of the license, please refer to the creativecommons.org website linked in the [bibliography](#9-bibliography) and the [LICENSE](./LICENSE) file included in this repository.

#### Explorative Data Analysis of the data set

To analyze, prepare and transform the data to be published as linked data, I selected the open source [OpenRefine](https://openrefine.org) software, as suggested in the course's training materials.

After creating the project `Infant mortality rate` and importing the CSV into it, I proceeded with the schema and metadata analysis. 

Each line of the CSV contains a record representing the value of the `Infant mortality rate` for a specific country and subset population, if the information is available.

The columns available in the data set are:

* **REF_AREA**: (Text) ISO 3166-1 alpha-3 code of the country (e.g. `AFG`)
* **Geographic area**: (Text) English name of the country (e.g. `Afghanistan`)
* **INDICATOR**: (Text) Code of the indicator (e.g. `CME_MRY0`)
* **Indicator**: (Text) English name of the indicator (e.g. `Infant mortality rate`)
* **SEX**: (Text) Gender code for the subset of the population the indicator is referred to (e.g. `F`)
* **Sex**: (Text) Gender description for the subset of the population the indicator is referred to (e.g. `Female`)
* **WEALTH_QUINTILE**: (Text) Code of the wealth quintile the indicator is referred to (e.g. `_T`)
* **Wealth Quintile**: (Text) Description of the wealth quintile the indicator is referred to (e.g. `Total`)
* **DATA_SOURCE**: (Text) Code of the division/entity publishing the data (e.g. `UN_IGME`)
* **COUNTRY_NOTES**: (Text) Notes about the country
* **UNIT_MEASURE**: (Text) Code of the unit of measure (e.g. `D_PER_1000_B`)
* **Unit of measure**: (Text) Description of the unit of measure (e.g. `Deaths per 1,000 live births`)
* **TIME_PERIOD**: (Integer) Year the indicator is referred to (e.g. `1962`)
* **OBS_VALUE**: (Float) Observed value for the indicator (e.g. `219.62798095743`)
* **REF_PERIOD**: (Integer) Period of reference
* **LOWER_BOUND**: (Float) Lower bound of the value for the indicator (e.g. `188.139849017438`)
* **UPPER_BOUND**: (Float) Lower bound of the value for the indicator (e.g. `259.584247018356`)
* **OBS_STATUS**: (Text) Code of the status of the observation (e.g. `A`)
* **Observation Status**: (Text) Description of the status of the observation (e.g. `Normal value`)

I transformed the columns marked as Integer and Float from the list above to number using the function `Edit cells > Common transforms > To number`.

Using the Facets functionality, I verified the number of distinct values for the following columns: **INDICATOR**, **Indicator**, **WEALTH_QUINTILE**, **Wealth Quintile**, **DATA_SOURCE**, **UNIT_MEASURE**, **Unit of measure**, **REF_PERIOD**, **OBS_STATUS**, **Observation Status**. As all these columns contained precisely one value, they did not add any value to single records, so I dropped them.

Additionally, the **Sex** column does not add any value to the data set, as it contains the gender description, which always matches the gender code specified in the column **SEX**, as I verified using Facets.

Using the Facets functionality and a simple sort, I verified the data ranges of the numerical values **OBS_VALUE**, **LOWER_BOUND**, and **UPPER_BOUND** and looked for outliers or anomalies. The data set does not contain spurious or out-of-range data, with maximum values for the indicators 293, 245, and 352, respectively. Given that the indicator is the number of deaths per 1,000 live births, values below 1,000 are congruent.

![Data Ranges in OpenRefine](./images/openrefine-ranges.png)

## 9. Bibliography

This project leverages the following resources available in the Internet:

- [UNICEF Open Data portal](https://data.unicef.org/)
- [Humanitarian Data Exchange Hub](https://data.humdata.org)
- [Infant mortality rate data set's web page](https://data.humdata.org/dataset/unicef-cme-mry0)
- [CC BY-NC 3.0 IGO license](https://creativecommons.org/licenses/by-nc/3.0/igo/deed.en)
- [CC BY-NC 4.0 license](https://creativecommons.org/licenses/by-nc/4.0/)
- [OpenRefine](https://openrefine.org)
