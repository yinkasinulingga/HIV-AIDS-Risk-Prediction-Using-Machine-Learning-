import streamlit as st
import pandas as pd
import numpy as np
import pickle
#load model

with open('model_svc.pkl', 'rb') as file:
    model = pickle.load(file)
# judul


# buat form untuk input data 
def run():
        
    with st.form("my_form"):
        st.write("## Data Form of Patient")

        time = st.number_input(label = "Time", 
                            help="Waktu yang dibutuhkan hingga pasien mengalami kegagalan atau berhenti dalam pengobatan", 
                            placeholder = 'Ex : 1',                   
                            min_value= 1, max_value=5000,
                            step=1, value=863) # value diisi berdasarkan rata-rata dari fitur
        
        trt = st.selectbox(
        label="Type of Treatment", 
        options=[0, 1, 2, 3], 
        format_func=lambda x: {
            0: "Zidovudine",
            1: "Zidovudine & Didanosine",
            2: "Zidovudine & Zalcitabine",
            3: "Didanosine"
        }.get(x, "Unknown"),
        help="Pilih jenis pengobatan yang diberikan berdasarkan kombinasi obat:")
        

        age = st.number_input(label = "Age", 
                            help="Usia saat Memulai Pengobatan", 
                            placeholder = 'Ex : 1',                   
                            min_value= 1, max_value=150,
                            step=1, value=34) # value diisi berdasarkan rata-rata dari fitur
        
        wtkg = st.number_input(label = "Body Weight(Kg)", 
                            help="Berat Badan saat Memulai Pengobatan", 
                            placeholder = 'Ex : 75',                   
                            min_value= 1, max_value=300,
                            step=1, value=75) # value diisi berdasarkan rata-rata dari fitur
        
        hemo = st.selectbox(
        label="Hemofilia", 
        options=[0, 1], 
        format_func=lambda x: {
            0: "No",
            1: "Yes",
        }.get(x, "Unknown"),
        help="Apakah pasien memiliki riwayat hemofilia ?")
        
        drugs = st.selectbox(
        label="Drugs", 
        options=[0, 1], 
        format_func=lambda x: {
            0: "No",
            1: "Yes",
        }.get(x, "Unknown"),
        help="Apakah pasien memiliki riwayat penggunaan narkoba suntik ?")
        
        karnof = st.number_input(label = "Skor of Karnofsky", 
                            help="Masukkan skor Karnofsky (tingkat kemampuan pasien dalam melakukan aktivitas sehari-hari)", 
                            placeholder = 'Ex : (1-100)',                   
                            min_value= 1, max_value=100,
                            step=1, value=96) # value diisi berdasarkan rata-rata dari fitur
        
        oprior = st.selectbox(
        label="Aprior", 
        options=[0, 1], 
        format_func=lambda x: {
            0: "No",
            1: "Yes",
        }.get(x, "Unknown"),
        help="Apakah pasien telah menerima pengobatan antiretroviral non-ZDV sebelum terapi 175?")
        
        z30 = st.selectbox(
        label="z30", 
        options=[0, 1], 
        format_func=lambda x: {
            0: "No",
            1: "Yes",
        }.get(x, "Unknown"),
        help="Apakah pasien mengonsumsi ZDV dalam 30 hari sebelum terapi 175?")
        
        preanti = st.number_input(label = "Preanti", 
                            help="Jumlah hari pasien mengonsumsi terapi antiretroviral sebelum terapi 175", 
                            placeholder = 'Ex : (1-5000)',                   
                            min_value= 1, max_value=5000,
                            step=1, value=350) # value diisi berdasarkan rata-rata dari fitur
        
        race = st.selectbox(
        label="Race", 
        options=[0, 1], 
        format_func=lambda x: {
            0: "White",
            1: "Not White",
        }.get(x, "Unknown"),
        help="Ras Pasien?")
    
        gender = st.selectbox(
        label="Gender", 
        options=[0, 1], 
        format_func=lambda x: {
            0: "Female",
            1: "Male",
        }.get(x, "Unknown"),
        help="Jenis kelamin pasien?")

        str2 = st.selectbox(
        label="Str2", 
        options=[0, 1], 
        format_func=lambda x: {
            0: "Never",
            1: "Ever",
        }.get(x, "Unknown"),
        help="Riwayat penggunaan terapi antiretroviral sebelumnya")
        
        strat = st.selectbox(
        label="Strat", 
        options=[ 1, 2, 3], 
        format_func=lambda x: {
            1: "Never",
            2: "More than 1 but less than 52 weeks",
            3: "More than 52 weeks",
        }.get(x, "Unknown"),
        help="Kategori berdasarkan pengalaman sebelumnya dengan terapi antiretroviral")
    
        symptom = st.selectbox(
        label="Symptom", 
        options=[0, 1], 
        format_func=lambda x: {
            0: "No",
            1: "Yes",
        }.get(x, "Unknown"),
        help="Apakah pasien menunjukkan gejala penyakit ?")
    
        treat= st.selectbox(
        label="Treatment", 
        options=[0, 1], 
        format_func=lambda x: {
            0: "Only Zidovudine",
            1: "Other",
        }.get(x, "Unknown"),
        help="Jenis pengobatan yang diberikan")
    
        offtrt = st.selectbox(
        label="Off Treatment", 
        options=[0, 1], 
        format_func=lambda x: {
            0: "No",
            1: "Yes",
        }.get(x, "Unknown"),
        help="Apakah seseorang berhenti pengobatan sebelum 96 minggu?")
    
        cd40 = st.number_input(label = "CD4 (immune cells)", 
                            help="Jumlah CD4 (sel kekebalan tubuh) pada awal pengobatan", 
                            placeholder = 'Ex : (1-5000)',                   
                            min_value= 1, max_value=5000,
                            step=1, value=313) # value diisi berdasarkan rata-rata dari fitur
        
        cd420 = st.number_input(label = "CD420 (immune cells)", 
                            help="Jumlah CD4 (sel kekebalan tubuh) setelah 20 minggu pengobatan", 
                            placeholder = 'Ex : (1-5000)',                   
                            min_value= 1, max_value=5000,
                            step=1, value=427) # value diisi berdasarkan rata-rata dari fitur
        
        cd820 = st.number_input(label = "CD820 (immune cells)", 
                            help="Jumlah CD8 (sel kekebalan tubuh) setelah 20 minggu pengobatan", 
                            placeholder = 'Ex : (1-5000)',                   
                            min_value= 1, max_value=5000,
                            step=1, value=902) # value diisi berdasarkan rata-rata dari fitur
        
        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")


    # DataFrame
    dict = {
    'time': time,
    'trt': trt,
    'age': age, 
    'wtkg': wtkg,
    'hemo': hemo,
    'drugs': drugs,
    'karnof': karnof,
    'oprior': oprior,
    'z30': z30,
    'preanti': preanti,
    'race': race,
    'gender': gender,
    'str2': str2,
    'strat': strat,
    'symptom': symptom,
    'treat': treat,
    'offtrt': offtrt,
    'cd40': cd40,
    'cd420': cd420,
    'cd820': cd820
    }


    st.write('# Dataset')
    df = pd.DataFrame([dict])
    st.dataframe(df, hide_index=True)


    # Model Prediksi
    result = model.predict(df)

    # Menentukan label berdasarkan prediksi
    result_label = "Infected" if result[0] == 1 else "Not Infected"

    # Menampilkan hasil prediksi
    with st.container():
        st.write("----------------------------------------------------")
        st.markdown(f"## Hasil Prediksi : {result_label}")
        st.write("----------------------------------------------------")


# Jika tidak ingin langsung run
if __name__ == "__main__":
    run()