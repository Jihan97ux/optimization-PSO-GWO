import numpy as np
from data import data, constraints
import time

# Parameter PSO
pop_size = 25
max_iter = 25
c1 = 1.5
c2 = 1.5
w = 0.5
num_runs = 10 

# Fungsi profit
def calculate_profit(selection):
    total_berat = 0
    total_volume = 0
    total_modal = 0
    total_profit = 0
    
    for i, item in enumerate(data):
        if selection[i] > item["jumlah"]:
            selection[i] = item["jumlah"]
        
        total_berat += item["berat"] * selection[i]
        total_volume += item["volume"] * selection[i]
        total_modal += item["harga_beli"] * selection[i]
        total_profit += (item["harga_jual"] - item["harga_beli"]) * selection[i]
    
    if total_berat > constraints["max_berat"] or total_volume > constraints["max_volume"] or total_modal > constraints["max_modal"]:
        return -np.inf, 0  
        
    return total_profit, total_modal 

# Menyimpan hasil terbaik dari setiap run
best_solutions = []
best_profits = []
computation_times = []
best_iters = []
total_modals = []  

for run in range(num_runs):
    # Inisialisasi populasi
    pop = np.random.randint(0, [item["jumlah"] for item in data], (pop_size, len(data)))
    vel = np.random.random((pop_size, len(data)))

    pbest = pop.copy()
    pbest_scores = np.array([calculate_profit(ind)[0] for ind in pop])
    gbest = pbest[np.argmax(pbest_scores)].copy()
    gbest_score = np.max(pbest_scores)
    best_iter = 0
    total_modal_run = 0

    start_time = time.time()

    # Iterasi PSO
    for t in range(max_iter):
        for i in range(pop_size):
            r1, r2 = np.random.random(), np.random.random()
            vel[i] = w * vel[i] + c1 * r1 * (pbest[i] - pop[i]) + c2 * r2 * (gbest - pop[i])
            pop[i] = pop[i] + vel[i]
            pop[i] = np.clip(pop[i], 0, [item["jumlah"] for item in data])
            
            profit, total_modal = calculate_profit(pop[i])
            if profit > pbest_scores[i]:
                pbest_scores[i] = profit
                pbest[i] = pop[i].copy()
            
            if profit > gbest_score:
                gbest_score = profit
                gbest = pop[i].copy()
                best_iter = t
            
            total_modal_run += total_modal  

    end_time = time.time()

    # Hasil akhir untuk satu run
    best_solution = gbest
    best_profit = gbest_score
    computation_time = end_time - start_time

    # Simpan hasil
    best_solutions.append(best_solution)
    best_profits.append(best_profit)
    computation_times.append(computation_time)
    best_iters.append(best_iter)
    total_modals.append(total_modal)  

avg_computation_time = np.mean(computation_times)
avg_profit = np.mean(best_profits)
max_profit = np.max(best_profits)
min_profit = np.min(best_profits)
std_profit = np.std(best_profits)

# Menghitung presentase standar deviasi berdasarkan profit
percent_devs = [(std_profit / profit) * 100 for profit in best_profits]

# Mencetak hasil dari 10 run
print("===PSO===")
for i in range(num_runs):
    print(f"Run {i+1}:")
    print("Best Solution:")
    for j, item in enumerate(data):
        if best_solutions[i][j] > 0:
            print(f"{item['nama']}: {best_solutions[i][j]} {item['satuan']}")
    print("Best Profit:", best_profits[i])
    print("Total Modal:", total_modals[i])  
    print("Waktu Komputasi:", computation_times[i], "detik")
    print("Solusi terbaik ditemukan pada iterasi ke:", best_iters[i])
    print(f"Presentase Standar Deviasi: {percent_devs[i]:.2f}%")
    print("\n")
    
print("===Statistik Keseluruhan===")
print(f"Rata-rata Profit: {avg_profit:.2f}")
print(f"Profit Maksimal: {max_profit:.2f}")
print(f"Profit Minimal: {min_profit:.2f}")
print(f"Rata-rata Waktu Komputasi: {avg_computation_time:.2f} detik")
print(f"Rata-rata Presentase Standar Deviasi: {np.mean(percent_devs):.2f}%")
