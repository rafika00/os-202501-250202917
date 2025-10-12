
# Laporan Praktikum Minggu 1
Topik: Arsitektur Sistem Operasi dan Kernel

---

## Identitas
- **Nama**  : Rafika Rahma
- **NIM**   : 250202917 
- **Kelas** : 1 IKRA

---

## Tujuan
Tujuan praktikum minggu ini yaitu :
> - Mahasiswa mampu menjelaskan peran sistem operasi dalam arsitektur komputer.
> - Mahasiswa mampu mengidentifikasi komponen utama OS (kernel, system call, device driver, file system).
> - Mahasiswa mampu membandingkan model arsitektur OS (monolithic, layered, microkernel).
> - Mahasiswa mampu menggambarkan diagram sederhana arsitektur OS menggunakan alat bantu digital (draw.io / mermaid).

---

## Dasar Teori
Sistem operasi adalah perangkat lunak inti yang mengelola perangkat keras komputer dan menyediakan layanan bagi program aplikasi. Fungsi utamanya meliputi pengelolaan proses, memori, perangkat keras, dan sistem file. Sistem operasi juga menyediakan antarmuka bagi pengguna untuk berinteraksi dengan komputer. Contoh sistem operasi meliputi Windows, Linux, dan macOS.

---

## Langkah Praktikum
1. **Setup Environment**
   - Pastikan Linux (Ubuntu/WSL) sudah terinstal.
   - Pastikan Git sudah dikonfigurasi dengan benar:
     ```bash
     git config --global user.name "Nama Anda"
     git config --global user.email "email@contoh.com"
     ```
2. **Diskusi Konsep**
   - Baca materi pengantar tentang komponen OS.
   - Identifikasi komponen yang ada pada Linux/Windows/Android.

3. **Eksperimen Dasar**
   Jalankan perintah berikut di terminal:
   ```bash
   uname -a
   whoami
   lsmod | head
   dmesg | head
   ```
   Catat dan analisis modul kernel yang tampil.

4. **Membuat Diagram Arsitektur**
   - Buat diagram hubungan antara *User → System Call → Kernel → Hardware.*
   - Gunakan **draw.io** atau **Mermaid**.
   - Simpan hasilnya di:
     ```
     praktikum/week1-intro-arsitektur-os/screenshots/diagram-os.png
     ```
5. **Penulisan Laporan**
   - Tuliskan hasil pengamatan, analisis, dan kesimpulan ke dalam `laporan.md`.
   - Tambahkan screenshot hasil terminal ke folder `screenshots/`.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 1 - Arsitektur Sistem Operasi dan Kernel"
   git push origin main
   ```
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
whoami
lsmod | head
sudo dmesg | head
```
---

## Hasil Eksekusi
![alt text](<screenshots/ss tugas1.png>)
---
![alt text](<screenshots/diagram-os.png>)
---

