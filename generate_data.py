import os
import random
import csv
from datetime import datetime, timedelta

# Set seed for reproducibility
random.seed(42)

output_dir = os.path.join("Food_Delivery_PowerBI_Project", "Dataset")
os.makedirs(output_dir, exist_ok=True)

# -------------------------------------------------------------
# 1. LOCATIONS DATASET (10 Cities)
# -------------------------------------------------------------
cities_data = [
    {"City_ID": "CT101", "City_Name": "Mumbai", "State": "Maharashtra", "Region": "West", "Population_Category": "Tier 1", "Weight": 0.18},
    {"City_ID": "CT102", "City_Name": "Pune", "State": "Maharashtra", "Region": "West", "Population_Category": "Tier 1", "Weight": 0.09},
    {"City_ID": "CT103", "City_Name": "Bengaluru", "State": "Karnataka", "Region": "South", "Population_Category": "Tier 1", "Weight": 0.17},
    {"City_ID": "CT104", "City_Name": "Delhi", "State": "Delhi", "Region": "North", "Population_Category": "Tier 1", "Weight": 0.16},
    {"City_ID": "CT105", "City_Name": "Hyderabad", "State": "Telangana", "Region": "South", "Population_Category": "Tier 1", "Weight": 0.12},
    {"City_ID": "CT106", "City_Name": "Chennai", "State": "Tamil Nadu", "Region": "South", "Population_Category": "Tier 1", "Weight": 0.08},
    {"City_ID": "CT107", "City_Name": "Kolkata", "State": "West Bengal", "Region": "East", "Population_Category": "Tier 1", "Weight": 0.07},
    {"City_ID": "CT108", "City_Name": "Ahmedabad", "State": "Gujarat", "Region": "West", "Population_Category": "Tier 1", "Weight": 0.05},
    {"City_ID": "CT109", "City_Name": "Jaipur", "State": "Rajasthan", "Region": "North", "Population_Category": "Tier 2", "Weight": 0.04},
    {"City_ID": "CT110", "City_Name": "Nagpur", "State": "Maharashtra", "Region": "Central", "Population_Category": "Tier 2", "Weight": 0.04},
]

locations_file = os.path.join(output_dir, "Locations.csv")
with open(locations_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["City_ID", "City_Name", "State", "Region", "Population_Category"])
    writer.writeheader()
    for c in cities_data:
        writer.writerow({
            "City_ID": c["City_ID"],
            "City_Name": c["City_Name"],
            "State": c["State"],
            "Region": c["Region"],
            "Population_Category": c["Population_Category"]
        })

print(f"Locations.csv created with {len(cities_data)} records.")

# -------------------------------------------------------------
# 2. RESTAURANTS DATASET (250 Restaurants)
# -------------------------------------------------------------
food_categories = [
    "North Indian", "South Indian", "Biryani", "Fast Food", 
    "Chinese", "Desserts & Beverages", "Italian", "Mughlai", "Healthy Food", "Street Food"
]

restaurant_prefixes = [
    "Royal", "The Great", "Spice", "Taste of", "Bawarchi", "Golden", "Urban", "Flavors of",
    "Saffron", "Paradise", "Curry", "Desi", "Grand", "Little", "Street", "Hungry",
    "Chef's", "Crispy", "Tandoori", "Green", "Aroma", "Daily", "Southern", "Heritage"
]

restaurant_suffixes = [
    "Kitchen", "Dhaba", "Bistro", "Cafe", "Grill", "Court", "Hub", "Point",
    "Corner", "Plaza", "Treats", "Express", "Villa", "Bites", "Station", "House"
]

restaurant_types = ["Casual Dining", "Fast Food", "Fine Dining", "Bakery & Desserts", "Cloud Kitchen", "Cafe"]
price_categories = ["Budget", "Mid-Range", "Premium"]

restaurants = []
restaurant_id_counter = 1001

for city in cities_data:
    # Scale restaurant count per city weight (~250 total)
    city_res_count = max(15, int(city["Weight"] * 250))
    for _ in range(city_res_count):
        cat = random.choice(food_categories)
        res_type = random.choice(restaurant_types)
        price_cat = random.choice(price_categories)
        
        # Consistent prep time according to restaurant type
        if res_type == "Fast Food" or res_type == "Bakery & Desserts":
            prep_time = random.randint(12, 22)
        elif res_type == "Cloud Kitchen":
            prep_time = random.randint(15, 28)
        elif res_type == "Fine Dining":
            prep_time = random.randint(25, 45)
        else:
            prep_time = random.randint(18, 35)

        avg_rating = round(random.uniform(3.4, 4.9), 1)
        name = f"{random.choice(restaurant_prefixes)} {cat} {random.choice(restaurant_suffixes)}"
        
        # Ensure unique name per ID
        restaurants.append({
            "Restaurant_ID": f"RES{restaurant_id_counter}",
            "Restaurant_Name": name,
            "City_ID": city["City_ID"],
            "Restaurant_Type": res_type,
            "Food_Category": cat,
            "Average_Rating": avg_rating,
            "Average_Preparation_Time": prep_time,
            "Price_Category": price_cat,
            "Restaurant_Status": random.choices(["Active", "Inactive"], weights=[0.94, 0.06])[0]
        })
        restaurant_id_counter += 1

