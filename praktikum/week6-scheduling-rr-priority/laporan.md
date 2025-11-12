
# Laporan Praktikum Minggu 6
Topik: Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling

---

## Identitas
- **Nama**  : Rafika Rahma 
- **NIM**   : 250202917 
- **Kelas** : 1 IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:

- Menghitung waiting time dan turnaround time pada algoritma RR dan Priority.
- Menyusun tabel hasil perhitungan dengan benar dan sistematis.
- Membandingkan performa algoritma RR dan Priority.
- Menjelaskan pengaruh time quantum dan prioritas terhadap keadilan eksekusi proses.
- Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.

---

## Dasar Teori
Round Robin (RR) merupakan algoritma penjadwalan CPU yang membagi waktu proses secara bergiliran dengan jatah waktu tertentu yang disebut time quantum. Setiap proses dijalankan selama waktu tersebut, kemudian jika belum selesai, proses akan dikembalikan ke antrian siap untuk menunggu giliran berikutnya. Algoritma ini bersifat preemptive dan sangat adil karena semua proses mendapat kesempatan yang sama menggunakan CPU. Kinerja RR sangat bergantung pada besar kecilnya time quantum jika terlalu kecil, sistem sering berpindah konteks jika terlalu besar, algoritma ini menjadi mirip dengan FCFS. RR cocok digunakan pada sistem time-sharing yang menuntut waktu respons cepat.

Priority Scheduling adalah algoritma yang menentukan urutan eksekusi proses berdasarkan tingkat prioritasnya. Proses dengan prioritas tertinggi akan dijalankan lebih dulu. Algoritma ini dapat bersifat preemptive atau non-preemptive, tergantung apakah proses baru dengan prioritas lebih tinggi boleh menghentikan proses yang sedang berjalan. Kelemahan utama Priority Scheduling adalah potensi terjadinya starvation, yaitu proses prioritas rendah tidak mendapat giliran eksekusi. Untuk mengatasinya dapat digunakan teknik aging, yaitu peningkatan prioritas proses yang menunggu terlalu lama. Algoritma ini efektif jika sistem memerlukan pengaturan sumber daya berdasarkan tingkat kepentingan tugas.

---

## Langkah Praktikum
1. **Siapkan Data Proses**
   Gunakan contoh data berikut (boleh dimodifikasi sesuai kebutuhan):
   | Proses | Burst Time | Arrival Time | Priority |
   |:--:|:--:|:--:|:--:|
   | P1 | 5 | 0 | 2 |
   | P2 | 3 | 1 | 1 |
   | P3 | 8 | 2 | 4 |
   | P4 | 6 | 3 | 3 |

2. **Eksperimen 1 – Round Robin (RR)**
   - Gunakan *time quantum (q)* = 3.  
   - Hitung *waiting time* dan *turnaround time* untuk tiap proses.  
   - Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).  
     ```
     | P1 | P2 | P3 | P4 | P1 | P3 | ...
     0    3    6    9   12   15   18  ...
     ```
   - Catat sisa *burst time* tiap putaran.

3. **Eksperimen 2 – Priority Scheduling (Non-Preemptive)**
   - Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).  
   - Lakukan perhitungan manual untuk:
     ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]
     ```
   - Buat tabel perbandingan hasil RR dan Priority.

4. **Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)**
   - Ubah *quantum* menjadi 2 dan 5.  
   - Amati perubahan nilai rata-rata *waiting time* dan *turnaround time*.  
   - Buat tabel perbandingan efek *quantum*.

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua hasil tabel dan screenshot ke:
     ```
     praktikum/week6-scheduling-rr-priority/screenshots/
     ```
   - Buat tabel perbandingan seperti berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | RR | ... | ... | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
     | Priority | ... | ... | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
   git push origin main
   ```

---

