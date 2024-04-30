import folium
import streamlit as st
import pandas as pd
from streamlit_folium import folium_static, st_folium

# Load the CSV file containing country names and coordinates
@st.cache_data
def load_data():
    return pd.read_csv("europe.csv")

data = load_data()

# Create a Streamlit app
st.title("European Countries Map")

# Create a Folium map centered around Europe
m = folium.Map(location=[data["Latitude"].mean(), data["Longitude"].mean()], zoom_start=4)

# Add country names as labels to the map
for _, row in data.iterrows():
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=row["Country"],
        tooltip=row["Country"],
    ).add_to(m)

# Render the Folium map using Streamlit
st_folium(m, width=800)