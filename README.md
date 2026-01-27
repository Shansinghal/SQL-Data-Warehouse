
# Medallion Architecture–Based Data Warehouse

 
This project implements an end-to-end data warehousing architecture, from raw data ingestion to structured storage. Advanced analytics and business intelligence layers are planned and will be integrated in subsequent iterations.
---
## 🏗️ Data Architecture

The data architecture for this project follows Medallion Architecture **Bronze**, **Silver**, and **Gold** layers:
![Data Architecture](docs/data_architecture.png)

1. **Bronze Layer**: Stores raw data as-is from the source systems. Data is ingested from CSV Files into SQL Server Database.
2. **Silver Layer**: This layer includes data cleansing, standardization, and normalization processes to prepare data for analysis.
3. **Gold Layer**: Houses business-ready data modeled into a star schema required for reporting and analytics.

---
## 📖 Project Overview

This project involves:

1. **Data Architecture**: Designing a Modern Data Warehouse Using Medallion Architecture **Bronze**, **Silver**, and **Gold** layers.
2. **ETL Pipelines**: Extracting, transforming, and loading data from source systems into the warehouse.
3. **Data Modeling**: Developing fact and dimension tables optimized for analytical queries.


---

## 🚀 Project Requirements

### 🏗️ Data Warehouse Development (Data Engineering)

#### Objective
Designing and implementing a modern data warehouse to consolidate sales data from multiple source systems, enabling scalable analytics and data-driven decision-making.

#### Specifications
- **Data Sources**: Ingest data from two heterogeneous source systems (ERP and CRM) provided as CSV files.
- **Data Quality**: Perform data cleansing, validation, and standardization to address inconsistencies and missing values.
- **Data Integration**: Merge data from multiple sources into a unified, analytics-friendly dimensional model.
- **Scope**: Work with the latest snapshot of data only; historical versioning is intentionally excluded.
- **Documentation**: Maintain clear and structured documentation of the data architecture, data models, and transformation logic to support both technical and business users.

---


## 📂 Repository Structure
```
SQL-Data-warehouse/
│
├── datasets/                           # Raw datasets used for the project (ERP and CRM data)
│
├── docs/                               # Project documentation and architecture details
│   ├── data_architecture.png           # PNG file shows the project's architecture
│   ├── data_catalog.md                 # Catalog of datasets, including field descriptions and metadata
│   ├── data_flow.jpeg                  # JPEG file for the data flow diagram
│   ├── data_models.jpeg                # JPEG file for data models (star schema)
│   ├── naming-conventions.md           # Consistent naming guidelines for tables, columns, and files
│
├── scripts/                            # SQL scripts for ETL and transformations
│   ├── bronze/                         # Scripts for extracting and loading raw data
│   ├── silver/                         # Scripts for cleaning and transforming data
│   ├── gold/                           # Scripts for creating analytical models
│
├── tests/                              # Test scripts and quality files
│
├── README.md                           # Project overview and instructions
└── LICENSE                             # License information for the repository
---



##🛡️ License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and share this project with proper attribution.


