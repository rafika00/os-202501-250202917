
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Anggota kelompok
1. Faik Setyawan (250202936)
2. Evelin Natalie (250202916)
3. Nadya Pramudita (250202956)
4. Rafika Rahma (2502029
5. Novia Safitri (2502029

---

## 1. Latar Belakang

Perkembangan teknologi komputer yang semakin pesat menuntut sistem operasi untuk mampu mengelola sumber daya secara efektif dan efisien. Sistem operasi memiliki peran penting sebagai penghubung antara perangkat keras (hardware) dan perangkat lunak (software), serta bertanggung jawab dalam mengatur pemrosesan, memori, dan sumber daya lainnya agar dapat digunakan secara optimal oleh berbagai proses yang berjalan secara bersamaan. Oleh karena itu, diperlukan mekanisme pengelolaan yang baik agar kinerja sistem tetap stabil dan responsif.

Salah satu aspek penting dalam sistem operasi adalah **CPU Scheduling**, yaitu mekanisme penjadwalan proses yang menentukan urutan eksekusi proses pada CPU. Salah satu algoritma CPU scheduling yang paling sederhana adalah **First Come First Served (FCFS)**. Algoritma ini mengeksekusi proses berdasarkan urutan kedatangan tanpa memperhatikan lama waktu eksekusi. Meskipun mudah diimplementasikan, FCFS memiliki kelemahan seperti kemungkinan terjadinya *waiting time* yang panjang dan *convoy effect*, sehingga dapat memengaruhi kinerja sistem secara keseluruhan.

Selain pengelolaan CPU, sistem operasi juga harus mengatur penggunaan memori secara efisien. Dalam manajemen memori virtual, diperlukan algoritma **Page Replacement** untuk menentukan halaman mana yang harus diganti ketika memori utama penuh. Salah satu algoritma yang umum digunakan adalah **First In First Out (FIFO)**. Algoritma FIFO menggantikan halaman yang pertama kali masuk ke memori tanpa mempertimbangkan frekuensi atau waktu penggunaan halaman tersebut. Walaupun sederhana, FIFO dapat menyebabkan terjadinya anomali seperti *Belady’s Anomaly* yang berdampak pada peningkatan *page fault*.

Di sisi lain, penggunaan sumber daya yang bersamaan oleh banyak proses berpotensi menimbulkan masalah **deadlock**, yaitu kondisi di mana dua atau lebih proses saling menunggu sumber daya yang sedang digunakan oleh proses lain sehingga tidak ada satu pun proses yang dapat berjalan. Untuk mengatasi hal tersebut, sistem operasi memerlukan mekanisme **Deadlock Detection** guna mendeteksi adanya deadlock dan mengambil tindakan pemulihan. Dengan adanya deteksi deadlock, sistem dapat menghindari kondisi macet yang dapat menurunkan kinerja bahkan menyebabkan sistem berhenti beroperasi.

Berdasarkan uraian tersebut, pemahaman mengenai **CPU Scheduling dengan algoritma FCFS, Page Replacement FIFO, serta Deadlock Detection** menjadi sangat penting dalam mempelajari konsep sistem operasi. Ketiga konsep ini merupakan dasar dalam pengelolaan proses, memori, dan sumber daya, sehingga mampu membantu dalam merancang sistem yang lebih efisien, stabil, dan andal.

---

## 2. Tujuan
Setelah menyelesaikan proyek ini, mahasiswa mampu:
1. Bekerja kolaboratif dalam tim dengan pembagian peran yang jelas.
2. Mengintegrasikan beberapa konsep sistem operasi dalam satu aplikasi sederhana.
3. Mengelola proyek menggunakan Git (branch/PR/commit yang rapi).
4. Menyusun dokumentasi dan laporan proyek yang sistematis.
5. Melakukan presentasi dan demo hasil proyek.

---
Berikut **bagian Arsitektur Aplikasi** yang menjelaskan **CPU Scheduling (FCFS), Page Replacement (FIFO), dan Deadlock Detection**, disusun dengan gaya **laporan/makalah Sistem Operasi** dan saling terintegrasi:

---

## 3. Arsitektur Aplikasi

Arsitektur aplikasi dirancang untuk menggambarkan bagaimana sistem mengelola proses, memori, dan sumber daya secara terstruktur dan terkoordinasi. Aplikasi ini mensimulasikan mekanisme kerja sistem operasi dengan fokus pada **CPU Scheduling menggunakan algoritma First Come First Served (FCFS)**, **Page Replacement menggunakan algoritma First In First Out (FIFO)**, serta **Deadlock Detection**. Setiap modul saling terhubung dan bekerja secara berurutan untuk memastikan sistem berjalan secara efisien dan terhindar dari kondisi konflik sumber daya.

### 1. Arsitektur CPU Scheduling (FCFS)

Modul CPU Scheduling bertugas mengatur eksekusi proses yang masuk ke dalam sistem. Proses yang datang akan ditempatkan ke dalam **Ready Queue** berdasarkan urutan kedatangan. Algoritma FCFS mengeksekusi proses pertama yang masuk ke antrian hingga selesai tanpa preemption. Setelah proses selesai, CPU akan mengambil proses berikutnya dari antrian. Arsitektur ini menekankan kesederhanaan alur kerja dan kemudahan implementasi, meskipun memiliki keterbatasan dalam hal waktu tunggu dan responsivitas sistem.

### 2. Arsitektur Page Replacement (FIFO)

Modul manajemen memori menggunakan algoritma FIFO untuk mengatur penggantian halaman dalam memori utama. Setiap halaman yang masuk ke memori dicatat berdasarkan urutan waktu kedatangannya. Ketika memori penuh dan terjadi *page fault*, sistem akan mengganti halaman yang paling lama berada di memori (halaman pertama yang masuk). Arsitektur ini memanfaatkan struktur data antrian untuk menyimpan urutan halaman, sehingga proses penggantian halaman dapat dilakukan dengan cepat dan sederhana.

### 3. Arsitektur Deadlock Detection

Modul Deadlock Detection berfungsi untuk memantau penggunaan sumber daya oleh setiap proses yang sedang berjalan. Sistem menyimpan informasi dalam bentuk **Resource Allocation Graph** atau tabel alokasi sumber daya yang mencatat hubungan antara proses dan sumber daya. Secara berkala, modul ini melakukan pemeriksaan siklus (cycle detection). Jika terdeteksi adanya siklus, maka sistem menyimpulkan bahwa terjadi deadlock. Selanjutnya, sistem dapat melakukan tindakan pemulihan seperti menghentikan proses tertentu atau membebaskan sumber daya agar sistem dapat kembali berjalan normal.

### 4. Integrasi Antar Modul

Ketiga modul dalam arsitektur aplikasi ini saling berinteraksi:

* Modul **CPU Scheduling FCFS** menentukan urutan eksekusi proses.
* Modul **Page Replacement FIFO** mendukung kebutuhan memori setiap proses yang sedang dieksekusi.
* Modul **Deadlock Detection** memastikan tidak terjadi konflik sumber daya antar proses.

Integrasi ini memungkinkan sistem untuk menjalankan simulasi sistem operasi secara menyeluruh, mulai dari penjadwalan proses, pengelolaan memori, hingga pengendalian konflik sumber daya. Dengan arsitektur seperti ini, aplikasi mampu memberikan gambaran nyata tentang cara kerja sistem operasi dalam mengelola sumber daya secara efektif.



## 4. Alur Data (Data Flow)

Berikut alur data dari arsitektur aplikasi secara keseluruhan:

1. **Input Data**

   * Data proses dimasukkan ke sistem (arrival time, burst time).
   * Data referensi halaman dimasukkan untuk simulasi memori.
   * Data alokasi dan permintaan sumber daya dimasukkan untuk deteksi deadlock.

2. **Proses CPU Scheduling**

   * Data proses masuk ke Ready Queue.
   * CPU mengeksekusi proses berdasarkan urutan FCFS.
   * Hasil eksekusi dikirim ke modul laporan.

3. **Manajemen Memori (Page Replacement FIFO)**

   * Proses yang berjalan mengakses halaman memori.
   * Jika terjadi *page fault*, data dikirim ke modul FIFO.
   * Modul FIFO menentukan halaman yang diganti.
   * Status memori diperbarui dan dikirim kembali ke sistem.

4. **Deadlock Detection**

   * Sistem mencatat penggunaan dan permintaan sumber daya.
   * Modul Deadlock Detection menganalisis matriks alokasi.
   * Jika deadlock terdeteksi, status dikirim ke sistem untuk ditangani.

5. **Output**

   * Hasil CPU Scheduling (urutan eksekusi, waiting time).
   * Jumlah page fault dan kondisi frame memori.
   * Status deadlock (aman atau terjadi deadlock).

## 7.Tugas setiap Anggota

Baik, berikut versi **lebih formal dengan penjelasan yang rinci**, cocok untuk **laporan praktikum, laporan proyek kelompok, atau laporan akademik**:

---

## Pembagian Peran dan Kontribusi Setiap Anggota

Dalam rangka pelaksanaan tugas kelompok ini, dilakukan pembagian peran dan tanggung jawab kepada setiap anggota agar proses pengerjaan berjalan secara efektif, terstruktur, dan sesuai dengan tujuan yang telah ditetapkan. Pembagian tugas ini juga bertujuan untuk meningkatkan kerja sama tim serta memastikan seluruh bagian tugas dapat diselesaikan dengan baik. Adapun pembagian peran dan kontribusi masing-masing anggota adalah sebagai berikut:

### 1. Anggota 1 – Penanggung Jawab Modul 1

Anggota 1 bertanggung jawab untuk mengerjakan **Modul 1** sesuai dengan pedoman dan instruksi yang telah diberikan. Tugas ini mencakup pemahaman materi, pengerjaan soal atau studi kasus, serta penyusunan hasil kerja secara sistematis dan terstruktur. Hasil dari Modul 1 kemudian disiapkan untuk dikompilasi ke dalam laporan kelompok.

### 2. Anggota 2 – Penanggung Jawab Modul 2

Anggota 2 bertugas mengerjakan **Modul 2** dengan memperhatikan ketentuan dan standar yang telah ditetapkan. Selain menyelesaikan isi modul, anggota ini juga melakukan pengecekan terhadap kelengkapan dan kebenaran hasil pekerjaan sebelum dikumpulkan ke dalam repository proyek kelompok.

### 3. Anggota 3 – Penanggung Jawab Modul 3

Anggota 3 memiliki tanggung jawab untuk mengerjakan **Modul 3** secara menyeluruh dan sesuai dengan panduan yang tersedia. Anggota ini juga memastikan bahwa hasil pengerjaan telah disusun dengan format yang konsisten agar mudah dipahami dan dapat digabungkan dengan modul-modul lainnya dalam laporan akhir.

### 4. Anggota 4 – Penanggung Jawab Dokumentasi (README)

Anggota 4 bertanggung jawab dalam penyusunan dan pengelolaan dokumentasi proyek pada file **README.md**. Tugas ini meliputi penulisan deskripsi proyek, tujuan pengerjaan, serta ringkasan isi dari setiap modul. Dokumentasi disusun secara jelas dan sistematis agar dapat memberikan gambaran menyeluruh mengenai proyek yang dikerjakan.

### 5. Ketua Kelompok – Koordinator dan Pengelola Repository GitHub

Ketua kelompok berperan sebagai koordinator utama dan pengelola repository GitHub. Tugas ketua meliputi pembuatan **branch** untuk pengumpulan tugas setiap anggota, pengelolaan alur kerja version control, serta melakukan pemeriksaan dan penggabungan (merge) branch ke branch utama (main/master). Selain itu, ketua kelompok juga bertanggung jawab memastikan seluruh kontribusi anggota terdokumentasi dengan baik dan repository berada dalam kondisi rapi serta siap untuk dikumpulkan.









---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

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
1. [Pertanyaan 1]  
   **Jawaban:**  
2. [Pertanyaan 2]  
   **Jawaban:**  
3. [Pertanyaan 3]  
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
