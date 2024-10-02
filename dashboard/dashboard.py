import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the cleaned dataset from the same directory
cleaned_file_path = 'cleaned_customers_data.csv'
customers_data_cleaned = pd.read_csv(cleaned_file_path)

# 1. Jumlah pelanggan di setiap state
state_counts = customers_data_cleaned['customer_state'].value_counts()

# Visualisasi: Bar Chart
st.subheader('Number of Customers by State')
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=state_counts.index, y=state_counts.values, palette='viridis', ax=ax)
ax.set_title('Number of Customers by State')
ax.set_xlabel('Customer State')
ax.set_ylabel('Number of Customers')
plt.xticks(rotation=45)
st.pyplot(fig)

# Menemukan state dengan jumlah customer paling sedikit
least_customers_state = state_counts.idxmin()
least_customers_count = state_counts.min()
st.write(f"The state with the least customers is {least_customers_state} with {least_customers_count} customers.")

# 2. Jumlah pelanggan di setiap state
# Visualisasi: Pie Chart untuk distribusi pelanggan
st.subheader('Customer Distribution by State')
fig, ax = plt.subplots(figsize=(10, 10))
ax.pie(state_counts, labels=state_counts.index, autopct='%1.1f%%', startangle=140)
ax.set_title('Customer Distribution by State')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
st.pyplot(fig)
