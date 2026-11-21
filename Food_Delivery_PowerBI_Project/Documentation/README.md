# Food Delivery & Restaurant Performance Analytics Dashboard

**Author:** Engineering & Business Intelligence Portfolio Project  
**Tooling:** Power BI Desktop, Power Query, DAX (Data Analysis Expressions)  
**Data Domain:** E-commerce / Quick-Commerce / Food Tech (Simulated Indian Metros Platform)  
**Architecture:** Star Schema Relational Data Model  

---

## Executive Summary

The **Food Delivery & Restaurant Performance Analytics Dashboard** is an end-to-end Business Intelligence solution designed to monitor, analyze, and optimize the operational and commercial dynamics of a high-volume food delivery platform operating across 10 major Indian metropolitan and tier-2 hubs.

Food delivery aggregators manage a multi-sided marketplace connecting millions of customers, hundreds of merchant restaurants, and a distributed fleet of delivery partners. In this low-margin, high-frequency industry, profitability and market share depend on three operational pillars:
1. **Commercial Growth & Monetization:** Tracking Gross Merchandise Value (GMV), net revenue, average order value (AOV), and customer discounting efficiency.
2. **Logistics & Delivery SLA Adherence:** Monitoring estimated vs. actual delivery times, delivery partner performance, traffic-related delays, and vehicle fleet distribution.
3. **Customer Retention & Merchant Quality:** Evaluating cancellation root causes, merchant order throughput, customer repeat ordering behaviors, and multi-tier customer lifetime engagement.

This project demonstrates professional data analytics engineering: rigorous data modeling (Star Schema), advanced DAX calculations with time-intelligence, robust Power Query ETL transformations, and an interactive 5-page dashboard adhering to modern UX/UI guidelines.

---

## Project Objectives & Key Analytical Inquiries

| # | Business Question | Dashboard Area | Key Metric / Dimension |
|---|---|---|---|
| **1** | Which restaurants generate the highest revenue? | Restaurant Performance | `[Total Revenue]`, `[Top 10 Restaurants by Revenue]` |
| **2** | Which food categories are most popular? | Business Overview & Orders | `[Total Orders]`, `[Revenue by Food Category]` |
| **3** | Which cities receive the highest number of orders? | Business Overview & Locations | `[City-wise Order Share]`, Map & Bar visuals |
| **4** | What is the average delivery time and delay? | Delivery Performance | `[Avg Delivery Time]`, `[Avg Delivery Delay]` |
| **5** | Which factors contribute to order cancellations? | Cancellation Analysis | `[Cancellation Rate]`, `[Cancellation Reasons]` |
| **6** | Which restaurants receive the highest customer ratings? | Restaurant Performance | `[Average Restaurant Rating]`, Merchant Matrix |
| **7** | Which delivery partners complete the most orders? | Delivery Performance | `[Completed Orders]`, Fleet Leaderboards |
| **8** | Which time periods experience the highest order demand? | Order & Cancellation Analysis | Hourly order volume & Peak Dinner/Lunch slots |
| **9** | How do discounts affect revenue and profitability? | Customer & Business Overview | `[Total Discounts]`, Discount % vs. AOV |
| **10**| Which vehicle types and regions face the highest delays? | Delivery Performance | Vehicle delay distributions & City SLA benchmarks |

---

## High-Level Data Model Architecture

The semantic model follows an optimized **Star Schema** to ensure high query performance, clean filter propagation, and predictable DAX behavior inside the VertiPaq memory engine.

```
                  +---------------------------+
                  |       Dim_Locations       |
                  |---------------------------|
                  | PK: City_ID               |
                  +-------------+-------------+
                                | 1
                                |
                                | *
+---------------------------+   |   +---------------------------+
|       Dim_Customers       |   |   |      Dim_Restaurants      |
|---------------------------|   |   |---------------------------|
| PK: Customer_ID           |   |   | PK: Restaurant_ID         |
+-------------+-------------+   |   +-------------+-------------+
              | 1               |                 | 1
              |                 |                 |
              | *               |                 | *
     +--------v-----------------v-----------------v--------+
     |                     Fact_Orders                     |
     |-----------------------------------------------------|
     | PK: Order_ID                                        |
     | FK: Customer_ID, Restaurant_ID, Delivery_Partner_ID |
     | FK: City_ID, Order_Date                             |
     +-----------------+-----------------+-----------------+
                       | *               | *
                       |                 |
                       | 1               | 1
+----------------------v----+       +----v----------------------+
|    Dim_DeliveryPartners   |       |         Dim_Date          |
|---------------------------|       |---------------------------|
| PK: Delivery_Partner_ID   |       | PK: Date (Calendar Table) |
+---------------------------+       +---------------------------+
```

---

## Dataset Overview

The datasets are stored in `Food_Delivery_PowerBI_Project/Dataset/` in standard UTF-8 CSV format, generated with verified referential integrity:

