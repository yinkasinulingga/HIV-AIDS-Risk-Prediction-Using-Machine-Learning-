# PAGE AWAL

import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import plotly.express as px



# Untuk menjalankan terminal streamlit >> streamlit run (nama_script)

def run():
    st.write('')
    st.write('')
    st.markdown("""
        <h1 style='text-align: center;  margin-bottom: 20px;'>Exploratory Data Analysis</h1>
    """, unsafe_allow_html=True)
    
    # Load Data
    st.write('## Dataset')
    df = pd.read_csv('data_aids_new.csv')

    # data
    st.dataframe(df, hide_index=True)

    # Define kolom numerical untuk kebutuhan eda
    st.write('')

    st.write('## Visualization')
    st.markdown('<h3 style="text-align: center;">Percentage of Distribution Data</h3>', unsafe_allow_html=True)
    # Daftar kolom kategorikal
    cat_columns = ["trt", "hemo", "homo", "drugs", "oprior", "z30", "race", "gender", "str2", "strat", "symptom", "treat", "offtrt"]

    # Membuat selectbox untuk memilih kolom
    selected_column = st.selectbox("Pilih kolom :", cat_columns)
    # Membuat pie chart menggunakan Plotly Express untuk kolom yang dipilih
    fig = px.pie(df, names=selected_column, title=f"Distribution of {selected_column}")
    st.plotly_chart(fig)

    st.markdown('<h3 style="text-align: center;">Distribution Data and Detection Outliers (Numerical)</h3>', unsafe_allow_html=True)
    # Daftar kolom numerik
    num_columns = ["time", "age", "wtkg", "karnof", "preanti", "cd40", "cd420", "cd80", "cd820"]
    # Pilih kolom untuk histogram
    st.write('')
    selected_column = st.selectbox("Pilih Kolom untuk Histogram :", num_columns)
    # Membuat histogram untuk kolom yang dipilih
    fig = px.histogram(df, x=selected_column, nbins=30)
    fig.update_layout(
        height=400, 
        width=600,
        title_text=f"Distribution of {selected_column}",
        yaxis_title="Frequency"  # Memperbaiki typo pada 'Frequecny' menjadi 'Frequency'
    )
    # Menampilkan plot histogram di Streamlit
    st.plotly_chart(fig)

    # Membuat selectbox untuk memilih kolom kedua untuk boxplot
    selected_column_2 = st.selectbox("Pilih Kolom untuk Boxplot Outliers :", num_columns)

    # Membuat boxplot untuk dua kolom numerik yang dipilih
    fig_box = px.box(df, y=selected_column_2)
    fig_box.update_layout(
        height=400, 
        width=600,
        title_text=f"Outliers Boxplot of {selected_column_2}"
    )
    # Menampilkan plot boxplot di Streamlit
    st.plotly_chart(fig_box)

    # Judul aplikasi Streamlit
    st.write('')
    st.markdown('<h3 style="text-align: center;">Scatter Plots for Numerical Columns</h3>', unsafe_allow_html=True)

    # Selectbox untuk memilih kolom pertama dan kolom kedua
    x_feature = st.selectbox(
        "Choose a feature for X-axis:",
        options=num_columns
    )

    y_feature = st.selectbox(
        "Choose a feature for Y-axis:",
        options=num_columns
    )

    # Membuat scatter plot menggunakan Plotly Express
    fig = px.scatter(
        df,
        x=x_feature,
        y=y_feature,
        title=f"Scatter Plot: {x_feature} vs {y_feature}",
        labels={x_feature: x_feature, y_feature: y_feature},
        template="plotly_white"
    )

    # Tampilkan scatter plot di Streamlit
    st.plotly_chart(fig)



# Jika tidak ingin langsung run
# if __name__ == "__main__":
# run()