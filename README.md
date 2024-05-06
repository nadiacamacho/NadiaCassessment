# Streamlit MySQL CRUD Application

## Overview
This is a simple Streamlit application that performs basic CRUD (Create, Read, Update, Delete) operations on a MySQL database. The database schema used for this application includes a single table named `sales` with the following fields:

- `id` (INT)
- `store_code` (VARCHAR)
- `total_sale` (DECIMAL)
- `transaction_date` (DATE)

The application allows the user to:
- Create a new record
- Read all existing records
- Update an existing record
- Delete an existing record

## Prerequisites
Ensure you have the following dependencies and requirements installed on your system before running the application.

### 1. Software Requirements
- Python 3.x
- MySQL Server
- PyCharm IDE (Optional)
### 2. Python Libraries
Install the required libraries using pip:

```bash
pip install streamlit mysql-connector-python
```
### Set up a virtual environment
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```
## MySQL Database Setup
Make sure you have a MySQL server running and a database named storedata with a table named sales. You can create these by running the following SQL commands:
CREATE DATABASE storedata;
```
USE storedata;

CREATE TABLE sales (
    id INT PRIMARY KEY,
    store_code VARCHAR(10),
    total_sale DECIMAL(10, 2),
    transaction_date DATE
);
```
## Loading Data into MySQL
You will need to load data into the sales table from an Excel file named MOCK_DATA.xlsx. First, convert the Excel file to CSV format.

Convert to CSV
- Open MOCK_DATA.xlsx in Excel.
- Go to File > Save As.
- Choose the CSV (Comma delimited) format and save the file as MOCK_DATA.csv.
- Load CSV Data into MySQL using MySQL Workbench
- Open MySQL Workbench and connect to your MySQL server.
- Right-click the sales table and select Table Data Import Wizard.
- Click Next and then browse to the MOCK_DATA.csv file.
- Follow the wizard instructions when importing the data.


## MySQL Database Setup
Ensure that the MySQL server credentials specified in the code match your MySQL server configuration
In the code, replace the following values with your own:
```
host="localhost",
user="root",
password="yourpassword",
database="storedata"
```
## Running the Application
To start the application, use the following command in your terminal:
```
streamlit run app.py
```
