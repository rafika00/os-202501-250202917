
# Laporan Praktikum Minggu 2
Topik: Struktur System Call dan Fungsi Kernel

---

## Identitas
- **Nama**  : Rafika Rahma
- **NIM**   : 250202917  
- **Kelas** : 1 IKRA

---

## Tujuan
Tujuan praktikum minggu ini, mahasiswa mampu :
1. Menjelaskan konsep dan fungsi system call dalam sistem operasi.
2. Mengidentifikasi jenis-jenis system call dan fungsinya.
3. Mengamati alur perpindahan mode user ke kernel saat system call terjadi.
4. Menggunakan perintah Linux untuk menampilkan dan menganalisis system call.

---

## Dasar Teori
System call adalah antarmuka antara program aplikasi dan sistem operasi yang memungkinkan program meminta layanan dari kernel. Digunakan untuk mengakses sumber daya sistem seperti file, memori, proses, dan perangkat keras secara aman dan terkendali. System call melibatkan perpindahan dari user mode ke kernel mode, karena hanya kernel yang memiliki hak penuh terhadap sistem. Terdiri dari beberapa jenis, seperti: manajemen proses, manajemen file, manajemen memori, dan manajemen perangkat.

---

## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).
   - Pastikan perintah `strace` dan `man` sudah terinstal.
   - Konfigurasikan Git (jika belum dilakukan di minggu sebelumnya).

2. **Eksperimen 1 – Analisis System Call**
   Jalankan perintah berikut:
   ```bash
   strace ls
   ```
   > Catat 5–10 system call pertama yang muncul dan jelaskan fungsinya.  
   Simpan hasil analisis ke `results/syscall_ls.txt`.

3. **Eksperimen 2 – Menelusuri System Call File I/O**
   Jalankan:
   ```bash
   strace -e trace=open,read,write,close cat /etc/passwd
   ```
   > Analisis bagaimana file dibuka, dibaca, dan ditutup oleh kernel.

4. **Eksperimen 3 – Mode User vs Kernel**
   Jalankan:
   ```bash
   dmesg | tail -n 10
   ```
   > Amati log kernel yang muncul. Apa bedanya output ini dengan output dari program biasa?

5. **Diagram Alur System Call**
   - Buat diagram yang menggambarkan alur eksekusi system call dari program user hingga kernel dan kembali lagi ke user mode.
   - Gunakan draw.io / mermaid.
   - Simpan di:
     ```
     praktikum/week2-syscall-structure/screenshots/syscall-diagram.png
     ```

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 2 - Struktur System Call dan Kernel Interaction"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
strace ls
strace -e trace=open,read,write,close cat /etc/passwd
dmesg | tail -n 10

