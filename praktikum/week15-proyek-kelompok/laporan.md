
# Laporan Praktikum Minggu [X]
Topik:  Proyek Kelompok – Mini Simulasi Sistem Operasi (Scheduling + Memory + Container)

---

## Anggota kelompok
1. Faik Setyawan (250202936)
2. Evelin Natalie (250202916)
3. Nadya Pramudita (250202956)
4. Rafika Rahma (250202917)
5. Novia Safitri (250202923)

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

Alur data dalam aplikasi berjalan secara terstruktur sebagai berikut:

### a. Input Data

* Data proses untuk CPU Scheduling dimasukkan melalui kode atau input pengguna
* Data antrian FIFO ditulis dan dibaca dari file `fifo.txt`
* Data resource deadlock didefinisikan dalam struktur data (dictionary)


### b. Proses

1. Pengguna memilih modul melalui menu CLI.
2. `main.py` memanggil modul yang sesuai.
3. Modul memproses data berdasarkan algoritma masing-masing:

   * FCFS → menghitung WT dan TAT
   * FIFO → menambah/menghapus data dari file
   * Deadlock → mendeteksi circular wait
4. Hasil pemrosesan dikirim kembali ke `main.py`.


### c. Output

* Hasil simulasi ditampilkan langsung di terminal:

  * Tabel CPU Scheduling
  * Status antrian FIFO
  * Informasi deadlock (terdeteksi atau tidak)


### 3. Integrasi dengan Docker

Seluruh arsitektur aplikasi dijalankan di dalam **Docker container**, sehingga:

* Alur data dan modul berjalan dalam lingkungan terisolasi
* Tidak bergantung pada sistem operasi host
* Aplikasi dapat dijalankan secara konsisten di berbagai perangkat

--- 

## 5. Demo Langsung Menjalankan Aplikasi Menggunakan Docker

Demo aplikasi dilakukan dengan menjalankan seluruh program simulasi sistem operasi di dalam **container Docker**. Aplikasi ditulis menggunakan bahasa **Python** dan terdiri dari beberapa modul, yaitu **CPU Scheduling (FCFS)**, **Page Replacement FIFO**, dan **Deadlock Detection**, yang dapat dijalankan melalui **menu/CLI** pada file utama (`main.py`).

### 1. Proses Build Docker Image

Berdasarkan file `Dockerfile` yang telah dibuat, image Docker dibangun menggunakan base image Python. Dockerfile berfungsi untuk:

* Menentukan environment Python yang digunakan
* Menyalin seluruh source code ke dalam container
* Menjalankan aplikasi utama secara otomatis

Perintah build yang digunakan:

```bash
docker build -t week15-proyek-kelompok .
```

Perintah ini akan menghasilkan image bernama `week15-proyek-kelompok .` yang berisi seluruh kode simulasi beserta dependensinya.


### 2. Menjalankan Container Docker

Setelah image berhasil dibuat, container dijalankan secara interaktif agar pengguna dapat memilih menu simulasi:

```bash
docker run -it week15-proyek-kelompok 
```

Mode `-it` digunakan agar input dari keyboard dapat diterima oleh aplikasi CLI di dalam container.


### 3. Demo CPU Scheduling – FCFS

Saat memilih menu **CPU Scheduling FCFS**, program akan:

* Membaca dataset proses (arrival time dan burst time)
* Mengurutkan proses berdasarkan waktu kedatangan
* Mengeksekusi proses satu per satu tanpa preemption
* Menghitung **Waiting Time (WT)** dan **Turnaround Time (TAT)**

Hasil ditampilkan dalam bentuk tabel, sesuai dengan logika pada kode FCFS yang menghitung waktu tunggu berdasarkan akumulasi burst time proses sebelumnya. Demo ini menunjukkan secara nyata efek **convoy effect**, terutama ketika proses dengan burst time besar berada di awal antrian.

---

### 4. Demo Page Replacement FIFO (Berbasis File)

Pada modul **Page Replacement FIFO**, simulasi dijalankan menggunakan file `fifo.txt` sebagai media antrian, sesuai dengan coding yang telah dibuat.

Alur kerja program:

* Pasien/proses ditambahkan ke file `fifo.txt` (enqueue)
* Pemanggilan dilakukan dengan membaca baris pertama file (dequeue)
* Setelah dipanggil, baris pertama dihapus dari file
* Jika file kosong, program menampilkan pesan bahwa antrian kosong

