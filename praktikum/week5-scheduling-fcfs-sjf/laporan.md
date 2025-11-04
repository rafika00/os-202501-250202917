
# Laporan Praktikum Minggu 5
Topik: Penjadwalan CPU – FCFS dan SJF

---

## Identitas
- **Nama**  : Rafika Rahma
- **NIM**   : 250202917
- **Kelas** : 1 IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menghitung *waiting time* dan *turnaround time* untuk algoritma FCFS dan SJF.  
2. Menyajikan hasil perhitungan dalam tabel yang rapi dan mudah dibaca.  
3. Membandingkan performa FCFS dan SJF berdasarkan hasil analisis.  
4. Menjelaskan kelebihan dan kekurangan masing-masing algoritma.  
5. Menyimpulkan kapan algoritma FCFS atau SJF lebih sesuai digunakan.  

---

## Dasar Teori
- Penjadwalan CPU adalah mekanisme sistem operasi untuk menentukan urutan eksekusi proses di CPU agar penggunaan prosesor menjadi efisien dan adil.
- FCFS (First Come First Served) merupakan algoritma penjadwalan paling sederhana yang mengeksekusi proses berdasarkan urutan kedatangan; proses yang datang lebih dulu akan dijalankan terlebih dahulu.
- SJF (Shortest Job First) menjadwalkan proses berdasarkan lama waktu eksekusi (burst time) yang paling pendek, sehingga dapat menghasilkan rata-rata waktu tunggu minimum.
- FCFS mudah diimplementasikan, tetapi dapat menimbulkan convoy effect, yaitu proses pendek tertunda karena menunggu proses panjang.
- SJF efisien dalam sistem batch, tetapi tidak cocok untuk sistem interaktif karena sulit memperkirakan waktu eksekusi proses dan berpotensi menyebabkan starvation bagi proses berdurasi panjang.

---

## Langkah Praktikum
1. **Siapkan Data Proses**
   Gunakan tabel proses berikut sebagai contoh (boleh dimodifikasi dengan data baru):
   | Proses | Burst Time | Arrival Time |
   |:--:|:--:|:--:|
   | P1 | 6 | 0 |
   | P2 | 8 | 1 |
   | P3 | 7 | 2 |
   | P4 | 3 | 3 |

2. **Eksperimen 1 – FCFS (First Come First Served)**
   - Urutkan proses berdasarkan *Arrival Time*.  
   - Hitung nilai berikut untuk tiap proses:
     ```
     Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
     Turnaround Time (TAT) = WT + Burst Time
     ```
   - Hitung rata-rata Waiting Time dan Turnaround Time.  
   - Buat Gantt Chart sederhana:  
     ```
     | P1 | P2 | P3 | P4 |
     0    6    14   21   24
     ```

3. **Eksperimen 2 – SJF (Shortest Job First)**
   - Urutkan proses berdasarkan *Burst Time* terpendek (dengan memperhatikan waktu kedatangan).  
   - Lakukan perhitungan WT dan TAT seperti langkah sebelumnya.  
   - Bandingkan hasil FCFS dan SJF pada tabel berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | FCFS | ... | ... | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
     | SJF | ... | ... | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |

4. **Eksperimen 3 – Visualisasi Spreadsheet (Opsional)**
   - Gunakan Excel/Google Sheets untuk membuat perhitungan otomatis:
     - Kolom: Arrival, Burst, Start, Waiting, Turnaround, Finish.
     - Gunakan formula dasar penjumlahan/subtraksi.
   - Screenshot hasil perhitungan dan simpan di:
     ```
     praktikum/week5-scheduling-fcfs-sjf/screenshots/
     ```

5. **Analisis**
   - Bandingkan hasil rata-rata WT dan TAT antara FCFS & SJF.  
   - Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya.  
   - Tambahkan kesimpulan singkat di akhir laporan.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 5 - CPU Scheduling FCFS & SJF"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## D. Tugas & Quiz
### Tugas
1. Hitung *waiting time* dan *turnaround time* dari minimal 2 skenario FCFS dan SJF.  
2. Sajikan hasil perhitungan dalam tabel perbandingan (FCFS vs SJF).  
3. Analisis kelebihan dan kelemahan tiap algoritma.  

### Quiz
1. Apa perbedaan utama antara FCFS dan SJF?

   **Jawaban :**

   Perbedaan utama antara FCFS (First Come First Served) dan SJF (Shortest Job First) terletak pada cara penjadwalan proses dilakukan yaitu urutan eksekusi proses berdasarkan kriteria waktu kedatangan atau lama waktu eksekusi (burst time).

| Aspek | FCFS (First Come First Served) | SJF (Shortest Job First) |
| :--- | :--- | :--- |
| Kriteria Penjadwalan | Berdasarkan urutan kedatangan proses. Proses yang datang lebih dulu dieksekusi lebih dulu | Berdasarkan lama waktu eksekusi (burst time). Proses dengan waktu eksekusi paling singkat dieksekusi lebih dulu |
| Sifat Algoritma | Non-preemptive (tidak bisa dihentikan sebelum selesai) | Bisa non-preemptive atau preemptive (SRTF - Shortest Remaining Time First) |
| Kelebihan | Mudah dipahami dan diimplementasikan | Waktu rata-rata tunggu (average waiting time) bisa lebih kecil, efisien untuk sistem dengan banyak proses pendek |
| Kekurangan | Bisa terjadi convoy effect (proses cepat menunggu proses lama) | Memerlukan informasi burst time sebelumnya (kadang sulit diketahui) |
| Contoh Urutan Eksekusi | Jika urutan kedatangan: P1, P2, P3 → maka urutan eksekusi juga P1 → P2 → P3 | Jika burst time: P1=6, P2=2, P3=4 → urutan eksekusi: P2 → P3 → P1 |

3. Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum?

   **Jawaban :**

   SJF (Shortest Job First) menghasilkan rata-rata waktu tunggu minimum karena proses dengan waktu eksekusi paling singkat dieksekusi terlebih dahulu, sehingga mengurangi waktu tunggu proses-proses pendek yang biasanya mendominasi antrean.
   
5. Apa kelemahan SJF jika diterapkan pada sistem interaktif

   **Jawaban :**

   Algoritma SJF (Shortest Job First) kurang cocok digunakan pada sistem interaktif karena sulit memperkirakan lama waktu eksekusi setiap proses dan dapat menyebabkan starvation bagi proses yang berdurasi panjang. Meskipun efisien dalam mengurangi waktu tunggu rata-rata, SJF tidak mampu menjamin respon cepat dan keadilan bagi semua proses dalam lingkungan yang bersifat interaktif.
   
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