## Kode / Perintah
 ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]
     Average Waiting Time (WT) = Total WT / Jumlah Proses
     Average Turnaround Time (TAT) = Total TAT / Jumlah Proses
 ```

---

## Hasil Eksekusi

![alt text](<screenshots/rr_priority.png>)

---

**Eksperimen 1 – Round Robin (RR)**

*Hasil Perhitungan*

| Proses | Burst Time | Arrival Time | Finish Time P1 | Finish Time P2 | Finish Time P3 | TAT (FT - AT) | WT (TAT - BT) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| P1 | 5 | 0 | 3 (sisa 2) | 14 (selesai) | - | 14 - 0 = 14 | 14 - 5 = 9 |
| P2 | 3 | 1 | 6 (selesai) | - | - | 6 - 1 = 5 | 5 - 3 = 2 |
| P3 | 8 | 2 | 9 (sisa 5) | 17 (sisa 2) | 22 (selesai ) | 22 - 2 = 20 | 20 - 8 = 12 |
| P4 | 6 | 3 | 12 (sisa 3) | 20 (selesai ) | - | 20 - 3 = 17 | 17 - 6 = 11 |

*Simulasi eksekusi menggunakan Gantt Chart*

```
   | P1 | P2 | P3 | P4 | P1 | P3 | P4 | P3 |
   0    3    6    9   12   14   17   20   22
```
---

**Eksperimen 2 – Priority Scheduling (Non-Preemptive)**

Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).

*Hasil Perhitungan*

| Proses | Arrival Time | Burst Time | Priority | Start | Finish Time (Start - BT) | WT (Start - AT) | TAT (WT + BT)
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| P1 | 0 | 5 | 2 | 0 | 0 + 5 = 5 | 0 - 0 = 0 | 0 + 5 = 5 |
| P2 | 1 | 3 | 1 | 5 | 5 + 3 = 8 | 5 - 1 = 4 | 4 + 3 = 7 |
| P4 | 3 | 6 | 3 | 8 | 8 + 6 = 14 | 8 - 3 = 5 | 5 + 6 = 11 |
| P3 | 2 | 8 | 4 | 14 | 14 + 8 = 22 | 14 - 2 = 12 | 12 + 8 = 20 |

*Simulasi eksekusi menggunakan Gantt Chart*

```
   | P1 | P2 | P3 | P4 |
   0    5    8    14   22
```

---

**Eksperimen 3 – Variasi Time Quantum**

![alt text](<screenshots/variasi time quantum.png>)

- **Time Quantum = 2**

*Hasil Perhitungan*

| Proses | Burst Time | Arrival Time | Finish Time P1 | Finish Time P2 | Finish Time P3 | Finish Time P4 |TAT (FT - AT) | WT (TAT - BT) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| P1 | 5 | 0 | 2 (sisa 3) | 10 (sisa 1) | 16 (selesai) | - | 16 - 0 = 16 | 16 - 5 = 11 |
| P2 | 3 | 1 | 4 (sisa 1) | 11 (selesai) | - | - | 11 - 1 = 10 | 10 - 3 = 7 |
| P3 | 8 | 2 | 6 (sisa 6) | 13 (sisa 4) | 18 (sisa 2) | 22 (selesai) | 22 - 2 = 20 | 20 - 8 = 12 |
| P4 | 6 | 3 | 8 (sisa 4) | 15 (sisa2) | 20 (selesai) | - | 20 - 3 = 17 | 17 - 6 = 11 |

*Simulasi eksekusi menggunakan Gantt Chart*

```
   | P1 | P2 | P3 | P4 | P1 | P2 | P3 | P4 | P1 | P3 | P4 | P3 |
   0    2    4    6    8   10   11   13   15   16   18    20   22
```

- **Time Quantum = 5**

*Hasil Perhitungan*

| Proses | Burst Time | Arrival Time | Finish Time P1 | Finish Time P2 |TAT (FT - AT) | WT (TAT - BT) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | 
| P1 | 5 | 0 | 5 (selesai) | - | 5 - 0 = 5 | 5 - 5 = 0 |
| P2 | 3 | 1 | 8 (selesai) | - | 8 - 1 = 7 | 7 - 3 = 4 |
| P3 | 8 | 2 | 13 (sisa 3) | 21 (selesai) | 21 - 2 = 19 | 19 - 8 = 11 |
| P4 | 6 | 3 | 18 (sisa 1) | 22 (selesai) | 22 - 3 = 19 | 19 - 6 = 13 |

*Simulasi eksekusi menggunakan Gantt Chart*

```
   | P1 | P2 | P3 | P4 | P3 | P4 |
   0    5    8   13   18   21   22   
