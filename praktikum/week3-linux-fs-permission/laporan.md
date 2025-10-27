# Laporan Praktikum Minggu 3
Topik : Manajemen File dan Permission di Linux

---

## Identitas
- **Nama**  : Rafika Rahma
- **NIM**   : 250202917 
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
Eksperimen 1
```bash
   pwd
   ls -l
   cd /tmp
   ls -a
```
Eksperimen 2
 ```bash
   cat /etc/passwd | head -n 5
   ```
Eksperimen 3
 ```bash
   echo "Hello <NAME><NIM>" > percobaan.txt
   ls -l percobaan.txt
   chmod 600 percobaan.txt
   ls -l percobaan.txt
   ```
 ```bash
   sudo chown root percobaan.txt
   ls -l percobaan.txt
   ```

---

## Hasil Eksekusi
![alt text](<screenshots/eksperimen week3.png>)

---

### Eksperimen 1

- **Perintah 1 :**
  
  | Perintah | Output | Penjelasan |
  | :--- | :--- | :---|
  | `pwd` | /home/rrfikaa | `pwd` (print working directory) menampilkan direktori kerja saat ini. Artinya, pengguna sedang berada di folder /home/rrfikaa — yaitu direktori home milik user `rrfikaa` |

- **Perintah 2 :**

    Perintah : `ls -l`
    
    Output : total 8
    
             -rw-r--r-- 1 rrfikaa rrfikaa 46 Oct 25 06:24 cat
    
             -rw------- 1 root    rrfikaa 32 Oct 24 23:27 percobaan.txt

    Penjelasan : `ls -l` menampilkan daftar file/folder dalam format long listing (lengkap dengan permission, pemilik, ukuran, dan tanggal).

    | Nama File | Permission | Owner | Group | Ukuran | Waktu Modifikasi | Keterangan |
    | :--- | :--- | :---| :--- | :--- | :--- | :--- |
    | `cat` | `-rw-r--r--` | `rrfikaa` | `rrfikaa` | 46 byte | Oct 25 06:24 | File biasa, dapat dibaca dan ditulis oleh pemilik, dibaca oleh group dan others |
    | `percobaan.txt` | `-rw-------` | `root` | `rrfikaa` | 32 byte | Oct 24 23:27 | File hanya bisa diakses oleh user `root` |

- **Perintah 3 :**

  Perintah : `cd /tmp`

  Penjelasan : cd (change directory) digunakan untuk berpindah direktori. Setelah perintah ini dijalankan, direktori aktif berubah menjadi /tmp (direktori sementara sistem Linux).

- **Perintah 4 :**

  Perintah : `ls -a`

  Output :

```
   .                 
  ..                
  .X11-unix         
  snap-private-tmp  
  systemd-private-785d171431054ac098d8d0a9a89305db-systemd-logind.service-FChNqp
  systemd-private-785d171431054ac098d8d0a9a89305db-systemd-resolved.service-5nhKjU
  systemd-private-785d171431054ac098d8d0a9a89305db-systemd-timesyncd.service-wfIk0q
  systemd-private-785d171431054ac098d8d0a9a89305db-wsl-pro.service-Af6XWU
```

  Penjelasan :

  | Nama | Jenis | Keterangan |
  | :--- | :--- | :---|
  | `.` | Folder | Menunjukkan direktori saat ini (`/tmp`) |
  | `..` | Folder | Menunjukkan direktori induk (`/`) |
  | `.X11-unix` | Folder tersembunyi | Digunakan oleh sistem grafis X11 untuk komunikasi antar proses |
  | `snap-private-tmp` | Folder | Area sementara yang digunakan oleh aplikasi Snap |
  | `systemd-private-*` | Folder | Direktori sementara yang dibuat oleh sistem `systemd` untuk menjaga keamanan dan isolasi layanan (misalnya `logind`, `resolved`, `timesyncd`, `wsl-pro`) |

### Eksperimen 2

```
rrfikaa@DESKTOP-TMK8VNI:/tmp$ cat /etc/passwd | head -n 5
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
```

Setiap baris berisi 7 kolom yang dipisahkan oleh tanda titik dua (:) dengan format :

```
username:password:UID:GID:comment:home_directory:login_shell
```

