# Final Project Report

- **Subject:** Semantic web and linked data
- **Master program:** Research in Artificial Intelligence
- **University:** [Universidad Internacional Menéndez Pelayo](https://www.uimp.es)
- **Author:** Fabio Tranchitella, [fabio.tranchitella@gmail.com](mailto:fabio.tranchitella@gmail.com)
- **Date:** November, 2024
- **Version:** 1.0

## Tables of contents

- [1. Introduction](#introduction)
- [2. Transformation process](#transformation-process)
  - [2.1. Selection of the dataset](#selection-of-the-dataset)
- [9. Bibliography](#bibliography)

## 1. Introduction

This document describes the final project for the subject "Semantic web and linked data," part of the University Master's "Research in Artificial Intelligence" from the Universidad Internacional Menéndez Pelayo.

In particular, this project consists of the selection, transformation, preparation, and publication of a data set for the `Infant mortality rate` indicator from [The United Nations Children's Fund (UNICEF)](https://www.unicef.org), one of the agencies of the United Nations.

It also includes a sample application exposing simple REST APIs that leverage the dataset, loaded in a triplestore, to answer queries that non-technical users cannot respond to directly because of the number of records contained in the dataset.

## 2. Transformation process

### 2.1 Selection of the dataset

I selected the data set containing the `Infant mortality rate` indicator published by [The United Nations Children's Fund (UNICEF)](https://www.unicef.org). The data set is available in the [UNICEF Open Data portal](https://data.unicef.org/), also known as UNICEF Data Warehouse, which publishes many freely available and distributable datasets that are part of UNICEF's Open Data initiative. It is also available in the [Humanitarian Data Exchange Hub](https://data.humdata.org), a catalog of open humanitarian data.

The full dataset with all the indicators includes 4,1789 data points, each representing the `Infant mortality rate` indicator value for a given country. The indicator data is drawn from inter-agency estimates and nationally representative household surveys such as Multiple Indicator Cluster Surveys (MICS) and Demographic and Health Surveys (DHS).

I downloaded the data in CSV format from the [data set's web page](https://data.humdata.org/dataset/unicef-cme-mry0) in the Humanitarian Data Exchange Hub.

As stated on the website, the data set is licensed under the terms of the Creative Commons Attribution-NonCommercial 3.0 IGO ([CC BY-NC 3.0 IGO](https://creativecommons.org/licenses/by-nc/3.0/igo/deed.en)) license.

The data set is available in this repository at the path [./data/CME.csv.gz](/data/CME.csv.gz).

## 9. Bibliography

This project leverages the following resources available in the Internet:

- [UNICEF Open Data portal](https://data.unicef.org/)
- [Humanitarian Data Exchange Hub](https://data.humdata.org)
- [Infant mortality rate data set's web page](https://data.humdata.org/dataset/unicef-cme-mry0)
- [CC BY-NC 3.0 IGO license](https://creativecommons.org/licenses/by-nc/3.0/igo/deed.en)
