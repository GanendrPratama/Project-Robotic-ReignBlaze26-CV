# Localization and Mapping

## 1. Deskripsi Tugas

**Tim Terlibat:** Nabil, Rafa  
**Fokus Utama:** Membuat sistem estimasi posisi robot dan pemetaan lingkungan menggunakan kamera, lidar, serta visualisasi RViz.

### 4.1 V-SLAM Menggunakan RealSense T265 dan Visualisasi RViz

**PIC:** Nabil, Rafa, Violin

**Detail Tugas:**
- Menghubungkan RealSense T265 ke sistem robot.
- Menginstall dan menguji driver RealSense T265.
- Mengambil data pose atau odometry dari kamera.
- Menghubungkan data pose ke ROS.
- Menentukan frame yang digunakan untuk odometry dan base robot.
- Menampilkan trajectory robot di RViz.
- Menguji estimasi posisi saat robot bergerak lurus, berbelok, dan kembali ke posisi awal.
- Mengamati drift atau error posisi dari hasil V-SLAM.
- Mengintegrasikan data V-SLAM dengan sistem mapping jika memungkinkan.

### 4.2 2D Mapping Menggunakan Lidar

**PIC:** Nabil, Rafa, Violin

**Detail Tugas:**
- Menghubungkan lidar ke robot.
- Menginstall dan menguji driver lidar.
- Mengambil data scan lidar melalui ROS topic.
- Menampilkan data scan lidar di RViz.
- Menentukan algoritma 2D mapping yang digunakan.
- Mengatur parameter mapping seperti frame, resolusi map, dan range sensor.
- Menjalankan proses mapping pada area uji.
- Menyimpan hasil map yang sudah dibuat.
- Menguji apakah posisi robot dapat dilihat relatif terhadap map.
- Mengamati kualitas map berdasarkan bentuk ruangan dan obstacle yang terbaca.

### 4.3 3D Mapping

**PIC:** Nabil, Rafa, Violin  
**Catatan:** Dikerjakan jika kamera 3D tersedia.

**Detail Tugas:**
- Menggunakan kamera depth atau sensor 3D yang tersedia.
- Mengambil data point cloud dari sensor.
- Menghubungkan point cloud dengan pose robot.
- Menampilkan data 3D di RViz.
- Membuat representasi lingkungan dalam bentuk 3D.
- Menguji 3D mapping pada beberapa area.
- Mengamati kualitas hasil 3D mapping.
- Mengidentifikasi kendala seperti noise, missing data, dan error pose.
- Menentukan apakah 3D mapping dapat digunakan untuk kebutuhan navigasi lanjutan.

## 2. Anggota Tim dan Pembagian Peran

Menjelaskan nama anggota tim dan tanggung jawab masing-masing anggota.

Contoh:

| Nama | Peran | Tanggung Jawab |
|---|---|---|
| Nabil | PIC Setup | Bertanggung jawab pada instalasi dan konfigurasi |
| Rafa | PIC Testing | Bertanggung jawab pada pengujian dan validasi |
| Violin | PIC Dokumentasi | Bertanggung jawab pada dokumentasi dan laporan |

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
