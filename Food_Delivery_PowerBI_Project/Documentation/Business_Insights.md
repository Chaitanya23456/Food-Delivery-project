# Business Insights & Executive Analytical Findings

**Project:** Food Delivery & Restaurant Performance Analytics  
**Data Grain:** 18,000 Transactions | 10 Metropolitan Hubs | 261 Restaurants | 5,500 Customers | 350 Couriers  
**Analysis Period:** Calendar Year 2024  

---

## Executive Scorecard

| Metric | Measured Value | Benchmark / Target | Variance / Health |
|---|---|---|---|
| **Total Orders Placed** | **18,000** | — | Top-of-funnel transaction volume |
| **Fulfilled Orders** | **15,901 (88.34%)** | $> 88.0\%$ | Within healthy operational limits |
| **Cancelled Orders** | **2,099 (11.66%)** | $< 10.0\%$ | Needs operational intervention |
| **Total Completed Revenue (GMV)** | **₹12,291,275.00** | ₹12.0M Target | $+2.43\%$ vs. annual baseline plan |
| **Average Order Value (AOV)** | **₹772.99** | ₹750.00 | $+3.07\%$ basket size performance |
| **Total Discounts Extended** | **₹1,198,341.25** | $< 10.0\%$ of GMV | $9.75\%$ discount burn rate |
| **Total Delivery Fees Collected**| **₹300,080.00** | — | Direct logistics cost recovery |
| **Average Door-to-Door Delivery**| **49.50 Minutes** | $< 45.0$ Minutes | $+4.50$ Minutes over SLA target |
| **On-Time Delivery Rate** | **47.32%** | $> 75.0\%$ | Severe bottleneck during rush hours |
| **Average Customer Rating** | **4.01 / 5.00** | $> 4.20$ | Rated across 13,517 customer responses |
| **Repeat Customer Rate** | **82.14%** | $> 70.0\%$ | Strong platform brand stickiness |

---

## 18 Key Business Insights Derived Directly from Data

### 1. Geographic Revenue Leadership: Bengaluru and Mumbai Generate Over 35% of Total GMV
- **Data Finding:** Bengaluru is the highest revenue-generating city at **₹2,239,669.00** across 3,095 orders, closely followed by Mumbai at **₹2,180,332.00** (3,233 orders) and Delhi at **₹1,976,913.00** (2,795 orders). Together, these top three mega-metros account for **₹6,396,914.00 (52.04%)** of total platform revenue.
- **Strategic Recommendation:** Focus corporate tier-1 partnerships and cloud kitchen expansions in Bengaluru and Mumbai. In Tier-2 cities like Nagpur (₹402,186.00) and Jaipur (₹470,132.00), lower order density can be boosted through local festival promotions and regional merchant onboarding.

---

### 2. Cuisine Demand Hierarchy: Mughlai and Street Food Dominate Order Volume
- **Data Finding:** **Mughlai** cuisine leads overall revenue generation at **₹1,868,451.00** with 2,386 fulfilled orders (AOV: ₹783.09). **Street Food** ranks second with **₹1,432,046.00** (1,846 orders). 
- **Premium Cuisine Basket Size:** While Mughlai has the highest gross volume, **Italian** cuisine captures the highest Average Order Value at **₹853.00** per order (1,544 completed orders yielding ₹1,317,027.00), followed by **Fast Food** at **₹831.00**.
- **Strategic Recommendation:** Bundle Mughlai family platters during dinner slots to maintain high margin flow, while launching Italian merchant cross-promotions on weekends to drive basket expansion.

---

### 3. Top Merchant Concentration: High-Performing Restaurants Drive Platform Loyalty
- **Data Finding:** The top 10 individual restaurants out of 261 onboarded merchants contribute over **₹1.03 Million** in realized revenue.
  1. `Saffron Italian House` (RES1086, Bengaluru): **₹109,436.00** (80 orders, 4.8 Rating)
  2. `Urban North Indian Hub` (RES1103, Bengaluru): **₹109,396.00** (83 orders, 4.8 Rating)
  3. `Taste of North Indian Station` (RES1127, Delhi): **₹106,564.00** (76 orders, 3.9 Rating)
  4. `Curry Chinese Villa` (RES1129, Delhi): **₹106,197.00** (77 orders, 4.4 Rating)
  5. `Paradise Chinese Station` (RES1108, Bengaluru): **₹101,869.00** (76 orders, 4.3 Rating)
- **Strategic Recommendation:** Implement a "Premier Merchant SLA" program for top vendors, providing them with dedicated priority delivery couriers during peak meal times to protect their 4.8+ ratings.

---

### 4. Peak Demand Windows: Lunch and Dinner Account for 79.96% of Daily Volume
- **Data Finding:** Order patterns exhibit a bimodal distribution:
  - **Lunch Rush (12:00 PM – 2:59 PM):** **6,331 orders (35.17%)**
  - **Dinner Rush (7:00 PM – 10:59 PM):** **8,062 orders (44.79%)**
  - **Off-Peak Morning (8:00 AM – 11:59 AM):** Only 661 orders (3.67%)
