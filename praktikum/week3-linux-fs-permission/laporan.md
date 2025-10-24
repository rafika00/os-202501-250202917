
# Laporan Praktikum Minggu 3
Topik : Manajemen File dan Permission di Linux

---

## Identitas
- **Nama**  : Rafika Rahma
- **NIM**   : 2502202917 
- **Kelas** : 1 IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menggunakan perintah `ls`, `pwd`, `cd`, `cat` untuk navigasi file dan direktori.
2. Menggunakan `chmod` dan `chown` untuk manajemen hak akses file.
3. Menjelaskan hasil output dari perintah Linux dasar.
4. Menyusun laporan praktikum dengan struktur yang benar.
5. Mengunggah dokumentasi hasil ke Git Repository tepat waktu.

---

## Dasar Teori

1. Setiap file dan direktori di Linux memiliki hak akses (permission) yang menentukan siapa yang dapat membaca, menulis, atau mengeksekusi file tersebut.
2. Sistem kepemilikan file dibagi menjadi tiga kategori pengguna, yaitu *user (pemilik)*, *group (kelompok)*, dan *others (pengguna lain)*, masing-masing dengan izin berbeda.
3. Perintah `chmod`, `chown`, dan `chgrp` digunakan untuk mengatur izin dan kepemilikan file atau direktori sesuai kebutuhan keamanan dan pengelolaan sistem.
4. Manajemen permission bertujuan menjaga keamanan sistem dengan membatasi akses hanya kepada pengguna yang berhak.
5. Struktur sistem file Linux bersifat hierarkis (tree structure), di mana seluruh file dan direktori berada di bawah direktori utama *(root)* `/`.

---

## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).
   - Pastikan folder kerja berada di dalam direktori repositori Git praktikum:
     ```
     praktikum/week3-linux-fs-permission/
     ```

2. **Eksperimen 1 – Navigasi Sistem File**
   Jalankan perintah berikut:
   ```bash
   pwd
   ls -l
   cd /tmp
   ls -a
   ```
   - Jelaskan hasil tiap perintah.
   - Catat direktori aktif, isi folder, dan file tersembunyi (jika ada).

3. **Eksperimen 2 – Membaca File**
   Jalankan perintah:
   ```bash
   cat /etc/passwd | head -n 5
   ```
   - Jelaskan isi file dan struktur barisnya (user, UID, GID, home, shell).

4. **Eksperimen 3 – Permission & Ownership**
   Buat file baru:
   ```bash
   echo "Hello <NAME><NIM>" > percobaan.txt
   ls -l percobaan.txt
   chmod 600 percobaan.txt
   ls -l percobaan.txt
   ```
   - Analisis perbedaan sebelum dan sesudah chmod.  
   - Ubah pemilik file (jika memiliki izin sudo):
   ```bash
   sudo chown root percobaan.txt
   ls -l percobaan.txt
   ```
   - Catat hasilnya.

5. **Eksperimen 4 – Dokumentasi**
   - Ambil screenshot hasil terminal dan simpan di:
     ```
     praktikum/week3-linux-fs-permission/screenshots/
     ```
   - Tambahkan analisis hasil pada `laporan.md`.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 3 - Linux File System & Permission"
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

## Quiz
1. Apa fungsi dari perintah `chmod`?
   
   **jawaban :**
Perintah `chmod` adalah singkatan dari change mode, yaitu perintah di sistem operasi Linux atau Unix yang digunakan untuk mengubah hak akses (permission) suatu file atau direktori. Hak akses ini menentukan siapa yang dapat membaca (read), menulis (write), atau mengeksekusi (execute) file atau direktori tersebut.
3. Apa arti dari kode permission `rwxr-xr--`?
   
    **jawaban :**
   
- `rwx` untuk pemilik (user) : artinya pemilik file dapat membaca, menulis, dan mengeksekusi.

- `r-x` untuk kelompok (group) : artinya anggota grup hanya dapat membaca dan mengeksekusi, tetapi tidak dapat menulis.

- `r--` untuk pengguna lain (others) : artinya pengguna di luar grup hanya bisa membaca file tanpa bisa menulis atau mengeksekusi.
5. Jelaskan perbedaan antara `chown` dan `chmod`.
  
    **jawaban :**
  
| Perintah | Fungsi Utama | Contoh |
| :--- | :--- | :--- |
| **`chown`** (*change owner*) | Mengubah **kepemilikan** file atau direktori (siapa pemilik dan grupnya) | `chown user1:group1 file.txt` yaitu Mengubah pemilik menjadi *user1* dan grup menjadi *group1* |
| **`chmod`** (*change mode*) | Mengubah **hak akses (permission)** file atau direktori (izin baca, tulis, eksekusi) | `chmod 755 file.txt` yaitu  Mengatur izin baca-tulis-eksekusi untuk pemilik, dan baca-eksekusi untuk lainnya |


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
