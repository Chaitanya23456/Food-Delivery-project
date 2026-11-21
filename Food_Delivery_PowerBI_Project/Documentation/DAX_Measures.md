# DAX Measures Catalog

This document provides complete, production-grade DAX (Data Analysis Expressions) formulas for the **Food Delivery & Restaurant Performance Analytics Dashboard**.

All measures are organized by analytical category and designed to be stored within a dedicated table named `_Measures`.

---

## Table of Contents
1. [Sales & Commercial KPIs](#1-sales--commercial-kpis)
2. [Delivery & Logistics KPIs](#2-delivery--logistics-kpis)
3. [Customer & Demographic KPIs](#3-customer--demographic-kpis)
4. [Restaurant & Merchant KPIs](#4-restaurant--merchant-kpis)
5. [Advanced Time Intelligence & Performance Measures](#5-advanced-time-intelligence--performance-measures)

---

## 1. Sales & Commercial KPIs

### 1.1 Total Orders
```dax
Total Orders = 
COUNTROWS(Orders)
```
- **Plain Language Explanation:** Counts the total number of order rows recorded in the `Orders` fact table.
- **Business Purpose:** Represents top-of-funnel transaction volume regardless of fulfillment status.
- **Assumptions:** Each row in `Orders` represents exactly one unique transaction (`Order_ID`).

---

### 1.2 Completed Orders
```dax
Completed Orders = 
CALCULATE(
    COUNTROWS(Orders),
    Orders[Order_Status] = "Completed"
)
```
- **Plain Language Explanation:** Counts only the orders where the fulfillment status is strictly "Completed".
- **Business Purpose:** Measures fulfilled orders that directly generate realized revenue and customer satisfaction.
- **Assumptions:** Only orders labeled `"Completed"` represent fulfilled deliveries.

---

### 1.3 Cancelled Orders
```dax
Cancelled Orders = 
CALCULATE(
    COUNTROWS(Orders),
    Orders[Order_Status] = "Cancelled"
)
```
- **Plain Language Explanation:** Filters the order table to count only orders marked as "Cancelled".
- **Business Purpose:** Tracks revenue leakage, platform friction, and merchant/courier supply-demand mismatches.
- **Assumptions:** Orders labeled `"Cancelled"` did not result in food delivery.

---

### 1.4 Total Revenue
```dax
Total Revenue = 
CALCULATE(
    SUM(Orders[Order_Amount]),
    Orders[Order_Status] = "Completed"
)
```
- **Plain Language Explanation:** Sums the gross order amounts for orders that were successfully completed.
- **Business Purpose:** Key commercial metric representing gross revenue (GMV) recognized by the platform.
- **Assumptions:** Cancelled orders are excluded from realized revenue recognition.

---

### 1.5 Average Order Value (AOV)
```dax
Average Order Value = 
DIVIDE(
    [Total Revenue],
    [Completed Orders],
    0
)
```
- **Plain Language Explanation:** Divides Total Revenue by the number of Completed Orders, safely returning 0 if there are no completed orders.
- **Business Purpose:** Monitors customer basket size. A rising AOV indicates customers are ordering more items or selecting premium restaurants.
- **Assumptions:** Uses `DIVIDE` to prevent divide-by-zero errors when filters return zero completed orders.

---

### 1.6 Total Discounts
```dax
Total Discounts = 
SUM(Orders[Discount_Amount])
```
- **Plain Language Explanation:** Sums the total monetary discount concessions provided to customers across all orders.
- **Business Purpose:** Evaluates marketing spend and coupon burn.
- **Assumptions:** `Discount_Amount` is a positive decimal number representing the price reduction.

---

### 1.7 Total Delivery Fees
```dax
Total Delivery Fees = 
CALCULATE(
    SUM(Orders[Delivery_Fee]),
    Orders[Order_Status] = "Completed"
)
```
- **Plain Language Explanation:** Sums delivery fees collected from completed orders.
- **Business Purpose:** Measures direct logistics cost recovery.
- **Assumptions:** Delivery fees are only recognized as platform income on fulfilled deliveries.

---

### 1.8 Revenue by Restaurant
```dax
Revenue by Restaurant = 
CALCULATE(
    [Total Revenue],
    VALUES(Restaurants[Restaurant_ID])
)
```
- **Plain Language Explanation:** Computes realized revenue specifically within the context of selected restaurant merchants.
- **Business Purpose:** Allows sorting, ranking, and filtering of merchant revenue in matrix and bar chart visuals.
- **Assumptions:** A valid 1-to-many relationship exists between `Restaurants[Restaurant_ID]` and `Orders[Restaurant_ID]`.

---

## 2. Delivery & Logistics KPIs

### 2.1 Average Delivery Time
```dax
Average Delivery Time = 
CALCULATE(
    AVERAGE(Orders[Actual_Delivery_Time_Minutes]),
    Orders[Order_Status] = "Completed"
)
```
- **Plain Language Explanation:** Calculates the average number of minutes taken from order placement to customer drop-off for completed deliveries.
- **Business Purpose:** Core SLA operational indicator for customer speed and courier responsiveness.
- **Assumptions:** `Actual_Delivery_Time_Minutes` is null for cancelled orders, so `AVERAGE` automatically skips cancelled transactions.

---

### 2.2 Estimated Delivery Time
```dax
Estimated Delivery Time = 
CALCULATE(
    AVERAGE(Orders[Estimated_Delivery_Time_Minutes]),
    Orders[Order_Status] = "Completed"
)
```
- **Plain Language Explanation:** Calculates the average estimated duration presented to customers at checkout for fulfilled orders.
- **Business Purpose:** Used as an operational benchmark against actual delivery times to assess prediction accuracy.
- **Assumptions:** Estimates are calculated as kitchen preparation time plus anticipated courier transit time.

---

### 2.3 Delayed Orders
```dax
Delayed Orders = 
CALCULATE(
    COUNTROWS(Orders),
    Orders[Order_Status] = "Completed",
    Orders[Actual_Delivery_Time_Minutes] > Orders[Estimated_Delivery_Time_Minutes]
)
```
- **Plain Language Explanation:** Counts completed orders where the actual delivery duration exceeded the promised estimated delivery duration.
- **Business Purpose:** Identifies deliveries that breached promised customer service-level agreements (SLAs).
- **Assumptions:** An order is delayed if actual time is greater than estimated time by 1 minute or more.

---

### 2.4 Average Delivery Delay
```dax
Average Delivery Delay = 
VAR DelayedOrdersTable = 
    FILTER(
        Orders,
        Orders[Order_Status] = "Completed" && 
        Orders[Actual_Delivery_Time_Minutes] > Orders[Estimated_Delivery_Time_Minutes]
    )
RETURN
    AVERAGEX(
        DelayedOrdersTable,
        Orders[Actual_Delivery_Time_Minutes] - Orders[Estimated_Delivery_Time_Minutes]
    )
```
- **Plain Language Explanation:** Computes the average excess delay time (in minutes) strictly for those orders that were delivered late.
- **Business Purpose:** Tells operations managers how severe late deliveries are on average (e.g. 5 minutes vs. 20 minutes).
- **Assumptions:** On-time orders (actual $\le$ estimated) are excluded so they do not artificially mask late delivery severity.

---

### 2.5 On-Time Delivery Percentage
```dax
On-Time Delivery Percentage = 
VAR TotalCompleted = [Completed Orders]
VAR DelayedCount = [Delayed Orders]
RETURN
    DIVIDE(TotalCompleted - DelayedCount, TotalCompleted, 0)
```
- **Plain Language Explanation:** Calculates the percentage of completed orders that arrived on or before the estimated delivery time.
- **Business Purpose:** The primary fulfillment SLA metric for food delivery aggregators (target is typically $>85\%$).
- **Assumptions:** Formatted as a percentage with 1 decimal place (`0.0%`).

---

### 2.6 Delivery Completion Rate
```dax
Delivery Completion Rate = 
DIVIDE(
    [Completed Orders],
    [Total Orders],
    0
)
```
- **Plain Language Explanation:** Proportion of total initiated orders that are successfully delivered.
- **Business Purpose:** High-level platform reliability benchmark.
- **Assumptions:** Measures overall operational success rate ($1 - \text{Cancellation Rate}$).

---

## 3. Customer & Demographic KPIs

### 3.1 Total Customers
```dax
Total Customers = 
DISTINCTCOUNT(Customers[Customer_ID])
```
- **Plain Language Explanation:** Counts the total number of distinct customer profiles registered in the database.
- **Business Purpose:** Measures total addressable customer base size on the platform.
- **Assumptions:** Each customer has a unique `Customer_ID`.

---

### 3.2 Active Customers
```dax
Active Customers = 
CALCULATE(
    DISTINCTCOUNT(Orders[Customer_ID]),
    Orders[Order_Status] = "Completed"
)
```
- **Plain Language Explanation:** Counts distinct customers who placed at least one completed order in the selected time period.
- **Business Purpose:** Monitors active user engagement and transacting user base.
- **Assumptions:** Customers who only placed cancelled orders are not counted as active.

---

### 3.3 Repeat Customers
```dax
Repeat Customers = 
VAR CustomerOrderCounts = 
    SUMMARIZE(
        CALCULATE(Orders, Orders[Order_Status] = "Completed"),
        Orders[Customer_ID],
        "OrderCount", COUNTROWS(Orders)
    )
RETURN
    COUNTROWS(
        FILTER(CustomerOrderCounts, [OrderCount] > 1)
    )
```
- **Plain Language Explanation:** Summarizes completed orders per customer and counts how many customers placed more than one order.
- **Business Purpose:** Evaluates customer loyalty, habit formation, and retention health.
- **Assumptions:** Requires 2 or more fulfilled orders within the filter context.

---

### 3.4 Customer Retention Rate
```dax
Customer Retention Rate = 
DIVIDE(
    [Repeat Customers],
    [Active Customers],
    0
)
```
- **Plain Language Explanation:** Ratio of repeat buyers to total active ordering customers.
- **Business Purpose:** Core growth metric indicating brand stickiness and customer lifetime value potential.
- **Assumptions:** Formatted as a percentage (`0.0%`).

---

### 3.5 Average Customer Rating
```dax
Average Customer Rating = 
CALCULATE(
    AVERAGE(Orders[Customer_Rating]),
    Orders[Order_Status] = "Completed",
    NOT(ISBLANK(Orders[Customer_Rating]))
)
```
- **Plain Language Explanation:** Averages all submitted customer satisfaction ratings (1 to 5 stars) for completed orders.
- **Business Purpose:** Direct measurement of customer satisfaction and perceived service quality.
- **Assumptions:** Ignores blank/unrated orders in denominator to prevent deflating the average.

---

## 4. Restaurant & Merchant KPIs

### 4.1 Total Restaurants
```dax
Total Restaurants = 
DISTINCTCOUNT(Restaurants[Restaurant_ID])
```
- **Plain Language Explanation:** Counts the total number of unique restaurant vendors in the database.
- **Business Purpose:** Measures supply variety and merchant acquisition coverage.
- **Assumptions:** Validated against `Restaurants.csv`.

---

### 4.2 Average Restaurant Rating
```dax
Average Restaurant Rating = 
AVERAGE(Restaurants[Average_Rating])
```
- **Plain Language Explanation:** Calculates the average historical rating score across all onboarded restaurants.
- **Business Purpose:** Tracks merchant catalog quality standards.
- **Assumptions:** Values range from 1.0 to 5.0.

---

### 4.3 Restaurant Order Count
```dax
Restaurant Order Count = 
CALCULATE(
    [Completed Orders],
    ALLEXCEPT(Restaurants, Restaurants[Restaurant_ID], Restaurants[Restaurant_Name])
)
```
- **Plain Language Explanation:** Returns the count of completed orders attributed to a restaurant, ignoring extraneous visual filters while keeping restaurant context.
- **Business Purpose:** Used in restaurant benchmarking matrices and ranking charts.
- **Assumptions:** Connected via `Restaurants[Restaurant_ID]`.

---

### 4.4 Top Performing Restaurants
```dax
Top Performing Restaurants = 
CALCULATE(
    [Total Revenue],
    TOPN(
        10, 
        ALLSELECTED(Restaurants[Restaurant_Name]), 
        [Total Revenue], 
        DESC
    )
)
```
- **Plain Language Explanation:** Calculates the collective revenue of the top 10 highest-earning restaurants within the active slicer context.
- **Business Purpose:** Benchmarks 80/20 Pareto revenue concentration across merchant partners.
- **Assumptions:** `ALLSELECTED` honors external slicers like City and Date.

---

## 5. Advanced Time Intelligence & Performance Measures

### 5.1 Previous Month Revenue
```dax
Previous Month Revenue = 
CALCULATE(
    [Total Revenue],
    DATEADD(Dim_Date[Date], -1, MONTH)
)
```
- **Plain Language Explanation:** Evaluates Total Revenue shifted backward by exactly one calendar month.
- **Business Purpose:** Used as the baseline denominator for Month-over-Month growth calculations.
- **Assumptions:** Requires an active relationship between `Dim_Date[Date]` and `Orders[Order_Date]`, with `Dim_Date` marked as a Date table.

---

### 5.2 Month-over-Month Revenue Growth
```dax
Month-over-Month Revenue Growth = 
VAR CurrentRevenue = [Total Revenue]
VAR PrevRevenue = [Previous Month Revenue]
RETURN
    IF(
        ISBLANK(PrevRevenue),
        BLANK(),
        DIVIDE(CurrentRevenue - PrevRevenue, PrevRevenue, 0)
    )
```
- **Plain Language Explanation:** Calculates the percentage change in completed revenue compared to the preceding calendar month.
- **Business Purpose:** Tracks revenue acceleration, seasonality, and campaign momentum.
- **Assumptions:** Returns `BLANK()` for the first month (January 2024) where no previous month data exists. Formatted as `+0.0%;-0.0%;0.0%`.

---

### 5.3 Cancellation Rate
```dax
Cancellation Rate = 
DIVIDE(
    [Cancelled Orders],
    [Total Orders],
    0
)
```
- **Plain Language Explanation:** Calculates the proportion of placed orders that were cancelled.
- **Business Purpose:** Critical indicator of operational failure, supply shortage, or weather disruptions.
- **Assumptions:** Formatted as a percentage (`0.0%`).

---

### 5.4 Revenue by Food Category
```dax
Revenue by Food Category = 
CALCULATE(
    [Total Revenue],
    VALUES(Orders[Food_Category])
)
```
- **Plain Language Explanation:** Calculates completed revenue sliced across culinary categories.
- **Business Purpose:** Visualizes cuisine popularity and guides merchandising/promotional campaigns.
- **Assumptions:** Categorized into standard culinary types.

---

### 5.5 Revenue by City
```dax
Revenue by City = 
CALCULATE(
    [Total Revenue],
    VALUES(Locations[City_Name])
)
```
- **Plain Language Explanation:** Calculates completed revenue sliced across geographic metropolitan territories.
- **Business Purpose:** Identifies top-performing regional markets.
- **Assumptions:** Driven by the relationship from `Locations[City_ID]` to `Orders[City_ID]`.

---

### 5.6 Average Discount Percentage
```dax
Average Discount Percentage = 
DIVIDE(
    [Total Discounts],
    CALCULATE(SUM(Orders[Order_Amount]), Orders[Order_Status] = "Completed"),
    0
)
```
- **Plain Language Explanation:** Computes total discounts given as a percentage of gross fulfilled order value.
- **Business Purpose:** Monitors promotional intensity and guards against margin dilution.
- **Assumptions:** Both discount and gross order amounts are expressed in INR.

---

### 5.7 Delivery Performance Score
```dax
Delivery Performance Score = 
VAR OnTimeWeight = 0.60
VAR RatingWeight = 0.40
VAR OnTimeScore = [On-Time Delivery Percentage] * 100
VAR RatingScore = ([Average Customer Rating] / 5.0) * 100
RETURN
    (OnTimeScore * OnTimeWeight) + (RatingScore * RatingWeight)
```
- **Plain Language Explanation:** A composite index (0 to 100) combining On-Time Delivery Rate (60% weight) and Normalized Customer Rating (40% weight).
- **Business Purpose:** Provides leadership with a single, holistic logistics health score across cities and courier cohorts.
- **Assumptions:** Normalized to a 0–100 scale; formatted as a decimal number with 1 decimal place.
