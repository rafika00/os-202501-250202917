import csv
import os

BASE_DIR = os.path.dirname(__file__)
DATASET_PATH = os.path.join(BASE_DIR, "data", "proses.csv")


def antrean_fotokopi_fcfs(nama_berkas_csv):
    proses = []

    with open(nama_berkas_csv, 'r', encoding='utf-8') as berkas:
        reader = csv.DictReader(berkas)
        for baris in reader:
            proses.append({
                "nama": baris["Proses"],
                "datang": int(baris["Waktu_Kedatangan"]),
                "pelayanan": int(baris["Waktu_Pelayanan"])
            })

    proses.sort(key=lambda x: x["datang"])

    waktu_sekarang = 0
    total_wt = 0
    total_tat = 0

    print("=" * 55)
    print("| Proses | Datang | Pelayanan | Menunggu | Turnaround |")
    print("-" * 55)

    for p in proses:
        if waktu_sekarang < p["datang"]:
            waktu_sekarang = p["datang"]

        wt = waktu_sekarang - p["datang"]
        tat = wt + p["pelayanan"]

        total_wt += wt
        total_tat += tat

        print(
            f"| {p['nama']:^6} | "
            f"{p['datang']:^6} | "
            f"{p['pelayanan']:^9} | "
            f"{wt:^8} | "
            f"{tat:^10} |"
        )

        waktu_sekarang += p["pelayanan"]

    n = len(proses)
    print("-" * 55)
    print(f"Rata-rata Waktu Menunggu   : {total_wt / n:.2f}")
    print(f"Rata-rata Turnaround Time : {total_tat / n:.2f}")
    print("=" * 55)


def main():
    antrean_fotokopi_fcfs(DATASET_PATH)


if __name__ == "__main__":
    main()