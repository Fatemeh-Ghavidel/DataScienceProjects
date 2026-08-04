
# Business Problem
Pistachio Small Family Business Analysis

# Dataset
The dataset is provided as `PistachioBusiness.csv`, which can be downloaded from the [DataScienceProject](https://github.com/Fatemeh-Ghavidel/DataScienceProjects) repository. The dataset is available in CSV format, and a zip file is also provided to test the data launching pipeline. Feel free to try either option.
Each row represents a single product sale, with various features described below.
Instead of NaN values, question marks have been used to indicate missing data, which will need to be converted to NaN values during the preprocessing stage.

**Features:** 
- **`amount`** : Weight of the sold product in kilograms (Kg). Data type: `str`
- **`selling`** : Method of sale; traditional (through personal connections), online (via the Internet), or in person. Data type: `str`
- **`paying`** : Payment method; credit card, cash, or item exchange. Data type: `str`
- **`type`** : Product type; dry or wet. Data type: `str`
- **`year`** : Year of sale. Data type: `int`
- **`date`** : Exact date of sale. Data type: `str`
**Target:**
- **`price`** : Price of the sold product (×1000 Toman)

**Data Type Conversions Required:**
- `amount`: string → float32
- `year`: float32 → string

# Method
## Data Analysis 

The `Pistachio` class is defined to perform all feature evaluations on the data for each year, supporting the data analysis process; for example, calculating the total weight sold per year for each sample.

 The `SoldProduct` class incorporates product type as an additional feature to extract subsets of data for analysis, as pricing differs between wet and dry products
 
- **`total_weight_type`** : Calculates how many kilograms of wet or dry product were sold per year.
- **`total_weight_wet`** : Adjusts the total annual sales by converting dry product weight to its wet equivalent (since 1 kg of dry product is approximately equivalent to 3 kg of wet product).
- **`total_price_type`** : Calculates the total price for each product type per year.

At the end, the class outputs a summary of business performance, generating the following values:
- `total_weight_wet`
- `total_weight_dry`
- `adjusted_total_weight`
- `total_price_wet`
- `total_price_dry`
- `total_price`         

### Analysis Overview
The project examines the following aspects:
- Distribution of selling weights for each product type per year
- Correlation between price and weight for each product type
- Percentage of total weight contributed by each product type per year
- Distribution of selling and payment method categories
- Average price for each weight category by product type
- Daily sales comparison for both price and weight
All insights from the data analysis and corresponding figures can be found in the `PistachioDataAnalysis` file.

# File Execution Order
1. `imports`
2. `data_launching`
3. `data_ingestion`
4. `data_processing`
5. `pistachio_class`
6. `exploratory_data_analysis`
7. `model_building`









> 

