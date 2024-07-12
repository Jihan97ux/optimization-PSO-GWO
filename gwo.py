import numpy as np
from data import data, constraints
import time

# Parameter GWO
pop_size = 250
max_iter = 1000
num_runs = 10  # Jumlah pengulangan

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
        return -np.inf, total_modal  
    
    return total_profit, total_modal

# Menyimpan hasil terbaik dari setiap run
best_solutions = []
best_profits = []
total_modals = []
computation_times = []
best_iters = []
profit_per_iter = []
deviation_per_iter = []

for run in range(num_runs):
    # Inisialisasi populasi
    pop = np.random.randint(0, [item["jumlah"] for item in data], (pop_size, len(data)))
    alpha, beta, delta = pop[0], pop[1], pop[2]
    alpha_score, beta_score, delta_score = -np.inf, -np.inf, -np.inf
    best_iter = 0

    start_time = time.time()

    # Simpan profit dan deviasi tiap iterasi
    profits_this_run = []
    deviations_this_run = []

    # Iterasi GWO
    for t in range(max_iter):
        for i in range(pop_size):
            fitness, total_modal = calculate_profit(pop[i])
            
            if fitness > alpha_score:
                delta_score = beta_score
                delta = beta.copy()
                beta_score = alpha_score
                beta = alpha.copy()
                alpha_score = fitness
                alpha = pop[i].copy()
                best_iter = t
            elif fitness > beta_score:
                delta_score = beta_score
                delta = beta.copy()
                beta_score = fitness
                beta = pop[i].copy()
            elif fitness > delta_score:
                delta_score = fitness
                delta = pop[i].copy()
        
        a = 2 - t * (2 / max_iter)  
        
        for i in range(pop_size):
            for j in range(len(data)):
                r1, r2 = np.random.random(), np.random.random()
                A1 = 2 * a * r1 - a
                C1 = 2 * r2
                D_alpha = abs(C1 * alpha[j] - pop[i][j])
                X1 = alpha[j] - A1 * D_alpha
                
                r1, r2 = np.random.random(), np.random.random()
                A2 = 2 * a * r1 - a
                C2 = 2 * r2
                D_beta = abs(C2 * beta[j] - pop[i][j])
                X2 = beta[j] - A2 * D_beta
                
                r1, r2 = np.random.random(), np.random.random()
                A3 = 2 * a * r1 - a
                C3 = 2 * r2
                D_delta = abs(C3 * delta[j] - pop[i][j])
                X3 = delta[j] - A3 * D_delta
                
                pop[i][j] = (X1 + X2 + X3) / 3
                pop[i][j] = np.clip(pop[i][j], 0, data[j]["jumlah"])
        
        # Simpan profit alpha di iterasi ini
        current_profit, _ = calculate_profit(alpha)
        profits_this_run.append(current_profit)

    end_time = time.time()

    # Hasil akhir untuk satu run
    best_solution = alpha
    best_profit, total_modal = calculate_profit(alpha)
    computation_time = end_time - start_time

    # Hitung deviasi persentase untuk setiap iterasi dalam run ini
    simplex_profit = max(profits_this_run)
    deviations_this_run = [(simplex_profit - profit) / simplex_profit * 100 for profit in profits_this_run]

    # Simpan hasil
    best_solutions.append(best_solution)
    best_profits.append(best_profit)
    total_modals.append(total_modal)
    computation_times.append(computation_time)
    best_iters.append(best_iter)
    profit_per_iter.append(profits_this_run)
    deviation_per_iter.append(deviations_this_run)

avg_computation_time = np.mean(computation_times)
avg_profit = np.mean(best_profits)
avg_iter = np.mean(best_iters)
avg_total_modal = np.mean(total_modals)
max_profit = np.max(best_profits)
min_profit = np.min(best_profits)

# Mencetak hasil dari 10 run
print("===GWO===")
for i in range(num_runs):
    print(f"Run {i+1}:")
    print("Best Solution:")
    for j, item in enumerate(data):
        if best_solutions[i][j] > 0:
            print(f"{item['nama']}: {best_solutions[i][j]} {item['satuan']}")
    print("Total Modal:", total_modals[i])
    print("Best Profit:", best_profits[i])
    print("Waktu Komputasi:", computation_times[i], "detik")
    print("Solusi terbaik ditemukan pada iterasi ke:", best_iters[i])
    
    # Hitung deviasi persentase dari profit tiap iterasi untuk run ini
    mean_deviation_percent = np.mean(deviation_per_iter[i])
    print(f"Rata-rata Deviasi Persentase Profit per Iterasi: {mean_deviation_percent:.2f}%")
    print("\n")
    
print("===Statistik Keseluruhan===")
print(f"Rata-rata Profit: {avg_profit:.2f}")
print(f"Profit Maksimal: {max_profit:.2f}")
print(f"Profit Minimal: {min_profit:.2f}")
print(f"Rata-rata Waktu Komputasi: {avg_computation_time:.2f} detik")
print(f"Rata-rata Iterasi: {avg_iter:.2f}")
print(f"Rata-rata Total Modal: {avg_total_modal:.2f}")
