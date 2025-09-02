import streamlit as st
import pandas as pd
import plotly.express as px  
from pathlib import Path


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




# with col2:
#     st.subheader("Chart analysis")
#     charttab1, charttab2, charttab3 = st.tabs(["Gender by Birth", "Day by Birth", "Month by Birth"])
    
#     with charttab1:
        
#         fig_gender_births = px.plot(
#             df.groupby("gender")["births"].sum(),
#             kind="bar",
#             x='births',
#             # y='Total births',
#             title='Total births by Gender',
#             # color='Gender'
#         )
#         st.plotly_chart(fig_gender_births, use_container_width=True)

#     with charttab2:

#         fig_day_births = px.plot(
#             daybybirth_drop99 ,
#             kind="bar",
#             x="births",
#             title = "Total births by day"

#         )
#         st.plotly_chart(fig_day_births, use_container_width=True)

#     with charttab3:

#         fig_month_births = px.plot(
#             monthbybirth ,
#             kind="bar",
#             x="births",
#             title = "Total births by Month"

#         )
#         st.plotly_chart(fig_month_births, use_container_width=True)