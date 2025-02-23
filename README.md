
---

# README: Proyek Pemodelan Data

## Deskripsi Proyek  
Proyek ini berfokus pada pemodelan data untuk [sebutkan tujuan spesifik proyek, misalnya prediksi penyakit, segmentasi pelanggan, atau klasifikasi teks]. Menggunakan dataset yang tersedia, proyek ini mencakup berbagai tahapan, mulai dari eksplorasi data, pembersihan, rekayasa fitur, hingga penerapan algoritma pembelajaran mesin untuk mendapatkan model dengan performa optimal.

## Struktur Folder  
- `Modelling.ipynb` : Notebook utama yang berisi seluruh proses analisis dan pemodelan.  
- `Model Inference.ipynb` : Notebook untuk melakukan prediksi menggunakan model yang telah dilatih.  
- `data_aids.csv` : File dataset yang digunakan dalam proyek.  
- `model_svc.pkl` : File untuk menyimpan model yang telah dilatih.  
- `deployments/` : Folder deployment menggunakan hugging face.  
 

## Dataset  
- **Sumber**: Kaggle  
- **Ukuran**: 30.000 sampel 
- **Fitur Utama**:  
  - **Numerik**: "time", "age", "wtkg", "karnof", "preanti", "cd40", "cd420", "cd80", "cd820"
  - **Kategorikal**: "trt", "hemo", "homo", "drugs", "oprior", "z30", "race", "gender", "str2", "strat", "symptom", "treat", "offtrt" 
  - **Target**: "infected" 

## Teknologi yang Digunakan  
- Python  
- Pandas, NumPy  
- Scikit-learn  
- XGBoost, Random Forest, SVM  
- Matplotlib, Seaborn  
- Jupyter Notebook  

## Alur Pemodelan  
1. **Eksplorasi Data**: Melihat distribusi data, menangani nilai yang hilang, dan melakukan analisis statistik.  
2. **Preprocessing**: Normalisasi fitur numerik, encoding fitur kategorikal, dan penanganan data imbalance.  
3. **Feature Engineering**: Seleksi fitur, rekayasa fitur tambahan, dan reduksi dimensi jika diperlukan.  
4. **Pemilihan Model**: Menggunakan berbagai algoritma ML seperti KNN, Decision Tree, Random Forest, dan XGBoost.  
5. **Evaluasi**: Menggunakan metrik seperti akurasi, precision, recall, F1-score, dan AUC-ROC.  
6. **Tuning Hyperparameter**: Mengoptimalkan model dengan Grid Search atau Random Search.  

## Hasil dan Evaluasi  
- **Model terbaik**: Support Vector Classifier  
- **Akurasi**: 74%  
- **Metrik lainnya**: Fokus Recall (False Negatuves), Precision, F1-score.  

## Cara Menjalankan Proyek  
1. Clone repositori ini:  
   ```bash
   git clone https://github.com/username/proyek-pemodelan.git
   ```  
2. Install dependensi yang diperlukan:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Jalankan Jupyter Notebook:  
   ```bash
   jupyter notebook
   ```  
4. Buka `Modelling.ipynb` dan jalankan sel sesuai urutan.  

## Catatan Tambahan  
- Jika dataset tidak tersedia di repositori, silakan unduh dari sumber yang disebutkan.  
- Model dapat dikembangkan lebih lanjut dengan teknik ensemble atau deep learning.  
- Proyek ini juga tersedia di Hugging Face: [Hugging Face Deployment](https://huggingface.co/spaces/yinkasinulingga/deployments).  

## Kontak  
Jika ada pertanyaan atau saran terkait proyek ini, silakan hubungi **Saya** di Email : yinkasinulingga@gmail.com  

---
