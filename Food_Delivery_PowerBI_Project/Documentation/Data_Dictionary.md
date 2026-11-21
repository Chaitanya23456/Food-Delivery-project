# Data Dictionary

This document provides a comprehensive technical and functional catalog of all entities, fields, data types, constraints, and business rules governing the **Food Delivery & Restaurant Performance Analytics** dataset.

---

## 1. Entity Overview & Storage Grain

| Entity / Table | File Name | Target Role in Model | Target Row Count | Primary Key | Grain (What does 1 row represent?) |
|---|---|---|---|---|---|
| **Fact_Orders** | `Orders.csv` | Fact Table | 18,000 | `Order_ID` | A single food delivery order placed by a customer |
| **Dim_Restaurants** | `Restaurants.csv` | Dimension Table | 261 | `Restaurant_ID` | A unique restaurant merchant partner onboarded on the platform |
| **Dim_Customers** | `Customers.csv` | Dimension Table | 5,500 | `Customer_ID` | A unique customer registered on the delivery mobile application |
| **Dim_DeliveryPartners** | `Delivery_Partners.csv` | Dimension Table | 350 | `Delivery_Partner_ID` | An active delivery courier / driver contracted with the platform |
| **Dim_Locations** | `Locations.csv` | Dimension Table | 10 | `City_ID` | A distinct metropolitan or urban operational territory |

---

## 2. Table: Orders (`Orders.csv`)

### Schema Specification

| Column Name | CSV Type | Power BI Type | Nullable? | Primary/Foreign Key | Description & Business Meaning | Allowed Values / Constraints | Sample Values |
|---|---|---|---|---|---|---|---|
| `Order_ID` | String | Text | No | **Primary Key** | Unique alphanumeric identifier for each order transaction. | Starts with `ORD` followed by 6 digits. Must be strictly unique. | `ORD100001`, `ORD100002` |
| `Order_Date` | String | Date | No | Foreign Key (`Dim_Date[Date]`) | Calendar date on which the order was placed by the customer. | ISO 8601 format (`YYYY-MM-DD`). Spans `2024-01-01` to `2024-12-31`. | `2024-03-15`, `2024-11-04` |
| `Order_Time` | String | Time | No | None | Timestamp showing the exact wall-clock time the order was initiated. | 24-hour clock format (`HH:MM:SS`). | `13:24:18`, `20:45:02` |
| `Customer_ID` | String | Text | No | Foreign Key (`Dim_Customers[Customer_ID]`) | Foreign key linking the order to the registered customer profile. | Must exist in `Customers.csv`. Pattern: `CUST` + 5 digits. | `CUST10042`, `CUST12984` |
| `Restaurant_ID` | String | Text | No | Foreign Key (`Dim_Restaurants[Restaurant_ID]`) | Foreign key linking the order to the fulfilling merchant partner. | Must exist in `Restaurants.csv`. Pattern: `RES` + 4 digits. | `RES1015`, `RES1180` |
| `Delivery_Partner_ID`| String | Text | No | Foreign Key (`Dim_DeliveryPartners[...]`) | Foreign key linking the assigned courier who picked up the order. | Must exist in `Delivery_Partners.csv`. Pattern: `DP` + 4 digits. | `DP1025`, `DP1210` |
| `City_ID` | String | Text | No | Foreign Key (`Dim_Locations[City_ID]`) | City code denoting the geographic region of the transaction. | Must exist in `Locations.csv`. Values: `CT101` to `CT110`. | `CT101`, `CT104` |
| `Food_Category` | String | Text | No | None | Primary cuisine categorization of the ordered items. | 10 standard cuisine categories (Biryani, Mughlai, North Indian, etc.) | `Biryani`, `North Indian` |
| `Order_Amount` | Float | Decimal Number | No | None | Total gross price of food items in Indian Rupees (INR) before discount. | Positive decimal number `> 0`. Range: ₹150.00 to ₹2,800.00. | `450.00`, `1250.00` |
| `Discount_Amount` | Float | Decimal Number | No | None | Promotional discount applied to the order in Indian Rupees (INR). | Decimal number `>= 0`. Always `<= Order_Amount`. | `0.00`, `75.00`, `150.00` |
| `Delivery_Fee` | Float | Decimal Number | No | None | Courier delivery charge levied to customer in Indian Rupees (INR). | Decimal number `>= 0`. (₹0 for premium users or orders > ₹650). | `0.00`, `35.00`, `50.00` |
| `Payment_Method` | String | Text | No | None | Financial channel used by the customer to settle the transaction. | `UPI`, `Credit Card`, `Debit Card`, `Cash on Delivery`, `Digital Wallet`, `Net Banking` | `UPI`, `Credit Card` |
| `Order_Status` | String | Text | No | None | Operational terminal status of the order. | `Completed` (delivered successfully), `Cancelled` (aborted prior to fulfillment). | `Completed`, `Cancelled` |
| `Cancellation_Reason`| String | Text | **Yes** (Null for Completed) | None | Reason logged when an order fails to complete. | Empty string if Completed. Else: `Restaurant Preparation Delay`, `Weather/Traffic Disruption`, `Item Out of Stock`, `Wrong Address Provided`, `Customer Changed Mind`, `Delivery Partner Unavailable`. | `Item Out of Stock`, `[Blank]` |
| `Estimated_Delivery_Time_Minutes` | Integer | Whole Number | No | None | Total estimated delivery duration communicated to customer at checkout. | Sum of average prep time + estimated transit time (typically 25 to 65 mins). | `38`, `45`, `52` |
| `Actual_Delivery_Time_Minutes` | Float/Int | Whole Number | **Yes** (Null for Cancelled) | None | Measured door-to-door transit and prep duration in minutes. | Blank/Null for `Cancelled` orders. Integer range: 18 to 85 minutes for `Completed`. | `42`, `65`, `[Blank]` |
| `Customer_Rating` | Float/Int | Whole Number | **Yes** (Null if unrated/cancelled) | None | Post-delivery satisfaction rating awarded by the customer (1 to 5). | Integer from 1 to 5. Null for Cancelled orders or when customer skips survey. | `5`, `4`, `1`, `[Blank]` |

