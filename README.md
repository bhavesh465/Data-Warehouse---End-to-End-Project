Data Warehouse & Analytics Pipeline ⚙️
An end-to-end data pipeline that extracts operational technology (OT) data using Python, warehouses it in Snowflake, and visualizes key metrics using Power BI.

This project serves as a complete blueprint for building a modern data warehouse. It automates the process of fetching data from a source (the "OT Downloader"), loading it into a scalable cloud data warehouse, and creating interactive dashboards for business intelligence and analysis.

📖 Table of Contents
Architecture

Tech Stack

Features

Getting Started

Prerequisites

Installation & Setup

Usage

Contributing

License

Contact

🏗️ Architecture
The project follows a classic Extract, Load, Transform (ELT) architecture:

Extract: A Python script (downloader.py) is scheduled to run periodically. It fetches the latest data from the source OT system (e.g., an API, a database, or log files).

Load: The raw data is immediately loaded into a landing schema in Snowflake, ensuring minimal data loss and a preserved raw history.

Transform: SQL models are run within Snowflake to clean, transform, and aggregate the raw data into analytics-ready tables (e.g., fact and dimension tables).

Visualize: Power BI connects directly to the transformed tables in Snowflake. A dashboard provides interactive visualizations and key performance indicators (KPIs) for business users.

🛠️ Tech Stack
Data Extraction: Python 3.9+ (pandas, snowflake-connector-python)

Data Warehouse: Snowflake ❄️

BI & Visualization: Microsoft Power BI 📊

Data Export (Optional): MS Excel

✨ Features
Automated Pipeline: Scripts for fully automated data extraction and loading.

Scalable Cloud DWH: Leverages Snowflake's power for massive datasets and complex queries.

Data Modeling: Includes SQL scripts for transforming raw data into a clean, usable star schema.

Interactive Dashboards: A pre-built Power BI (.pbix) file for immediate data visualization.

🚀 Getting Started
Follow these instructions to set up the project environment on your local machine.

Prerequisites
Make sure you have the following software installed:

Python 3.9+ and pip

A Snowflake account with ACCOUNTADMIN privileges to set up the database and roles.

Power BI Desktop

Installation & Setup
Clone the repository:

Bash

git clone https://github.com/[YOUR_USERNAME]/[YOUR_REPO_NAME].git
cd [YOUR_REPO_NAME]
Python Environment:
Create and activate a virtual environment, then install the required packages.

Bash

# For Windows
python -m venv venv
.\venv\Scripts\activate

# For MacOS/Linux
python3 -m venv venv
source venv/bin/activate

# Install packages
pip install -r requirements.txt
Snowflake Configuration:

Log in to your Snowflake account.

Use the SQL scripts in the /snowflake_setup folder to create the database, schemas, tables, and warehouse.

Update the config.ini file with your Snowflake account details and credentials.

Power BI Connection:

Open the OT_Analytics_Dashboard.pbix file.

When prompted, enter your Snowflake server URL and credentials to connect Power BI to the data warehouse.

🎈 Usage
Run the Python Downloader:
Execute the main script to start the data pipeline. This will fetch new data and load it into Snowflake's landing zone.


Open a Pull Request