## Analisis
- Makna hasil percobaan ini yaitu :
  
  **1. uname -a**
     ```bash
     Linux cs-580648964653-default 6.6.105+ #1 SMP PREEMPT_DYNAMIC Sat Sep 27 08:48:45 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
     ```
     - Linux: Sistem operasi berbasis Linux.
     - cs-580648964653-default: Hostname mesin virtual (VM).
     - 6.6.105+: Versi kernel Linux.
     - #1 SMP PREEMPT_DYNAMIC: Build informasi:
       - SMP = Symmetric MultiProcessing, artinya kernel mendukung beberapa CPU/core.
       - PREEMPT_DYNAMIC = Kernel mendukung preemptive multitasking yang bisa dikonfigurasi secara dinamis.
     - Sat Sep 27 08:48:45 UTC 2025: Waktu kernel dibangun.
     - x86_64 x86_64 x86_64: Arsitektur 64-bit (CPU, platform, dan kernel semuanya x86_64).
     - GNU/Linux: Sistem berbasis GNU/Linux.
      
   **2. whoami**
    ```bash
    rafikarahma007
    ```
    Menampilkan nama pengguna saat ini yang sedang login di shell. 

  **3. lsmod | head**
  ```bash
  Module                  Size  Used by
  ip6table_nat           12288  1
  xt_set                 20480  0
  ip_set                 53248  1 xt_set
  ...
  ```
  Perintah lsmod menampilkan modul kernel (driver) yang dimuat saat ini.
  - Module: Nama modul.
  - Size: Ukuran modul dalam memori.
  - Used by: Berapa banyak entitas (modul/fitur) lain yang menggunakan modul ini.
    
    **Contoh:**
    - ip6table_nat: Modul untuk NAT (Network Address Translation) di IPv6.
    - ip_set: Digunakan untuk manajemen kumpulan IP, biasanya dipakai untuk firewall rules.
    - veth: Virtual Ethernet, biasanya digunakan di container networking (Docker, LXC, dsb).

  **4. sudo dmesg | head**
   ```bash
   [    0.000000] Linux version 6.6.105+ (builder@...) ...
   [    0.000000] Command line: BOOT_IMAGE=/syslinux/vmlinuz.A ...
   [    0.000000] BIOS-provided physical RAM map:
   ...
   ```
   Perintah ini menampilkan pesan log kernel dari saat sistem booting. Ini penting untuk debugging hardware/software.
  - [0.000000]: Waktu relatif sejak kernel mulai boot.
  - Linux version 6.6.105+: Versi kernel yang dijalankan.
  - Command line: Parameter boot yang diberikan ke kernel (misalnya opsi keamanan, partisi root, logging, dsb).
  - BIOS-e820: Informasi dari BIOS tentang layout memori fisik di sistem, seperti bagian mana dari RAM yang bisa digunakan.

    **Contoh:**
    ```bash
    [mem 0x0000000000000000-0x0000000000000fff] reserved
    ```
   Bagian memori fisik dari 0x00000000 sampai 0x00000fff tidak bisa digunakan (reserved).

- Hubungan hasil teori dengan fungsi kernel, system call, arsitektur OS :
  
Berdasarkan hasil percobaan menggunakan perintah terminal Linux, terlihat bahwa kernel berfungsi sebagai pengatur utama komunikasi antara perangkat hardware dan software, dan memberikan layanan sistem melalui system call. Arsitektur sistem operasi yang terlihat adalah modular monolithic kernel, di mana modul dapat dimuat secara dinamis, dan ada pemisahan ruang kerja antara user space dan kernel space.

- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?
  
Linux memberikan akses yang lebih transparan dan terbuka terhadap fungsi kernel, sistem call, serta informasi perangkat keras, sedangkan Windows membatasi akses tersebut untuk menjaga stabilitas dan keamanan, dengan lebih mengandalkan antarmuka grafis dan tool khusus.

---

## Kesimpulan
- Sistem operasi Linux bersifat terbuka dan transparan, memungkinkan pengguna untuk melihat informasi detail tentang kernel, modul yang dimuat, arsitektur sistem, dan proses booting secara langsung melalui terminal.
- Kernel Linux berperan penting dalam mengelola sumber daya sistem dan menyediakan layanan inti kepada perangkat lunak melalui system call. Kernel yang digunakan bersifat modular monolithic, di mana modul kernel dapat dimuat dan dilepas secara dinamis sesuai kebutuhan sistem.
- Perintah seperti ```uname, whoami, lsmod, dan dmesg``` menunjukkan bagaimana Linux memberikan akses langsung ke informasi sistem dan aktivitas kernel, yang sangat membantu dalam pemantauan, debugging, dan manajemen sistem.

---
## Tugas

### Perbedaan dan Contoh OS Nyata dari Monolithic Kernel, Microkernel, dan Layered Architecture
1. **Monolithic Kernel**
   Semua komponen kernel seperti driver perangkat, sistem file, manajemen proses, manajemen memori, penjadwalan CPU    dijalankan dalam satu ruang alamat kernel yang sama (kernel space). Kelebihannya adalah performa tinggi karena antar-komponen cepat tanpa overhead dan mudah dikembangkan untuk fitur kompleks. Namun kurang modular, jika satu modul mengalami bug atau carsh, seluruh kernel bisa gagal. Sulit untuk debugging dan pemeliharaan jangka panjang. Contoh OS yang menggunakan Monolithic Kernel yaitu Linux, MS-DOS, dan FreeBSD.

