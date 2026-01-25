import os

# Ambil direktori file Python ini
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Simpan file antrian di folder data
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

FILE_ANTRIAN = os.path.join(DATA_DIR, "fifo.txt")

# Fungsi mengambil nomor antrian (menambah ke file)
def ambil_nomor(nama):
    with open(FILE_ANTRIAN, "a", encoding="utf-8") as file:
        file.write(nama + "\n")
    print(f"{nama} berhasil mengambil nomor antrian.")

# Fungsi memanggil pasien (FIFO)
def panggil_pasien():
    try:
        with open(FILE_ANTRIAN, "r", encoding="utf-8") as file:
            data = file.readlines()

        if not data:
            print("Tidak ada pasien dalam antrian.")
            return

        pasien = data[0].strip()

        with open(FILE_ANTRIAN, "w", encoding="utf-8") as file:
            file.writelines(data[1:])

        print(f"Pasien {pasien} dipanggil untuk pemeriksaan.")

    except FileNotFoundError:
        print("File antrian belum tersedia.")


# ====== ENTRY POINT UNTUK main.py ======
def main():
    # Reset antrian agar output konsisten
    open(FILE_ANTRIAN, "w").close()

    ambil_nomor("Andi")
    ambil_nomor("Budi")
    ambil_nomor("Citra")

    panggil_pasien()
    panggil_pasien()
    panggil_pasien()
    panggil_pasien()


# Bisa dijalankan langsung atau lewat Docker
if __name__ == "__main__":
    main()import os

# Ambil direktori file Python ini
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Simpan file antrian di folder data
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

FILE_ANTRIAN = os.path.join(DATA_DIR, "fifo.txt")

# Fungsi mengambil nomor antrian (menambah ke file)
def ambil_nomor(nama):
    with open(FILE_ANTRIAN, "a", encoding="utf-8") as file:
        file.write(nama + "\n")
    print(f"{nama} berhasil mengambil nomor antrian.")

# Fungsi memanggil pasien (FIFO)
def panggil_pasien():
    try:
        with open(FILE_ANTRIAN, "r", encoding="utf-8") as file:
            data = file.readlines()

        if not data:
            print("Tidak ada pasien dalam antrian.")
            return

        pasien = data[0].strip()

        with open(FILE_ANTRIAN, "w", encoding="utf-8") as file:
            file.writelines(data[1:])

        print(f"Pasien {pasien} dipanggil untuk pemeriksaan.")

    except FileNotFoundError:
        print("File antrian belum tersedia.")


# ====== ENTRY POINT UNTUK main.py ======
def main():
    # Reset antrian agar output konsisten
    open(FILE_ANTRIAN, "w").close()

    ambil_nomor("Andi")
    ambil_nomor("Budi")
    ambil_nomor("Citra")

    panggil_pasien()
    panggil_pasien()
    panggil_pasien()
    panggil_pasien()


# Bisa dijalankan langsung atau lewat Docker
if __name__ == "__main__":
    main()
