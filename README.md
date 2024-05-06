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

### 2. Python Libraries
Install the required libraries using pip:

```bash
pip install streamlit mysql-connector-python
