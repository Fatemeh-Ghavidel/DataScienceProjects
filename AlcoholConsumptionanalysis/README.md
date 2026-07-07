
# Introduction
## **Project Title**:

Analysis Weekly Alcohol Consumption among secondary school  students 

## **Dataset:** 

Dataset was downloaded from Kaggle: 
https://www.kaggle.com/datasets/uciml/student-alcohol-consumption

It consists of survey data from secondary school students, examining various features in relation to their alcohol consumption. The features characterize students across multiple dimensions including:
* Education
* Family background 
* Leisure time activities
* Personality traits
**Target Variable:** Weekly alcohol consumption times (`Walc`)

## Objective: 
This project aims to:

* Analyze the distribution of features in the dataset

* Investigation the correlation between alcohol consumption and other features:
	* Identify features  that may lead to higher consumptions 
	* Determine features that may be influenced by higher consumption (e.g., health and  academic performance ) 



# Method:
## Problem Formulation

The problem is framed as a binary classification task. While this simplifies the problem, it leads to better model accuracy. 
## Machine Learning Models

The following machine learning models were implemented: 
* `Logistic Regression`
* `Random Forest classifier`
* `Xgboost classifier`
* `Support Vector Classifier (SVC)`.  

**Model Performance:** Achieved accuracy ranging from 0.67 to 0.78 across different models.

## **Alternative Target Formulation:** 

The problem was explored using different forms of the target variable by combining `Walc` (weekly alcohol consumption) and `Dalc` (daily alcohol consumption):

|Method|Description|
|---|---|
|Weighted sum|Weighted combination of Walc and Dalc|
|Product|Multiplication of Dalc and Walc|
|Walc only|Retained Walc as target, removed Dalc|
|Average|Mean of Dalc and Walc|

### Feature Engineering

|Feature|Transformation|
|---|---|
|**Age**|Grouped into two age categories|
|**G (Grades)**|Average of three grade components (G1, G2, G3)|

## Data Exploratory Analysis (EDA):

What was analyzed:
* Distribution of features across each category with respect to `Walc`  
* Correlation between the target variable and  features in each category   
**Note:** Detailed results are documented in accompanying analysis file. 

## Data Preprocessing: 

### Data Types

The dataset contains both categorical (ordinal or nominal) and numerical data. 

### Preprocessing Steps 

|Feature Type|Processing Method|
|---|---|
|Binary (Yes/No)|Converted to 0/1 using `LabelEncoder`|
|Ordinal categorical|Retained as numerical values|
|Nominal categorical|One-hot encoded using `get_dummies`|



# Model Building Pipeline:

The following sequential steps were followed for model development: 

1. Specify features and target variable
2. Split the dataset into training and testing sets
3. Scale features (Standardization)

For each model, the following steps were performed:

4. Train the model on training data
5. Evaluate the model performance on test data


# Files Execution Order: 

The project was executed in the following logical sequence: 

1. imports
2. data-loading
3. data-ingestion
4. data-visualization 
5. data-analysis 
6. data-processing  
7. model-building




