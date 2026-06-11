# Exploratory Data Analysis (EDA) & Data Forensics Portfolio Project

## Project Overview
This project serves as a diagnostic phase to evaluate data integrity and uncover hidden patterns, trends, and distributions within an e-commerce transactional dataset. Rather than relying on simple reporting, this codebase implements descriptive statistics, handles missing fields, isolates high-value outlier cohorts, and checks multi-variable correlation logic to turn raw data into structured business context.

---

## Analytical Architecture & Phases

### Phase 1: Data Cleaning & Forensics
* **Structural Review:** Analyzes data properties using pandas summary frameworks.
* **Missing Data Resolution:** Identifies structural gaps and systematically replaces missing marketing campaign indicators (`CouponCode`) with a default `"None"` label.
* **Temporal Consistency:** Directs uniform timestamp mapping by formatting transaction values cleanly down to standard date objects, dropping invalid record rows.
* **De-duplication Purge:** Identifies and clears duplicate records from the baseline collection to secure data integrity.

### Phase 2: Exploratory Data Analysis (EDA) & Statistics
* **Center of Gravity:** Calculates fundamental summary descriptive statistics (Mean, Median, Count) to locate primary baseline metrics.
* **Geometry of Distribution (Skewness):** Quantifies distribution symmetry coefficients across transaction values (`TotalPrice`) and structural volumes (`Quantity`, `ItemsInCart`) to evaluate geometric right-skewed data distributions.
* **Core Business Financials:** Summarizes aggregate metrics covering total gross sales revenue, physical product counts sold, and transaction capacity thresholds.
* **Basket Dynamics:** Evaluates average items per individual cart transaction alongside base unit pricing metrics.

### Phase 3: Outlier Segmentation & Hidden Channels
* **Robust Outlier Tracking:** Isolates exceptional customer transaction values by setting a structural boundary threshold via the Interquartile Range (IQR) method ($Q3 + 1.5 \times IQR$).
* **VIP Customer Profiling:** Segments standard transactional behaviors from high-value outlier orders to track marketing asset choices among high-spending cohorts.
* **Linear Correlation Mapping:** Evaluates linear relationships and statistical strength directions across continuous metrics via Pearson Correlation Matrix metrics.
* **Hidden Details Extraction:**
  * Groups financial volume counts and structural order sums across marketing traffic channels (`ReferralSource`).
  * Aggregates financial velocity across unique campaign codes (`CouponCode`).
  * Segments transaction values dynamically into explicit unit price groups (`Low`, `Mid`, and `High` value tiers via `pd.qcut`).
  * Runs a descriptive cross-tabulation table mapping standard customers against VIP cohorts across different marketing paths via `pd.crosstab`.

### Phase 4: Visualizing the Evidence
* **Design Strategy:** Follows flat, minimal visual practices, cutting out distracting 3D chart elements and background noise to put primary focus directly on core data findings.
* **Strategic Accent Tracking:** Utilizes targeted color highlighting to spotlight primary revenue-driving channels (e.g., Facebook) while maintaining general gray anchors for structural comparison.
* **Data Annotations:** Integrates exact financial string annotations directly beside the graphical plots, removing the need for auxiliary visual grid lines.

---

## Core Technologies Implemented
* **Python** (Core Environment)
* **Pandas** (Data Wrangling, Forensics, Cross-Tabulations, Quantile Slicing, Conditional Filtering)
* **Matplotlib** (Plot Canvas Management)
* **Seaborn** (Statistical Visualization Framework)