- **Strategic Recommendation:** Implement surge incentive pricing for delivery riders between 12:00–2:30 PM and 7:30–10:00 PM. Launch breakfast and morning snack discounts ("Breakfast Combos") to monetize kitchen idle capacity between 8:00 AM and 11:00 AM.

---

### 5. Delivery SLA Breaches: 52.68% of Orders Suffer Delays
- **Data Finding:** Out of 15,901 completed orders, **8,376 orders (52.68%)** were delivered after the estimated delivery time, with an average delay of **9.76 minutes** on late orders. Overall actual delivery time averaged **49.50 minutes** against an estimated promise of **45.55 minutes**.
- **Root Cause Correlation:** Delays surge by over 60% during the 8:00–9:00 PM dinner peak and during monsoon season (June–August), where rain and traffic congestion heavily slow down two-wheelers.
- **Strategic Recommendation:** Implement dynamic machine learning ETA estimation during peak hours, adding a 10–12 minute buffer to prevent customer dissatisfaction and false delivery expectations.

---

### 6. Delivery Delay Impact on Customer Ratings
- **Data Finding:** Rating data reveals a direct link between delivery punctuality and customer satisfaction:
  - Deliveries completed **on or before ETA** have an average rating of **4.62 / 5.0**.
  - Deliveries delayed by **8 to 20 minutes** drop to an average rating of **3.31 / 5.0**.
  - Deliveries delayed by **$>20$ minutes** drop sharply to **1.68 / 5.0**, with 45% of these customers giving a 1-star rating.
- **Strategic Recommendation:** Trigger automated real-time apologies with wallet credits (e.g. ₹50 voucher) as soon as an order crosses the +15-minute delay threshold to salvage customer retention.

---

### 7. Cancellation Root-Cause Analysis: Merchant Delays and Traffic Cause 35.54% of Drop-Offs
- **Data Finding:** 2,099 orders (11.66%) were cancelled. The primary drivers are:
  1. `Restaurant Preparation Delay`: **383 orders (18.25%)**
  2. `Weather/Traffic Disruption`: **363 orders (17.29%)**
  3. `Item Out of Stock`: **359 orders (17.10%)**
  4. `Wrong Address Provided`: **354 orders (16.87%)**
  5. `Customer Changed Mind`: **325 orders (15.48%)**
  6. `Delivery Partner Unavailable`: **315 orders (15.01%)**
- **Strategic Recommendation:** Provide restaurant partners with tablet alerts when kitchen prep exceeds 20 minutes. Implement auto-inventory syncing to prevent orders for out-of-stock items.

---

### 8. City-Level Cancellation Disparity: Hyderabad Highest, Nagpur Lowest
- **Data Finding:** 
  - **Highest Cancellation:** Hyderabad recorded the highest cancellation rate at **12.37%** (266 cancellations out of 2,151 orders).
  - **Lowest Cancellation:** Nagpur demonstrated the lowest cancellation rate at **9.93%** (69 cancellations out of 695 orders), followed by Ahmedabad at **11.08%**.
- **Strategic Recommendation:** Audit courier availability and restaurant prep delays in Hyderabad's high-demand IT corridors (Hitec City, Gachibowli) where supply bottlenecks are concentrated.

---

### 9. Digital Payment Dominance: UPI Captures 51.67% Share
- **Data Finding:** 
  - **UPI** is the dominant payment rail, powering **9,300 orders (51.67%)** and **₹6,316,459.00** in completed revenue.
  - **Credit Cards** generate **3,239 orders (17.99%)** with the highest AOV of **₹796.42**.
  - **Cash on Delivery (COD)** accounts for only **1,835 orders (10.19%)**.
  - **Digital Wallets** and **Net Banking** make up the remaining 8.15%.
- **Strategic Recommendation:** UPI and Credit Cards deliver the lowest settlement friction and zero cash-handling risks. Partner with leading UPI payment apps (PhonePe, Google Pay) to offer co-branded cashback promotions.

---

### 10. Customer Segmentation Economics: Premium Customers Spend 29.3% More Per Order
- **Data Finding:**
  - `Regular Customers`: 7,205 completed orders (₹5,264,650.00 GMV) with an AOV of **₹730.69**.
  - `Premium Customers`: 3,126 completed orders (₹2,954,428.00 GMV) with an industry-leading AOV of **₹945.11**.
  - `New Customers`: 3,902 completed orders (₹2,847,646.00 GMV) with an AOV of **₹729.79**.
  - `Inactive Customers`: 1,668 completed orders (₹1,224,551.00 GMV).
- **Strategic Recommendation:** Premium subscribers generate ₹214 more per order than regular users. Invest in loyalty perks (e.g. zero delivery fee, priority customer support) to convert Regular users into Premium members.

---

### 11. Exceptional Customer Retention: 82.14% Repeat Order Rate
- **Data Finding:** Out of 5,206 distinct customers who placed completed orders in 2024, **4,276 customers (82.14%)** placed 2 or more orders. Only 930 users were single-order churn risks.
- **Top Spender Profile:** The highest spending customer, `Preeti Pillai` (CUST12449), completed 11 orders totaling **₹10,417.00**, followed by `Neha Hegde` (CUST13040) with 7 orders totaling **₹9,863.00**.
- **Strategic Recommendation:** Launch automated personalized re-ordering nudges for users after 14 days of inactivity to protect this 82% repeat retention rate.

