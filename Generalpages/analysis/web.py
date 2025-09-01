import streamlit as st
import pandas as pd

with st.expander("See explanation"):
    # df = pd.read_csv(r"C:\Users\user\Desktop\Web scrapping project\jijipage5_data.csv")
    df = pd.read_csv("././data/jijipage5_data.csv")

    st.dataframe(df.head())

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
    st.write(total_price)

with tab2:
    st.markdown("*Maximum* **Price**.")
    max_price = df["Price"].max()
    st.write(max_price)

with tab3:
    st.markdown("*Minimum* **Price**.")
    min_price = df["Price"].min()
    st.write(min_price)

with tab4:
    st.markdown("*Items above 100k*.")
    price_above_100k = df[df["Price"] > 100000]
    st.write(price_above_100k)

with tab5:
    st.markdown("*Outlier Detection (Price > 1M)*.")
    outlier_detection = df[df["Price"] > 1_000_000]
    st.write(outlier_detection)




st.subheader("Price analysis")

sectab1, sectab2, sectab3 = st.tabs(["Title by price", "Median Price per Location", "Average Price per Location"])

with sectab1:
    Title_by_price = df.groupby("Title")["Price"].count().reset_index().rename(columns={"Price": "Count"})
    st.dataframe(Title_by_price)

with sectab2:
    Median_Price_per_Location = (
        df.groupby("Location")["Price"]
        .median()
        .sort_values(ascending=False)
        .reset_index()
        .head(10)
    )
    st.dataframe(Median_Price_per_Location)

with sectab3:
    Avg_Price_per_Location = (
        df.groupby("Location")["Price"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
        .head(10)
    )
    st.dataframe(Avg_Price_per_Location)
