
# Mini Simulasi Sistem Operasi  
**CPU Scheduling (FCFS), Page Replacement (FIFO), dan Deadlock Detection**

---

##  Deskripsi Proyek

Proyek ini merupakan aplikasi berbasis **Command Line Interface (CLI)** yang mensimulasikan beberapa konsep utama dalam **Sistem Operasi**, yaitu:

1. **CPU Scheduling** menggunakan algoritma **First Come First Served (FCFS)**
2. **Page Replacement** menggunakan algoritma **First In First Out (FIFO)**
3. **Deadlock Detection** dengan pendekatan *circular wait*

Aplikasi dikembangkan menggunakan **Python** dan dapat dijalankan baik secara langsung maupun melalui **Docker** untuk memastikan konsistensi lingkungan eksekusi.

---

## Anggota Kelompok

| No | Nama | NIM |
|----|------|-----|
| 1 | Faik Setyawan | 250202936 |
| 2 | Evelin Natalie | 250202916 |
| 3 | Nadya Pramudita | 250202956 |
| 4 | Rafika Rahma | 250202917 |
| 5 | Novia Safitri | 250202923 |

---

##  Modul yang Diimplementasikan

### 1. CPU Scheduling – FCFS
- **Skenario**: Transfer File
- **Input**: Dataset proses (arrival time & burst time)
- **Output**:
  - Waiting Time (WT)
  - Turnaround Time (TAT)
  - Rata-rata WT dan TAT

### 2. Page Replacement – FIFO
- **Skenario**: Pemantauan CCTV / Antrian Pasien
- **Input**: Reference string / file antrian
- **Output**:
  - Jumlah page fault
  - Hit ratio
  - Status antrian FIFO

### 3. Deadlock Detection
- **Skenario**: Dining Philosophers
- **Pendekatan**: Circular Wait Detection
- **Output**:
  - Status deadlock
  - Proses yang terlibat dalam deadlock

---

##  Struktur Proyek

```

code/
├─ data/
│  ├─ process.csv
│  ├─ fifo.txt
│  └─ dataset.csv
├─ cpu_scheduling.py
├─ page_replacement.py
├─ deadlock_detection.py
├─ main.py
├─ Dockerfile
└─ README.md

````

---

## Cara Menjalankan Aplikasi

### Menjalankan Tanpa Docker

1. Pastikan **Python 3** sudah terinstal.
2. Masuk ke direktori `code/`.
3. Jalankan perintah:
   ```bash
   python main.py

4. Pilih menu:

   * 1 CPU Scheduling (FCFS)
   * 2 Page Replacement (FIFO)
   * 3 Deadlock Detection
   * 0 Keluar

---

###  Menjalankan Menggunakan Docker

1. Masuk ke direktori `code/`.
2. Build Docker image:

   ```bash
   docker build -t week15-proyek-kelompok .
   ```
3. Jalankan container:

   ```bash
   docker run -it --rm week15-proyek-kelompok
   ```
4. Gunakan menu CLI seperti pada mode non-Docker.
   * 1 CPU Scheduling (FCFS)
   * 2 Page Replacement (FIFO)
   * 3 Deadlock Detection
   * 0 Keluar

---

##  Dataset

### `process.csv` (CPU Scheduling)

| Proses | Waktu_kedatangan | Waktu_Pelayanan |
| ------ | ------------ | ---------- |
| F1     | 0            | 12         |
| F2     | 1            | 1          |
| F3     | 2            | 30         |
| F4     | 3            | 3          |
| F5     | 4            | 70         |

### `fifo.txt` (Page Replacement)

```
Andi
Budi
Citra
```

### `dataset.csv` (Deadlock Detection)

| Mobil | Memegang_jalan | Menunggu_jalan |
| ----------- | ---------- | ------- |
| A          | UTARA         | TIMUR      |
| B          | TIMUR         | SELATAN    |
| C          | SELATAN       | BARAT      |
| 4          | BARAT         | UTARA      |

---

## Hasil Pengujian

* FCFS menunjukkan **convoy effect** pada proses dengan burst time besar
* FIFO berjalan sesuai prinsip *first in first out*
* Deadlock berhasil terdeteksi melalui *circular wait*

Seluruh modul berjalan normal baik di environment lokal maupun Docker.

---
