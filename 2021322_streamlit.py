import pandas as pd
import streamlit as st
from joblib import load
import altair as alt
import plotly.express as px
import numpy as np
from streamlit_option_menu import option_menu

import warnings
warnings.filterwarnings("ignore") 

scadata = pd.read_csv('scadata.csv')
cleaned_data = pd.read_csv('cleaned_data.csv')

data_dictionary = {
    'scadata': {
        'Column A': 'Description for Column A',
        'Column B': 'Description for Column B',
        'Column C': 'Description for Column C'
    },
    'cleaned_data': {
        'Feature 1': 'Description for Feature 1',
        'Feature 2': 'Description for Feature 2',
        'Feature 3': 'Description for Feature 3'
    }
}

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Dataset Information", "Data Visualisation", "Training Results", "Models"],
        icons=["house", "info-circle", "image", "clipboard", "gear"],
        menu_icon="cast",
        default_index=0,
    )
    
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;500;700&display=swap');
    
    .info-box {
        padding: 10px; 
        margin-top: 30px;
        margin-bottom: 20px; 
        border-radius: 5px;
        text-align: left;
        color: #ffffff;
        width: 100%; 
        margin-left: auto;
        margin-right: auto;
        font-family: 'Quicksand', sans-serif; 
    }
    .name {
        font-size: 18px; 
        font-weight: bold;
    }
    .institution {
        font-size: 14px;
        font-style: italic;
    }
    .link {
        font-size: 12px;
        color: #1f77b4;
        text-decoration: none;
    }
    .link:hover {
        text-decoration: underline;
    }
    </style>
    <div class="info-box">
        <p class="name">Luciana Teixeira</p>
        <p class="institution">MSc Data Analytics | 2021322</p>
        <p><a href="https://github.com/LucianaTeixeira322" class="link">GitHub</a> | <a href="https://www.cct.ie/" class="link"> CCT College</a></p>
    </div>
    """, unsafe_allow_html=True)

if selected == "Home":
    st.header('Harnessing the power of data: Enhancing e-commerce transaction security through analytics')
    st.write("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        ### Abstract
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

        ### Objectives
        - **1**: Learn about the dataset used in this application.
        - **2**: Explore various visualizations to understand the data better.
        - **3**: View results from machine learning models trained on the dataset.

    """)

elif selected == "Dataset Information":
    st.subheader(f"**You Have selected {selected}**")

    # Dropdown menu 
    dataset_option = st.selectbox(
        "Select a dataset:",
        options=["Original Dataset", "Feature Engineered Dataset"]
    )
    
    if dataset_option == "Original Dataset":
        data = scadata
        data_key = 'scadata'
    else:
        data = cleaned_data
        data_key = 'cleaned_data'

    show_data_dict = st.checkbox("Data Dictionary")
    show_describe = st.checkbox("Describe")
    show_data_types = st.checkbox("Data Types")
    show_missing_values = st.checkbox("Missing Values")
    show_correlation = st.checkbox("Correlation")
    
    if show_data_dict:
        st.subheader("Data Dictionary")
        dictionary = data_dictionary.get(data_key, {})
        for col, desc in dictionary.items():
            st.write(f"**{col}:** {desc}")
    
    if show_describe:
        st.subheader("Describe")
        st.write(data.describe())
    
    if show_data_types:
        st.subheader("Data Types")
        st.write(data.dtypes)
    
    if show_missing_values:
        st.subheader("Missing Values")
        st.write(data.isna().sum())
    
    if show_correlation:
        st.subheader("Correlation")
        st.write(data.corr())

elif selected == "Data Visualisation":
    st.subheader(f"**You Have selected {selected}**")

elif selected == "Training Results":
    st.subheader(f"**You Have selected {selected}**")

elif selected == "Models":
    st.subheader(f"**You Have selected {selected}**")