```

- **Tabel Perbandingan Efek Quantum**

| Time Quantum | Rata-rata Waiting Time (WT) | Rata-rata Turnaround Time (TAT) | Efek |
| :--- | :--- | :--- | :--- |
|Quantum Kecil (q = 2) | Lebih besar (10,25) | Lebih besar (15,75) | Proses sering berganti sehingga sistem lebih responsif, tetapi waktu tunggu (WT) dan turnaround time (TAT) menjadi lebih besar akibat banyaknya context switch. |
|Quantum Besar (q = 5) | Lebih kecil (7,00) | Lebih kecil (12,50) | Proses berganti lebih jarang sehingga efisiensi meningkat dan WT serta TAT lebih kecil, namun sistem menjadi kurang responsif seperti FCFS. |

---

**Eksperimen 4 – Perbandingan Round Robin (RR) dan Priority Scheduling**

   | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
   |------------|------------------|----------------------|------------|-------------|
   | RR | 8,5 | 14 | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
   | Priority | 5,25 | 10,75 | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

---

## Analisis
Pada percobaan Round Robin, setiap proses mendapat giliran secara bergantian sehingga sistem lebih adil, tetapi waktu tunggu dan turnaround-nya lebih besar karena sering terjadi pergantian konteks.

Sementara pada Priority Scheduling, proses dengan prioritas tertinggi dieksekusi lebih dulu sehingga waktu tunggu dan turnaround rata-ratanya lebih kecil. Namun, proses berprioritas rendah bisa menunggu lama jika banyak proses prioritas tinggi, yang dapat menyebabkan starvation.

Ketika time quantum kecil (q = 2), sistem menjadi lebih responsif, tetapi terlalu sering melakukan context switch sehingga efisiensinya menurun. Sebaliknya, jika time quantum besar (q = 5), efisiensi meningkat dan waktu rata-rata menurun, tetapi responsivitas terhadap proses baru menjadi lebih lambat. 

---

## Kesimpulan
- Algoritma Round Robin memberikan keadilan dan responsivitas yang baik, tetapi terlalu kecilnya time quantum menyebabkan banyak context switch dan menurunkan efisiensi sistem.
- Algoritma Priority Scheduling lebih efisien karena proses dengan prioritas tinggi dijalankan lebih dulu, namun dapat menyebabkan starvation pada proses berprioritas rendah.
- Pemilihan time quantum yang tepat sangat penting untuk menyeimbangkan antara responsivitas dan efisiensi sistem.
 
---

## Quiz

1. Apa perbedaan utama antara Round Robin dan Priority Scheduling?  

**Jawaban:**
Perbedaan utama antara Round Robin (RR) dan Priority Scheduling terletak pada dasar penentuan urutan eksekusi proses. Round Robin menjadwalkan proses secara bergiliran berdasarkan urutan kedatangan, dengan jatah waktu tetap (time quantum) untuk setiap proses. Fokusnya pada pembagian waktu yang adil agar semua proses mendapat kesempatan yang sama. Sedangkan Priority Scheduling menjadwalkan proses berdasarkan tingkat prioritas, di mana proses dengan prioritas tertinggi akan dijalankan lebih dahulu. Fokusnya pada tingkat kepentingan proses, bukan pada keadilan waktu.

2. Apa pengaruh besar/kecilnya *time quantum* terhadap performa sistem?  

**Jawaban:**
Jika time quantum terlalu kecil, sistem jadi tidak efisien karena terlalu sering berganti proses. Jika terlalu besar, respons sistem melambat. Jadi, perlu ukuran time quantum yang seimbang agar sistem efisien dan responsif.

3. Mengapa algoritma Priority dapat menyebabkan *starvation*?  

**Jawaban:**
Algoritma Priority Scheduling dapat menyebabkan *starvation* karena proses berprioritas rendah terus tertunda oleh proses berprioritas tinggi yang datang berulang kali. Hal ini bisa dicegah dengan teknik aging, yaitu menaikkan prioritas proses yang menunggu terlalu lama.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  

**Jawaban:**
Menurut saya yang menantang minggu ini yaitu memahami cara mengerjakan langkah-langkah penjadwalan proses pada algoritma Round Robin dan Priority Scheduling.

- Bagaimana cara Anda mengatasinya?  

**Jawaban:**
Saya mempelajari kembali langkah perhitungan tiap proses secara sistematis

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
