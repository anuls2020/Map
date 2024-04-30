import folium
import streamlit as st
import pandas as pd
from streamlit_folium import folium_static, st_folium


# Load csv file containing country names and co-ordinates
@st.cache_data
def load_data():
    return pd.read_csv("countries.csv")

# def load_data():
#     return pd.read_csv("europe.csv")

data = load_data()

# Create streamlit app
st.title("World Country Map")

# Create a folium map
m = folium.Map(location=[data["Latitude"].mean(), data["Longitude"].mean()], zoom_start=4)

# Add country names as labels to the map
for _, row in data.iterrows():
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup = row["Country"],
        tooltip = row["Country"],
    ).add_to(m)

# Render the folium map using streamlit application
st_folium(m, width=800)
