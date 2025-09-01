import streamlit as st
import pandas as pd
import plotly.express as px

# use full screen width
st.set_page_config(layout="wide")  

# Load data
with st.expander("See Table below"):
    df = pd.read_csv(r"C:\Users\user\Desktop\Web scrapping project\jijipage5_data.csv")
    
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
