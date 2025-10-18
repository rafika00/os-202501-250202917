
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

2. Eksperimen 2
   ![alt text](<screenshots/strace_io.png>)

3. Eksperimen 3
   ![alt text](<screenshots/dmesg.png>)

4. Diagram alur system call
   ![alt text](<screenshots/syscall-diagram.png>)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Tugas


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
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
