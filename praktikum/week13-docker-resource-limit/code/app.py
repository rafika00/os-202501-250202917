import time

data = []
iterasi = 0

print("=== Program Uji Resource Docker ===")
print("Tekan Ctrl+C untuk menghentikan\n")

try:
    while True:
        # CPU test (total hitung)
        total = 0
        for x in range(500_000):
            total += x

        # Memory test (5 MB per iterasi)
        data.append("X" * 5_000_000)
        iterasi += 1

        print(
            f"Iterasi {iterasi} | Total hitung: {total} | "
            f"Perkiraan memori: {iterasi * 5} MB"
        )

        time.sleep(1)

except MemoryError:
    print("ERROR: Memori tidak cukup! Container terkena limit memori.")

except KeyboardInterrupt:
    print("\nProgram dihentikan manual.")
