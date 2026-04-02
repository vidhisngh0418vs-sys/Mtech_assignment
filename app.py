# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title="Fuel Price Dashboard", layout="wide")

st.title("🌍 Fuel Price Intelligence Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("fuel_prices.csv")
    df['price_date'] = pd.to_datetime(df['price_date'])
    return df

df = load_data()

# ---------------- KPI Section ----------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Avg Petrol Price", round(df['gasoline_usd_per_liter'].mean(), 2))
col2.metric("Avg Diesel Price", round(df['diesel_usd_per_liter'].mean(), 2))
col3.metric("Avg Affordability", round(df['fuel_affordability_index'].mean(), 2))

# ---------------- Trend Chart ----------------
st.subheader("📈 Fuel Price Trend")

fig, ax = plt.subplots()
sns.lineplot(data=df, x='price_date', y='gasoline_usd_per_liter', ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# ---------------- Region Comparison ----------------
st.subheader("🌎 Region-wise Comparison")

region_avg = df.groupby('sub_region')['gasoline_usd_per_liter'].mean().sort_values()

fig2, ax2 = plt.subplots()
region_avg.plot(kind='barh', ax=ax2)
st.pyplot(fig2)

# ---------------- EV vs Price ----------------
st.subheader("⚡ EV Adoption vs Fuel Price")

fig3, ax3 = plt.subplots()
sns.scatterplot(
    data=df,
    x='gasoline_usd_per_liter',
    y='ev_adoption_pct',
    ax=ax3
)
st.pyplot(fig3)

# ---------------- Logs Section ----------------
st.subheader("📝 Pipeline Logs")

log_file = "pipeline.log"

if os.path.exists(log_file):
    with open(log_file, "r") as f:
        logs = f.read()
    st.text_area("Logs", logs, height=300)
else:
    st.warning("No logs found. Run pipeline first.")