| Kolom | Nama Field | Arti / Fungsi |
| :--- | :--- | :---|
| 1 | username | Nama pengguna yang digunakan untuk login |
| 2 | password | Biasanya berisi `x`, artinya password disimpan secara terenkripsi di file `/etc/shadow` |
| 3 | UID (User ID) | Nomor identitas unik untuk pengguna. `0` adalah UID khusus untuk `root` |
| 4 | GID (Group ID) | Nomor identitas grup utama pengguna |
| 5 | comment / GECOS field | Deskripsi atau nama lengkap pengguna (opsional) |
| 6 | home directory | Lokasi direktori utama pengguna di sistem |
| 7 | login shell | Program shell yang digunakan saat pengguna login (misalnya `/bin/bash`) |

***Analisi Output***

| No | Username | UID | GID | Home Directory | Login Shell | Keterangan |
| :--- | :--- | :---| :--- | :--- | :--- | :--- |
| 1 | root   | 0 | 0 | `/root` | `/bin/bash` | Akun administrator utama (superuser) dengan akses penuh ke sistem |
| 2 | daemon | 1 | 1 | `/usr/sbin` | `/usr/sbin/nologin` | Akun sistem untuk menjalankan layanan background (daemon), tidak bisa login |
| 3 | bin | 2 | 2 | `/bin` | `/usr/sbin/nologin` | Akun sistem yang memiliki program biner standar. Tidak digunakan oleh user biasa |
| 4 | sys | 3 | 3 | `/dev` | `/usr/sbin/nologin` | Akun sistem untuk proses internal kernel dan device management |
| 5 | sync | 4 | 65534 | `/bin` | `/bin/sync` | Akun khusus yang dapat menjalankan perintah sinkronisasi sistem file, tidak untuk login |



### Eksperimen 3 

```
rrfikaa@DESKTOP-TMK8VNI:/tmp$ echo "Hello <Rafika Rahma><250202917>" > percobaan.txt
rrfikaa@DESKTOP-TMK8VNI:/tmp$ ls -l percobaan.txt
-rw-r--r-- 1 rrfikaa rrfikaa 32 Oct 25 08:26 percobaan.txt
rrfikaa@DESKTOP-TMK8VNI:/tmp$ chmod 600 percobaan.txt
rrfikaa@DESKTOP-TMK8VNI:/tmp$ ls -l percobaan.txt
-rw------- 1 rrfikaa rrfikaa 32 Oct 25 08:26 percobaan.txt
rrfikaa@DESKTOP-TMK8VNI:/tmp$ cat percobaan.txt
Hello <Rafika Rahma><250202917>
rrfikaa@DESKTOP-TMK8VNI:/tmp$ sudo chown root percobaan.txt
[sudo] password for rrfikaa:
rrfikaa@DESKTOP-TMK8VNI:/tmp$ ls -l percobaan.txt
-rw------- 1 root rrfikaa 32 Oct 25 08:26 percobaan.txt
rrfikaa@DESKTOP-TMK8VNI:/tmp$ cd
rrfikaa@DESKTOP-TMK8VNI:~$
```

```
echo "Hello <Rafika Rahma><250202917>" > percobaan.txt
```

Penjelasan : 

- Membuat file baru bernama percobaan.txt di direktori /tmp.
- Isi file : `Hello <Rafika Rahma><250202917>`
- File otomatis dibuat dengan izin default, yaitu :

  `-rw-r--r--`
   - Pemilik (owner): dapat membaca dan menulis
   - Grup dan pengguna lain: hanya dapat membaca
 
**Setelah diperiksa dengan perintah `ls -l`**

```
-rw-r--r-- 1 rrfikaa rrfikaa 32 Oct 25 08:26 percobaan.txt
```

Keterangan:
- Pemilik: rrfikaa
- Grup: rrfikaa
- Ukuran: 32 byte
- Permission: rw-r--r-- (mode 644)

```
chmod 600 percobaan.txt
```

Penjelasan:

- chmod digunakan untuk mengubah izin (permission) file
- Mode 600 berarti:
  - Pemilik `rw-` : dapat membaca dan menulis
  - Grup `---` : tidak ada akses
  - Lainnya `---` : tidak ada akses
- Hasilnya file hanya bisa diakses oleh pemilik

**Setelah `chmod 600` hasil `ls -l` menjadi :**

```
-rw------- 1 rrfikaa rrfikaa 32 Oct 25 08:26 percobaan.txt
```

