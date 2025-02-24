
---

# **HIV/AIDS Risk Prediction Using Machine Learning**  

## **Deskripsi Proyek**  
Proyek ini berfokus pada **prediksi risiko HIV/AIDS** menggunakan algoritma Machine Learning untuk membantu tenaga medis dalam mendeteksi individu dengan risiko tinggi. Model ini dikembangkan dengan menggunakan **dataset pasien HIV/AIDS**, melalui tahapan eksplorasi data, preprocessing, rekayasa fitur, dan pemodelan untuk menghasilkan prediksi yang akurat.  

## **Struktur Folder**  
- `Modelling.ipynb` → Notebook utama yang berisi seluruh proses analisis dan pemodelan.  
- `Model Inference.ipynb` → Notebook untuk melakukan prediksi menggunakan model yang telah dilatih.  
- `data_aids.csv` → Dataset yang digunakan dalam proyek.  
- `model_svc.pkl` → Model yang telah dilatih untuk prediksi risiko HIV/AIDS.  
- `deployments/` → Folder deployment menggunakan Hugging Face.  

## **Dataset**  
- **Sumber**: Kaggle  
- **Ukuran**: 30.000 sampel  
- **Fitur Utama**:  
  - **Numerik**: "time", "age", "wtkg", "karnof", "preanti", "cd40", "cd420", "cd80", "cd820"  
  - **Kategorikal**: "trt", "hemo", "homo", "drugs", "oprior", "z30", "race", "gender", "str2", "strat", "symptom", "treat", "offtrt"  
  - **Target**: "infected" (indikasi apakah pasien terinfeksi atau tidak)  

## **Teknologi yang Digunakan**  
- **Pemrograman**: Python  
- **Analisis Data**: Pandas, NumPy  
- **Machine Learning**: Scikit-learn, XGBoost, Random Forest, SVM  
- **Visualisasi**: Matplotlib, Seaborn  
- **Notebook**: Jupyter Notebook  

## **Alur Pemodelan**  
1. **Eksplorasi Data** → Analisis statistik awal, melihat distribusi data, dan menangani nilai yang hilang.  
2. **Preprocessing** → Normalisasi fitur numerik, encoding fitur kategorikal, serta penanganan data imbalance.  
3. **Feature Engineering** → Seleksi fitur, pembuatan fitur tambahan, dan reduksi dimensi jika diperlukan.  
4. **Pemilihan Model** → Mencoba berbagai algoritma ML seperti **KNN, Decision Tree, Random Forest, dan XGBoost**.  
5. **Evaluasi Model** → Menggunakan metrik **akurasi, precision, recall, F1-score, dan AUC-ROC** untuk menilai performa model.  
6. **Tuning Hyperparameter** → Mengoptimalkan model dengan **Grid Search atau Random Search**.  

## **Hasil dan Evaluasi**  
- **Model terbaik**: Support Vector Classifier (SVC)  
- **Akurasi**: 74%  
- **Fokus utama**: Recall (mengurangi false negatives), Precision, dan F1-score  

## **Kesimpulan**  
- **Model Machine Learning dapat membantu deteksi dini HIV/AIDS** dengan tingkat akurasi yang cukup baik, sehingga memungkinkan intervensi medis lebih cepat.  
- **Recall lebih diutamakan daripada akurasi keseluruhan**, karena kesalahan dalam mendeteksi pasien berisiko dapat berdampak fatal.  
- **Feature engineering memainkan peran penting** dalam meningkatkan performa model, terutama dalam menangani ketidakseimbangan data.  

## **Saran untuk Pengembangan Selanjutnya**  
- **Meningkatkan akurasi dengan lebih banyak data** → Menggunakan dataset tambahan dari rumah sakit atau organisasi kesehatan.  
- **Menggunakan teknik ensemble learning** → Menggabungkan beberapa model untuk meningkatkan performa prediksi.  
- **Mengintegrasikan model dengan sistem kesehatan** → Mengembangkan aplikasi berbasis web untuk memudahkan tenaga medis dalam menggunakan prediksi model.  

## **Dampak Bisnis**  
- **Meningkatkan efisiensi layanan kesehatan** → Tenaga medis dapat lebih fokus pada pasien dengan risiko tinggi berdasarkan prediksi model.  
- **Mengoptimalkan distribusi sumber daya medis** → Model ini dapat membantu organisasi kesehatan dalam merancang strategi pencegahan berbasis data.  
- **Mempercepat intervensi dini** → Deteksi awal memungkinkan pengobatan lebih cepat, yang dapat mengurangi tingkat infeksi dan meningkatkan harapan hidup pasien.  

## **Cara Menjalankan Proyek**  
1. Clone repositori ini:  
   ```bash
   git clone https://github.com/username/proyek-prediksi-hiv.git
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

## **Catatan Tambahan**  
- Jika dataset tidak tersedia di repositori, silakan unduh dari sumber yang disebutkan.  
- Model dapat dikembangkan lebih lanjut dengan teknik **ensemble learning atau deep learning**.  
- Proyek ini juga tersedia di Hugging Face: [Hugging Face Deployment](https://huggingface.co/spaces/yinkasinulingga/deployments).  

## **Kontak**  
Jika ada pertanyaan atau saran terkait proyek ini, silakan hubungi:  
📧 **Email**: yinkasinulingga@gmail.com  

---
