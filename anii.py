import streamlit as st
import pandas as pd

# Title
st.title("🛒 Grocery Store Sales Ledger")

# Ledger Data
data = {
    "Date": ["2025-04-28", "2025-04-28", "2025-04-28"],
    "Item Name": ["Apples", "Bananas", "Milk"],
    "Quantity": [5, 3, 2],
    "Price per Unit ($)": [1.00, 0.50, 2.00],
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Calculate Total Price
df["Total Price ($)"] = df["Quantity"] * df["Price per Unit ($)"]

# Display the table
st.table(df)
