import csv

def antrean_fotokopi_fcfs(nama_berkas_csv):
    proses = []

    # Membaca data dari CSV
    with open(nama_berkas_csv, 'r') as berkas:
        reader = csv.DictReader(berkas)
        for baris in reader:
            proses.append({
                "nama": baris["Proses"],
                "datang": int(baris["Waktu_Kedatangan"]),
                "pelayanan": int(baris["Waktu_Pelayanan"])
            })

    # FCFS → urut berdasarkan waktu kedatangan
    proses.sort(key=lambda x: x["datang"])

    waktu_sekarang = 0
    total_wt = 0
    total_tat = 0

    print("SIMULASI ANTRIAN FOTOKOPI (FCFS)")
    print("Proses | Datang | Pelayanan | Menunggu | Turnaround")
    print("----------------------------------------------------")

    for p in proses:
        if waktu_sekarang < p["datang"]:
            waktu_sekarang = p["datang"]

        waktu_menunggu = waktu_sekarang - p["datang"]
        waktu_turnaround = waktu_menunggu + p["pelayanan"]

        total_wt += waktu_menunggu
        total_tat += waktu_turnaround

        print(f"{p['nama']:6} | {p['datang']:6} | {p['pelayanan']:9} | {waktu_menunggu:9} | {waktu_turnaround:10}")

        waktu_sekarang += p["pelayanan"]

    n = len(proses)
    print("\nRata-rata Waktu Menunggu   :", total_wt / n)
    print("Rata-rata Turnaround Time :", total_tat / n)


# Jalankan program
antrean_fotokopi_fcfs("proses.csv")