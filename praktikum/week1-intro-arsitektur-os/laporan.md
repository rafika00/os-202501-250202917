
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
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

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
lsmod | head
dmesg | head
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
     - cs-580648964653-default: Hostname mesin virtual (VM) kamu.
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
    Menampilkan nama pengguna saat ini yang sedang login di shell. Dalam hal ini, kamu adalah pengguna rafikarahma007.

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
   Artinya: Bagian memori fisik dari 0x00000000 sampai 0x00000fff tidak bisa digunakan (reserved).

- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?



---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Sebutkan tiga fungsi utama sistem operasi.
   **Jawaban:**  
3. Jelaskan perbedaan antara kernel mode dan user mode.
   **Jawaban:**  
4. Sebutkan contoh OS dengan arsitektur monolithic dan microkernel. 
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