2. **Microkernel**
   Inti sistem operasi (OS) hanya menangani fungsi dasar minimal seperti manajemen memori, penjadwalan proses dan komunikasi antar-proses (IPC), sedangkan komponen lain seperti drive, sistem file, dll., dijalankan sebagai proses terpisah di ruang pengguna (user space). Sangat modular dan aman, kegagalan satu modul tidak memengaruhi kernel utama. Mudah untuk portabilitas dan verifikasi keamanan. Kekurangannya overhead komunikasi tinggi karena IPC melalui pesan yang bisa menurunkan performa, terutama untuk tugas intensif. Contoh OS yang menggunakan Microkenel adalah Minix, QNX, dan L4.

3. **Layered Architecture**
   Kernel dibagi menjadi lapisan-lapisan dengan tanggung jawab yang spesifik dimana setiap lapisan bergantung pada lapisan dibawahnya untuk menyederhanakan pengembangan, pemeliharaan, dan pemahaman sistem. Modular secara vertikal, memudahkan pemahaman dan pengujian per lapisan, lebih terstruktur daripada monolithic. Kekurangannya ketergantungan antar-lapisan bisa menyebabkan bottleneck (lapisan ataas haarus melewati semua lapisan bawah), kurang fleksibel untuk perubahan, dan performa bisa lambat daripada monolithic. Contoh OS yang menggunakan Layered Architecture adalah THE Operating System, Multics, Unix awal, dan Windows NT.

### Analisis Model yang Paling Relevan untuk Sistem Modern
Dari penjelasan diatas dapat disimpulkan bahwa Hybrid Kernel menjadi pilihan paling relevan karena mampu menggabungkan performa tinggi dari monolithic kernel dan modularitas serta keamanan dari microkernel. Meskipun monolithic kernel seperti Linux masih mendominasi, evolusi menuju arsitektur modular dan hybrid menunjukkan bahwa fleksibilitas dan keamanan semakin menjadi kebutuhan utama dalam pengembangan sistem operasi masa kini dan masa depan.

## Quiz
1. Sebutkan tiga fungsi utama sistem operasi.
   
   **Jawaban:**
   - Manajemen Sumber Daya : Mengatur CPU, memori, disk, dan I/O agar digunakan secara efisien
   - Manajemen Proses : Menjalankan dan mengatur banyak proses secara simultan
   - Antarmuka & Sistem File : Memberikan UI/CLI serta mengelola file dan direktori
   
2. Jelaskan perbedaan antara kernel mode dan user mode.
   
   **Jawaban:**
   Dalam sistem operasi, kernel mode memungkinkan sistem berjalan dengan akses penuh terhadap semua sumber daya komputer, seperti memori, perangkat keras, dan CPU digunakan oleh kernel dan driver. kesalahan di kernel mode dapat menyebabkan seluruh sistem crash. Sementara itu, user mode digunakan oleh aplikasi pengguna dengan akses terbatas. Aplikasi tidak bisa langsung mengakses perangkat keras, dan harus menggunakan system call untuk berkomunikasi dengan kernel. Pemisahan ini penting untuk menjaga keamanan dan stabilitas sistem.
   
3. Sebutkan contoh OS dengan arsitektur monolithic dan microkernel.
   
   **Jawaban:**
   - Monolithic Kernel
     - Linux (Ubuntu, Fedora, Debian, dll.)
     - MS-DOS
     - Unix klasik (seperti BSD awal)
     - Solaris (versi lama)
     - MacOS klasik (pra-Mac OS X)
    
   - Microkernel
     - Minix (sering dipakai untuk pendidikan)
     - QNX (digunakan dalam sistem tertanam/embedded seperti mobil)
     - L4 (berbagai varian, digunakan di riset dan sistem ringan)
     - GNU Hurd (proyek dari GNU dengan microkernel Mach)
     - macOS (modern) dan iOS → berbasis XNU kernel (hybrid dengan elemen microkernel dari Mach)
     
---

## Refleksi Diri
Tuliskan secara singkat:
- Bagian yang paling menantang bagi saya di minggu ini yaitu belajar mengoperasikan dan mengumpulkan tugas di github karena bagi saya ini adalah hal baru.
- Cara mengatasi hal tersebut saya berusaha mencari tutorial-tutorial di internet misalnya YouTube, Google dll., dan saya juga berdikusi dengan teman.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