```

---

## Hasil Eksekusi
1. Eksperimen 1
   ![alt text](<screenshots/syscall_ls.png>)
   ![alt text](<screenshots/syscall_ls1.png>)
   ![alt text](<screenshots/syscall_ls2.png>)
*Tabel Observasi perintah `strace ls`*

| No | Nama System Call | Fungsi Utama | Keterangan |
| :--- | :--- | :--- | :--- |
| 1. | execve () | Menjalankan program baru | Mengganti proses saat ini dengan program lain. Misalnya, saat mengetik `cat /etc/passwd`, shell memanggil `execve()` untuk mengeksekusi program `cat` | 
| 2. | mmap () | Memetakan file atau memori ke ruang alamat proses | Digunakan untuk memuat library, file, atau mengalokasikan memori besar secara efisien ke alamat virtual proses |
| 3. | access () | Mengecek hak akses file | Memeriksa apakah proses memiliki izin untuk membaca, menulis, atau mengeksekusi file tertentu |
| 4. | openat () | Membuka file atau direktori | Versi lebih modern dari `open()`. Digunakan untuk membuka file `(/etc/passwd, library, dsb.)` dengan dukungan relative path terhadap direktori tertentu |
| 5. | fstat () | Mendapatkan informasi tentang file terbuka | Mengambil metadata file seperti ukuran, tipe, waktu modifikasi, dan hak akses dari file yang sudah dibuka (melalui file descriptor) |
| 6. | close () | Menutup file descriptor | Melepaskan koneksi ke file atau resource yang sudah tidak digunakan, agar tidak membebani sistem | 
| 7. | read () | Membaca data dari file | Membaca isi file dari disk ke buffer memori program, misalnya `cat` membaca isi `/etc/passwd dengan read()` |
| 8. | mprotect () | Mengatur hak akses pada area memori | Melindungi atau mengubah izin `(read/write/execute)` pada segmen memori tertentu, biasanya untuk keamanan eksekusi |
| 9. | prlimit64 () | Mengatur atau memeriksa batas sumber daya proses | Mengecek atau menetapkan batas seperti jumlah file terbuka, ukuran memori maksimum, CPU time, dll. |
| 10. | exit_group () | Mengakhiri proses secara bersih | Menghentikan semua thread dalam proses dan mengembalikan status keluar ke sistem operasi. Menandakan program selesai dijalankan tanpa error |


3. Eksperimen 2
   ![alt text](<screenshots/strace_io.png>)
*Tabel Observasi perintah `strace -e trace=open,read,write,close cat /etc/passwd`*

| No | Nama System Call | Fungsi Utama | Keterangan |
| :--- | :--- | :--- | :--- |
| 1. | `open("/etc/passwd", O_RDONLY)` *(tidak terlihat di potongan)* | Membuka file `/etc/passwd` untuk dibaca | Berisi daftar akun pengguna sistem |
| 2. | `read(3, "root:x:0:0:root:/root:/bin/bash\n...", 131072)` | Membaca isi file `/etc/passwd` | Data dibaca ke buffer, total 1428 byte |
| 3. | `write(1, "root:x:0:0:root:/root:/bin/bash\n...", 1428)` | Menulis isi buffer ke stdout (layar terminal) | Output ini yang akan terlihat di layar |
| 4. | `read(3, "", 131072) = 0` | Mencoba membaca lagi, tapi file sudah habis (EOF) | Mengembalikan nilai 0 → tanda akhir file | 
| 5. | `close(3)` | Menutup file `/etc/passwd` | Melepaskan file descriptor 3 | 
| 6. | `close(1) dan close(2)` | Menutup STDOUT dan STDERR | Terjadi saat proses `cat` akan keluar |
| 7. | `+++ exited with 0 +++` | Keluar dengan status sukses | Program `cat` selesai tanpa error |


5. Eksperimen 3
   ![alt text](<screenshots/dmesg.png>)
*Tabel Observasi perintah `dmesg | tail -n 10`*

| No | Nama System Call | Fungsi Utama | Keterangan |
| :--- | :--- | :--- | :--- |
| 1. | systemd-journald[66] | Mengelola dan menyimpan log sistem di Linux | Bagian dari systemd yang bertugas mencatat semua pesan log dari kernel, service, dan aplikasi ke dalam journal (`/var/log/journal/`). Pesan “Time jumped backwards” muncul saat sistem mendeteksi waktu mundur (biasanya karena sinkronisasi waktu oleh NTP atau host) |
| 2. | hv_balloon | Mengatur memori dinamis pada mesin virtual Hyper-V | Driver kernel Hyper-V yang menambah atau mengurangi memori virtual mesin Linux sesuai kebutuhan dan konfigurasi host (fitur Dynamic Memory). Pesan seperti “Max. dynamic memory size: 1758 MB” berarti guest Linux dapat menggunakan memori hingga 1758 MB secara dinamis. |
| 3. | mini_init (174) | Proses kecil yang melakukan inisialisasi sistem ringan dan perintah tertentu seperti drop_caches | `mini_ini`t bukan bagian utama Linux, melainkan skrip atau binary kecil yang menggantikan `init` di sistem ringan (misalnya di WSL atau container). Pesan “drop_caches: 1” berarti sistem menjalankan perintah untuk membersihkan page cache (membebaskan memori sementara tanpa memengaruhi data) | 

---

## Analisis
#### Jelaskan makna hasil percobaan.
***Eksperimen 1 (`strace ls`)*** menunjukkan bahwa setiap perintah sederhana seperti ls melakukan banyak system call ke kernel, seperti `execve()`, `openat()`, `read()`, `mmap()`, dan `exit_group()`. menggambarkan bahwa program user space tidak bisa langsung mengakses hardware, tetapi harus menggunakan system call sebagai jalur resmi menuju kernel.
System call yang muncul mencerminkan tiga fungsi utama OS:

- Manajemen Proses : `execve()`, `exit_group()`
- Manajemen File / I/O : `openat()`, `read()`, `fstat()`, `close()`
- Manajemen Memori :   `mmap()`, `mprotect()`

***Eksperimen 2 (`strace -e trace=open,read,write,close cat /etc/passwd`)*** menunjukkan siklus operasi I/O yang utuh : buka file → baca → tulis → tutup. Saat cat dijalankan, kernel membuka file `/etc/passwd`, membaca isinya ke buffer, menulis ke layar, lalu menutup file descriptor. Urutan ini memperlihatkan bahwa kernel menyediakan abstraksi file descriptor untuk semua resource, mendukung prinsip “Everything is a file” di Linux.

***Eksperimen 3 (`dmesg | tail -n 10`)*** menampilkan aktivitas log kernel seperti `systemd-journald`, `hv_balloon`, dan `mini_ini`t. Pesan-pesan seperti “Time jumped backwards” menandakan sinkronisasi waktu antara sistem tamu (guest) dan host Hyper-V. `hv_balloon` memperlihatkan pengelolaan memori dinamis di lingkungan virtual. `mini_init` menunjukkan proses ringan untuk inisialisasi dan pembersihan cache, menegaskan fungsi kernel dalam efisiensi penggunaan memori.

#### Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS). 
- Kernel sebagai Inti OS : 
Ketiga eksperimen menunjukkan bahwa kernel adalah penghubung antara user space dan hardware. Semua aktivitas program harus melalui kernel menggunakan system call interface.

- System Call :
Merupakan pintu masuk resmi bagi program untuk meminta layanan OS.
Misalnya, `read()` dan `write()` digunakan untuk I/O, sedangkan `execve()` untuk membuat proses baru. Kernel menyediakan layanan seperti manajemen proses, file, memori, dan perangkat I/O.

- Arsitektur Kernel (Linux) :
Linux menggunakan kernel monolitik, di mana semua komponen utama (scheduler, file system, network stack, driver, dll.) berjalan di ruang kernel.
Hasil eksperimen seperti `mmap`, `fstat`, dan `hv_balloon` menunjukkan fungsi yang diimplementasikan langsung di kernel monolitik ini.

- Konsep Virtualisasi:
Modul seperti `hv_balloon` menegaskan bahwa Linux dapat berjalan sebagai guest OS di bawah Hyper-V host.
Kernel bekerja sama dengan hypervisor untuk mengatur alokasi sumber daya seperti memori dinamis dan sinkronisasi waktu.

#### Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

| Aspek | Linux | Windows |
| :--- | :--- | :--- |
| System Call Interface | Terbuka dan terdokumentasi (`open`, `read`, `write`, `execve`, dll). | Tersembunyi di balik Windows API (misalnya `CreateFile`, `ReadFile`, dll) |
| Manajemen File | Semua resource diperlakukan sebagai file (Everything is a file) | Menggunakan Handle untuk mengakses objek kernel (file, socket, dll) |
| Logging Sistem | Menggunakan `dmesg`, `journalctl`, dan `/var/log/` | Menggunakan Event Viewer dan System Logs |
| Manajemen Memori Virtual | Melalui system call seperti `mmap`, `mprotect`, `brk` | Melalui API seperti VirtualAlloc dan MapViewOfFile |
| Virtualisasi / Hypervisor Integration | Driver `hv_balloon` dan `hv_utils` untuk integrasi dengan Hyper-V | Native Hyper-V di sisi host; guest diatur oleh Integration Services |


---

## Kesimpulan
Ketiga eksperimen membuktikan bahwa setiap perintah yang dijalankan di Linux sekecil apapun akan berinteraksi dengan kernel melalui serangkaian system call.
Kernel berperan penting dalam menyediakan layanan dasar sistem operasi (I/O, memori, proses), menjaga keamanan dan isolasi antarproses dan mengatur komunikasi antara perangkat keras dan perangkat lunak. Hasil dmesg memperlihatkan aktivitas kernel di level rendah, termasuk sinkronisasi waktu dan pengelolaan memori virtual dalam lingkungan virtualisasi. Dibanding Windows, Linux lebih transparan dan terbuka dalam memperlihatkan mekanisme internal kernel dan system call-nya.

---

## Tugas
1. Diagram alur system call dari aplikasi → kernel → hardware → kembali ke aplikasi.
   ![alt text](<screenshots/syscall-diagram.png>)

### Mengapa system call penting untuk keamanan OS?
System call memiliki peran penting dalam menjaga keamanan sistem operasi karena berfungsi sebagai penghubung aman antara program pengguna dan kernel. Dalam sistem operasi yang menggunakan mode ganda, hanya kernel yang dapat menjalankan instruksi istimewa seperti pengendalian I/O, manajemen timer, dan interrupt. Program pengguna tidak memiliki akses langsung ke perangkat keras, sehingga harus menggunakan system call untuk meminta layanan dari sistem operasi. Melalui mekanisme ini, setiap permintaan pengguna dijalankan di bawah kendali kernel, yang memastikan bahwa operasi dilakukan secara aman dan terkendali. Selain itu, kernel memeriksa parameter dari system call untuk mencegah akses ilegal terhadap memori atau instruksi berbahaya. Dengan demikian, system call membantu melindungi sistem operasi dari kesalahan pengguna maupun potensi serangan yang dapat mengancam kestabilan dan keamanan sistem.

### Bagaimana OS memastikan transisi user–kernel berjalan aman?
Sistem operasi memastikan transisi dari user mode ke kernel mode berjalan aman melalui dukungan perangkat keras dan mekanisme pengendalian yang ketat. Proses ini diawali dengan adanya mode bit pada CPU yang menandakan apakah sistem sedang berjalan di mode pengguna atau mode kernel. Saat terjadi trap, interrupt, atau system call, perangkat keras secara otomatis mengubah mode bit menjadi kernel mode sehingga sistem operasi mendapatkan kendali penuh. Semua instruksi yang bersifat penting, seperti pengendalian I/O, pengaturan timer, dan manajemen interrupt, dikategorikan sebagai instruksi istimewa (privileged instructions) yang hanya dapat dijalankan di kernel mode. Jika program pengguna mencoba mengeksekusi instruksi tersebut di user mode, perangkat keras akan menolaknya dan mengirim trap ke sistem operasi. Selama proses transisi ini, kendali CPU dialihkan melalui interrupt vector menuju rutin layanan di kernel yang telah ditentukan, memastikan bahwa hanya kode yang terpercaya dapat dijalankan. Setelah itu, kernel akan memeriksa parameter dari permintaan pengguna untuk memastikan keamanan operasi yang diminta. Dengan mekanisme ini, sistem operasi dapat menjaga agar perpindahan antara user mode dan kernel mode berlangsung aman, mencegah pelanggaran akses, dan melindungi sistem dari kerusakan atau penyalahgunaan.

### Sebutkan contoh system call yang sering digunakan di Linux.
- System call untuk I/O (Input/Output) control
  
Misalnya read(), write(), dan open() yang digunakan untuk membaca, menulis, atau membuka file maupun perangkat.
- System call untuk manajemen timer
  
Misalnya alarm() atau setitimer() yang digunakan untuk mengatur waktu atau timer dalam sistem.
- System call untuk manajemen interrupt dan sistem
  
Misalnya signal() atau kill() untuk mengirim sinyal antarproses.
- System call untuk manajemen proses

  Misalnya fork(), exec(), dan exit() yang digunakan untuk membuat, menjalankan, atau menghentikan proses.
- System call untuk manajemen memori

Misalnya brk() atau mmap() untuk mengatur alokasi memori proses.




## Quiz
1. Apa fungsi utama system call dalam sistem operasi?
   
   **Jawaban:**

System call adalah mekanisme yang digunakan program untuk meminta layanan dari sistem operasi, seperti membaca file, membuat proses, atau mengakses perangkat. Fungsi utamanya adalah menjadi jembatan antara aplikasi dan kernel, agar program bisa mengakses sumber daya sistem secara aman dan terkendali.
   
2. Sebutkan 4 kategori system call yang umum digunakan.
   
   **Jawaban:**
   
- Manajemen Proses (Process Control)
Contoh: fork(), exec(), exit(), wait()
- Manajemen File (File Management)
Contoh: open(), read(), write(), close()
- Manajemen Perangkat (Device Management)
Contoh: ioctl(), read(), write()
- Manajemen Memori (Memory Management)
Contoh: mmap(), brk()

3. Mengapa system call tidak bisa dipanggil langsung oleh user program?
   
   **Jawaban:**
   
System call tidak bisa dipanggil langsung oleh user program karena program berjalan dalam user mode, yang tidak memiliki akses langsung ke sumber daya sistem. Untuk alasan keamanan dan stabilitas, hanya kernel mode yang boleh mengakses perangkat keras, memori, dan operasi penting lainnya. Oleh karena itu, program harus menggunakan system call agar sistem operasi bisa mengatur akses tersebut dengan aman.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
  
  **jawab** : memahami hubungan antara perintah yang dijalankan di user space dengan aktivitas yang terjadi di kernel space.
- Bagaimana cara Anda mengatasinya?

  **jawab** : mempelajari konsep system call dan menggunakan strace untuk melihat bagaimana perintah di user space berinteraksi dengan kernel dan berdiskusi dengan teman. 

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
