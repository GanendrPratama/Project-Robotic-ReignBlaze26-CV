Jadwal Proyek: Vision & Object Detection (Modul 3)

Platform: Raspberry Pi 4 (dan PC/Server untuk Training jika perlu)
Tools/Tech: Roboflow / YOLO, ROS (Robot Operating System), OpenCV, Intel RealSense SDK
Tim Terlibat: Ganen, Owen, Thoriq
Fokus Utama: Membuat sistem deteksi objek menggunakan kamera, menggabungkan deteksi visual dengan jarak, pengolahan data 3D (opsional D435), serta integrasi navigasi.

📌 Alokasi Tugas & Penanggung Jawab (PIC)

Tugas dibagi menjadi 4 kategori utama sesuai dengan requirement proyek.

3.1 Model Machine Learning untuk Object Detection

No

Detail Tugas

PIC Utama

Status

1

Menentukan jenis objek target & Mengumpulkan dataset gambar.

Semua

[ ] To Do

2

Melakukan labeling gambar menggunakan bounding box.

Semua

[ ] To Do

3

Menentukan model (YOLO / ringan) & Melakukan training/fine-tuning.

Owen

[ ] To Do

4

Menguji model (gambar statis & video real-time) serta mengukur confidence score.

Owen

[ ] To Do

5

Mengoptimalkan model agar berjalan cepat di perangkat (Raspi 4).

Owen

[ ] To Do

3.2 Deteksi Objek Berbasis Image dan Jarak

No

Detail Tugas

PIC Utama

Status

1

Mengambil posisi bounding box & Menghubungkannya dengan data jarak (Sensor Fusion).

Thoriq

[ ] To Do

2

Menentukan logika jarak: Depth camera (area bbox) ATAU sensor tambahan (Lidar/Ultrasonic).

Ganen

[ ] To Do

3

Menampilkan UI: Nama objek, confidence score, dan estimasi jarak.

Owen

[ ] To Do

4

Membuat ROS topic (Publisher) untuk mengirim hasil deteksi & jarak objek.

Ganen

[ ] To Do

5

Memastikan hasil deteksi siap digunakan oleh tim navigasi/mapping.

Thoriq

[ ] To Do

3.3 Processing Data 3D dari RealSense D435 (Jika Tersedia)

No

Detail Tugas

PIC Utama

Status

1

Menghubungkan RealSense D435, instalasi, dan uji driver di sistem.

Ganen

[ ] To Do

2

Mengambil data RGB, Depth, dan Point Cloud dari kamera.

Ganen

[ ] To Do

3

Menampilkan Point Cloud di RViz & mengolah posisi objek 3D.

Thoriq

[ ] To Do

4

Menguji kualitas depth pada berbagai jarak & identifikasi noise / masalah pencahayaan.

Semua

[ ] To Do

3.4 Bantuan untuk Navigasi dan Path Planning

No

Detail Tugas

PIC Utama

Status

1

Membaca data sensor untuk obstacle detection (kamera/lidar).

Thoriq

[ ] To Do

2

Mengintegrasikan hasil vision ke sistem ROS tim mapping / navigasi.

Thoriq

[ ] To Do

3

Menyesuaikan format data vision menjadi input untuk path planning.

Owen

[ ] To Do

4

Menguji langsung apakah data vision berhasil membantu robot menghindari obstacle.

Semua

[ ] To Do

📅 Timeline Proyek (Estimasi 7 Minggu)

Minggu 1: Persiapan Dataset & Hardware Dasar

Fokus: Akuisisi data awal dan setup lingkungan kerja.

[ ] [Semua] Diskusi penentuan objek target, kumpulkan gambar dataset, dan mulai proses labeling di Roboflow/tools lain.

[ ] [Ganen] Setup OS di Raspberry Pi 4, Install ROS, dan siapkan driver sensor (termasuk RealSense SDK jika D435 tersedia).

[ ] [Owen] Eksplorasi arsitektur model (YOLOv8 nano, TensorFlow Lite) yang kompatibel dengan resource Raspi 4.

Minggu 2: Training Model & Ekstraksi Data Sensor

Fokus: Melatih AI dan memunculkan data raw dari sensor.

[ ] [Owen] Selesaikan training model ML. Ekspor model ke format ringan (TFLite/ONNX).

[ ] [Owen] Buat script Python (OpenCV) untuk menjalankan inference deteksi di kamera secara real-time.

[ ] [Ganen] Tulis script untuk mengambil data RGB, Depth, dan (jika D435) Point Cloud dari sensor/kamera.

Minggu 3: Point Cloud, RViz & Pengujian Model

Fokus: Evaluasi hasil deteksi dan pemrosesan data spasial (3D).

