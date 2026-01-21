# Menggunakan image Python versi 3.12 (slim) yang stabil dan ringan
FROM python:3.12-slim

# Menentukan direktori kerja di dalam container
WORKDIR /app

# Menyalin seluruh file Python (.py) ke dalam direktori kerja
COPY *.py .

# Menyalin folder data dari host ke dalam container
COPY data/ ./data/

# Menjalankan file utama saat container dijalankan
CMD ["python", "main.py"]
