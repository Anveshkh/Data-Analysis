import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 500)
pd.set_option('display.expand_frame_repr', False)  # Prevent line wrapping


df = pd.read_csv("dataset/Sales_Product_Details.csv")
print(df.head())

# Find out how many unique customers we have
print(df["Customer_ID"].unique())

# Find out how many unique products do we have
print(df["Product_ID"].unique())

# Find out the distribution of the prices of the Unit.
df["Unit_Price"].hist()
plt.title("Distribution of Unit_Prices", color="red")
plt.xlabel("Unit_Price")
plt.ylabel("Frequency")
plt.show()

# Find the shape of the data
print(df.shape)

# Which is the best-selling product category?
vals = df["Product_Category"].value_counts().values
plt.bar(["Menswear", "Womenswear", "Sports", "Accessories"], [13, 13, 2, 2])
plt.title("Best selling product category", color="red")
plt.xlabel("Product Categories")
plt.ylabel("Frequency")
plt.show()

# Which is the Region with most purchases
vals1 = df["Region"].value_counts().values
plt.bar(["Wakefield", "Wells", "Truro", "York", "Winchester", "Worcester"], vals1)
plt.title("Most Popular Regions", color="red")
plt.xlabel("Regions")
plt.ylabel("Frequency")
plt.show()

# Which product line is most popular?
vals2 = df["Product_Line"].value_counts().values
plt.bar(["Tops", "Trousers", "Leathers", "Shoes"], vals2)
plt.title("Most Popular Product_line", color="red")
plt.xlabel("Product_Line")
plt.ylabel("Frequency")
plt.show()

# Split date into three columns
def process_year(date):
    str_yr = str(date)
    return str_yr[:4]


def process_month(date):
    str_month = str(date)
    return str_month[4:6]


def process_day(date):
    str_day = str(date)
    return str_day[6:]


df["Year"] = df["Date"].apply(process_year)
df["Month"] = df["Date"].apply(process_month)
df["Day"] = df["Date"].apply(process_day)
df.drop("Date", axis=1, inplace=True)

print(df.head())

# Maximum price in each region
max_prices_by_region = df.groupby("Region")["Unit_Price"].max().values
print(max_prices_by_region)
plt.bar(["Truro", "Wakefield", "Wells", "Winchester", "Worcester", "York"], max_prices_by_region)
plt.title("Maximum Price in each region", color="red")
plt.xlabel("Regions")
plt.ylabel("Max price")
plt.show()

# Sales by region
sales_by_region = df.groupby("Region")["Sales_Revenue"].sum()
plt.bar(["Truro", "Wakefield", "Wells", "Winchester", "Worcester", "York"], sales_by_region)
plt.title("Sales by region", color="red")
plt.xlabel("Regions")
plt.ylabel("Revenue")
plt.show()