restaurants_file = os.path.join(output_dir, "Restaurants.csv")
with open(restaurants_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "Restaurant_ID", "Restaurant_Name", "City_ID", "Restaurant_Type", 
        "Food_Category", "Average_Rating", "Average_Preparation_Time", 
        "Price_Category", "Restaurant_Status"
    ])
    writer.writeheader()
    writer.writerows(restaurants)

print(f"Restaurants.csv created with {len(restaurants)} records.")

# -------------------------------------------------------------
# 3. CUSTOMERS DATASET (5,500 Customers)
# -------------------------------------------------------------
first_names = [
    "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai", "Reyansh", "Ayaan", "Krishna", "Ishaan",
    "Shaurya", "Atharva", "Ananya", "Diya", "Isha", "Aditi", "Tanvi", "Kavya", "Pooja", "Priya",
    "Rohan", "Rahul", "Sneha", "Neha", "Vikram", "Meera", "Deepak", "Anjali", "Karan", "Simran",
    "Manish", "Swati", "Nikhil", "Shreya", "Amit", "Ritu", "Gaurav", "Nisha", "Suresh", "Divya",
    "Sanjay", "Preeti", "Sunil", "Payal", "Rajesh", "Poonam", "Ajay", "Komal", "Vikas", "Monika"
]

last_names = [
    "Sharma", "Verma", "Patel", "Gupta", "Singh", "Kumar", "Mehta", "Shah", "Reddy", "Nair",
    "Iyer", "Rao", "Joshi", "Kulkarni", "Deshmukh", "Choudhury", "Bose", "Banerjee", "Chatterjee",
    "Mishra", "Pandey", "Trivedi", "Bhatia", "Kapoor", "Malhotra", "Saxena", "Agarwal", "Jain",
    "Pillai", "Menon", "Shetty", "Hegde", "Ghosh", "Mukherjee", "Das", "Dutta", "Yadav", "Chauhan"
]

customer_segments = ["Regular Customer", "Premium Customer", "New Customer", "Inactive Customer"]
segment_weights = [0.45, 0.20, 0.25, 0.10]

city_ids_list = [c["City_ID"] for c in cities_data]
city_weights_list = [c["Weight"] for c in cities_data]

customers = []
start_reg_date = datetime(2023, 1, 1)

for cid in range(10001, 15501):
    c_city = random.choices(city_ids_list, weights=city_weights_list)[0]
    first = random.choice(first_names)
    last = random.choice(last_names)
    gender = random.choices(["Male", "Female", "Other"], weights=[0.52, 0.46, 0.02])[0]
    age = random.choices(
        [random.randint(18, 24), random.randint(25, 34), random.randint(35, 49), random.randint(50, 65)],
        weights=[0.30, 0.45, 0.18, 0.07]
    )[0]
    
    # Registration date between 2023-01-01 and 2024-10-31
    reg_days = random.randint(0, 670)
    reg_date = (start_reg_date + timedelta(days=reg_days)).strftime("%Y-%m-%d")
    
    seg = random.choices(customer_segments, weights=segment_weights)[0]
    
    customers.append({
        "Customer_ID": f"CUST{cid}",
        "Customer_Name": f"{first} {last}",
        "Age": age,
        "Gender": gender,
        "City_ID": c_city,
        "Registration_Date": reg_date,
        "Customer_Segment": seg
    })

customers_file = os.path.join(output_dir, "Customers.csv")
with open(customers_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "Customer_ID", "Customer_Name", "Age", "Gender", "City_ID", 
        "Registration_Date", "Customer_Segment"
    ])
    writer.writeheader()
    writer.writerows(customers)

print(f"Customers.csv created with {len(customers)} records.")

# -------------------------------------------------------------
# 4. DELIVERY PARTNERS DATASET (350 Partners)
# -------------------------------------------------------------
partner_first_names = [
    "Ramesh", "Suresh", "Mahesh", "Ganesh", "Dinesh", "Mukesh", "Naresh", "Santosh", "Sachin", "Vijay",
    "Ashok", "Pramod", "Deepak", "Anil", "Sunil", "Vinod", "Manoj", "Pradeep", "Sanjay", "Raju",
    "Ajay", "Bablu", "Chandan", "Dharmendra", "Govind", "Hari", "Jagdish", "Kishore", "Laxman", "Mohan"
]