Pendekatan ini menyerupai **mekanisme queue pada sistem operasi**, di mana struktur FIFO diterapkan secara nyata menggunakan file sebagai penyimpanan data.

### 5. Demo Deadlock Detection

Modul **Deadlock Detection** mensimulasikan kondisi deadlock menggunakan konsep **circular wait**:

* Setiap proses (mobil) memegang satu resource (jalan)
* Setiap proses menunggu resource lain yang sedang dipegang proses berbeda
* Program mendeteksi adanya siklus dalam relasi menunggu

Berdasarkan struktur data yang digunakan pada kode, sistem berhasil mengidentifikasi bahwa seluruh kondisi deadlock terpenuhi, sehingga disimpulkan bahwa terjadi deadlock.


---


## 6.Analisis dan Hasil uji
### 6.1 cpu_scheduling
![WhatsApp Image 2026-01-25 at 20 37 39](https://github.com/user-attachments/assets/e9813c31-0565-4aa2-940e-67e17b3842a4)

tabel hasil simulasi 
| Proses | Datang | Pelayanan | Waktu Menunggu (WT) | Turnaround Time (TAT) |
| ------ | ------ | --------- | ------------------- | --------------------- |
| F1     | 0      | 12        | 0                   | 12                    |
| F2     | 1      | 1         | 11                  | 12                    |
| F3     | 2      | 30        | 11                  | 41                    |
| F4     | 3      | 3         | 40                  | 43                    |
| F5     | 4      | 70        | 41                  | 111                   |

Analisis

1. **Proses awal (F1)**
   * Datang pertama dan langsung diproses.
   * Tidak mengalami waktu menunggu (WT = 0).
   * Cocok menggambarkan prinsip dasar FCFS.

2. **Efek Convoy Effect**
   * Proses **F3 (30 detik)** dan terutama **F5 (70 detik)** menyebabkan proses berikutnya menunggu sangat lama.
   * F4 dan F5 mengalami waktu menunggu tinggi (40 dan 41).

3. **Ketidakadilan untuk proses pendek**
   * F2 dan F4 memiliki waktu pelayanan kecil, tetapi harus menunggu lama karena proses sebelumnya panjang.
   * Ini menunjukkan FCFS **kurang optimal untuk sistem dengan variasi burst time besar**.

4. **Kelebihan FCFS**
   * Implementasi sederhana
   * Tidak menyebabkan starvation
   * Cocok untuk sistem batch sederhana

5. **Kekurangan FCFS**
   * Rata-rata waktu tunggu tinggi
   * Tidak efisien untuk sistem interaktif
   * Sangat dipengaruhi oleh urutan kedatangan

## 6.2 deadlock_detection
![WhatsApp Image 2026-01-25 at 20 38 26](https://github.com/user-attachments/assets/68584d90-05f6-4f37-8023-0c93e4e51fce)

tabel hasil simulasi 
| Mobil | Memegang Jalan | Menunggu Jalan |
| ----- | -------------- | -------------- |
| A     | Utara          | Timur          |
| B     | Timur          | Selatan        |
| C     | Selatan        | Barat          |
| D     | Barat          | Utara          |

analisis
1. Terbentuk Circular Wait

Terjadi rantai menunggu melingkar** sebagai berikut:

* Mobil A menunggu jalan **Timur** (dipegang B)
* Mobil B menunggu jalan **Selatan** (dipegang C)
* Mobil C menunggu jalan **Barat** (dipegang D)
* Mobil D menunggu jalan **Utara** (dipegang A)

Tidak ada satu pun mobil yang dapat melanjutkan perjalanan.

2. Empat Kondisi Deadlock Terpenuhi

Simulasi ini memenuhi seluruh syarat deadlock dalam sistem operasi:

| Kondisi Deadlock | Terpenuhi | Penjelasan                                           |
| ---------------- | --------- | ---------------------------------------------------- |
| Mutual Exclusion | ✅        | Setiap jalan hanya bisa dipakai satu mobil           |
| Hold and Wait    | ✅        | Mobil memegang satu jalan sambil menunggu jalan lain |
| No Preemption    | ✅        | Jalan tidak bisa direbut paksa                       |
| Circular Wait    | ✅        | Terjadi siklus A → B → C → D → A                     |


## 6.3 Page_replacement
![WhatsApp Image 2026-01-25 at 20 38 09](https://github.com/user-attachments/assets/932c6908-289e-44ab-81e0-f42beedb39d7)

tabel hasil simulasi 
| Langkah | Aksi           | Pasien | Isi Antrian Setelah Aksi |
| ------- | -------------- | ------ | ------------------------ |
| 1       | Ambil Nomor    | Andi   | Andi                     |
| 2       | Ambil Nomor    | Budi   | Andi, Budi               |
| 3       | Ambil Nomor    | Citra  | Andi, Budi, Citra        |
| 4       | Panggil Pasien | Andi   | Budi, Citra              |
| 5       | Panggil Pasien | Budi   | Citra                    |
| 6       | Panggil Pasien | Citra  | (kosong)                 |
| 7       | Panggil Pasien | –      | (kosong)                 |

Analisis 
1. Prinsip FIFO Berjalan dengan Benar

Program menerapkan **First In First Out**, dibuktikan dengan:
* Andi dipanggil pertama karena datang lebih dulu
* Diikuti Budi, lalu Citra

2. Mekanisme File sebagai Queue
* File `fifo.txt` berfungsi sebagai **media penyimpanan antrian**
* Baris pertama selalu menjadi pasien yang dipanggil
* Setelah dipanggil, baris tersebut dihapus (shift queue)

Ini menyerupai **queue pada sistem operasi**.

### 3. Penanganan Kondisi Kosong

Saat pemanggilan ke-4:
* File sudah kosong
* Program menampilkan pesan:

  > *"Tidak ada pasien dalam antrian."*

Hal ini menunjukkan **error handling berjalan dengan baik**.

## 7.Tugas setiap Anggota

| NIM | Nama | Peran | Kontribusi |
| :---: | :---: | :---: | :---: |
| 250202917 | Rafika Rahma | Project Lead/Integrator| - Inisiasi project (merancang struktur awal dan main.py) <br> - merge PR & fix conflict <br> - Uji modul aplikasi  |
| 250202923 | Novia Safitri  | Developer 1 (Modul CPU Scheduling) | - Merancang modul aplikasi CPU Scheduling <br> - Membuat dataset process.csv <br> - Analisis eksekusi aplikasi | 
| 250202946 | Evelin Natalie | Developer 2 (Modul Page Replacement) | - Merancang modul aplikasi Page Replacement (FIFO) <br> - Membuat dataset reference_string.txt <br> - Analisis eksekusi aplikasi |
| 250202956 | Nadya Pramudita | Developer 3 (Deadlock Detection) | - Merancang modul apllikasi Deadlock Detection <br> - Membuat dataset.csv <br> - Analisis eksekusi aplikasi |
| 250202936 | Faik setyawan | Dokumentasi & QA | - Menyusun laporan proyek <br> - Mengumpulkan dokumentasi eksekusi (screenshots) <br> - Menyelesaikan quiz |
--- 





### 1. Novia Safitri – Penanggung Jawab Modul 1

Anggota 1 bertanggung jawab untuk mengerjakan **Modul 1** sesuai dengan pedoman dan instruksi yang telah diberikan. Tugas ini mencakup pemahaman materi, pengerjaan soal atau studi kasus, serta penyusunan hasil kerja secara sistematis dan terstruktur. Hasil dari Modul 1 kemudian disiapkan untuk dikompilasi ke dalam laporan kelompok.

### 2. Evelin Natalie – Penanggung Jawab Modul 2

Anggota 2 bertugas mengerjakan **Modul 2** dengan memperhatikan ketentuan dan standar yang telah ditetapkan. Selain menyelesaikan isi modul, anggota ini juga melakukan pengecekan terhadap kelengkapan dan kebenaran hasil pekerjaan sebelum dikumpulkan ke dalam repository proyek kelompok.

### 3. Nadya Pramudita – Penanggung Jawab Modul 3

Anggota 3 memiliki tanggung jawab untuk mengerjakan **Modul 3** secara menyeluruh dan sesuai dengan panduan yang tersedia. Anggota ini juga memastikan bahwa hasil pengerjaan telah disusun dengan format yang konsisten agar mudah dipahami dan dapat digabungkan dengan modul-modul lainnya dalam laporan akhir.

### 4. Faik Setyawan – Penanggung Jawab Dokumentasi (README)

Anggota 4 bertanggung jawab dalam penyusunan dan pengelolaan dokumentasi proyek pada file **README.md** dan **laporan.md**. Tugas ini meliputi penulisan deskripsi proyek, tujuan pengerjaan, serta ringkasan isi dari setiap modul. Dokumentasi disusun secara jelas dan sistematis agar dapat memberikan gambaran menyeluruh mengenai proyek yang dikerjakan.

### 5. Rafika Rahma – Koordinator dan Pengelola Repository GitHub

Ketua kelompok berperan sebagai koordinator utama dan pengelola repository GitHub. Tugas ketua meliputi pengelolaan branch, pengaturan alur kerja version control, peninjauan serta penggabungan (merge) kontribusi anggota ke branch utama (main/master), pengembangan main.py, dan penyusunan Dockerfile. Ketua kelompok juga memastikan seluruh kontribusi terdokumentasi dengan baik dan repository siap untuk dikumpulkan.

---

### Tugas & Quiz
#### Tugas
1. Implementasikan proyek sesuai spesifikasi (minimal 2 modul).
2. Sediakan dataset contoh dan dokumentasi run (`code/README.md`).
3. Buat `Dockerfile` dan pastikan demo berjalan.
4. Tulis laporan proyek pada `laporan.md`.

#### Quiz
1. Tantangan terbesar integrasi modul apa, dan bagaimana solusinya?

Tantangan terbesar dalam integrasi modul adalah **menyatukan tiga konsep sistem operasi yang berbeda (CPU Scheduling, Page Replacement, dan Deadlock Detection)** ke dalam satu alur aplikasi yang konsisten. Setiap modul memiliki input, proses, dan output yang berbeda, sehingga berpotensi menimbulkan ketidaksesuaian format data dan alur eksekusi.

**Solusi yang dilakukan:**

* Mendesain **alur program yang modular**, di mana setiap modul berdiri sendiri namun dapat dipanggil dari satu *main program*.
* Menyamakan format input dan output (misalnya menggunakan struktur data sederhana seperti list, dictionary, dan tabel).
* Menggunakan **menu/CLI** agar pengguna dapat menjalankan modul secara terpisah tanpa saling mengganggu.
* Melakukan pengujian tiap modul secara individual sebelum digabungkan ke dalam container Docker.


2. Mengapa Docker membantu proses demo dan penilaian proyek?

Docker sangat membantu karena mampu menyediakan **lingkungan eksekusi yang konsisten dan terisolasi**. Dengan Docker, aplikasi dapat dijalankan tanpa bergantung pada konfigurasi sistem operasi host.

Manfaat utama penggunaan Docker dalam proyek ini:

* **Konsistensi lingkungan**: Aplikasi berjalan sama di komputer pengembang maupun penguji.
* **Kemudahan demo**: Dosen atau penguji cukup melakukan `docker build` dan `docker run` tanpa instalasi tambahan.
* **Isolasi sistem**: Tidak mengganggu sistem utama pengguna.
* **Reproducibility**: Hasil simulasi dapat direplikasi dengan mudah.

Dengan demikian, Docker mempermudah proses demonstrasi, evaluasi, dan penilaian proyek.


3. Jika dataset diperbesar 10x, modul mana yang paling terdampak performanya? Jelaskan.

Modul yang **paling terdampak performanya** jika dataset diperbesar 10x adalah **CPU Scheduling (FCFS)** dan **Page Replacement (FIFO)**, dengan dampak terbesar pada **CPU Scheduling FCFS**.

Penjelasan:

* **CPU Scheduling FCFS**:

  * Semakin banyak proses, semakin panjang *waiting time*.
  * Proses dengan burst time besar di awal akan memperparah **convoy effect**.
  * Waktu simulasi dan perhitungan meningkat secara signifikan.

* **Page Replacement FIFO**:

  * Jumlah page reference yang meningkat akan menyebabkan **page fault lebih sering**.
  * Pengelolaan antrian frame menjadi lebih berat, meskipun masih relatif sederhana.

* **Deadlock Detection**:

  * Dampaknya relatif lebih kecil dibanding dua modul lainnya.
  * Namun, jika jumlah proses dan resource meningkat drastis, pemeriksaan siklus juga akan membutuhkan waktu lebih lama.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
