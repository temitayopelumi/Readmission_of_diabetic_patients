# Prediction of Readmission of Diabetic patients

## The aim of this is to predict if a patient will be readmitted within 30 days and to know what causes the readmission so that prevention can be made.

## How Does this work

This system is a flask web application hosted on heroku. The user(targeted at hosipital workers) has to input some data and get the prediction immediately. the system is built  using HTML and Bootstrap. The data trained using Catboost Classifier, sterilized with Pickle.

## Dataset
The dataset is gotten from the University of california ivrine machine learning Repository.


The dataset represents 10 years (1999-2008) of clinical care at 130 US hospitals and integrated delivery networks. It includes over 50 features representing patient and hospital outcomes. Information was extracted from the database for encounters that satisfied the following criteria.
(1) It is an inpatient encounter (a hospital admission).
(2) It is a diabetic encounter, that is, one during which any kind of diabetes was entered to the system as a diagnosis.
(3) The length of stay was at least 1 day and at most 14 days.
(4) Laboratory tests were performed during the encounter.
(5) Medications were administered during the encounter.
The data contains such attributes as patient number, race, gender, age, admission type, time in hospital, medical specialty of admitting physician, number of lab test performed, HbA1c test result, diagnosis, number of medication, diabetic medications, number of outpatient, inpatient, and emergency visits in the year before the hospitalization, etc.

[Download the data her](https://archive.ics.uci.edu/ml/datasets/diabetes+130-us+hospitals+for+years+1999-2008#)

## Technology Used are
1.Flask
2.Heroku
edit(i used scalingo first)
3.Pickle

## Project demo
https://predicition.herokuapp.com/

## Prerequisites

All the dependencies and required libraries are included in the file requirements.txt [See here](https://github.com/temitayopelumi/Readmission_of_diabetic_patients/blob/main/requirements.txt)


Made By Olalekan Temitayo


