# Jiji-Agriculture-Foodstuff


# Home page
import streamlit as st
import numpy as np
import pandas as pd
import base64
from style import set_black_background

set_black_background() 

# ========== CUSTOM CSS ==========
sidebar_bg = """
<style>
[data-testid="stSidebar"] {
    background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
                url("https://images.unsplash.com/photo-1602621951019-1b8ca8f9e7d9");
    background-size: cover;
    background-position: center;
}
[data-testid="stSidebar"] * {
    color: white !important;
}
</style>
"""

st.markdown(sidebar_bg, unsafe_allow_html=True)


# ========== BOOTSTRAP NAVBAR ==========
st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" 
rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
""", unsafe_allow_html=True)

st.markdown("""
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" 
integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)

st.markdown("""
<nav class="navbar navbar-expand-lg navbar-light bg-light" style="background-color: blue;margin-top: -70px;">
  <div class="container-fluid" >
    <a class="navbar-brand" href="https://streamlit.io/">Streamlit</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" 
    aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item"><a class="nav-link active" aria-current="page" href="https://streamlit.io/gallery">Gallery</a></li>
        <li class="nav-item"><a class="nav-link" href="https://streamlit.io/components">Components</a></li>
        <li class="nav-item"><a class="nav-link" href="https://streamlit.io/cloud">Cloud</a></li>
        <li class="nav-item"><a class="nav-link" href="https://streamlit.io/community" tabindex="-1">Community</a></li>
      </ul>
    </div>
  </div>
</nav>
""", unsafe_allow_html=True)


# ========== SIDEBAR NAVIGATION ==========
About = st.Page(page="pages/About.py", title="About", icon="🅰️")
Analysis = st.Page(page="pages/Analysis.py", title="Analysis", icon="📈")
Visualization = st.Page(page="pages/Visualization.py", title="Visualization", icon="Ⓜ️")
Contact = st.Page(page="pages/Contact.py", title="Contact", icon="🏦")

pg = st.navigation([About, Analysis, Visualization, Contact])
pg.run()


#About page
import streamlit as st
from pathlib import Path
from style import set_black_background

set_black_background() 


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
# st.image("static/project_overview.jpg", caption="Agriculture is beautiful")

# Base directory (Generalpages)
BASE_DIR = Path(__file__).resolve().parent.parent  

# Point to static folder
STATIC_DIR = BASE_DIR / "static"

# Images
st.image(STATIC_DIR / "project_overview.jpg", caption="Agriculture is beautiful")

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

# st.image("././static/why_choose_agriculture_and_foodstuff.jpg", caption="Why choose agriculture and foodstuff")

# Base directory (Generalpages)
BASE_DIR = Path(__file__).resolve().parent.parent  

# Point to static folder
STATIC_DIR = BASE_DIR / "static"

# Images
st.image(STATIC_DIR / "why_choose_agriculture_and_foodstuff.jpg", caption="Why choose agriculture and foodstuff")

# Analysis page
import streamlit as st
import pandas as pd
import plotly.express as px  
from pathlib import Path
from style import set_black_background

set_black_background() 


# use full screen width
st.set_page_config(layout="wide") 

# Load Data
# with st.expander("See Table below"):
#     # df = pd.read_csv(r"C:\Users\user\Desktop\Web scrapping project\jijipage5_data.csv")
#     df = pd.read_csv("data/jijipage5_data.csv")

    
    # # Reset index and start from 1
    # df_reset = df.head(10).reset_index(drop=True)
    # df_reset.index = df_reset.index + 1
    
    # st.table(df_reset)

# Step 1: go up ONE level from Analysis.py → Generalpages/
BASE_DIR = Path(__file__).resolve().parent.parent  

# Step 2: point to the Data folder
DATA_PATH = BASE_DIR / "Data" / "jijipage5_data.csv"

with st.expander("See Table below"):
    df = pd.read_csv(DATA_PATH)

    # Reset index and start from 1
    df_reset = df.head(10).reset_index(drop=True)
    df_reset.index = df_reset.index + 1

    st.table(df_reset)

# Introduction
st.markdown("""
    ### Introduction  

    This analysis is based on data scraped from the **Agriculture and Foodstuff** category on [Jiji.ng](https://jiji.ng/agriculture-and-foodstuff).  
    The dataset contains product listings with details such as **title, price, and location**.  

    The purpose of this analysis is to explore pricing patterns, detect anomalies, and understand market distribution across different locations.  
    We summarize the data using descriptive statistics and tab-based visualizations:  

    - **Table Analysis** highlights total, maximum, and minimum prices, while also flagging unusually high values and items above certain thresholds.  
    - **Price Analysis** provides deeper insights by grouping ads by product titles and locations, showing median and average price variations across different regions.  

    This gives a clear overview of pricing behavior in the agricultural and foodstuff sector on Jiji.ng, helping to identify trends, outliers, and possible opportunities in the market.  
""")

# st.image("././static/intro_agriculture_and_foodstuff.jpg", caption="intro_agriculture_and_foodstuff")

# Base directory (Generalpages)
BASE_DIR = Path(__file__).resolve().parent.parent  

# Point to static folder
STATIC_DIR = BASE_DIR / "static"

# Images
st.image(STATIC_DIR / "intro_agriculture_and_foodstuff.jpg", caption="Intro agriculture and foodstuff")

# Table Analysis
st.subheader("Table analysis")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Total Price", 
    "Maximum Price", 
    "Minimum Price", 
    "Items above 100k", 
    "Outlier Detection (Price > 1M)"
])

with tab1:
    st.markdown("*Total* **Price**.")
    total_price = df["Price"].sum()
    st.write(f"{total_price:,.0f}")  # formatted with commas