---

### 12. Fleet Vehicle Performance: Bicycles Suffer Highest Delays; EV Adoption Shows High Promise
- **Data Finding:**
  - `Motorcycles`: 8,956 orders (56.32% fleet share), 52.41% delay rate, $+3.81$ min average delay/lead.
  - `Scooters`: 4,220 orders (26.54% fleet share), 53.06% delay rate, $+4.12$ min average delay/lead.
  - `Electric Bikes`: 1,915 orders (12.04% fleet share), 52.43% delay rate, $+4.08$ min average delay/lead.
  - `Bicycles`: 810 orders (5.09% fleet share), **54.20% delay rate**, $+4.12$ min average delay/lead.
- **Strategic Recommendation:** Restrict Bicycle dispatch radii to $<2.5$ km hyper-local deliveries. Accelerate Electric Bike onboarding with battery-swapping partnerships, as EVs match motorcycle delivery times while lowering fuel overhead.

---

### 13. Courier Fleet Leaders: Top Delivery Partners Deliver High Reliability
- **Data Finding:** The platform's top delivery partners consistently complete high order volumes while maintaining 4.0+ ratings:
  - `Kishore Iyer` (DP1178, Motorcycle): **75 orders**, 4.0 Rating
  - `Deepak Reddy` (DP1324, Scooter): **74 orders**, 4.0 Rating
  - `Sunil Verma` (DP1318, Scooter): **74 orders**, 4.4 Rating
  - `Laxman Trivedi` (DP1268, Motorcycle): **71 orders**, 4.6 Rating
  - `Dharmendra Saxena` (DP1046, Motorcycle): **70 orders**, 4.0 Rating
- **Strategic Recommendation:** Establish quarterly performance bonuses and fuel allowances for couriers completing $>70$ orders per month with ratings $>4.2$.

---

### 14. Promotional Efficiency: 65.16% of Orders Utilize Discounts
- **Data Finding:** 11,729 orders utilized discounts totaling **₹1,198,341.25** (average discount ₹102.17 per discounted order). 
- **Discount vs. Basket Size:** Discounted orders achieved an average order size of **₹771.45**, compared to **₹782.71** for full-price orders (6,271 orders).
- **Strategic Recommendation:** Discounts are effectively driving trial and order velocity without excessively eroding basket sizes. Shift from flat percentage discounts (e.g. "20% off") to tiered minimum basket spend coupons (e.g. "₹100 off on orders above ₹800") to push AOVs past ₹850.

---

### 15. Demographic Insights: Young Professionals (25–34) Drive 44.5% of Revenue
- **Data Finding:**
  - `Age 25–34 (Young Professionals)`: **8,097 orders (44.98%)**, generating **₹5,470,226.00**.
  - `Age 18–24 (Gen Z / College)`: **5,319 orders (29.55%)**, generating **₹3,665,824.00**.
  - `Age 35–49 (Families / Mid-Career)`: **3,515 orders (19.53%)**, generating **₹2,436,878.00**.
  - `Age 50–65 (Seniors)`: **1,069 orders (5.94%)**, generating **₹718,347.00**.
- **Strategic Recommendation:** Design mobile app UI experiences tailored to Young Professionals and Gen Z, featuring one-click checkout, split-billing options, and late-night curated menus.

---

### 16. Day of Week Ordering Patterns: Weekend Order Surges
- **Data Finding:** The three weekend days (Friday, Saturday, Sunday) generate **7,636 orders (42.42%)** and **₹5,173,442.00** in revenue. On a daily basis, weekend demand averages **2,545 orders/day**, with Saturday dinner exhibiting the single highest hourly order spike across the entire week.
- **Strategic Recommendation:** Reallocate merchant marketing budgets and platform ad inventory to run from Friday 4:00 PM through Sunday midnight.

---

### 17. Stable Monthly Run-Rate Across 2024
- **Data Finding:** Platform revenue remained stable across all 12 months, averaging ~₹1.02M per month:
  - **Highest Month:** September 2024 at **₹1,057,424.00** (1,341 orders), closely followed by January (₹1,052,011.00) and July (₹1,047,634.00).
  - **Lowest Month:** February 2024 at **₹960,748.00** (1,225 orders), due to the shorter 29-day month.
- **Strategic Recommendation:** Monthly revenue stability indicates a mature, non-seasonal core customer habit. Introduce targeted festival campaigns in Q4 to capitalize on the Indian festive season.

---

### 18. Logistics Cost Recovery: Delivery Fees Offset Platform Costs
- **Data Finding:** The platform collected **₹300,080.00** in delivery fees from 15,901 completed orders, averaging ₹18.87 per fulfilled order across all customer tiers (including zero-fee premium orders).
- **Strategic Recommendation:** For small basket orders ($<\text{₹250}$), consider increasing the delivery fee from ₹35 to ₹45 to cover courier fulfillment costs without affecting customer retention.
