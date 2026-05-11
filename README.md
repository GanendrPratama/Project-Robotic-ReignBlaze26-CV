## 3. Vision and Object Detection

**Tim Terlibat:** Ganen, Owen, Thoriq  
**Fokus Utama:** Membuat sistem deteksi objek menggunakan kamera, menggabungkan deteksi visual dengan jarak, serta membantu kebutuhan navigasi jika diperlukan.

### 3.1 Membuat Model Machine Learning untuk Object Detection

**PIC:** Ganen, Owen, Thoriq

**Detail Tugas:**
- Menentukan jenis objek yang perlu dideteksi robot.
- Mengumpulkan dataset gambar sesuai objek target.
- Melakukan labeling gambar menggunakan bounding box.
- Menentukan model object detection yang akan digunakan, seperti YOLO atau model ringan lainnya.
- Melakukan training atau fine-tuning model.
- Menguji model menggunakan gambar statis.
- Menguji model menggunakan input video atau kamera real-time.
- Mengukur performa model berdasarkan confidence score dan hasil deteksi.
- Mengoptimalkan model agar dapat berjalan cukup cepat di perangkat yang tersedia.

### 3.2 Deteksi Objek Berbasis Image dan Jarak

**PIC:** Ganen, Owen, Thoriq

**Detail Tugas:**
- Menggabungkan hasil object detection dengan informasi jarak.
- Mengambil posisi bounding box objek pada gambar.
- Menghubungkan posisi objek di gambar dengan data depth atau sensor jarak.
- Menampilkan nama objek, confidence score, dan estimasi jarak objek.
- Jika menggunakan kamera depth, mengambil jarak objek berdasarkan area bounding box.
- Jika kamera depth tidak tersedia, mempertimbangkan sensor tambahan seperti lidar atau ultrasonic.
- Membuat ROS topic untuk mengirim hasil deteksi objek.
- Menguji akurasi jarak pada beberapa posisi objek.
- Memastikan hasil deteksi bisa digunakan oleh tim navigasi atau mapping.

### 3.3 Processing Data 3D dari RealSense D435

**PIC:** Ganen, Owen, Thoriq  
**Catatan:** Dikerjakan jika kamera RealSense D435 tersedia.

**Detail Tugas:**
- Menghubungkan RealSense D435 ke sistem.
- Menginstall dan menguji driver RealSense.
- Mengambil data RGB dari kamera.
- Mengambil data depth dari kamera.
- Mengambil data point cloud dari kamera.
- Menampilkan point cloud di RViz.
- Mengolah data depth untuk mengetahui posisi objek dalam ruang 3D.
- Menguji kualitas depth pada beberapa jarak.
- Mengidentifikasi kendala seperti noise depth, pencahayaan, dan permukaan objek yang sulit terbaca.

### 3.4 Bantuan untuk Navigasi dan Path Planning

**PIC:** Ganen, Owen, Thoriq  
**Catatan:** Dikerjakan jika tugas object detection tidak menjadi fokus utama atau membutuhkan integrasi tambahan.

**Detail Tugas:**
- Membantu membaca data sensor untuk kebutuhan obstacle detection.
- Membantu menentukan posisi obstacle dari kamera atau lidar.
- Membantu menyediakan data objek/halangan untuk tim mapping.
- Membantu mengintegrasikan hasil vision ke sistem ROS.
- Membantu membuat input yang dapat digunakan untuk path planning.
- Menguji apakah data vision dapat membantu robot menghindari obstacle.
- Menyesuaikan format data agar mudah digunakan oleh tim localization dan mapping.

---

# Dokumentasi Wajib Semua Tim

Setiap tim wajib membuat dokumentasi dengan struktur berikut:

## 1. Deskripsi Tugas

Menjelaskan bagian yang dikerjakan oleh tim, tujuan pengerjaan, dan hubungannya dengan sistem robot secara keseluruhan.

## 2. Anggota Tim dan Pembagian Peran

Menjelaskan nama anggota tim dan tanggung jawab masing-masing anggota.

Contoh:

| Nama | Peran | Tanggung Jawab |
|---|---|---|
| Nama Anggota 1 | PIC Setup | Bertanggung jawab pada instalasi dan konfigurasi |
| Nama Anggota 2 | PIC Testing | Bertanggung jawab pada pengujian dan validasi |
| Nama Anggota 3 | PIC Dokumentasi | Bertanggung jawab pada dokumentasi dan laporan |

## 3. Tools dan Dependencies

Menuliskan tools, library, package, hardware, dan software yang digunakan.

Contoh:
- ROS
- RViz
- RealSense SDK
- Dynamixel SDK
- Lidar driver
- Joystick driver
- Python/C++
- Ubuntu

## 4. Langkah Instalasi dan Setup

Menjelaskan langkah-langkah instalasi secara runtut agar dapat diikuti ulang oleh anggota lain.

## 5. Cara Menjalankan Program

Menuliskan command terminal, launch file, script, atau urutan menjalankan sistem.

## 6. Proses Pengujian

Menjelaskan skenario pengujian yang dilakukan oleh tim.

Contoh:
- Pengujian koneksi.
- Pengujian sensor.
- Pengujian gerakan robot.
- Pengujian visualisasi RViz.
- Pengujian performa sistem.

# Ringkasan Pembagian Tim

| No | Divisi | Anggota Tim | Fokus Kerja |
|---|---|---|---|
| 1 | Teleoperation and Telemetry | Rafzhar, Zein, Milla | Joystick control, wireless connection, RViz operator display, dan network degradation |
| 2 | Kinematics and Locomotion | Shaq, Ara, Khanyfa | Hexapod controller, inverse kinematics, gait, dan Dynamixel servo |
| 3 | Vision and Object Detection | Ganen, Owen, Thoriq | Object detection, image + distance detection, RealSense D435, dan bantuan navigasi |
| 4 | Localization and Mapping | Nabil, Rafa, Violin | V-SLAM, 2D mapping lidar, 3D mapping, dan visualisasi RViz |

---
