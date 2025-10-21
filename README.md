# Buat folder proyek
mkdir yolo-realtime-detector
cd yolo-realtime-detector

# Buat virtual environment
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)

# Instal library yang dibutuhkan
pip install ultralytics opencv-python

# STRUCTURE FOLDER
yolo-realtime-detector/
│
├── venv/                     # virtual environment
├── models/                   # tempat model YOLO
│   └── yolov8n.pt            # model YOLO versi ringan
│
├── src/                      # folder utama source code
│   ├── main.py               # file utama untuk menjalankan deteksi
│   ├── detector.py           # logika deteksi (pemisahan agar rapi)
│   └── utils.py              # fungsi tambahan (optional)
│
├── requirements.txt          # daftar dependensi
└── README.md                 # panduan singkat proyek

# REQUIREMENTS 
ultralytics
opencv-python