vehicle_types = ["Motorcycle", "Scooter", "Electric Bike", "Bicycle"]
vehicle_weights = [0.55, 0.25, 0.15, 0.05]

delivery_partners = []
start_join_date = datetime(2022, 1, 1)

for pid in range(1001, 1351):
    p_city = random.choices(city_ids_list, weights=city_weights_list)[0]
    name = f"{random.choice(partner_first_names)} {random.choice(last_names)}"
    v_type = random.choices(vehicle_types, weights=vehicle_weights)[0]
    
    join_days = random.randint(0, 730)
    join_date = (start_join_date + timedelta(days=join_days)).strftime("%Y-%m-%d")
    
    p_rating = round(random.uniform(3.8, 5.0), 1)
    completed_del = random.randint(50, 1800)
    
    delivery_partners.append({
        "Delivery_Partner_ID": f"DP{pid}",
        "Partner_Name": name,
        "City_ID": p_city,
        "Vehicle_Type": v_type,
        "Joining_Date": join_date,
        "Partner_Rating": p_rating,
        "Completed_Deliveries": completed_del
    })

delivery_partners_file = os.path.join(output_dir, "Delivery_Partners.csv")
with open(delivery_partners_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "Delivery_Partner_ID", "Partner_Name", "City_ID", "Vehicle_Type", 
        "Joining_Date", "Partner_Rating", "Completed_Deliveries"
    ])
    writer.writeheader()
    writer.writerows(delivery_partners)

print(f"Delivery_Partners.csv created with {len(delivery_partners)} records.")

# -------------------------------------------------------------
# 5. ORDERS DATASET (18,000 Records)
# -------------------------------------------------------------
# Index entities by city for rapid lookup and realistic referential alignment
city_restaurants = {}
for r in restaurants:
    city_restaurants.setdefault(r["City_ID"], []).append(r)

city_customers = {}
for c in customers:
    city_customers.setdefault(c["City_ID"], []).append(c)

city_partners = {}
for p in delivery_partners:
    city_partners.setdefault(p["City_ID"], []).append(p)

payment_methods = ["UPI", "Credit Card", "Debit Card", "Cash on Delivery", "Digital Wallet", "Net Banking"]
payment_weights = [0.52, 0.18, 0.12, 0.10, 0.05, 0.03]

cancellation_reasons = [
    "Customer Changed Mind",
    "Restaurant Preparation Delay",
    "Delivery Partner Unavailable",
    "Wrong Address Provided",
    "Item Out of Stock",
    "Weather/Traffic Disruption"
]

order_start_date = datetime(2024, 1, 1)
total_days = 366  # 2024 is a leap year

orders = []
order_id_counter = 100001
target_orders = 18000

