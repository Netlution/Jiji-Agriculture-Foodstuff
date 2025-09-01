import streamlit as st


# use full screen width
st.set_page_config(layout="wide") 

st.title("About Us ")

st.header("Project Overview", anchor=False)

st.markdown("""
This project was developed as part of a broader initiative to **analyze agricultural market trends using data-driven techniques**.  
Our focus is on providing **valuable insights** into the online marketplace by examining pricing patterns, market distribution, and anomalies that could affect both **buyers and sellers**.  

We specialize in **web data extraction, cleaning, and analysis**, turning unstructured online information into actionable intelligence. By applying these methods to the Agriculture and Foodstuff category on [Jiji.ng](https://jiji.ng/agriculture-and-foodstuff), we offer a clearer understanding of how agricultural products are priced and distributed across different regions in Nigeria.  
""")

# st.image("././static/project_overview.jpg", caption="Agriculture is beautiful")
st.image("static/project_overview.jpg", caption="Agriculture is beautiful")

st.markdown("""
---
## Why This Analysis Matters  

### 📊 Importance of the Analysis  
- **Market Insights** → Identifies pricing trends and demand variations across products.  
- **Regional Comparisons** → Shows how prices shift across locations, reflecting supply and demand dynamics.  
- **Risk Detection** → Highlights outliers that may indicate unrealistic listings, fraud risks, or premium pricing.  
- **Decision-Making Support** → Provides a knowledge base for farmers, traders, policymakers, and businesses.  

### 🌐 Why Scrape Jiji.ng?  
Jiji.ng is one of Nigeria’s largest online marketplaces, widely used for buying and selling agricultural products.  
Scraping its data allows us to:  
- Collect **real-time, large-scale market information** not readily available elsewhere.  
- Understand the **economic value chain** of agricultural products online.  
- Build datasets that can guide **business strategy, economic research, and policy-making**.  

---

This project demonstrates how **web scraping and data analysis** can bridge the gap between **raw market data** and **strategic decision-making**, empowering stakeholders with reliable insights into Nigeria’s agricultural e-commerce landscape.  
""")

st.image("././static/why_choose_agriculture_and_foodstuff.jpg", caption="Why choose agriculture and foodstuff")