with tab2:
    st.markdown("*Maximum* **Price**.")
    max_price = df["Price"].max()
    st.write(f"{max_price:,.0f}")

with tab3:
    st.markdown("*Minimum* **Price**.")
    min_price = df["Price"].min()
    st.write(f"{min_price:,.0f}")

with tab4:
    st.markdown("*Items above 100k*.")
    price_above_100k = df[df["Price"] > 100_000]
    st.dataframe(price_above_100k)

with tab5:
    st.markdown("*Outlier Detection (Price > 1M)*.")
    outlier_detection = df[df["Price"] > 1_000_000]
    st.dataframe(outlier_detection)


# Price Analysis
st.subheader("Price analysis")

sectab1, sectab2, sectab3 = st.tabs([
    "Title by price", 
    "Median Price per Location", 
    "Average Price per Location"
])

with sectab1:
    title_price = (
        df.groupby("Title")["Price"]
        .count()
        .reset_index()
        .rename(columns={"Price": "Count"})
        .sort_values(by="Count", ascending=False)
    )
    title_price.index = range(1, len(title_price) + 1)  # Index starts from 1
    st.dataframe(title_price)


with sectab2:
    median_price = (
        df.groupby("Location")["Price"]
        .median()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    median_price.index = range(1, len(median_price) + 1)  
    st.dataframe(median_price)

with sectab3:
    avg_price = (
        df.groupby("Location")["Price"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    avg_price.index = range(1, len(avg_price) + 1) 
    st.dataframe(avg_price)

    import streamlit as st
import pandas as pd
import mysql.connector
from pathlib import Path
from style import set_black_background

set_black_background() 

# Title
st.title("Message Us")


# use full screen width
st.set_page_config(layout="wide")  

# Step 1: go up ONE level from Analysis.py → Generalpages/
BASE_DIR = Path(__file__).resolve().parent.parent  

# Step 2: point to the Data folder
DATA_PATH = BASE_DIR / "Data" / "jijipage5_data.csv"

with st.expander("See Table below"):
    df = pd.read_csv(DATA_PATH)

    # Reset index and start from 1
    df_reset = df.head(10).reset_index(drop=True)
    df_reset.index = df_reset.index + 1

    st.table(df_reset)

# MySQL connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",       # or your server
        user="Netlution",
        password="Samkuljax1995",
        database="contact_form_db"
    )

# Save data to MySQL
def save_to_db(first_name, last_name, address, phone_number, message):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO submissions (first_name, last_name, address, phone_number, message)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (first_name, last_name, address, phone_number, message))
    conn.commit()
    cursor.close()
    conn.close()

#Contact page

# Simple Form 
with st.form("contact_form"):
    st.subheader("Contact Form")
    
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    address = st.text_area("Address")
    phone_number = st.text_input("Phone Number")
    message = st.text_area("Your Message")

    submitted = st.form_submit_button("Submit")
    
    if submitted:
        missing_fields = []
        if not first_name:
            missing_fields.append("First Name")
        if not last_name:
            missing_fields.append("Last Name")
        if not address:
            missing_fields.append("Address")
        if not phone_number:
            missing_fields.append("Phone Number")
        if not message:
            missing_fields.append("Message")
        
        if missing_fields:
            st.error(f"⚠️ Please fill out the following fields: {', '.join(missing_fields)}")
        else:
            save_to_db(first_name, last_name, address, phone_number, message)
            st.success("✅ Form submitted successfully and saved to database!")


# visualization page

import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
from style import set_black_background

set_black_background() 

# use full screen width
st.set_page_config(layout="wide")

# Step 1: go up ONE level from Analysis.py → Generalpages/
BASE_DIR = Path(__file__).resolve().parent.parent  

# Step 2: point to the Data folder
DATA_PATH = BASE_DIR / "Data" / "jijipage5_data.csv"

with st.expander("See Table below"):
    df = pd.read_csv(DATA_PATH)

    # Reset index and start from 1
    df_reset = df.head(10).reset_index(drop=True)
    df_reset.index = df_reset.index + 1

    st.table(df_reset)

charttab1, charttab2, charttab3, charttab4 = st.tabs([
    "Title by price", 
    "Median Price per Location", 
    "Average Price per Location", 
    "Outlier Detection"
])

with charttab1:
    title_price = (
        df.groupby("Title")["Price"]
        .count()
        .reset_index()
        .rename(columns={"Price": "Count"})
        .sort_values(by="Count", ascending=False)
        .head(20)  # top 20
    )

    fig1 = px.treemap(
        title_price,
        path=["Title"],
        values="Count",
        color="Count",
        color_continuous_scale="Viridis",
        title="📦 Top 20 Ads by Title"
    )

    fig1.update_layout(
        title_font=dict(size=22, family="Arial", color="white"),
        coloraxis_colorbar=dict(
            title=dict(text="Number of Ads", side="right")  # ✅ correct way
        )
    )

    st.plotly_chart(fig1, use_container_width=True)


with charttab2:
    median_price = df.groupby("Location")["Price"].median().sort_values(ascending=False).reset_index().head(10)
    fig2 = px.bar(median_price, x="Location", y="Price", title="Median Price per Location (Top 10)")
    st.plotly_chart(fig2, use_container_width=True)

with charttab3:
    avg_price = df.groupby("Location")["Price"].mean().sort_values(ascending=False).reset_index().head(10)
    fig3 = px.pie(avg_price, names="Location", values="Price", title="Average Price per Location (Top 10)")
    st.plotly_chart(fig3, use_container_width=True)

with charttab4:
    outliers = df[df["Price"] > 1_000_000]
    fig4 = px.scatter(outliers, x="Location", y="Price", color="Title", title="Outlier Detection (Price > 1M)")
    st.plotly_chart(fig4, use_container_width=True)
