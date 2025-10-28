
# Laporan Praktikum Minggu 4
Topik: Manajemen Proses dan User di Linux

---

## Identitas
- **Nama**  : Rafika Rahma 
- **NIM**   : 250202917
- **Kelas** : 1 IKRA

---

## Tujuan

Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menjelaskan konsep proses dan user dalam sistem operasi Linux  
2. Menampilkan daftar proses yang sedang berjalan dan statusnya 
3. Menggunakan perintah untuk membuat dan mengelola user
4. Menghentikan atau mengontrol proses tertentu menggunakan PID 
5. Menjelaskan kaitan antara manajemen user dan keamanan sistem
   
---

## Dasar Teori

Manajemen proses dan user di Linux merupakan bagian penting dalam pengelolaan sistem operasi yang bertujuan untuk memastikan penggunaan sumber daya komputer secara efisien dan aman. Proses adalah program yang sedang dijalankan dan dikelola oleh kernel, di mana setiap proses memiliki identitas unik berupa PID (Process ID). Proses dapat berjalan di latar depan (foreground) atau latar belakang (background), serta dapat dimonitor dan dikendalikan menggunakan perintah seperti `ps`, `top`, `kill`, `bg`, dan `fg`.
Dalam sistem Linux, setiap proses memiliki hubungan hierarkis antara parent process dan child process, dengan proses induk utama yaitu `init` atau `systemd`. Sementara itu, manajemen user berkaitan dengan pengaturan akun pengguna dan grup. Linux mendukung sistem multiuser, di mana setiap pengguna memiliki UID (User ID) dan grup dengan GID (Group ID). Pengelolaan ini dilakukan menggunakan perintah seperti `adduser`, `deluser`, dan `usermod`.
Dari sisi keamanan, setiap file dan proses di Linux memiliki hak akses tertentu berupa izin baca (read), tulis (write), dan eksekusi (execute), yang membedakan akses antara pemilik, grup, dan pengguna lain. Administrator (root) memiliki hak tertinggi dalam sistem untuk mengatur proses maupun pengguna. Dengan demikian, manajemen proses dan user berperan penting dalam menjaga stabilitas, efisiensi, dan keamanan sistem Linux.

---

## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).  
   - Pastikan Anda sudah login sebagai user non-root.  
   - Siapkan folder kerja:
     ```
     praktikum/week4-proses-user/
     ```

2. **Eksperimen 1 – Identitas User**
   Jalankan perintah berikut:
   ```bash
   whoami
   id
   groups
   ```
   - Jelaskan setiap output dan fungsinya.  
   - Buat user baru (jika memiliki izin sudo):
     ```bash
     sudo adduser praktikan
     sudo passwd praktikan
     ```
   - Uji login ke user baru.

3. **Eksperimen 2 – Monitoring Proses**
   Jalankan:
   ```bash
   ps aux | head -10
   top -n 1
   ```
   - Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.  
   - Simpan tangkapan layar `top` ke:
     ```
     praktikum/week4-proses-user/screenshots/top.png
     ```

4. **Eksperimen 3 – Kontrol Proses**
   - Jalankan program latar belakang:
     ```bash
     sleep 1000 &
     ps aux | grep sleep
     ```
   - Catat PID proses `sleep`.  
   - Hentikan proses:
     ```bash
     kill <PID>
     ```
   - Pastikan proses telah berhenti dengan `ps aux | grep sleep`.

5. **Eksperimen 4 – Analisis Hierarki Proses**
   Jalankan:
   ```bash
   pstree -p | head -20
   ```
   - Amati hierarki proses dan identifikasi proses induk (`init`/`systemd`).  
   - Catat hasilnya dalam laporan.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 4 - Manajemen Proses & User"
   git push origin main
   ```

---

## Kode / Perintah
Eksperimen 1
  ```bash
   whoami
   id
   groups
  ```

   ```bash
     sudo adduser praktikan
     sudo passwd praktikan
   ```

Eksperimen 2

  ```bash
   ps aux | head -10
   top -n 1
  ```

Eksperimen 3

  ```bash
     sleep 1000 &
     ps aux | grep sleep
  ```

  ```bash
     kill <PID>
  ```

Eksperimen 4

 ```bash
   pstree -p | head -20
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
1. Apa fungsi dari proses `init` atau `systemd` dalam sistem Linux?

   **jawaban :**
Proses `init` atau `systemd` merupakan komponen utama dalam sistem Linux yang berfungsi sebagai proses pertama yang dijalankan setelah kernel aktif. Proses ini bertanggung jawab untuk memulai seluruh layanan dan proses penting, mengatur urutan booting, serta menjadi induk dari semua proses lain di sistem. Dengan perannya tersebut, `init` atau `systemd` memastikan sistem Linux dapat berjalan dengan stabil, terstruktur, dan siap digunakan oleh pengguna maupun aplikasi lain.

2. Apa perbedaan antara `kill` dan `killall`?

   **jawaban :**
Perintah `kill` digunakan untuk menghentikan satu proses tertentu berdasarkan PID (Process ID), sedangkan `killall` digunakan untuk menghentikan semua proses yang memiliki nama program yang sama. `kill` lebih spesifik dan menargetkan satu proses, sementara `killall` bersifat lebih luas karena mematikan semua proses dengan nama yang ditentukan.

3. Mengapa user `root` memiliki hak istimewa di sistem Linux?

   **jawaban :**
User `root` memiliki hak istimewa di sistem Linux karena berperan sebagai administrator utama yang memiliki akses penuh terhadap seluruh sistem. Akun ini digunakan untuk melakukan tugas-tugas penting seperti pengelolaan pengguna, konfigurasi sistem, instalasi perangkat lunak, dan pemeliharaan keamanan. Dengan hak istimewanya, `root` memastikan sistem dapat dikelola dan dikendalikan sepenuhnya, namun harus digunakan dengan hati-hati karena kesalahan dapat memengaruhi seluruh sistem.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