| File Name | Record Count | Description | Primary Key | Foreign Keys |
|---|---|---|---|---|
| **Orders.csv** | **18,000** | Transactional order facts with amounts, delivery times, status, ratings | `Order_ID` | `Customer_ID`, `Restaurant_ID`, `Delivery_Partner_ID`, `City_ID`, `Order_Date` |
| **Restaurants.csv** | **261** | Merchant profiles, cuisine specialties, average prep times, price tiers | `Restaurant_ID` | `City_ID` |
| **Customers.csv** | **5,500** | Customer demographics, age brackets, registration dates, tiers | `Customer_ID` | `City_ID` |
| **Delivery_Partners.csv**| **350** | Courier profiles, vehicle classifications, historical performance | `Delivery_Partner_ID`| `City_ID` |
| **Locations.csv** | **10** | Indian metro & tier-2 geographical mapping, state, population tier | `City_ID` | None |

### Geographic Scope (10 Indian Hubs)
* **West:** Mumbai, Pune, Ahmedabad
* **South:** Bengaluru, Hyderabad, Chennai
* **North:** Delhi, Jaipur
* **East:** Kolkata
* **Central:** Nagpur

---

## Project Directory Structure

```text
Food_Delivery_PowerBI_Project/
├── Dataset/
│   ├── Orders.csv                    # 18,000 order transactions
│   ├── Restaurants.csv               # 261 restaurant merchants
│   ├── Customers.csv                 # 5,500 customer demographic profiles
│   ├── Delivery_Partners.csv         # 350 active delivery couriers
│   └── Locations.csv                 # 10 city operational zones
│
├── Documentation/
│   ├── README.md                     # Executive overview & architecture guide
│   ├── Data_Dictionary.md            # Detailed schema, data types & constraints
│   ├── Data_Model.md                 # Star Schema design & relationship mechanics
│   ├── DAX_Measures.md               # 25+ verified DAX formulas with explanations
│   └── Business_Insights.md          # 18 deep analytical findings from real data
│
└── PowerBI/
    └── Implementation_Guide.md       # Step-by-step visual creation, ETL & UX guide
```

---

## 5-Page Dashboard Structure

1. **Page 1: Business Overview**  
   Executive health metrics, Gross Merchandise Value, Net Revenue, Completed vs. Cancelled Order splits, Regional Revenue contributions, and Cuisine demand share.
2. **Page 2: Restaurant Performance**  
   Merchant profitability, Top 10 revenue-generating vendors, average food prep times, customer satisfaction matrix, and category-level pricing benchmarks.
3. **Page 3: Delivery Performance**  
   Logistics SLA monitoring, estimated vs. actual delivery duration, delay distributions, courier fleet efficiency across vehicle categories (EVs, Scooters, Bikes, Bicycles).
4. **Page 4: Customer Analytics**  
   Demographic breakdowns (Age brackets, Gender splits), customer tier spending habits (Regular vs. Premium vs. New), repeat purchase retention, and top platform spenders.
5. **Page 5: Order & Cancellation Analysis**  
   Hourly demand surges (Lunch and Dinner rushes), weekend vs. weekday spending, cancellation root-cause Pareto analysis, and payment channel distribution (UPI, Cards, COD).

---

## How to Set Up and Use This Project

1. **Download / Clone the Repository:**  
   Ensure the `Food_Delivery_PowerBI_Project` folder is saved to your local storage.
2. **Launch Power BI Desktop:**  
   Open a blank report in Power BI Desktop (Free or Pro).
3. **Connect to Data:**  
   Use **Get Data > Text/CSV** to load each of the 5 CSV files from the `Dataset/` directory.
4. **Apply Power Query Steps:**  
   Follow the detailed M transformations described in `Documentation/Data_Dictionary.md` and `PowerBI/Implementation_Guide.md` (e.g., creating calculated delay fields, enforcing numeric and date formats).
5. **Build Relationships:**  
   Open **Model View** and verify the 1-to-many single-direction star schema shown in `Documentation/Data_Model.md`.
6. **Create DAX Measures:**  
   Create a dedicated `_Measures` table and paste the measures documented in `Documentation/DAX_Measures.md`.
7. **Construct Visuals:**  
   Follow `PowerBI/Implementation_Guide.md` for exact visual coordinates, card designs, and slicer synchronization across the 5 pages.

---

## Interview & Portfolio Presentation Tips

When showcasing this project to hiring managers or technical recruiters:
- **Lead with Business Impact:** Explain how delivery delays directly degrade customer ratings (orders delayed >20 mins suffer a 45% probability of receiving a 1-star rating).
- **Highlight Technical Rigor:** Emphasize why Star Schema was chosen over a single flat file (reducing memory footprint, preventing grain corruption in multi-level aggregations).
- **Discuss Time Intelligence:** Walk through the month-over-month revenue growth measure and explain how `SAMEPERIODLASTYEAR` / `DATEADD` require a contiguous calendar date table.
- **Demonstrate Data Governance:** Discuss the realistic operational constraints implemented—such as ensuring cancelled orders contain null actual delivery durations and zero ratings.
