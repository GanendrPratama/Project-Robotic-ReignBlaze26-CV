# Pembagian Tugas Project Robot

## 1. Teleoperation and Telemetry

**Tim Terlibat:** Rafzhar, Zein, Milla  
**Fokus Utama:** Mengatur sistem kendali robot dari laptop operator, komunikasi wireless, tampilan data robot, serta pengujian performa jaringan.

### 1.1 Mapping Input DualShock 3 ke Robot

**PIC:** Rafzhar, Zein, Milla

**Detail Tugas:**
- Menghubungkan DualShock 3 ke laptop operator.
- Memastikan joystick terbaca oleh sistem operasi dan ROS.
- Membaca input dari tombol, analog, dan trigger DualShock 3.
- Membuat daftar mapping tombol sesuai kebutuhan robot.
- Menentukan fungsi kontrol utama, seperti:
  - Analog kiri untuk maju, mundur, kiri, dan kanan.
  - Analog kanan untuk rotasi atau arah gerak tambahan.
  - Tombol tertentu untuk start, stop, mode jalan, reset, dan emergency stop.
- Membuat node ROS untuk mengubah input joystick menjadi command robot.
- Menghubungkan command joystick ke topic yang digunakan controller robot.
- Menguji respons robot terhadap setiap input joystick.
- Memastikan kontrol robot aman, stabil, dan mudah digunakan operator.

### 1.2 Manajemen Koneksi Wireless Robot dan Laptop Operator

**PIC:** Rafzhar, Zein

**Detail Tugas:**
- Mengatur koneksi wireless antara robot dan laptop operator.
- Menentukan skema jaringan yang digunakan, misalnya hotspot laptop, router, atau jaringan lokal.
- Mengatur IP address robot dan laptop operator.
- Mengatur konfigurasi ROS networking, seperti `ROS_MASTER_URI` dan `ROS_IP`.
- Memastikan laptop dapat mengirim command ke robot.
- Memastikan robot dapat mengirim data sensor dan status ke laptop operator.
- Melakukan uji koneksi menggunakan `ping`, `rostopic list`, `rostopic echo`, dan tools sejenis.
- Membuat prosedur troubleshooting jika koneksi robot tidak terdeteksi.
- Menguji kestabilan koneksi dalam beberapa kondisi jarak dan posisi operator.

### 1.3 Konfigurasi RViz untuk Operator

**PIC:** Rafzhar, Zein

**Detail Tugas:**
- Membuat tampilan RViz untuk kebutuhan operator.
- Menampilkan visualisasi 2D grid map.
- Menampilkan data 3D point cloud jika tersedia.
- Menampilkan robot state, TF, dan posisi robot.
- Menampilkan data sensor penting seperti lidar, kamera, atau odometry.
- Mengatur layout RViz agar mudah dipahami saat robot berjalan.
- Menentukan frame utama yang digunakan, seperti `map`, `odom`, atau `base_link`.
- Menyimpan konfigurasi RViz dalam file `.rviz`.
- Menguji apakah semua data penting robot tampil dengan benar di RViz.

### 1.4 Testing Network Degradation

**PIC:** Rafzhar, Zein

**Detail Tugas:**
- Mempelajari penggunaan tools network degradation, seperti `vsting-sa`.
- Menyiapkan skenario pengujian kualitas jaringan.
- Menguji robot pada kondisi jaringan normal.
- Menguji robot dengan tambahan delay rendah, sedang, dan tinggi.
- Menguji robot dengan packet loss.
- Menguji robot dengan jitter.
- Mengamati perubahan respons joystick terhadap robot.
- Mengamati delay data telemetry dari robot ke laptop operator.
- Mengamati apakah RViz tetap menampilkan data secara stabil.
- Menentukan batas kondisi jaringan yang masih aman untuk teleoperation.

---

## 2. Kinematics and Locomotion

