# GSTR-1 Summery Report Automation: Python Project

## Project Overview


This project automates the generation of GSTR-1 reports using Python and Pandas, eliminating the need for manual processing in Excel. It extracts, cleans, and structures GST-related data, ensuring accurate and efficient reporting for tax compliance. 
- Utilise the `.ipynb` file to comprehend the coding process. 
- Use a `.py` file for automation and reusability.
### Key Features:

- Automated Data Processing: Cleans and organizes raw invoice data.
- Tax Computation: Calculates GST, taxable values, HSN Summery and other required fields.
- Pivot & Aggregation: Summarizes data by category, customer, and tax Rates.
- Excel Export: Generates a ready-to-file GSTR-1 Summery report.


---

##  Steps


### 1. Download Masters Data
   - **Dataset Link**: https://github.com/RutwikDeuskar/GSTR-1-Summery-Report-Automation/blob/main/Master_Files.zip

### 2. Explore the Data
   - **Goal**: Conduct an initial data exploration to understand data distribution, check column names, types, and identify potential issues.
   - **Analysis**: Use functions like `.info()` and `.head()` to get a quick overview of the data structure.

### 3. Data Cleaning
   - **Handle Missing Values**: Drop rows or columns with missing values if they are insignificant; fill values where essential.
   - **Validation**: Check for any remaining inconsistencies and verify the cleaned data.

### 4. Understand Basic Concepts of GST
   - **State Code**: First 2 numbers of GSTN represents STATE CODE of GSTN holder.	
   - **CGST/SGST/IGST**: When Supplier And Recipients have same state CGST & SGST will apply. When they have different States IGST will apply.
   - **B2B/B2C/CDNR**: When there is no GST number available it means its B2C sell or Export, but here i assumed there is no export. CDNR means credit/debit notes of register person. Invoice with GSTN is B2B supply
   - ** Taxable Value**: Sale value before GST, to which GST will be added. 

### 5. Transform Data
   - **Merge all Relevant Data**: 
    	- Merge product master to get product data such as GST-Rate, HSN, Price
	- Merge State code with above steps(4), get customer state code
	- from customer state determine CGST/SGST/IGST
	- Merge Customer Data With GST number to get Customer Name
	- Group B2B,B2C,CDNR Supplies in respected tables of GSTR1

### 6. Conduct analysis using the data.
   - **HSN Wise Tax Summery**: Perform a summary of GST by HSN using Groupby or Pivot_table.
   - **GTSR -1 Table Summery** Perform a summary of GST by R1 Table using Groupby or Pivot_table.

### 7. Export report to Excel.
   - Export All reports Along with Main Data file back to excel using ExcelWriter.



---

## Requirements

- **Python 3.8+**
- **Python Libraries**:
  - `pandas`, `numpy`




---

## Project Structure

```plaintext
|-- data/                     # Raw data and transformed data
|-- notebooks/                # Jupyter notebooks for Python analysis
|-- README.md                 # Project documentation
|-- requirements.txt          # List of required Python libraries
|-- main.py                   # Main script for Automation
```
---
