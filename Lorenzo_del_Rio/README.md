# Final Project Report

- **Subject:** Semantic web and linked data
- **Master program:** Research in Artificial Intelligence
- **University:** [Universidad Internacional Menéndez Pelayo](https://www.uimp.es)
- **Author:** Lorenzo del Río Trujillo, [lorenzo_del_rio@hotmail.com](mailto:lorenzo_del_rio@hotmail.com)
- **Date:** May, 2025
- **Version:** 1.0

## Table of contents

- [1. Introduction](#1-introduction)
  - [1.1. Input/outputs](#21-input-outputs)
  - [1.2. Process outline](#22-process-outline)
- [2. Transformation process](#2-transformation-process)
  - [2.1. Selection of the data set](#21-selection-of-the-data-set)
  - [2.2. Analysis of the data set](#22-analysis-of-the-data-set)
  - [2.3. Naming stratregy](#23-naming-strategy)
  - [2.4. Ontology development](#24-ontology-development)
  - [2.5. External links](#25-external-links)
  - [2.6. Data mapping from csv to rdf/xml](#26-data-mapping-from-csv-to-rdf-xml)
  - [2.7. OpenRefine project](#27-openrefine-project)
- [3. Publication & access ](#3-publication-and-access)
  - [3.1. GraphDB](#31-graph-db)
  - [3.2. Python/SPARQLWrapper Interface](#32-python-sparql-wrapper-interface)
- [4. Conclusions](#4-conclusions)
- [5. Bibliography](#5-bibliography)

## 1. Introduction

This document describes the final project for the subject "Semantic web and linked data," part of the University Master's "Research in Artificial Intelligence" from the Universidad Internacional Menéndez Pelayo.

In particular, this project consists of the selection, transformation, preparation, and publication in GraphDB of a dataset about german credit data taken from the "UC Irvine Machine Learning Repository" (https://archive.ics.uci.edu). 

As part of the project a python script will allow an user to extract data from the dataset using SPARQL queries.

### 1.1. Input/outputs

#### 1.1.1. Dataset
The dataset contains 1000 rows and includes some demographic data (gender, marital status, job level) and also bank related data (if has or not credits, salary range, installment plans...). The dataset does not reflect the current parameter values for any given client, as it is intended for developing classification algorithms to predict whether a debtor will be good or bad (i.e., whether they will repay the credit or not).The dataset reflect the values of the parameteres at the time of its creation.

#### 1.1.2. Results
The main outcomes are:
- Ontology (reusing when possible/appropriate standard vocabularies)
- Dataset in rdf format including references to external datasources
- Dataset published in GraphDB
- Python script to query the data

### 1.2. Process outline
To get the results the following steps have been followed:
- Selection and analysis of the dataset.
- Set naming strategy
- Develop the ontology 
- Link/reconcile data with external datasources
- Generate rdf output
- Publish GraphDB
- Creation of the python script with SPARQLwrapper to query the data

## 2. Transformation process

### 2.1. Selection of the data set and additional info on it
I selected this dataset as it has a moderate but significant number of records, some columns that are described in standard vocabularies and also some information that could be linked to external sources.

There is no mention of any particular bank. Also there is no explicit info that allows to link each record with any specific person. It's licensed by the owner, which is also the creator. The dataset is meant to be used in the development of credit classification of customers. For the purposes of the project is not essential if the data has been made up or if it's extracted from actual bank data so no further inquiries have been done on this respect.

The dataset has been downloaded from https://archive.ics.uci.edu/
[German Credit Data](https://archive.ics.uci.edu/dataset/144)
and can be found in this repository at [./data/statlog+german+credit+data.zip](/data/statlog+german+credit+data.zip)

The zip file includes two datasets, an index document and a word document with the description of the fields. The two datasets are equivalent, one is the original (german.data) and the other is derived, replacing non-numeric fields with numeric fields (german.data-numeric) for use in classification algorithms that do not support non-numeric data.

This dataset is made available under the Creative Commons Attribution 4.0 International License, so the user is free to share the material, including adapt and transform it. However, the user must give appropriate credit to the publisher of the data set, provide a link to the license and indicate if changes were made. All these info can be found in the archive LICENSE in the root folder of this repository. This job is licensed under the terms in the ./LICENSE file in the repo.


### 2.2. Analysis of the data set

#### 2.2.1. Explorative Data Analysis of the data set

I selected [OpenRefine](https://openrefine.org) to prepare and do an initial transform the data, as according to what was demonstrated in the course materials has all the features needed for this task.
The OpenRefine project is available in the repo (./openrefine/german-data.openrefine.tar.gz)

After creating the project `German credit` and importing the CSV into it, I proceeded with the schema and metadata analysis. 

Each row in the input dataset is a independent record that represent a credit evaluation. The data included seems to be the bare information needed for the evaluation and the result of the evaluation. Otherwise seemingly important data is not present (like customer personal info or credit additional info like date of the request or some specific credit conditions as if interest is fixed or not)
Each row has the following info (for coded fields note that not all code values are represented in the actual dataset):

- **status_checking_account**: Status of existing checking account  
        | code | meaning                                                       |
        |------|---------------------------------------------------------------|
        | A11  | x < 0 DM                                                      |
        | A12  | 0 <= x < 200 DM                                               |
        | A13  | x >= 200 DM / salary assignments for at least 1 year          |
        | A14  | no checking account                                           |

- **duration**: Duration of the requested loan in months.

- **credit_history**: Credit history  
        | code | meaning                                                      |
        |------|--------------------------------------------------------------|
        | A30  | no credits taken / all credits paid back duly                |
        | A31  | all credits at this bank paid back duly                      |
        | A32  | existing credits paid back duly till now                     |
        | A33  | delay in paying off in the past                              |
        | A34  | critical account / other credits existing (not at this bank) |

- **purpose**: Purpose of the loan  
        | code  | meaning                 |
        |-------|-------------------------|
        | A40   | car (new)               |
        | A41   | car (used)              |
        | A42   | furniture/equipment     |
        | A43   | radio/television        |
        | A44   | domestic appliances     |
        | A45   | repairs                 |
        | A46   | education               |
        | A47   | vacation                |
        | A48   | retraining              |
        | A49   | business                |
        | A410  | others                  |

- **credit_amount**: Credit amount requested. The currency is not explicitly defined in the dataset, could be DM (Deutsche Marks) but if relevant should be asked to the dataset owner/creator. It will be kept undefined in this work.

- **savings_account**: Savings account or bonds  
        | code | meaning  (x is the amount)     |
        |------|--------------------------------|
        | A61  | x < 100 DM                     |
        | A62  | 100 <= x < 500 DM              |
        | A63  | 500 <= x < 1000 DM             |
        | A64  | x >= 1000 DM                   |
        | A65  | unknown / no savings account   |

- **present_employment**: Present employment duration  
        | code | meaning (the duration refers to current employment)     |
        |------|---------------------------------------------------------|
        | A71  | unemployed                                              |
        | A72  | employed less than 1 year                               |
        | A73  | emmployed between 1 and 4 years                         |
        | A74  | employed between 4 and 7 years                          |
        | A75  | employed over 7 years                                   |

- **installment_rate**: Installment rate in percentage of disposable income.

- **personal_status_sex**: Personal status and sex  
        | code | meaning                                  |
        |------|------------------------------------------|
        | A91  | male : divorced/separated                |
        | A92  | female : divorced/separated/married      |
        | A93  | male : single                            |
        | A94  | male : married/widowed                   |
        | A95  | female : single                          |

- **other_debtors_guarantors**: Other debtors or guarantors  
        | code  | meaning        |
        |-------|----------------|
        | A101  | none           |
        | A102  | co-applicant   |
        | A103  | guarantor      |

- **present_residence**: Present residence duration. The unit is not explictly defined in the word document so we assume years. The found values (see below) are 1 to 4 so perhaps the meaning of this field described in the word as "numeric" and "Present residence since" has been misunderstood. As it's not essential for the purposes of this exercise it will described as 'Present residence duration' considering the unit 'years', but please note that perhaps is not the actual meaning. Should it be important the exact meaning should clarified with the dataset owner.

- **property**: Type of property  
        | code  | meaning                                                      |
        |-------|--------------------------------------------------------------|
        | A121  | real estate                                                  |
        | A122  | building society savings agreement / life insurance          |
        | A123  | car or other, not in attribute 6                             |
        | A124  | unknown / no property                                        |

- **age**: The age of the customer.

- **other_installment_plans**: Other installment plans  
        | code  | meaning |
        |-------|---------|
        | A141  | bank    |
        | A142  | stores  |
        | A143  | none    |

- **housing**: Housing situation  
        | code  | meaning |
        |-------|---------|
        | A151  | rent    |
        | A152  | own     |
        | A153  | for free|

- **existing_credits**: Number of existing credits at this bank.

- **job**: Occupation/job type  
        | code  | meaning                                                   |
        |-------|-----------------------------------------------------------|
        | A171  | unemployed / unskilled – non-resident                     |
        | A172  | unskilled – resident                                      |
        | A173  | skilled employee / official                               |
        | A174  | management / self-employed / highly qualified employee    |

- **dependents**: Number of people being liable to provide maintenance for.

- **telephone**: Telephone ownership  
        | code  | meaning                                      |
        |-------|----------------------------------------------|
        | A191  | none                                         |
        | A192  | yes, registered under the customer's name    |

- **foreign_worker**: Whether the customer is a foreign worker  
        | code  | meaning |
        |-------|---------|
        | A201  | yes     |
        | A202  | no      |

- **class**: If the risk is good or bad. The 'code' has only numeric values but should be considered as text code with represents the meaning in the table, it's not a numeric value.  
        | code | meaning                                      |
        |------|----------------------------------------------|
        | 1    | Good credit risk (will repay as agreed)      |
        | 2    | Bad credit risk (will default, pay late, etc)|


Using facets I have validated that the cualitative columns have the expected values and also that the numeric ones have values that make sense (for instance regarding age, number of dependants, etc). 
All fields are populated for all rows. Unless told otherwise for coded values all codes are represented:
- **status_checking_account**: Values follow the expected coding scheme
- **duration**: 4 to 73 monts.
- **credit_history**: Values follow the expected coding scheme
- **purpose**: Values follow the expected coding scheme. A47 (vacation) is not present.
- **credit_amount**: 250 - 18424. In this case the fact histogram shows 0-19000, I got the actual max/min by using the sort function.
- **savings_account**: Values follow the expected coding scheme
- **present_employment**: Values follow the expected coding scheme  
- **installment_rate**: 1% to 4% 
- **personal_status_sex**: Values follow the expected coding scheme. A95 (female:single) is not present
- **other_debtors_guarantors**: Values follow the expected coding scheme.
- **present_residence**: 1 to 4. 
- **property**: Values follow the expected coding scheme.
- **age**: 19 to 76.
- **other_installment_plans**: Values follow the expected coding scheme.
- **housing**: Values follow the expected coding scheme.
- **existing_credits**: 1 to 4.
- **job**: Values follow the expected coding scheme.
- **dependents**: 1-2.
- **telephone**: Values follow the expected coding scheme. 
- **foreign_worker**: Values follow the expected coding scheme. 
- **class**:  Values follow the expected coding scheme. 


Please find below images of the OpenRefine facets for the different fields of the dataset:
![Facets 1 ](./images/Facets_first.PNG)
![Facets 2 ](./images/Facets_second.PNG)
![Facets 3 ](./images/Facets_third.PNG)
![Facets 4 ](./images/Facets_fourth.PNG)


#### 2.2.2. Changes done to the dataset
##### 2.2.2.1 Columns added
As the columns have not unique identifier a row_number column is added (values 1-1000). Its done using Edit column -> Add column based on this column and typing
```
row.index + 1
```
in the GREL expression box.

As the assignment requires to link data we will derive a couple of columns to link to dbpedia. One will be a direct link and for the other we will keep a human readable label and the link will be done using owl same as. 

The columns will be derived from personal_status_sex and present_employment.

personal_status_sex has the following codes:
        | code | meaning                                  |
        |------|------------------------------------------|
        | A91  | male : divorced/separated                |
        | A92  | female : divorced/separated/married      |
        | A93  | male : single                            |
        | A94  | male : married/widowed                   |
        | A95  | female : single                          |
so the new column sex will contain
https://dbpedia.org/resource/Male if personal_status_sex has values A91, A93, A94
https://dbpedia.org/resource/Female if personal_status_sex has values A92, A95

To achieve it Python has been used instead of GREL, as OpenRefine also allows use of Python in the expression to transform  a column:
return "https://dbpedia.org/resource/Male" if value in ["A91", "A93", "A94"] else \
       "https://dbpedia.org/resource/Female" if value in ["A92", "A95"] else None


present_employment has the following codes:
        | code | meaning (the duration refers to current employment)     |
        |------|---------------------------------------------------------|
        | A71  | unemployed                                              |
        | A72  | employed less than 1 year                               |
        | A73  | emmployed between 1 and 4 years                         |
        | A74  | employed between 4 and 7 years                          |
        | A75  | employed over 7 years                                   |
a new column "employment_status" will be derived from this one, will contain:
unemployed if present_employment is A71
employed if present_employment is A72, A73, A74, A75
To achieve it Python has been used instead of GREL, as OpenRefine also allows use of Python in the expression to transform  a column:
return "unemployed" if value in ["A71"] else \
       "employed" if value in ["A72", "A73", "A74", "A75"] else None


#### 2.2.3. Final fields 
After the changes the fields of the datasets are:
- **row_number**
- **status_checking_account**
- **duration**
- **credit_history**
- **purpose**
- **credit_amount**
- **savings_account**
- **present_employment**
- **employment_status**
- **installment_rate**
- **personal_status_sex**
- **sex**
- **other_debtors_guarantors**
- **present_residence**
- **property**
- **age**
- **other_installment_plans**
- **housing**
- **existing_credits**
- **job**
- **dependents**
- **telephone**
- **foreign_worker**
- **class**

The dataset once transformed with OpenRefine to add these columns can be found in the repository:
german-data_transformed.csv

### 2.3. Naming strategy
As recommended in the training materials:
- For the individual objects the separator will be the slash (`/`)  (big amount of items that could change in data refresh)
- For the ontology the separator will be the hash ('#') (small amount of items with no or few expected changes). The codes "concept schemes/concepts" will be part of the ontology

There will be two main classes of individuals, credit_evaluation and credit_requestor, additional details on this can be found in section 2.4 Ontology Development

Let's assume that we own the domain creditclassification.biz . The following prefixes will be used (ccf -> credit classification):

* `http://data.creditclassification.biz/ontology/ccf#` for the ontology terms;
* `http://data.creditclassification.biz/resource/ccf/credit_evaluation/` for each individual credit classification.
* `http://data.creditclassification.biz/resource/ccf/credit_requestor` for each credit requestor.
* `http://data.creditclassification.biz/resource/ccf/<concept_category>#` for the concept categories (coded fields).


And so the generated URIs will be:

* `http://data.creditclassification.biz/ontology/ccf#<term>` for ontology terms;
* `http://data.creditclassification.biz/resource/ccf/credit_evaluation/<credit_evaluation_id>` for each credit classification.
* `http://data.creditclassification.biz/resource/ccf/credit_requestor/<credit_requestor_id>` for each credit requestor.
* `http://data.creditclassification.biz/resource/ccf/<concept_category>#<concept>` for the different code values .


The ids for credit evaluation and credit requestor will be generated from the row_id added to the dataset. E<row_id> for the credit evaluation and R<row_id> for the credit requestor. 

The URI naming cannot be enforced at ontology level using OWL alone (it's possible with additional tools like SHACL), but an annotation can be provided in each class explaining how URIs should be created. 

Initially for the code values the naming scheme was conceived as for the other ontolology terms:
* `http://data.creditclassification.biz/ontology/ccf#<term>`
This could be valid as of now because the code names, except for the class (credit class) have the following structure:
A<columNumber><codenumber>
So the code names do not overlap. But if in the future new code schemes are added with different coding rules they could overlap rendering insufficient the initial (simpler) approach. Hence a more scalable approach was followed:
* `http://data.creditclassification.biz/resource/ccf/<concept_category>#<concept>`

To transform the URIs in the ontology file from the 'plain' to the 'nested' approach the following python program was developed:
./codeAux/transformXml.py
It does not use any rdf library, takes advantage of the xml format in which the file is stored as I am familiar with xml processing.

### 2.4. Ontology development
#### 2.4.1. General approach/tools
Each row in the dataset represents the risk of a requested loan. Many of the info is related to the requestor and other part of the info is related to the loan, including the risk evaluation. 
We do not know any identification data for these customers but they are still banking customers and to represent them we can extend the 'Party' class of the FIBO (Financial Industry Business Ontology) to represent them. As the dataset does not explicitly tell that the requestors are people 'Party' was preferred to subclass, at the concept 'Party' would allow also for businesses. 
The class name will be credit_requestor and the identification will be based in the row_number column. 

Regarding the info of the credit FIBO could also be used as it has an extensive vocabulary for loans and credits but is very complex and also it seems interesting for the practice to include other estandar ontology. Then the class Loan or Credit of schema.org is used to derive the credit_evaluation class. The identification of each credit_evaluation individual will be based also in the row_number column. 

Descriptions and/or usage notes have been added for some classes and properties as demonstration of the capabilities of the model; as the ontology is not for real use I did not invest time in creating descriptions/annotations for all the classes/properties.

Regarding external linking different approaches were used to demonstrate in this work several ways in which this could be done. One has been used for "coded columns", other for column 'sex' and other for column 'unemployment'. A common approach would have been easier and also more consistent and should be the choice in an ontology for 'real world' use. 

##### 2.4.1.2 DataTypes in schema.org
When trying to use schema.org in Protégé the version that worked best was an experimental OWL version of schema.org. The problem with this version is that it enforces strict OWL and properties that in the original schema.org ontology are Data Properties (literals) end up being Object Properties which inherit from DataType. For instance "amount" is a property with range Number which is a subclass of DataType.
Then no property in the OWL schema.org ontology has domain 'Number' so it's not well defined the actual 'number' is represented as a property of the class 'Number'.

A custom property could have been defined having domain 'Number' (or 'Text' for the case of the loan duration), but for the sake of simplicity, and to follow how schema.org is commonly used, wherever an individual has a schema.org property whose range is a subclass of 'DataType' it's used as a data property (literal).

##### 2.4.1.3 Coded columns
The coded columns will be mapped as skos concept schemes, each code value being a skos concept. For some of the codes external references have been added. For some of the codes labels in several languages (Spanish, French and Esperanto have been added). Additional info on these columns is provided in section 2.4.3 Coded fields

##### 2.4.1.4 Tools
The ontology has been developed using the following tools:
- Protégé as main tool for the development of the ontology and exporting it to rdf/Turtle.
- Visual Code with the plugin Stardog for RDF Grammars to do some direct changes in the rdf/xml.
- Grok, to get the labels in several languages.
- chatGPT to get the wikidata and DBpedia references for the 'purpose' and 'foreing_worker' different values. A manual revision of all references has been needed so I do not recommend to use chatGPT for this purpose. 
- Python to transform code element URIs from 'plain' to 'nested' (as explained in section 2.3. Naming strategy)

In the following sections of this topic more info about the classes and properties will be provided.

#### 2.4.3. credit_requestor
credit_requestor represents the entity requesting the credit whose risk is being evaluated. 
It inherits from FIBO Party class as the info is finacial-related and also related to an actor which is not an automated agent but also we do not know if is a business or an individual customer so Party is a suitable superclass for credit_requestor.
The following fields (or some transformation of them) of the dataset will be mapped as properties of credit_requestor:

- **row_number**
- **status_checking_account**
- **credit_history**
- **savings_account**
- **present_employment**
- **employment_status**
- **personal_status_sex**
- **sex**
- **other_debtors_guarantors**
- **present_residence**
- **property**
- **other_installment_plans**
- **housing**
- **existing_credits**
- **job**
- **dependents**
- **telephone**
- **foreign_worker**



#### 2.4.4. credit_evaluation
credit_evaluation represents the loan requested and its evaluation ('class'). 
It inherits from schema.org 'LoanOrCredit', that has the main fields of the load (term and amount). 

The following fields (or some transformation of them) of the dataset will be mapped as properties of credit_evaluation:

- **row_number**
- **duration**
- **age**
- **purpose**
- **credit_amount**
- **class**
- **installment_rate**

'age' is included in the credit_evaluation as it is considered to be the age of the requestor in the moment the evaluation was done, so this property is bound to the evaluation (the actual age of the requestor will increase with time, consider that if we add further evaluations to a requestor 'age' will be different for each evaluation)

#### 2.4.3. Coded fields

The following fields are coded fields:
- **status_checking_account**
- **credit_history**
- **purpose**
- **savings_account**
- **present_employment**
- **personal_status_sex**
- **other_debtors_guarantors**
- **property**
- **other_installment_plans**
- **housing**
- **job**
- **telephone**
- **foreign_worker**
- **class**

The general approach to integrate those coded fields in the ontology has been:
- Each field is mapped as individual of skos:ConceptScheme, with the same name of the field (for instance foreign_worker)
- Each code in each field is mapped as an individual of skos:Concept, with the code being the identifier of the individual. A skos:altLabel in English contains the meaning of the code as provided by the dataset creator.
The property skos:inScheme is used to relate the codes with their ConceptScheme
- For each code field a subclass of OMG CodeElement has been created, so we can use it to describe the range in a property as the inviduals of the subclass (the list of codes of a code field). The class will be named as the field + '_code' (for instance foreing_worker_code)
- For each code field an object property has been created with domain 'credit_requestor' (or 'credit_evaluation' depending on the specific code), so it can be used in the credit_requestor (or 'credit_evaluation') individuals. The object property name is 'has_' + <name of the field>, for instance 'has_foreing_worker'.

An example, for the foreing worker status will be:

- Concept scheme
```
    <owl:NamedIndividual rdf:about="http://data.creditclassification.biz/ontology/ccf#foreign_worker">
        <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#ConceptScheme"/>
        <terms:description>Foreign worker status</terms:description>
        <skos:prefLabel xml:lang="en">Foreign worker status</skos:prefLabel>
    </owl:NamedIndividual>
```

- Codes
```
    <!-- foreign_worker: yes -->
    <owl:NamedIndividual rdf:about="http://data.creditclassification.biz/ontology/ccf#A201">
        <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
        <skos:inScheme rdf:resource="http://data.creditclassification.biz/ontology/ccf#foreign_worker"/>
        <terms:description>yes</terms:description>
        <skos:altLabel xml:lang="en">yes</skos:altLabel>
    </owl:NamedIndividual>

    <!-- foreign_worker: no -->
    <owl:NamedIndividual rdf:about="http://data.creditclassification.biz/ontology/ccf#A202">
        <rdf:type rdf:resource="http://www.w3.org/2004/02/skos/core#Concept"/>
        <skos:inScheme rdf:resource="http://data.creditclassification.biz/ontology/ccf#foreign_worker"/>
        <terms:description>no</terms:description>
        <skos:altLabel xml:lang="en">no</skos:altLabel>
     </owl:NamedIndividual>
```
- Class that groups all the codes
```
   <owl:Class rdf:about="http://data.creditclassification.biz/ontology/ccf#foreign_worker_code">
        <rdfs:subClassOf rdf:resource="https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement"/>
        <owl:equivalentClass>
            <owl:Class>
                <owl:intersectionOf rdf:parseType="Collection">
                    <rdf:Description rdf:about="http://www.w3.org/2004/02/skos/core#Concept"/>
                    <owl:Restriction>
                        <owl:onProperty rdf:resource="http://www.w3.org/2004/02/skos/core#inScheme"/>
                        <owl:hasValue rdf:resource="http://data.creditclassification.biz/ontology/ccf#foreign_worker"/>
                    </owl:Restriction>
                </owl:intersectionOf>
            </owl:Class>
        </owl:equivalentClass>
    </owl:Class>
```    

- Property that has domain credit_requestor and range the set of codes of the field (foreing_worker_code)
```
    <owl:ObjectProperty rdf:about="http://data.creditclassification.biz/ontology/ccf#has_foreign_worker">
        <rdfs:domain rdf:resource="http://data.creditclassification.biz/ontology/ccf#credit_requestor"/>
        <rdfs:range rdf:resource="http://data.creditclassification.biz/ontology/ccf#foreign_worker_code"/>
        <rdfs:label xml:lang="en">has foreign worker status</rdfs:label>
    </owl:ObjectProperty>
```

Besides for the following fields labels in Spanish, French and Esperanto have been added (they could have been added for more fields or in other languages, but for demonstration purposes these could be enough):
- **credit_history**
- **present_employment**
- **personal_status_sex**
- **other_debtors_guarantors**
- **property**
- **other_installment_plans**
- **job**
- **telephone**
- **foreign_worker**
- **class**

And for the following fields some external references for their codes have been added (some with skos:exactMatch and other with skos:closeMatch). Sometimes two references are included, one to Dbpedia and other to wikidata, but sometimes only one of them is included:
- **purpose**
- **foreign_worker**


#### 2.4.4. Fields representing a lenght of time (duration)
The following fields are time lenght fields:

- **duration**
- **present_residence**
- **age**

##### 2.4.4.1 Age
It seems that 'age' could be reused from another vocabulary but he concept of 'age' was deprecated in FOAF favoring 'birth date', which allows to compute the actual age at any time. The Person Core Ontology also allows only to map 'age' indirectly, using birth date.
In this case the birth date cannot be inferred and also has no sense as 'age' is the age at the moment when the credit class (good or bad risk) was decided and this is a difference with the general concept of 'age', so a specific property derived from schema.org duration is defined ('age_when_risk_evaluated').
Considering this specific mean of 'age' this property has 'credit_evaluation' and not 'credit_requestor' as its domain (refer also to section 2.4.4. credit_evaluation)

##### 2.4.4.2 Duration
The duration will be represented using the 'LoanTerm' property. The range of LoanTerm is:
```
		<rdfs:range>
			<owl:Class>
				<owl:unionOf rdf:parseType="Collection">
					<owl:Class rdf:about="https://schema.org/QuantitativeValue"/>
					<owl:Class rdf:about="https://schema.org/Text"/>
					<owl:Class rdf:about="https://schema.org/URL"/>
					<owl:Class rdf:about="https://schema.org/Role"/>
				</owl:unionOf>
			</owl:Class>
```
For the best interoperability 'QuantitativeValue' could have been selected as it allows to respresent in a structured way the quantity and the unit. In this case in the dataset especification the unit is explicit so the usage of QuantitativeValue is not required and 'Text' will be used. 

##### 2.4.4.3 Present Residence
As stated in section 2.2.1 the unit for this field is not explictly defined so schema.org duration is used, using Text range. 

#### 2.4.5. Numeric fields
##### 2.4.5.1 Credit amount
The credit amount will be mapped to the amount property of 'LoanOrCredit', using the range 'Number', as the range 'MonetaryAmount' would require the currency and it's not defined.
A custom comment will be added to the property to explain that the currency is not defined.
##### 2.4.5.2 Existing credits
A custom data property is created to map this field.
##### 2.4.5.3 Dependents
A custom data property is created to map this field.
##### 2.4.5.3 Installment rate
A custom data property is created to map this field.
##### 2.4.5.4 Row number
The row number added with OpenRefine will be used to create the URIs for credit_evaluation and credit_requestor individuals.

#### 2.4.6. Other fields
A couple of fields were derived in the intial review/transformation stage to have fields that map with external entities, to model the relation with external entities in different ways. Besides two additional properties are added to link the credit requestor with the credit evaluation and the credit evaluation with its requestor.

##### 2.4.6.1. Sex
In this case when processing the initial dataset a new column was derived that has the link to Male or Female in DBpedia. A property 'hasSex' is created whose range is a custom created class that is limited to Male and Female individuals in dbpedia:

```
  <!-- Sex class restricted to Male and Female -->
  <owl:Class rdf:about="http://data.creditclassification.biz/ontology/ccf#Sex">
    <owl:oneOf rdf:parseType="Collection">
      <rdf:Description rdf:about="http://dbpedia.org/resource/Male"/>
      <rdf:Description rdf:about="http://dbpedia.org/resource/Female"/>
    </owl:oneOf>
    <rdfs:label xml:lang="en">Sex</rdfs:label>
    <rdfs:comment xml:lang="en">
      The class of biological sexes, limited to the individuals Male and Female from DBpedia.
    </rdfs:comment>
  </owl:Class>

  <!-- hasSex object property -->
  <owl:ObjectProperty rdf:about="http://data.creditclassification.biz/ontology/ccf#hasSex">
    <rdfs:domain rdf:resource="http://data.creditclassification.biz/ontology/ccf#credit_requestor"/>
    <rdfs:range rdf:resource="http://data.creditclassification.biz/ontology/ccf#Sex"/>
    <rdfs:label xml:lang="en">has sex</rfs:label>
    <rdfs:comment xml:lang="en">The biological sex of the credit requestor.</rdfs:comment>
  </owl:ObjectProperty>

```

##### 2.4.6.2. Employment status
In this case the info derived in the initial processing is 'unemployed' or 'employed'. The implementation for this property has been done defining first a datatype and then using it in the range of the property. The external links are defined as 'seeAlso' in the definition of the property.

```
<rdfs:Datatype rdf:about="http://data.creditclassification.biz/ontology/ccf#employment_status_enum">
  <owl:equivalentClass>
    <rdfs:Datatype>
      <owl:withRestrictions rdf:parseType="Collection">
        <rdf:Description>
          <xsd:pattern>employed|unemployed</xsd:pattern>
        </rdf:Description>
      </owl:withRestrictions>
      <rdfs:subClassOf rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
    </rdfs:Datatype>
  </owl:equivalentClass>
</rdfs:Datatype>

<owl:DatatypeProperty rdf:about="http://data.creditclassification.biz/ontology/ccf#has_employment_status">
  <rdfs:domain rdf:resource="http://data.creditclassification.biz/ontology/ccf#credit_requestor"/>
  <rdfs:range rdf:resource="http://data.creditclassification.biz/ontology/ccf#employment_status_enum"/>
  <rdfs:label xml:lang="en">has employment status</rdfs:label>
  <rdfs:comment xml:lang="en">
    The employment status as a string: 'employed' or 'unemployed'.
    Refer to DBpedia for more information.
  </rdfs:comment>
  <rdfs:seeAlso rdf:resource="http://dbpedia.org/resource/Employment"/>
  <rdfs:seeAlso rdf:resource="http://dbpedia.org/resource/Unemployment"/>
</owl:DatatypeProperty>
```
##### 2.4.6.1. has_credit_requestor / has_credit_evaluation
Two object properties are added, one to credit_requestor (has_credit_evaluation) and other to credit_evaluation (has_credit_requestor)
As a demonstration of how to set cardinallity of properties using OWL those two properties are bound to restrictions. A credit_requestor could have 0 to N credit_evaluation and a credit_evaluation must have 1 and only 1 credit_requestor.
This does not match what is in the initial dataset where due to the lack of exact identification of the requestor we consider each row a different requestor/evaluation so the relationship is 1-1 between evaluations and requestors, but in this way the initial dataset fits the model and also it makes possible to add more evaluations to a requestor.
Besides the relationship between the two properties is modelled with inverseOf, as for instance in has_credit_evaluation:
  <owl:inverseOf rdf:resource="http://data.creditclassification.biz/ontology/ccf#has_credit_requestor"/>

#### 2.4.7. Ontology validation
The ontology has been validated with OOPS (https://oops.linkeddata.es/), using RDF/XML format from Protégé and uploading in the validator. The first interaction yielded the following results:
Pitfalls detected:

Results for P04: Creating unconnected ontology elements.Minor 13 cases
Results for P07: Merging different concepts in the same class.Minor 2 cases
Results for P08: Missing annotations.Minor 37 cases
Results for P11: Missing domain or range in properties.Important 268 cases
Results for P12: Equivalent properties not explicitly declared.Important 13 cases
Results for P13: Inverse relationships not explicitly declared.Minor 122 cases
Results for P21: Using a miscellaneous class.Minor 2 cases
Results for P22: Using different naming conventions in the ontology.Minor Ontology*
Results for P30: Equivalent classes not explicitly declared.Important 7 cases
Results for P34: Untyped class.Important 5 cases
Results for P35: Untyped property. Important 1 case1 case

P04, P12, P30, P35 issues refer to the imported ontologies

P07 was due to a incorrect reference to http://schema.org/LoanOrCredit instead of the correct with https

P08 Some cases fixed, as stated in section 2.4.1 not all the items have been provided with annotations.

P11 All items with the problem but one are from imported ontologies. The only one in the credit classification ontology is:
 http://data.creditclassification.biz/ontology/ccf#age_when_risk_evaluated
I added the domain and range to the property.

P13 It affects to 16 items in the credit classification ontology, the other affected items are from imported ontologies. In any case I  decided to ignore P13, due to the purpose of the project I think that there is no need to define the inverse properties.

P21 refers to: 
› http://data.creditclassification.biz/ontology/ccf#other_installment_plans_code
› http://data.creditclassification.biz/ontology/ccf#other_debtors_guarantors_code
And I think they  have been classified as 'miscellaneous' class incorrectly, because the 'other' in their names is not meaning that is 'other' among several of the same 'superclass' but that refers to the credit requestor having other installment plans besides the requested loan or being with other debt obligations.

P22 Some of the items were named using 'CamelCase' and others using lower case and _ delimiter.  All are unified to lower case with _ delimiter. 

P34 Affects to several item. Of these two are fixed as they are from the cretit evaluation dataset. 
› http://example.org/ontology/EmploymentStatusEnum
› http://example.org/ontology/CreditRequestor


After the review:

Results for P04: Creating unconnected ontology elements.Minor 12 cases
Results for P07: Merging different concepts in the same class. Minor 1 case
Results for P08: Missing annotations.Minor 28 cases
Results for P11: Missing domain or range in properties.Important 267 cases
Results for P12: Equivalent properties not explicitly declared.Important 13 cases
Results for P13: Inverse relationships not explicitly declared.Minor 123 cases
Results for P21: Using a miscellaneous class.Minor 2 cases
Results for P22: Using different naming conventions in the ontology.Minor Ontology*
Results for P30: Equivalent classes not explicitly declared.Important 7 cases
Results for P34: Untyped class. Important 1 case
Results for P35: Untyped property. Important 1 case

P04, P12, P30, P35, P11, P34 issues refer to the imported ontologies
P08, P13, P21 were justified
P22 After changing camelCase ids to lower case with _ delimiter the warning stil appears, might be due to the code names, which start with capital 'A'. In any case is cosmetical (minor) and it's not explorer further. 

Together with the 'pitfalls' a warning is issued:
SUGGESTION: symmetric or transitive object properties  6 cases
This suggestion only affects imported ontologies.

#### 2.4.1. General approach/tools
The ontology in rdf/xml and Turtle format is delivered in the folder ./ontology of the repo (ccf.* files)


### 2.5. Data reconciliation
For the sex (male/female) and employment status (employed/unemployed) I searched manually in Dbpedia/Wikidata the matching resources. 
In case of the coded fields that include equivalences in Dbpedia/Wikidata I used ChatGPT to find them and then validated manually. As commented before I cannot recommend using ChatGPT for this task as in my case there were many cases in which the provided links pointed to resources that have no semantical relationship with the concepts.

### 2.6. Data mapping from csv to rdf/xml
For the datamapping I created a jinja2 template and then used a python script to render the final file from the csv and the jinja2 template.
Files involved:
- template_xml.j2 -> jinja2 word template
- csvTordf.py -> python script 
- german-data_transformed.csv -> csv generated from the initial dataset using openRefine
- german_data_rdf.rdf -> dataset tranformed to linked data rdf/xml

After processing the csv with the Python
They can be found in the folder ./transform of the repo

Protégé was used to validate the output file (german_data_rdf.rdf)

### 2.7. OpenRefine project
<pending to decide if this section will be present as there is other info about OpenRefine>

## 3. Publication & access
<pending>

### 3.1. GraphDB

### 3.2. Python/SPARQLWrapper Interface

## 4. Conclusions
<pending>
#### License 

#### other 

## 5. Bibliography
<pending>

