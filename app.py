import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('E-commerce Company Insights')
st.write('Here is our LLM generated dashboard')
import matplotlib.pyplot as plt

# Data
categories = ['Outerwear & Coats', 'Suits & Sport Coats', 'Blazers & Jackets', 'Dresses', 'Suits']
margins = [81.04, 75.76, 57.48, 46.27, 45.98]

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(categories, margins, color='skyblue')
plt.xlabel('Product Categories')
plt.ylabel('Average Margin ($)')
plt.title('Top 5 Product Categories by Average Margin')
plt.xticks(rotation=45)

st.pyplot()