**Analisis Perubahan**

 | Nama | Jenis | Keterangan |
 | :--- | :--- | :---|
 | Sebelum `(rw-r--r--)` | Sesudah `(rw-------)` | Efek |
 | Owner bisa baca & tulis | Owner tetap bisa baca & tulis | Tidak berubah |
 | Group bisa baca | Group tidak bisa akses | Lebih aman |
 | Others bisa baca | Others tidak bisa akses | Lebih aman |

```
sudo chown root percobaan.txt
```

Penjelasan:
- `chown` (change owner) digunakan untuk mengubah kepemilikan file
- Karena butuh hak administratif, digunakan `sudo`
- File `percobaan.txt` sekarang dimiliki oleh user root

**Setelah `sudo chown root` hasil `ls -l` menjadi :**

```
-rw------- 1 root rrfikaa 32 Oct 25 08:26 percobaan.txt
```

**Analisis Perubahan**

| Atribut | Sebelum | Sesudah | Efek |
| :--- | :--- | :--- | :--- |
| Owner | `rrfikaa` | `root` | File kini milik administrator |
| Group | `rrfikaa` | `rrfikaa` | Tetap sama |
| Permission | `rw-------` | `rw-------` | Tidak berubah |
| Akses oleh user biasa | Bisa (karena pemilik) | Tidak bisa lagi, kecuali via `sudo` | Membatasi akses |

---

## Analisi

**Eksperimen 1 :** Perintah dasar Linux seperti `pwd`, `ls -l`, `cd`, dan `ls -a` berfungsi untuk menampilkan lokasi kerja, isi direktori, serta berpindah antar direktori dalam sistem. Hasil percobaan juga menunjukkan pentingnya konsep manajemen file dan permission, di mana setiap file memiliki pemilik (user), grup, dan hak akses (read, write, execute) yang menentukan siapa saja yang dapat mengakses atau mengubah file tersebut. Selain itu, direktori /tmp berperan sebagai tempat penyimpanan sementara untuk berbagai proses sistem, termasuk layanan `systemd`.

**Eksperimen 2 :** `/etc/passwd` berfungsi sebagai database utama yang menyimpan informasi seluruh akun pengguna di sistem Linux, baik akun pengguna biasa maupun akun sistem.
Lima baris pertama yang ditampilkan menunjukkan bahwa sebagian besar adalah akun sistem seperti `daemon`, `bin`, `sys`, dan `sync` yang digunakan untuk menjalankan layanan internal, bukan untuk login pengguna. Hanya akun root yang memiliki hak akses penuh terhadap sistem.

**Eksperimen 3 :** Perintah `echo`, `chmod`, dan `chown` memiliki peran penting dalam manajemen file dan permission di Linux. Perintah `echo` digunakan untuk membuat file dan menuliskan isi ke dalamnya, `chmod` digunakan untuk mengubah izin akses file agar hanya pihak tertentu yang dapat membaca atau menulis, sedangkan `chown` berfungsi untuk mengubah kepemilikan file. Setelah file `percobaan.txt` diubah kepemilikannya menjadi `root` dan izinnya diset ke `rw-------`, maka hanya pengguna root yang dapat mengakses file tersebut. Hal ini menunjukkan bagaimana Linux menerapkan pengendalian hak akses yang ketat guna menjaga keamanan dan privasi data di dalam sistem.

---

## Kesimpulan
1. Setiap file dan direktori di Linux memiliki atribut kepemilikan dan izin akses (permission) yang mengatur siapa yang dapat membaca, menulis, atau mengeksekusi file tersebut. Perintah seperti `ls -l`, `chmod`, dan `chown` digunakan untuk melihat dan mengubah hak akses tersebut.

2. Perintah `chmod` digunakan untuk mengatur tingkat keamanan file. Dengan mengubah mode permission (misalnya dari `rw-r--r--` menjadi `rw-------`), pengguna dapat membatasi akses hanya untuk pemilik dan melindungi file dari pengguna lain.

3. Perintah `chown` memungkinkan perubahan kepemilikan file. Saat kepemilikan diubah (misalnya dari `rrfikaa` ke `root`), hanya pemilik baru yang memiliki hak akses penuh terhadap file, sehingga meningkatkan kontrol dan keamanan sistem.

---

## Tugas & Quiz

---

### Tugas

