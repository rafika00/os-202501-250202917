
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

![alt text](<screenshots/proses_user.png>)
***Jelaskan setiap output dan fungsinya***

1. Pemeriksaan User

- `whoami` : menampilkan user aktif (`rrfikaa`)
- `id` : menampilkan UID, GID, dan grup yang dimiliki user
- `groups` : daftar grup tempat user tergabung

2. Membuat User Baru

- `sudo adduser praktikan` : membuat akun baru bernama praktikan, membuat grup dan home directory, lalu meminta password serta info tambahan
- `Is the information correct? [Y/n]` : konfirmasi data user
  
 3. Beralih ke User Baru

- `su - praktikan` : login sebagai user praktikan
- Muncul pesan selamat datang Ubuntu berisi info sistem (versi, load, memori, IP, dsb)

---

![alt text](<screenshots/proses_user1.png>)
***Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND***

| Kolom | Arti | Fungsi |
| :--- | :--- | :--- |
| **USER** | Nama user pemilik proses | Menunjukkan siapa yang menjalankan proses contoh : `root`, `praktikan`, `rrfikaa` |
| **PID** | Process ID | Nomor unik untuk setiap proses di sistem. Digunakan saat ingin menghentikan atau memantau proses, contoh : `kill <PID>` |
| **%CPU** | Persentase penggunaan CPU | Menunjukkan seberapa banyak CPU digunakan oleh proses tersebut. Semakin tinggi, semakin berat prosesnya |
| **%MEM** | Persentase penggunaan memori (RAM) | Menunjukkan jumlah memori yang dipakai proses terhadap total RAM |
| **COMMAND** | Perintah atau program yang dijalankan | Menampilkan nama aplikasi atau service yang sedang aktif, contoh : `/sbin/init`, `systemd`, `bash`, `sleep` |

---

![alt text](<screenshots/proses_user2.png>)
***Catat PID proses sleep***

```bash
ps aux | grep sleep
```

Output :

```
praktik+   624  0.0  0.0  3124  1664  pts/0  S+  06:04  0:00  sleep 1000
```

**PID proses `sleep` adalah 624**

Artinya proses dengan **ID 624** sedang menjalankan perintah `sleep 1000` di background (mode diam selama 1000 detik)

---

***Amati hierarki proses dan identifikasi proses induk (init/systemd)***

- **Proses induk tertinggi:** `systemd(1)` : proses pertama (init process) yang dijalankan oleh kernel setelah booting. Semua proses lain di sistem Linux merupakan turunan (child process) dari `systemd(1)`

- **Rantai proses `sleep`:**

```
    |-init-systemd(Ub(2)-+-SessionLeader(313)---Relay(315)(314)---bash(315)---su(534)---bash(560)-+-head(650)
           |                    |                                                                        |-pstree(649)
           |                    |                                                                         `-sleep(624)
