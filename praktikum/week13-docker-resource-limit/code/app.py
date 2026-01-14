import time
import os

memory_blocks = []
iteration = 0

print("=== PROGRAM UJI CPU & MEMORI ===")
print(f"PID Container : {os.getpid()}")
print("Program berjalan...\n")

try:
    while True:
        iteration += 1

        # ======================
        # UJI CPU (komputasi berat)
        # ======================
        cpu_result = 0
        for i in range(5_000_000):
            cpu_result += i % 3

        # ======================
        # UJI MEMORI (alokasi bertahap)
        # ======================
        memory_blocks.append(bytearray(20 * 1024 * 1024))  # 20 MB
        allocated_mb = len(memory_blocks) * 20

        print(f"Iterasi {iteration}")
        print(f"- CPU task selesai (dummy result: {cpu_result})")
        print(f"- Memori teralokasi: {allocated_mb} MB")
        print("-" * 40)

        time.sleep(1)

except MemoryError:
    print("\nERROR: Batas memori tercapai (MemoryError)")

except KeyboardInterrupt:
    print("\nProgram dihentikan oleh pengguna")

except Exception as e:
    print(f"\nContainer dihentikan: {e}")