for i in range(target_orders):
    # Select city according to population/market weight
    city = random.choices(cities_data, weights=[c["Weight"] for c in cities_data])[0]
    cid = city["City_ID"]
    
    # Select customer from this city
    cust = random.choice(city_customers[cid])
    
    # Select restaurant from this city (must be active or very rarely inactive)
    res = random.choice(city_restaurants[cid])
    
    # Select delivery partner from this city
    partner = random.choice(city_partners[cid])
    
    # Realistic date generation with seasonal trends (festive peak in Oct/Nov, monsoon dip/peak)
    day_offset = random.randint(0, total_days - 1)
    o_date = order_start_date + timedelta(days=day_offset)
    
    # Weekend surge (Friday, Saturday, Sunday have higher order probability)
    weekday = o_date.weekday() # 4=Fri, 5=Sat, 6=Sun
    is_weekend = weekday in [4, 5, 6]
    
    # Realistic time generation with Lunch peak (12:00 - 14:45) and Dinner peak (19:00 - 22:45)
    time_slot = random.choices(["Lunch", "Dinner", "Evening_Snacks", "Late_Night", "Breakfast/Morning"], weights=[0.35, 0.45, 0.10, 0.06, 0.04])[0]
    if time_slot == "Lunch":
        hr = random.randint(12, 14)
    elif time_slot == "Dinner":
        hr = random.randint(19, 22)
    elif time_slot == "Evening_Snacks":
        hr = random.randint(16, 18)
    elif time_slot == "Late_Night":
        hr = random.choice([23, 0, 1])
    else:
        hr = random.randint(8, 11)
        
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    o_time = f"{hr:02d}:{minute:02d}:{second:02d}"
    
    food_cat = res["Food_Category"]
    price_tier = res["Price_Category"]
    
    # Order Amount based on price tier and customer segment
    if price_tier == "Budget":
        base_amt = random.randint(150, 450)
    elif price_tier == "Mid-Range":
        base_amt = random.randint(350, 850)
    else: # Premium
        base_amt = random.randint(700, 1800)
        
    if cust["Customer_Segment"] == "Premium Customer":
        base_amt = int(base_amt * random.uniform(1.15, 1.4))
    
    order_amount = round(base_amt, 2)
    
    # Discount amount (promotions: higher on large orders and weekends)
    has_discount = random.random() < 0.65
    if has_discount:
        disc_pct = random.choice([0.10, 0.15, 0.20, 0.25, 0.30])
        discount_amount = round(min(order_amount * disc_pct, random.randint(50, 250)), 2)
    else:
        discount_amount = 0.0
        
    # Delivery fee: standard 30-60, free delivery for premium or large orders > 600
    if order_amount > 650 or (cust["Customer_Segment"] == "Premium Customer" and random.random() < 0.7):
        delivery_fee = 0.0
    else:
        delivery_fee = float(random.choice([25, 35, 45, 50, 60]))
        
    payment_method = random.choices(payment_methods, weights=payment_weights)[0]
    
    # Estimated Delivery Time (minutes) = Prep time + travel time (15-30 mins)
    est_prep = res["Average_Preparation_Time"]
    est_travel = random.randint(14, 28)
    est_delivery_time = est_prep + est_travel
    
    # Order Status: ~88% Completed, ~12% Cancelled
    # Rainy season (June-August) or peak dinner has slightly higher cancellation
    is_monsoon = o_date.month in [6, 7, 8]
    cancel_prob = 0.10
    if is_monsoon: cancel_prob += 0.03
    if hr in [20, 21]: cancel_prob += 0.02
    
    is_cancelled = random.random() < cancel_prob
    
    if is_cancelled:
        order_status = "Cancelled"
        cancellation_reason = random.choice(cancellation_reasons)
        actual_delivery_time = ""  # Blank for cancelled orders
        customer_rating = ""       # Blank for cancelled orders
    else:
        order_status = "Completed"
        cancellation_reason = ""
        
        # Delivery delay logic:
        # Delays happen more often during peak hours (13, 20, 21), bad weather, or bicycle/busy vehicle
        is_rush = hr in [13, 20, 21]
        delay_chance = 0.28 if (is_rush or is_monsoon) else 0.14
        
        if random.random() < delay_chance:
            # Delayed order
            delay_minutes = random.randint(6, 35)
            actual_delivery_time = est_delivery_time + delay_minutes
        else:
            # On-time or early
            saving = random.randint(-4, 5)
            actual_delivery_time = max(18, est_delivery_time - saving)
            
        # Rating correlation:
        # If delayed significantly (>15 mins), rating drops heavily
        delay = actual_delivery_time - est_delivery_time
        if delay > 20:
            rating_pool = [1, 2, 3]
            rating_weights = [0.45, 0.40, 0.15]
        elif delay > 8:
            rating_pool = [2, 3, 4]
            rating_weights = [0.25, 0.45, 0.30]
        elif actual_delivery_time <= est_delivery_time:
            rating_pool = [4, 5]
            rating_weights = [0.35, 0.65]
        else:
            rating_pool = [3, 4, 5]
            rating_weights = [0.20, 0.50, 0.30]
            
        # Sometimes customers don't rate (~15% unrated)
        if random.random() < 0.15:
            customer_rating = ""
        else:
            customer_rating = random.choices(rating_pool, weights=rating_weights)[0]
            
    orders.append({
        "Order_ID": f"ORD{order_id_counter}",
        "Order_Date": o_date.strftime("%Y-%m-%d"),
        "Order_Time": o_time,
        "Customer_ID": cust["Customer_ID"],
        "Restaurant_ID": res["Restaurant_ID"],
        "Delivery_Partner_ID": partner["Delivery_Partner_ID"],
        "City_ID": cid,
        "Food_Category": food_cat,
        "Order_Amount": order_amount,
        "Discount_Amount": discount_amount,
        "Delivery_Fee": delivery_fee,
        "Payment_Method": payment_method,
        "Order_Status": order_status,
        "Cancellation_Reason": cancellation_reason,
        "Estimated_Delivery_Time_Minutes": est_delivery_time,
        "Actual_Delivery_Time_Minutes": actual_delivery_time,
        "Customer_Rating": customer_rating
    })
    order_id_counter += 1

orders_file = os.path.join(output_dir, "Orders.csv")
with open(orders_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "Order_ID", "Order_Date", "Order_Time", "Customer_ID", "Restaurant_ID", 
        "Delivery_Partner_ID", "City_ID", "Food_Category", "Order_Amount", 
        "Discount_Amount", "Delivery_Fee", "Payment_Method", "Order_Status", 
        "Cancellation_Reason", "Estimated_Delivery_Time_Minutes", 
        "Actual_Delivery_Time_Minutes", "Customer_Rating"
    ])
    writer.writeheader()
    writer.writerows(orders)

print(f"Orders.csv created with {len(orders)} records.")
print("All datasets generated successfully!")