[ ] [Owen] Uji coba performa model ML di Raspi 4. Cek Frame Rate (FPS) dan lakukan optimasi jika terjadi bottleneck.

[ ] [Thoriq] Tampilkan data Point Cloud dari RealSense ke dalam software RViz.

[ ] [Thoriq] Olah data depth dasar untuk mulai memetakan koordinat ruang 3D.

Minggu 4: Sensor Fusion (Image + Jarak)

Fokus: Menggabungkan kotak deteksi (Bounding Box) dengan nilai jarak meter.

[ ] [Thoriq & Ganen] Buat algoritma untuk memotong (crop) atau mengambil nilai rata-rata depth/point cloud yang berada di dalam area bounding box objek.

[ ] [Ganen] Jika RealSense tidak ada, sinkronisasikan angle Lidar/Ultrasonic dengan center kamera.

[ ] [Owen] Update UI visualisasi agar memunculkan [Nama Kelas] | [Score %] | [Jarak: X meter].

Minggu 5: Pembuatan ROS Node & Integrasi Navigasi Awal

Fokus: Membungkus sistem menjadi node yang bisa berkomunikasi dengan tim lain.

[ ] [Ganen] Buat custom ROS Message dan siapkan ROS Publisher untuk hasil deteksi objek beserta estimasi jarak.

[ ] [Thoriq] Olah format data vision agar sesuai dengan standar input yang dibutuhkan oleh algoritma Path Planning atau tim Mapping.

[ ] [Thoriq] Mulai broadcasting data halangan (obstacle detection) ke sistem ROS.

Minggu 6: Pengujian Lapangan & Identifikasi Kendala (Noise/Cahaya)

Fokus: Pengujian di dunia nyata.

[ ] [Semua] Uji coba lapangan menyeluruh. Cek deteksi pada berbagai jarak tempuh (1m, 2m, dst).

[ ] [Semua] Identifikasi dan catat kendala (misal: noise depth pada benda transparan, pengaruh cahaya matahari silau, dll).

[ ] [Ganen] Lakukan kalibrasi ulang atau filtering pada data depth jika fluktuasi jarak terlalu tinggi.

Minggu 7: Handover Navigasi & Obstacle Avoidance Test

Fokus: Demonstrasi akhir dan tuning.

[ ] [Semua] Jalankan robot secara penuh. Verifikasi apakah robot mampu menghindari halangan (obstacle avoidance) berdasarkan data dari vision.

[ ] [Thoriq] Handover sistem dan troubleshooting akhir bersama tim Navigasi/Mapping.

[ ] [Semua] Rapikan codebase, dokumentasikan cara running node, spesifikasi topik ROS, dan catatan instalasi driver di README.

📁 Rekomendasi Struktur Repository (ROS Package)

Karena proyek ini terintegrasi dengan sistem ROS, sangat disarankan untuk mengatur kode sumber dalam bentuk ROS Package standar. Package ini nantinya akan diletakkan di dalam folder src pada ROS workspace Anda (misalnya ~/catkin_ws/src/ untuk ROS 1 atau ~/colcon_ws/src/ untuk ROS 2).

Berikut adalah rancangan struktur repository yang direkomendasikan:

vision_obstacle_pkg/           # Nama direktori package ROS utama
├── CMakeLists.txt             # Aturan build ROS (wajib)
├── package.xml                # Informasi dependensi package (wajib)
├── README.md                  # Dokumentasi cara install & run package
├── launch/                    # Folder berisi file .launch
│   └── vision_core.launch     # File untuk menjalankan semua node sekaligus
├── msg/                       # Folder untuk definisi custom message ROS
│   └── ObjectDistance.msg     # Contoh isian: string class_name, float32 dist, dll
├── models/                    # Tempat menyimpan model Machine Learning
│   ├── best_model.tflite      # File model ringan hasil export (TFLite/ONNX)
│   └── labels.txt             # File teks berisi daftar nama kelas target
├── config/                    # Folder untuk file parameter (.yaml)
│   └── camera_params.yaml     # Konfigurasi resolusi kamera, nilai threshold, dll
├── scripts/                   # Source code utama berbasis Python (ROS Nodes)
│   ├── __init__.py
│   ├── camera_rs_node.py      # Node pembaca data RealSense D435 (Ganen)
│   ├── object_detect_node.py  # Node inference YOLO/Roboflow (Owen)
│   ├── sensor_fusion_node.py  # Node penggabung data BBox dan Depth (Thoriq)
│   └── utils.py               # Fungsi bantuan (misal: visualisasi OpenCV)
└── rviz/                      # Konfigurasi tampilan RViz
    └── vision_config.rviz     # Layout default agar tidak perlu setting ulang RViz
