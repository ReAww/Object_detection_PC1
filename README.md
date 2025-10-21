| Komponen       | Teknologi                                      | Keterangan                                |
| -------------- | ---------------------------------------------- | ----------------------------------------- |
| Bahasa         | **Python 3.10+**                               | Bahasa yang didukung YOLO                 |
| Model Deteksi  | **YOLOv8 (Ultralytics)**                       | Model terbaru, mudah dipakai              |
| Library Kamera | **OpenCV**                                     | Untuk akses webcam dan tampilan video     |
| Framework AI   | **PyTorch** (otomatis diinstal bersama YOLOv8) | Backend dari YOLO                         |
| Virtual Env    | **venv**                                       | Agar dependensi bersih                    |
| Visualisasi    | **cv2.imshow()**                               | Menampilkan hasil deteksi secara langsung |


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
