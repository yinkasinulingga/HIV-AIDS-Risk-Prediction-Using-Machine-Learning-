import streamlit as st
import pandas as pd
import numpy as np

def run():     
    st.markdown("""
        <h1 style='text-align: center;  margin-bottom: 20px;'>HIV & AIDS Virus Prediction</h1>
    """, unsafe_allow_html=True)

    st.image('https://spiritia.or.id/cdn/images/artikel/file_5c4582e6840a7.png')

    st.write('___')
    st.markdown('''
    # About 
    Welcome to the HIV & AIDS Virus Prediction application. This tool leverages advanced machine learning algorithms to predict the likelihood of HIV or AIDS 
    in individuals based on a variety of health and demographic data. Our goal is to provide an early detection system that can help healthcare professionals 
    and individuals take preventive measures in a timely manner''')

    st.markdown('''
    # Background of the Problem
    HIV/AIDS masih menjadi masalah kesehatan global yang serius, termasuk di Indonesia. 
    Menurut https://www.cnnindonesia.com/gaya-hidup/20241203114247-255-1173200/11-provinsi-ini-jadi-penyumbang-terbesar-kasus-hiv-di-indonesia ada Januari- September 2024, tercatat 35.415 kasus HIV dan 12.481 kasus AIDS, dengan DKI Jakarta 
    dan provinsi lainnya di Pulau Jawa sebagai penyumbang terbesar. Sebanyak 71% kasus terjadi pada pria, 
    dengan kelompok usia 20-49 tahun yang paling terdampak. Tingginya angka ini mempengaruhi kesehatan, ekonomi,
    dan kehidupan masyarakat. Oleh karena itu, sistem prediksi risiko infeksi HIV/AIDS berbasis machine learning 
    diperlukan untuk menganalisis faktor-faktor seperti usia, jenis kelamin, dan gaya hidup. Proyek ini bertujuan 
    membantu masyarakat mendeteksi risiko lebih dini dan mendukung tenaga medis dalam mengidentifikasi pasien berisiko tinggi.
                ''')

  