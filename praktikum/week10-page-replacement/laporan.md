
# Laporan Praktikum Minggu 10
Topik: Manajemen Memori – Page Replacement (FIFO & LRU)

---

## Identitas
- **Nama**  : Rafika Rahma
- **NIM**   : 250202917
- **Kelas** : 1 IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Mengimplementasikan algoritma page replacement FIFO dalam program.
2. Mengimplementasikan algoritma page replacement LRU dalam program.
3. Menjalankan simulasi page replacement dengan dataset tertentu.
4. Membandingkan performa FIFO dan LRU berdasarkan jumlah *page fault*.
5. Menyajikan hasil simulasi dalam laporan yang sistematis.

---

## Dasar Teori
1. **Page replacement** adalah mekanisme sistem operasi untuk menentukan halaman mana yang akan diganti ketika memori penuh dan terjadi *page fault*.
2. **FIFO (First In First Out)** mengganti halaman yang paling awal masuk ke memori tanpa mempertimbangkan frekuensi atau waktu akses.
3. **LRU (Least Recently Used)** mengganti halaman yang paling lama tidak digunakan berdasarkan riwayat akses halaman.
4. FIFO dapat mengalami **Belady’s Anomaly**, yaitu kondisi ketika penambahan jumlah frame justru meningkatkan *page fault*.
5. LRU umumnya memberikan performa lebih baik karena memanfaatkan **prinsip locality** dalam pola akses memori.

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Gunakan *reference string* berikut sebagai contoh:
   ```
   7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
   ```
   Jumlah frame memori: **3 frame**.

2. **Implementasi FIFO**

   - Simulasikan penggantian halaman menggunakan algoritma FIFO.
   - Catat setiap *page hit* dan *page fault*.
   - Hitung total *page fault*.

3. **Implementasi LRU**

   - Simulasikan penggantian halaman menggunakan algoritma LRU.
   - Catat setiap *page hit* dan *page fault*.
   - Hitung total *page fault*.

4. **Eksekusi & Validasi**

   - Jalankan program untuk FIFO dan LRU.
   - Pastikan hasil simulasi logis dan konsisten.
   - Simpan screenshot hasil eksekusi.

5. **Analisis Perbandingan**

   Buat tabel perbandingan seperti berikut:

   | Algoritma | Jumlah Page Fault | Keterangan |
   |:--|:--:|:--|
   | FIFO | ... | ... |
   | LRU | ... | ... |


   - Jelaskan mengapa jumlah *page fault* bisa berbeda.
   - Analisis algoritma mana yang lebih efisien dan alasannya.

6. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 10 - Page Replacement FIFO & LRU"
   git push origin main
   ```

---

## Kode / Perintah

```
reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_size = 3

def fifo_page_replacement(ref, frame_size):
    frames = []
    page_fault = 0

    print("=== FIFO Simulation ===")
    print("Page | Status | Frames")
    print("-" * 30)

    for page in ref:
        if page in frames:
            status = "HIT"
        else:
            status = "FAULT"
            page_fault += 1
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)

        print(f"{page:^4} | {status:^6} | {frames}")

    print("-" * 30)
    print(f"Total Page Fault (FIFO): {page_fault}\n")
    return page_fault

def lru_page_replacement(ref, frame_size):
    frames = []
    page_fault = 0

    print("=== LRU Simulation ===")
    print("Page | Status | Frames")
    print("-" * 30)

    for page in ref:
        if page in frames:
            status = "HIT"
            frames.remove(page)
            frames.append(page)
        else:
            status = "FAULT"
            page_fault += 1
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)

        print(f"{page:^4} | {status:^6} | {frames}")

    print("-" * 30)
    print(f"Total Page Fault (LRU): {page_fault}\n")
    return page_fault

fifo_fault = fifo_page_replacement(reference_string, frame_size)
lru_fault = lru_page_replacement(reference_string, frame_size)

print("=== Comparison Result ===")
print(f"FIFO Page Faults : {fifo_fault}")
print(f"LRU Page Faults  : {lru_fault}")

```

---

## Hasil Eksekusi
![alt text](<screenshots/page_replacement.png>)

---

## Analisis
**Tabel perbandingan seperti berikut:**

  | Algoritma | Jumlah Page Fault | Keterangan |
  | :--- | :--- | :--- |
  | FIFO (First-In-First-Out) | 10 | Mengganti halaman yang paling awal masuk tanpa melihat pola akses |
  | LRU (Least Recently Used) | 9 | Mengganti halaman yang paling lama tidak digunakan |

**Penjelasan Perbedaan *Page Fault***

Jumlah page fault bisa berbeda karena strategi penggantian halaman yang digunakan tidak sama. FIFO hanya berdasarkan urutan masuk halaman, sehingga dapat mengganti halaman yang masih sering digunakan. Sebaliknya, LRU mempertimbangkan riwayat akses, sehingga halaman yang sering dipakai tetap berada di memori.

**Analisis Efisiensi**

Algoritma LRU lebih efisien dibanding FIFO karena menghasilkan jumlah page fault yang lebih sedikit. Hal ini disebabkan LRU memanfaatkan prinsip locality, sehingga kinerja pengelolaan memori menjadi lebih optimal.

---

## Kesimpulan

   1. Algoritma page replacement FIFO dan LRU dapat diimplementasikan untuk mensimulasikan pengelolaan memori dan mendeteksi terjadinya *page fault*.
   2. Berdasarkan hasil simulasi, algoritma LRU menghasilkan jumlah *page fault* yang lebih sedikit dibanding FIFO karena mempertimbangkan riwayat penggunaan halaman.
   3. Pemilihan algoritma page replacement yang tepat berpengaruh terhadap efisiensi penggunaan memori dan kinerja sistem secara keseluruhan.

---

## Quiz
1. Apa perbedaan utama FIFO dan LRU?

   **Jawaban:**  

   - FIFO (First In First Out) mengganti halaman yang paling lama masuk, tanpa melihat apakah masih sering digunakan.

   - LRU (Least Recently Used) mengganti halaman yang paling lama tidak digunakan, berdasarkan riwayat akses.

2. Mengapa FIFO dapat menghasilkan *Belady’s Anomaly*?

   **Jawaban:**  

   FIFO tidak mempertimbangkan pola penggunaan halaman, sehingga penambahan jumlah frame justru bisa meningkatkan page fault.

3. Mengapa LRU umumnya menghasilkan performa lebih baik dibanding FIFO?

   **Jawaban:**  

   LRU memanfaatkan prinsip locality, sehingga halaman yang sering digunakan tetap berada di memori dan page fault lebih sedikit.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 

     **Jawaban:**  
    Membedakan proses penggantian halaman pada FIFO dan LRU, terutama memahami riwayat akses pada LRU

- Bagaimana cara Anda mengatasinya?  
    **Jawaban:**  
    Melakukan simulasi langkah demi langkah dan mencoba program sederhana, sehingga alur page hit dan page fault lebih mudah dipahami.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