```

Jadi, proses `sleep(624)` adalah turunan dari shell `bash(560)`, yang dijalankan oleh user melalui terminal, dan pada akhirnya semuanya bermuara ke **systemd(1)** sebagai induk utama.

---

## Analisis

**Eksperimen 1 :**

Perintah `adduser` berhasil digunakan untuk membuat akun baru bernama **praktikan** dengan direktori home dan konfigurasi default sendiri. Akun ini termasuk dalam grup `users` namun tidak memiliki hak administratif seperti `sudo`. Sementara itu, akun **rrfikaa** tetap menjadi pengguna utama dengan akses penuh terhadap sistem.

**Eksperimen 2 :**

Perintah `ps aux` dan `top` menjalankan berbagai proses penting milik **root** untuk menjaga kestabilan dan layanan sistem. User **praktikan** hanya memiliki prosesnya sendiri dan tidak dapat mengubah proses milik pengguna lain, sehingga keamanan sistem tetap terjaga. Selain itu, kondisi sistem terlihat ringan dan stabil karena penggunaan CPU serta memori sangat rendah.

**Eksperimen 3 :**

User **praktikan** menjalankan perintah `sleep 1000 &` yang berfungsi menunda proses selama 1000 detik dan dijalankan di latar belakang. Sistem menampilkan PID **624** sebagai identitas proses tersebut. Melalui perintah `ps aux | grep sleep`, terlihat bahwa proses `sleep` benar-benar aktif dengan PID 624, sementara baris kedua adalah proses `grep` yang digunakan untuk mencari kata “sleep”.

Ketika user mencoba menghentikan proses menggunakan `kill <PID>`, muncul pesan kesalahan karena simbol `<PID>` hanyalah contoh, bukan angka sebenarnya. Untuk menghentikan proses dengan benar, user seharusnya menggunakan `kill 624`.

Selanjutnya, dengan perintah `pstree -p`, ditampilkan struktur pohon proses sistem. Dari hasilnya terlihat bahwa proses `sleep(624)` merupakan turunan dari shell `bash(560)` milik user **praktikan**, sementara proses-proses lain seperti `systemd`, `cron`, dan `dbus-daemon` merupakan proses utama sistem.

Percobaan ini menunjukkan bahwa sistem Linux menjalankan proses secara hierarkis (induk–anak), dan setiap proses memiliki PID unik. Selain itu, user dapat menjalankan proses di latar belakang, memeriksa statusnya, serta menghentikannya bila diperlukan.

---

## Kesimpulan
### **Kesimpulan Praktikum**

1. **Manajemen User:**
   Sistem Linux memungkinkan pembuatan dan pengelolaan user baru dengan `adduser`. Setiap user memiliki direktori home dan hak akses berbeda, menjaga keamanan dan pemisahan data antar pengguna

2. **Manajemen Proses:**
   Setiap perintah atau program yang dijalankan akan membentuk proses dengan PID unik. Proses dapat dipantau menggunakan `ps aux` dan dijalankan di latar belakang menggunakan `&`

3. **Hierarki Proses:**
   Semua proses di Linux memiliki struktur induk–anak dan pada akhirnya berasal dari systemd(1) sebagai proses pertama yang dijalankan oleh sistem. Proses `sleep(624)` adalah contoh turunan yang berawal dari `systemd`

---

## Tugas & Quiz

### Tugas

1. Jelaskan fungsi tiap printah

   **Jawaban :**

| Perintah | Keterangan |
| :--- | :--- |
| `whoami` | Menampilkan nama user yang sedang login (contoh: `rrfikaa`) |
| `id` | Menampilkan UID, GID, dan daftar grup yang dimiliki user aktif |
| `groups` | Menampilkan daftar grup yang diikuti oleh user saat ini |
| `sudo adduser praktikan` | Membuat user baru bernama praktikan, lengkap dengan direktori home dan grup default |
| `su – praktikan` | Berpindah login ke user praktikan sepenuhnya |
| `ps aux  head -10` | Menampilkan 10 baris pertama dari daftar semua proses yang sedang berjalan |
| `sleep 1000 &` | Menjalankan proses sleep selama 1000 detik di background (tidak mengunci terminal) |
| `ps aux  grep sleep` | Menampilkan informasi proses yang mengandung kata *sleep* (untuk memastikan proses berjalan) |
| `kill <PID>` | Menghentikan proses dengan PID tertentu |
| `pstree -p  head -20` | Menampilkan struktur hierarki proses (pohon proses) lengkap dengan PID dan hanya 20 baris pertama |
| PID Sleep = 624 | Menunjukkan ID proses untuk perintah `sleep 1000` |
| Hierarki proses |Hierarki proses menunjukkan hubungan induk-anak antarproses di Linux. Contoh : `systemd(1)` - `init-systemd(Ub(2))` - `SessionLeader(313)` - `bash(315)` - `su(534)` - `bash(560)` - `sleep(624)` |
| roses induk (parent process) | Proses induk tertinggi adalah systemd (PID 1) - induk dari semua proses di sistem Linux |

2. Gambarkan hierarki proses dalam bentuk diagram pohon (pstree)

    **Jawaban :**
   
```
 systemd(1)-+-50-mdot-news(627)---wget(647)
           |-agetty(203)
           |-agetty(213)
           |-cron(176)
           |-dbus-daemon(177)
           |-init-systemd(Ub(2)-+-SessionLeader(313)---Relay(315)(314)---bash(315)---su(534)---bash(560)-+-head(650)
           |                    |                                                                        |-pstree(649)
           |                    |                                                                         `-sleep(624)
           |                    |-init(8)---{init}(9)
           |                    |-login(316)---bash(386)
           |                    `-{init-systemd(Ub}(10)
           |-rsyslogd(192)-+-{rsyslogd}(215)
           |               |-{rsyslogd}(216)
           |               `-{rsyslogd}(217)
           |-systemd(363)---(sd-pam)(364)
           |-systemd(537)---(sd-pam)(538)
           |-systemd-journal(60)
           |-systemd-logind(185)
           |-systemd-resolve(128)
           |-systemd-timesyn(140)---{systemd-timesyn}(168)
```

3. Jelaskan hubungan antara user management dan keamanan sistem Linux

    **Jawaban :**
   
- Pembatasan Akses : Setiap user punya akun dan izin sendiri, mencegah akses tidak sah ke data sistem
- Pemisahan Hak Istimewa : User biasa dibatasi, hanya root yang punya akses penuh untuk mencegah kerusakan sistem
- Pengawasan Aktivitas : Log sistem mencatat login dan penggunaan perintah penting untuk mendeteksi penyalahgunaan
- Manajemen Grup & Izin File : Grup dan permission (r, w, x) mengontrol siapa yang boleh membaca, menulis, atau menjalankan file

### Quiz
1. Apa fungsi dari proses `init` atau `systemd` dalam sistem Linux?

   **Jawaban :**
Proses `init` atau `systemd` merupakan komponen utama dalam sistem Linux yang berfungsi sebagai proses pertama yang dijalankan setelah kernel aktif. Proses ini bertanggung jawab untuk memulai seluruh layanan dan proses penting, mengatur urutan booting, serta menjadi induk dari semua proses lain di sistem. Dengan perannya tersebut, `init` atau `systemd` memastikan sistem Linux dapat berjalan dengan stabil, terstruktur, dan siap digunakan oleh pengguna maupun aplikasi lain.

2. Apa perbedaan antara `kill` dan `killall`?

   **Jawaban :**
Perintah `kill` digunakan untuk menghentikan satu proses tertentu berdasarkan PID (Process ID), sedangkan `killall` digunakan untuk menghentikan semua proses yang memiliki nama program yang sama. `kill` lebih spesifik dan menargetkan satu proses, sementara `killall` bersifat lebih luas karena mematikan semua proses dengan nama yang ditentukan.

3. Mengapa user `root` memiliki hak istimewa di sistem Linux?

   **Jawaban :**
User `root` memiliki hak istimewa di sistem Linux karena berperan sebagai administrator utama yang memiliki akses penuh terhadap seluruh sistem. Akun ini digunakan untuk melakukan tugas-tugas penting seperti pengelolaan pengguna, konfigurasi sistem, instalasi perangkat lunak, dan pemeliharaan keamanan. Dengan hak istimewanya, `root` memastikan sistem dapat dikelola dan dikendalikan sepenuhnya, namun harus digunakan dengan hati-hati karena kesalahan dapat memengaruhi seluruh sistem.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
  
  **Jawaban :**
  Memahami hubungan hierarki proses dan cara kerja perintah seperti `ps`, `pstree`, serta `kill`, karena perlu memahami bagaimana setiap proses saling terhubung dan dijalankan oleh sistem.
  
- Bagaimana cara Anda mengatasinya?
  
  **Jawaban :**
  Saya mengatasinya dengan mencoba langsung di terminal Linux, menjalankan perintah satu per satu dari perintah `ps aux`, `pstree -p`, dan `kill <PID>)`, lalu mencatat hasilnya untuk melihat hubungan antarproses secara nyata dan saya juga berdiskusi dengan teman.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