---

## 3. Table: Restaurants (`Restaurants.csv`)

### Schema Specification

| Column Name | CSV Type | Power BI Type | Nullable? | Key Role | Description & Business Meaning | Allowed Values / Constraints | Sample Values |
|---|---|---|---|---|---|---|---|
| `Restaurant_ID` | String | Text | No | **Primary Key** | Unique merchant vendor identifier. | Pattern: `RES` + 4 digits. Unique across all records. | `RES1001`, `RES1050` |
| `Restaurant_Name` | String | Text | No | None | Commercial trading name of the restaurant or cloud kitchen. | Up to 100 characters. | `Urban North Indian Hub`, `Royal Biryani Court` |
| `City_ID` | String | Text | No | Foreign Key (`Dim_Locations[City_ID]`) | Geographic zone where the kitchen is located. | Valid `City_ID` referencing `Locations.csv`. | `CT101`, `CT103` |
| `Restaurant_Type` | String | Text | No | None | Operating format and culinary operational classification. | `Casual Dining`, `Fast Food`, `Fine Dining`, `Bakery & Desserts`, `Cloud Kitchen`, `Cafe` | `Cloud Kitchen`, `Casual Dining` |
| `Food_Category` | String | Text | No | None | Signature food category or specialty of the establishment. | One of 10 standard categories. | `Mughlai`, `Italian` |
| `Average_Rating` | Float | Decimal Number | No | None | Aggregated historical merchant food rating score on platform. | Decimal number between `3.0` and `5.0` (rounded to 1 decimal). | `4.2`, `4.8` |
| `Average_Preparation_Time` | Integer | Whole Number | No | None | Benchmark kitchen food preparation time in minutes. | Positive integer between 12 and 45 minutes. | `15`, `25`, `35` |
| `Price_Category` | String | Text | No | None | Target affordability tier. | `Budget`, `Mid-Range`, `Premium` | `Mid-Range`, `Premium` |
| `Restaurant_Status` | String | Text | No | None | Current platform listing status. | `Active` (~94%), `Inactive` (~6%) | `Active`, `Inactive` |

---

## 4. Table: Customers (`Customers.csv`)

### Schema Specification

| Column Name | CSV Type | Power BI Type | Nullable? | Key Role | Description & Business Meaning | Allowed Values / Constraints | Sample Values |
|---|---|---|---|---|---|---|---|
| `Customer_ID` | String | Text | No | **Primary Key** | Unique customer account identifier. | Pattern: `CUST` + 5 digits. Strictly unique. | `CUST10001`, `CUST15499` |
| `Customer_Name` | String | Text | No | None | Full legal or display name of the customer. | Indian full name (First + Last Name). | `Aarav Sharma`, `Pooja Reddy` |
| `Age` | Integer | Whole Number | No | None | Age of the registered consumer in years. | Integer between 18 and 65. | `24`, `31`, `48` |
| `Gender` | String | Text | No | None | Self-declared gender identity. | `Male`, `Female`, `Other` | `Male`, `Female` |
| `City_ID` | String | Text | No | Foreign Key (`Dim_Locations[City_ID]`) | Primary registered delivery city. | Valid `City_ID` referencing `Locations.csv`. | `CT101`, `CT105` |
| `Registration_Date` | String | Date | No | None | Date the user signed up on the platform. | ISO Date `YYYY-MM-DD` between 2023-01-01 and 2024-10-31. | `2023-05-14`, `2024-02-19` |
| `Customer_Segment` | String | Text | No | None | Algorithmic loyalty/recency segmentation tier. | `New Customer`, `Regular Customer`, `Premium Customer`, `Inactive Customer` | `Regular Customer`, `Premium Customer` |

