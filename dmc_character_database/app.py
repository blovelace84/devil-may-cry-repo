import streamlit as st
import pandas as pd
from PIL import Image
import os

# load character data
df = pd.read_csv("data/characters.csv")

st.title("Devil May Cry Character Database")

#Sidebar filters
game_filter = st.sidebar.multiselect("Filter by Game", df['Game'].unique())
weapon_filter = st.sidebar.multiselect("Filter by Weapon", df['Weapon'].unique())

#Apply filter
filtered_df = df.copy()
if game_filter:
    filter_df = filtered_df[filtered_df['Game'].isin(game_filter)]
if weapon_filter:
    filtered_df = filtered_df[filtered_df['Weapon'].isin(game_filter)]

#Display characters
for _, row in filtered_df.iterrows():
    st.subheader(row['Name'])
    st.text(f"Style: {row['Game']}")
    st.text(f"Health: {row['Style']}")
    st.text(f"Weapon: {row['Weapon']}")
    st.text(f"Abilities: {row['Abilities']}")
    st.text(f"Quote: \"{row['Quote']}\"")


    #Show image
    img_path = os.path.join("images", str(row['ImageFile']))
    if os.path.exists(img_path):
        image = Image.open(img_path)
        st.image(image, width=200)
    st.markdown("---")