**Tim Terlibat:** Shaq, Ara, Khanyfa  
**Fokus Utama:** Mengatur sistem gerak robot hexapod, inverse kinematics, pola langkah, dan kontrol servo Dynamixel.

### 2.1 Konfigurasi `hexapod_controller`

**PIC:** Shaq, Ara, Khanyfa

**Detail Tugas:**
- Mempelajari struktur dan cara kerja `hexapod_controller`.
- Mengidentifikasi jumlah kaki robot dan jumlah joint pada setiap kaki.
- Menentukan konfigurasi joint untuk setiap kaki.
- Mengatur parameter posisi awal setiap kaki.
- Mengatur batas gerakan joint agar tidak melewati batas mekanik.
- Mengatur parameter kecepatan, akselerasi, dan tinggi langkah.
- Menghubungkan controller dengan command dari sistem teleoperation.
- Menguji gerakan dasar robot seperti maju, mundur, belok kiri, dan belok kanan.
- Memastikan gerakan antar kaki sinkron dan tidak saling bertabrakan.

### 2.2 Inverse Kinematics pada Kaki dan Claw

**PIC:** Shaq, Ara, Khanyfa

**Detail Tugas:**
- Mempelajari struktur mekanik kaki robot.
- Menentukan panjang link pada setiap bagian kaki.
- Membuat model perhitungan inverse kinematics untuk kaki robot.
- Menghitung sudut joint berdasarkan target posisi kaki.
- Menguji posisi kaki pada beberapa titik target.
- Memastikan hasil sudut IK masih dalam range gerak servo.
- Mengintegrasikan IK dengan `hexapod_controller`.
- Jika claw digunakan, membuat perhitungan sederhana untuk posisi buka dan tutup claw.
- Menguji gerakan claw agar tidak terlalu cepat, terlalu kuat, atau melewati batas mekanik.

### 2.3 Gerakan Kaki Robot di Uneven Terrain

**PIC:** Shaq, Ara, Khanyfa

**Detail Tugas:**
- Menentukan pola jalan atau gait yang akan digunakan robot.
- Menguji beberapa gait seperti tripod gait, wave gait, atau ripple gait.
- Mengatur tinggi angkat kaki agar robot dapat melewati permukaan tidak rata.
- Mengatur urutan kaki yang bergerak agar robot tetap seimbang.
- Mengatur kecepatan langkah robot sesuai kondisi terrain.
- Menguji robot pada permukaan datar terlebih dahulu.
- Menguji robot pada permukaan tidak rata secara bertahap.
- Mengamati kestabilan badan robot saat berjalan.
- Melakukan tuning parameter gait jika robot mudah tergelincir, tersangkut, atau tidak stabil.

### 2.4 Konfigurasi Servo Driver Dynamixel

**PIC:** Shaq, Ara, Khanyfa

**Detail Tugas:**
- Menghubungkan servo Dynamixel ke sistem robot.
- Mengidentifikasi ID setiap servo Dynamixel.
- Mengatur baudrate dan protocol Dynamixel.
- Membuat daftar ID servo berdasarkan posisi kaki dan joint.
- Menguji komunikasi antara laptop/controller dengan servo.
- Mengatur mode operasi servo sesuai kebutuhan.
- Mengatur batas posisi, kecepatan, dan torque servo.
- Membuat prosedur kalibrasi posisi awal setiap kaki.
- Menguji setiap servo satu per satu sebelum diuji sebagai satu sistem robot.

---

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

## 4. Localization and Mapping

**Tim Terlibat:** Nabil, Rafa  
**Fokus Utama:** Membuat sistem estimasi posisi robot dan pemetaan lingkungan menggunakan kamera, lidar, serta visualisasi RViz.

### 4.1 V-SLAM Menggunakan RealSense T265 dan Visualisasi RViz

**PIC:** Nabil, Rafa

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

**PIC:** Nabil, Rafa  
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
