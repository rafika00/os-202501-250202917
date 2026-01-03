# FCFS schedulling simulation
# Dataset proses
processes = [
    {"id": "P1", "arrival": 0, "burst": 6},
    {"id": "P2", "arrival": 1, "burst": 8},
    {"id": "P3", "arrival": 2, "burst": 7},
    {"id": "P4", "arrival": 3, "burst": 3},
]

time = 0
total_waiting = 0
total_turnaround = 0

print("Proses | Arrival | Burst | Waiting | Turnaround")
print("------------------------------------------------")

for p in processes:
    if time < p["arrival"]:
        time = p["arrival"]

    waiting_time = time - p["arrival"]
    turnaround_time = waiting_time + p["burst"]

    total_waiting += waiting_time
    total_turnaround += turnaround_time

    time += p["burst"]

    print(f"{p['id']:>6} | {p['arrival']:>7} | {p['burst']:>5} | {waiting_time:>7} | {turnaround_time:>10}")

avg_waiting = total_waiting / len(processes)
avg_turnaround = total_turnaround / len(processes)

print("------------------------------------------------")
print(f"Rata-rata Waiting Time     : {avg_waiting}")
print(f"Rata-rata Turnaround Time  : {avg_turnaround}")