**Jelaskan fungsi tiap perintah dan arti kolom permission (`rwxr-xr--`)**

| No | Perintah | Fungsi | Keterangan |
| :--- | :--- | :--- | :--- |
| 1  | `pwd` | Menampilkan direktori kerja aktif (current working directory) | Menunjukkan bahwa user berada di `/home/rrfikaa` |
| 2  | `ls -l` | Menampilkan isi direktori secara detail (long listing format) | Menunjukkan nama file, pemilik, grup, ukuran, tanggal, dan hak akses file |
| 3  | `cd /tmp` | Berpindah direktori ke `/tmp` | Pindah ke direktori sementara yang digunakan oleh sistem untuk menyimpan file temporer |
| 4  | `ls -a` | Menampilkan semua file, termasuk file tersembunyi (hidden file) | Menampilkan isi lengkap direktori `/tmp`, termasuk file sistem seperti `.X11-unix` dan `systemd-private-*` |
| 5  | `cat /etc/passwd \| head -n 5` | Menampilkan 5 baris pertama dari file `/etc/passwd` | Menunjukkan daftar akun pengguna sistem Linux beserta informasi UID, GID, direktori home, dan shell |
| 6  | `echo "Hello <Rafika Rahma><250202917>" > percobaan.txt` | Membuat file baru `percobaan.txt` dan menulis teks ke dalamnya | File `percobaan.txt` dibuat dengan isi teks yang dimasukkan setelah perintah echo |
| 7  | `ls -l percobaan.txt` | Menampilkan detail file `percobaan.txt` | Menunjukkan pemilik, grup, ukuran, dan hak akses file |
| 8  | `chmod 600 percobaan.txt` | Mengubah izin akses file agar hanya pemilik yang dapat membaca dan menulis | Permission berubah menjadi `rw-------` |
| 9  | `sudo chown root percobaan.txt` | Mengubah kepemilikan file menjadi milik user `root` | Pemilik file berubah dari `rrfikaa` menjadi `root` |
| 10 | `ls -l percobaan.txt` | Menampilkan kembali detail file setelah perubahan izin dan kepemilikan | File sekarang dimiliki oleh root dengan permission `rw-------` |

| Simbol | Keterangan |
| :--- | :--- |
| `-` | Jenis file (`-` = file biasa, `d` = direktori, `l` = link) |
| `rwx` | Hak akses pemilik (user) : dapat membaca (`r`), menulis (`w`), dan mengeksekusi (`x`) |
| `r-x` | Hak akses grup : dapat membaca (`r`) dan mengeksekusi (`x`), tetapi tidak menulis |
| `r--` | Hak akses lainnya (others) : hanya dapat membaca |

**Analisis peran chmod dan chown dalam keamanan sistem Linux**

| **Aspek** | **`chmod`** | **`chown`** |
| :--- | :--- | :--- | 
| **Fungsi** | Mengatur izin akses (r, w, x) | Mengubah kepemilikan file atau direktori |
| **Tujuan** | Membatasi tindakan pengguna pada file | Menentukan siapa yang berhak atas file |
| **Dampak Keamanan** | Mencegah akses, perubahan, atau eksekusi tanpa izin | Menjaga agar file hanya dikelola oleh pemilik sah |
| **Contoh** | `chmod 600 data.txt` → hanya pemilik bisa akses | `chown root:admin config.txt` hanya root & admin punya hak |
| **Risiko Jika Salah** | File bisa diakses semua user (`chmod 777`) | File penting bisa diambil alih user biasa |
| **Peran Utama** | Mengatur apa yang boleh dilakukan | Mengatur siapa yang memiliki file |

---

### Quiz
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
  
  **Jawaban :**
  memahami cara kerja dan hubungan antara izin (permission) serta kepemilikan (ownership) file atau direktori.
  
- Bagaimana cara Anda mengatasinya?
  
  **Jawaban :**
Dengan latihan praktik dan pengamatan langsung menggunakan perintah di terminal Linux dan mengamati hasilnya secara bertahap. Saya mencoba berbagai kombinasi perintah seperti `chmod`, `chown`, dan `ls -l` untuk melihat perubahan pada permission dan kepemilikan file. Selain itu, saya juga mencatat arti setiap kode izin r (read), w (write), x (execute) dan saya juga berdiskusi dengan teman.
  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
