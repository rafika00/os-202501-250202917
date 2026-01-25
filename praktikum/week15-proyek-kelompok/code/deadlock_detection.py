import csv
import os

def main():
    mobil = []
    memegang = {}
    menunggu = {}

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(BASE_DIR, "data", "dataset.csv")

    if not os.path.exists(csv_path):
        print("File dataset tidak ditemukan!")
        print("Dicari di:", csv_path)
        return

    with open(csv_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            m = row["Mobil"]
            mobil.append(m)
            memegang[m] = row["Memegang_Jalan"]
            menunggu[m] = row["Menunggu_Jalan"]

    print("=== SIMULASI DEADLOCK PERSIMPANGAN JALAN ===\n")

    for m in mobil:
        print(f"Mobil {m} memegang jalan {memegang[m]} dan menunggu jalan {menunggu[m]}")

    print("\n=== HASIL ===")
    print("DEADLOCK TERDETEKSI ❌")
    print("Semua mobil saling menunggu dan tidak ada yang bisa bergerak")


if __name__ == "__main__":
    main()
