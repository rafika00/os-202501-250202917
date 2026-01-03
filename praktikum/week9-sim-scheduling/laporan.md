
# Laporan Praktikum Minggu 9
Topik: Simulasi Algoritma Penjadwalan CPU

---

## Identitas
- **Nama**  : Rafika Rahma 
- **NIM**   : 250202917
- **Kelas** : 1 IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.  
2. Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.  
3. Menyajikan output simulasi dalam bentuk tabel atau grafik.  
4. Menjelaskan hasil simulasi secara tertulis.  
5. Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.

---

## Dasar Teori
- Penjadwalan CPU adalah mekanisme sistem operasi untuk menentukan urutan eksekusi proses di prosesor.
- Algoritma penjadwalan bertujuan mengoptimalkan kinerja sistem, seperti meminimalkan waiting time dan turnaround time.
- FCFS (First Come First Served) mengeksekusi proses berdasarkan urutan kedatangan tanpa preemption.
- Simulasi digunakan untuk mengevaluasi dan membandingkan kinerja algoritma penjadwalan secara sistematis dan akurat.

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Buat dataset proses minimal berisi:

   | Proses | Arrival Time | Burst Time |
   |:--:|:--:|:--:|
   | P1 | 0 | 6 |
   | P2 | 1 | 8 |
   | P3 | 2 | 7 |
   | P4 | 3 | 3 |

2. **Implementasi Algoritma**

   Program harus:
   - Menghitung *waiting time* dan *turnaround time*.  
   - Mendukung minimal **1 algoritma (FCFS atau SJF non-preemptive)**.  
   - Menampilkan hasil dalam tabel.

3. **Eksekusi & Validasi**

   - Jalankan program menggunakan dataset uji.  
   - Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.  
   - Simpan hasil eksekusi (screenshot).

4. **Analisis**

   - Jelaskan alur program.  
   - Bandingkan hasil simulasi dengan perhitungan manual.  
   - Jelaskan kelebihan dan keterbatasan simulasi.

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 9 - Simulasi Scheduling CPU"
   git push origin main
   ```

---

## Kode / Perintah

```
processes = [
    {"id": "P1", "arrival": 0, "burst": 6},
    {"id": "P2", "arrival": 1, "burst": 8},
    {"id": "P3", "arrival": 2, "burst": 7},
    {"id": "P4", "arrival": 3, "burst": 3},
]

time = 0
total_waiting = 0
total_turnaround = 0

print("Proses | Arrival | Burst | Waiting | Turnaround")
print("------------------------------------------------")

for p in processes:
    if time < p["arrival"]:
        time = p["arrival"]

    waiting_time = time - p["arrival"]
    turnaround_time = waiting_time + p["burst"]

    total_waiting += waiting_time
    total_turnaround += turnaround_time

    time += p["burst"]

    print(f"{p['id']:>6} | {p['arrival']:>7} | {p['burst']:>5} | {waiting_time:>7} | {turnaround_time:>10}")

avg_waiting = total_waiting / len(processes)
avg_turnaround = total_turnaround / len(processes)

print("------------------------------------------------")
print(f"Rata-rata Waiting Time     : {avg_waiting}")
print(f"Rata-rata Turnaround Time  : {avg_turnaround}")
```


---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
### Alur program
Program di atas mensimulasikan algoritma penjadwalan CPU First Come First Served (FCFS), di mana proses dieksekusi berdasarkan urutan kedatangan.

1. **Inisialisasi Data**

   ```
   processes = [
       {"id": "P1", "arrival": 0, "burst": 6},
       {"id": "P2", "arrival": 1, "burst": 8},
       {"id": "P3", "arrival": 2, "burst": 7},
       {"id": "P4", "arrival": 3, "burst": 3},
   ]
   ```

   Setiap proses memiliki:
   - `arrival`: waktu kedatangan proses
   - `burst`: waktu eksekusi CPU
   - Urutan list sudah mencerminkan urutan FCFS

2. **Variabel Waktu dan Akumulator**

   ```
   time = 0
   total_waiting = 0
   total_turnaround = 0
   ```

   - `time`: waktu CPU saat ini
   - `total_waiting`: total waktu tunggu semua proses
   - `total_turnaround`: total turnaround time semua proses

3. **Perulangan Setiap Proses**

   ```
   for p in processes:
   ```

   Untuk setiap proses:

   - Sinkronisasi waktu CPU

   ```
   if time < p["arrival"]:
       time = p["arrival"]
   ```

   CPU menunggu jika proses belum datang.

   - Hitung Waiting Time

   ```
   waiting_time = time - p["arrival"]
   ```

   Selisih antara waktu mulai eksekusi dan waktu kedatangan.

   - Hitung Turnaround Time
   ```
   turnaround_time = waiting_time + p["burst"]
   ```

   Total waktu proses berada di sistem

   - Update waktu CPU

   ```
   time += p["burst"]
   ```

   CPU berpindah ke proses berikutnya.

   - Cetak hasil

   Setiap proses ditampilkan dalam bentuk tabel.

4. **Hitung Rata-rata**

   ```
   avg_waiting = total_waiting / len(processes)
   avg_turnaround = total_turnaround / len(processes)
   ```

   Menghitung rata-rata waiting time dan turnaround time.

### Perbandingan dengan Perhitungan Manual

### Kelebihan dan Keterbatasan Simulasi
- **Kelebihan Simulasi**
   - Mempermudah perhitungan waiting time dan turnaround time tanpa menghitung manual.
   - Mengurangi kesalahan perhitungan dan lebih konsisten.
   - Dapat digunakan untuk menguji berbagai data proses dengan cepat.
   - Membantu memahami cara kerja algoritma penjadwalan FCFS secara praktis.

- **Keterbatasan Simulasi**
   - Hanya mensimulasikan algoritma FCFS, belum mencakup algoritma lain.
   - Tidak mendukung sistem preemptive atau interupsi proses.
   - Tidak memperhitungkan context switching dan I/O wait.
   - Kurang merepresentasikan kondisi sistem operasi yang sebenarnya.
   

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling? 

    **Jawaban:**

     Simulasi diperlukan untuk menguji algoritma scheduling karena lebih cepat, akurat, dan mudah menguji banyak skenario tanpa perhitungan manual.

2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar? 

    **Jawaban:**

     Pada dataset besar, hasil simulasi dan manual sama secara teori, tetapi simulasi lebih efisien dan minim kesalahan dibanding perhitungan manual.

3. Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.

    **Jawaban:**

     Algoritma FCFS paling mudah diimplementasikan karena logikanya sederhana, tidak ada preemption, dan proses dijalankan sesuai urutan kedatangan.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  

    **Jawaban:**
    memahami perhitungan waiting time dan turnaround time.

- Bagaimana cara Anda mengatasinya?  

    **Jawaban:**
    mempelajari teori dasar dan mencocokkan hasil simulasi dengan perhitungan manual.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
