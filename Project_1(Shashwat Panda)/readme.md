# README: Project 1 - Data Cleaning & Preparation

## 1. Project Overview
Welcome to the production-ready **"Gold Standard"** dataset for Project 1. In data analytics, poor data quality costs organizations an average of 15–25% of their annual revenue, making data scrubbing a vital architectural phase. 

This project focused on transforming raw, noisy transaction data into a reliable, high-integrity source of truth by systematically identifying missing values, eliminating duplicates, and correcting formatting anomalies.

---

## 2. Reference Files
The following files are associated with this project and should be referred to verbatim by their exact names:
* **`Dataset for Data Analytics.xlsx`** – The original, uncleaned raw data source containing structural noise and missing values.
* **`Changed_dataset(Project1).xlsx`** – The finalized, cleaned, and production-ready dataset.
* **`Change log(project1).pdf`** – The official audit log documenting every explicit transformation performed.
* **`DATA ANALYTICS p1.pdf`** – The foundational project guide and training kit provided by DecodeLabs[cite: 2].

---

## 3. Core Data Transformation Ledger
Based on the documentation in `Change log(project1).pdf`, a 0% error rate threshold was enforced for unique identifiers and date formats before marking the dataset as resolved:

| Change ID | Target Column / Feature | Transformation Performed | Business & Operational Impact | Status |
| :--- | :--- | :--- | :--- | :--- |
| **CR001** | `OrderID` | Removed duplicate records based strictly on the `OrderID` field. | Ensures absolute uniqueness of transaction counts and eliminates inflated revenue metrics. | **Resolved** |
| **CR002** | Transaction Dates | Standardized all variant date fields into strict **ISO 8601 format (`YYYY-MM-DD`)**. | Achieved a 0% error rate across all 1,200 records, allowing flawless chronological sorting. | **Resolved** |
| **CR003** | `CouponCode` | Imputed 309 missing rows with the uniform categorical identifier **`'NONE'`**. | Preserved 100% of rows, completely avoiding the statistical power loss associated with listwise deletion. | **Resolved** |
| **CR004** | `UnitPrice` & `TotalPrice` | Applied explicit numeric rounding rules. | Standardized financial line items to a strict precision of **2 decimal places**. | **Resolved** |

---

## 4. Analytical Pipeline Specifications
* **Row Retention:** 100% data preservation achieved through strategic imputation rather than raw deletion.
* **Volume:** 1,200 validated records optimized for downstream Business Intelligence (BI) and predictive modeling tools.
* **Data Integration:** Cleaned and formatted perfectly to match standard data warehousing workflows (proper case structure, trimmed whitespace, and strict numeric boundaries).