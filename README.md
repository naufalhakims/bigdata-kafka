# bigdata-kafka
### NAUFAL SYAFI' HAKIM - 5027231022

# 🎯 Latar Belakang Masalah

Sebuah perusahaan logistik mengelola beberapa gudang penyimpanan yang menyimpan barang sensitif seperti makanan, obat-obatan, dan elektronik. Untuk menjaga kualitas penyimpanan, gudang-gudang tersebut dilengkapi dengan dua jenis sensor:

    Sensor Suhu

    Sensor Kelembaban

Sensor akan mengirimkan data setiap detik. Perusahaan ingin memantau kondisi gudang secara real-time untuk mencegah kerusakan barang akibat suhu terlalu tinggi atau kelembaban berlebih.

## 📋 Tugas Mahasiswa
1. Buat Topik Kafka

Buat dua topik di Apache Kafka:

    sensor-suhu-gudang

    sensor-kelembaban-gudang

Topik ini akan digunakan untuk menerima data dari masing-masing sensor secara real-time.
2. Simulasikan Data Sensor (Producer Kafka)

Buat dua Kafka producer terpisah:
a. Producer Suhu

    Kirim data setiap detik

    Format:

    {"gudang_id": "G1", "suhu": 82}

b. Producer Kelembaban

    Kirim data setiap detik

    Format:

    {"gudang_id": "G1", "kelembaban": 75}

Gunakan minimal 3 gudang: G1, G2, G3.
3. Konsumsi dan Olah Data dengan PySpark
a. Buat PySpark Consumer

    Konsumsi data dari kedua topik Kafka.

b. Lakukan Filtering:

    Suhu > 80°C → tampilkan sebagai peringatan suhu tinggi

    Kelembaban > 70% → tampilkan sebagai peringatan kelembaban tinggi

Contoh Output:

[Peringatan Suhu Tinggi]
Gudang G2: Suhu 85°C

[Peringatan Kelembaban Tinggi]
Gudang G3: Kelembaban 74%

4. Gabungkan Stream dari Dua Sensor

Lakukan join antar dua stream berdasarkan gudang_id dan window waktu (misalnya 10 detik) untuk mendeteksi kondisi bahaya ganda.
c. Buat Peringatan Gabungan:

Jika ditemukan suhu > 80°C dan kelembaban > 70% pada gudang yang sama, tampilkan peringatan kritis.
✅ Contoh Output Gabungan:

[PERINGATAN KRITIS]
Gudang G1:
- Suhu: 84°C
- Kelembaban: 73%
- Status: Bahaya tinggi! Barang berisiko rusak

Gudang G2:
- Suhu: 78°C
- Kelembaban: 68%
- Status: Aman

Gudang G3:
- Suhu: 85°C
- Kelembaban: 65%
- Status: Suhu tinggi, kelembaban normal

Gudang G4:
- Suhu: 79°C
- Kelembaban: 75%
- Status: Kelembaban tinggi, suhu aman


# Prerequiset
1. Pastikan kita sudah menginstall docker
2. Nyalakan dulu docker dekstop saat memulai project ini

# Pengerjaan step by step
1. Pastikan kita menyimpan seluruh proyek dalam satu direktori
2. Jalankan command ini untuk melakukan konfigurasi yaml
```bash
docker-compose up -d
```
3. Gunakan command ini untuk membuat topic
```bash
docker exec -it kafka bash
# setelah kita masuk
kafka-topics --create --topic sensor-suhu-gudang --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
kafka-topics --create --topic sensor-kelembaban-gudang --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```
4. Copy direktori proyek ke app lalu masuk ke dalamnya
```bash
docker cp "D:\PATH\KE\DIREKTORI\PROYEK" pyspark:/app/ 
docker exec -it pyspark bash
```
5. Install semua yang ada di requirements.txt
```bash
pip install -r requirements.txt --no-cache-dir
```
6. Jalankan `producer_suhu.py` dan `producer_kelembaban.py` secara bersama, kita bisa menggunakan 2 terminal
```bash
python producer_suhu.py
python producer_kelembaban.py
```
![image](https://github.com/user-attachments/assets/3b522e82-3c5c-4c74-a3b7-8b99cb0e0a24)

7. Buat terminal baru untuk menjalankan `consumer_pyspark.py`
```bash
python consumer_pyspark.py
```
![image](https://github.com/user-attachments/assets/b5976f47-f8d9-49a9-a2ff-a3638c8dabf3)
![image](https://github.com/user-attachments/assets/bcc78e61-4a03-4f76-a713-dc01f3319657)
![image](https://github.com/user-attachments/assets/2f57f7a7-1762-4988-81ca-3f256f1ad383)

8. Selesai