---

## 5. Table: Delivery Partners (`Delivery_Partners.csv`)

### Schema Specification

| Column Name | CSV Type | Power BI Type | Nullable? | Key Role | Description & Business Meaning | Allowed Values / Constraints | Sample Values |
|---|---|---|---|---|---|---|---|
| `Delivery_Partner_ID`| String | Text | No | **Primary Key** | Unique logistics courier identifier. | Pattern: `DP` + 4 digits. Strictly unique. | `DP1001`, `DP1349` |
| `Partner_Name` | String | Text | No | None | Full name of the contracted delivery driver/rider. | Indian full name. | `Ramesh Verma`, `Suresh Gupta` |
| `City_ID` | String | Text | No | Foreign Key (`Dim_Locations[City_ID]`) | Operating urban sector for courier dispatches. | Valid `City_ID` referencing `Locations.csv`. | `CT101`, `CT103` |
| `Vehicle_Type` | String | Text | No | None | Mode of transportation used by rider for food delivery. | `Motorcycle` (55%), `Scooter` (25%), `Electric Bike` (15%), `Bicycle` (5%) | `Motorcycle`, `Electric Bike` |
| `Joining_Date` | String | Date | No | None | Date rider signed courier contract with the platform. | ISO Date `YYYY-MM-DD` between 2022-01-01 and 2024-06-30. | `2022-08-11`, `2023-11-20` |
| `Partner_Rating` | Float | Decimal Number | No | None | Average customer delivery service rating for the rider. | Decimal number between `3.5` and `5.0`. | `4.2`, `4.9` |
| `Completed_Deliveries`| Integer | Whole Number | No | None | Cumulative lifetime deliveries completed by rider. | Integer from 50 to 1,800. | `412`, `1240` |

---

## 6. Table: Locations (`Locations.csv`)

### Schema Specification

| Column Name | CSV Type | Power BI Type | Nullable? | Key Role | Description & Business Meaning | Allowed Values / Constraints | Sample Values |
|---|---|---|---|---|---|---|---|
| `City_ID` | String | Text | No | **Primary Key** | Standardized operational territory code. | Unique 5-character string: `CT101` through `CT110`. | `CT101`, `CT102` |
| `City_Name` | String | Text | No | None | Official English name of the metropolitan area. | 10 Indian cities: Mumbai, Pune, Bengaluru, Delhi, Hyderabad, Chennai, Kolkata, Ahmedabad, Jaipur, Nagpur | `Bengaluru`, `Mumbai` |
| `State` | String | Text | No | None | Indian federal state / union territory. | State name (Maharashtra, Karnataka, Delhi, etc.) | `Maharashtra`, `Karnataka` |
| `Region` | String | Text | No | None | Macro-geographic economic zone. | `West`, `South`, `North`, `East`, `Central` | `South`, `West` |
| `Population_Category`| String | Text | No | None | Urbanization demographic classification. | `Tier 1` (Mega-metro / Metro), `Tier 2` (High-growth urban center) | `Tier 1`, `Tier 2` |

---

## 7. Business Rules, Constraints & Assumptions

1. **Transactional Integrity for Cancelled Orders:**
   - When `Order_Status == 'Cancelled'`, food delivery was never completed. Therefore, `Actual_Delivery_Time_Minutes` is stored as an empty string (evaluates to `BLANK()` in Power BI) and `Customer_Rating` is stored as an empty string (evaluates to `BLANK()`).
   - A valid `Cancellation_Reason` is strictly mandatory for cancelled orders.
2. **Delivery Delay Definition:**
   - An order is considered **Delayed** if and only if `Actual_Delivery_Time_Minutes > Estimated_Delivery_Time_Minutes`.
   - The delay margin is calculated as:  
     $$\text{Delivery Delay (Minutes)} = \text{Actual Delivery Time} - \text{Estimated Delivery Time}$$
   - If actual delivery time is less than or equal to estimated time, the delay is treated as $0$ minutes in business reporting (on-time delivery).
3. **Monetary Relationships:**
   - `Order_Amount` represents the gross merchandise value (GMV) of ordered food.
   - `Discount_Amount` represents promotional coupons funded by the platform or merchant.
   - Net Food Revenue is defined as:  
     $$\text{Net Revenue} = \text{Order Amount} - \text{Discount Amount}$$
   - Total Platform Cash Collected includes `Delivery_Fee` collected from non-premium orders.
4. **Referential Integrity Constraints:**
   - Every order in `Orders.csv` has a matching customer, restaurant, courier partner, and city.
   - Deliveries only occur intra-city (i.e. the customer, restaurant, courier, and order all share the same `City_ID`).
