# fastapi-randomforest-predictor

API sederhana menggunakan FastAPI dan **Random Forest Classifier** untuk prediksi keputusan membeli berdasarkan usia dan pendapatan.

# 📦 Prediksi Keputusan Membeli dengan FastAPI + Random Forest

Proyek ini merupakan implementasi sederhana dari **Random Forest Classifier** menggunakan `scikit-learn`, dan disajikan sebagai **REST API dengan FastAPI**.

## 🚀 Fitur

- [✓] Dataset sintetik (usia & pendapatan)
- [✓] Training model Random Forest
- [✓] Simpan model ke file `.pkl`
- [✓] Endpoint API untuk prediksi

## 📁 Struktur Proyek

```
.
├── app.py              # FastAPI server (endpoint /predict)
├── main.py             # Training model dan save ke pickle
├── requirements.txt    # Daftar dependency Python
├── .gitignore          # File/folder yang diabaikan Git
└── models/
    └── random_forest_model.pkl  # File model hasil training
```

## ⚙️ Instalasi

```bash
# 1. Clone repository ini
git clone https://github.com/username/fastapi-random-forest-api.git
cd fastapi-random-forest-api

# 2. Install dependensi
pip install -r requirements.txt

# 3. Jalankan training untuk membuat model
python main.py

# 4. Jalankan server API
uvicorn app:app --reload
```

## 📬 API Endpoint

### POST `/predict`

#### Request Body
```json
{
  "usia": 40,
  "pendapatan": 6000
}
```

#### Response
```json
{
  "prediction": 1
}
```

## 🧠 Teknologi yang Digunakan

- Python 3.x
- scikit-learn
- FastAPI
- Pickle
- Matplotlib
- NumPy & Pandas

## 📌 Lisensi

Proyek ini dilisensikan di bawah lisensi MIT — bebas digunakan, dimodifikasi, dan dibagikan.

---

Created with ❤️ by arielshakaramiro
