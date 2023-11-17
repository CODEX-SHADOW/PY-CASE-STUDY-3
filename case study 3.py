import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a Pandas DataFrame from the sales data
df = pd.DataFrame({
    "date": pd.to_datetime(["2023-08-01", "2023-08-02", "2023-08-03"]),
    "product": ["Product 1", "Product 2", "Product 3"],
    "quantity": [10, 20, 30],
    "price": [10, 20, 30]
})

# Calculate total sales
df["total_sales"] = df["quantity"] * df["price"]

# Create a bar chart of total sales by product
plt.figure(figsize=(10, 6))
plt.bar(df["product"], df["total_sales"])
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.title("Sales by Product")
plt.show()

# Create a line chart of total sales by date
plt.figure(figsize=(10, 6))
plt.plot(df["date"], df["total_sales"])
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.title("Sales by Date")
plt.show()

# Create a pie chart of sales distribution by product
plt.figure(figsize=(6, 6))
plt.pie(df["total_sales"], labels=df["product"], autopct="%1.1f%%")
plt.title("Sales Distribution by Product")
plt.show()
