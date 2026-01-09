# Dataset
allocation = {
    "P1": "R1",
    "P2": "R2",
    "P3": "R3"
}

request = {
    "P1": "R2",
    "P2": "R3",
    "P3": "R1"
}

# Membangun Wait-For Graph
wfg = {}
for p in allocation:
    wfg[p] = []
    for q in allocation:
        if request[p] == allocation[q]:
            wfg[p].append(q)

# Deteksi siklus (DFS)
visited = set()
rec_stack = set()
deadlock_processes = set()

def dfs(process):
    visited.add(process)
    rec_stack.add(process)

    for neighbor in wfg[process]:
        if neighbor not in visited:
            if dfs(neighbor):
                deadlock_processes.add(process)
                return True
        elif neighbor in rec_stack:
            deadlock_processes.add(process)
            return True

    rec_stack.remove(process)
    return False

for p in wfg:
    if p not in visited:
        dfs(p)

# Output
if deadlock_processes:
    print("Deadlock terdeteksi pada proses:", ", ".join(deadlock_processes))
else:
    print("Tidak terjadi deadlock")
