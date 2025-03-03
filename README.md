# 🦊🐦 Comparison of Grey Wolf Optimization (GWO) and Particle Swarm Optimization (PSO) for Multiple Constraints Bounded Knapsack Problem  

## 👤 Author  
**Jihan Fadila**   
📧 Email: jihan4han97@gmail.com  

---

## 📌 Introduction  
This study compares the effectiveness of **Grey Wolf Optimization (GWO)** and **Particle Swarm Optimization (PSO)** in solving the **Multiple Constraints Bounded Knapsack Problem (MCBK)**. The research is based on the inventory optimization problem at **Toko Citra Tani Jember**, inspired by Vidiyanti et al.  

The **objective** is to maximize **profit** while considering the following constraints:  
- **Maximum weight**: 5,000 kg  
- **Maximum volume**: 9,000,000 cm³  
- **Maximum budget**: Rp 20,000,000  

**Findings:**  
- GWO achieved an optimal profit of **Rp 3,923,000** with a standard deviation of **0.13%**.  
- GWO showed more **stable results** with a **lower deviation (0.167%)** than PSO (4.3695%).  
- PSO was **faster**, but its solutions were **less stable and more variable**.  

---

## 🎯 Research Objectives  
1. **Compare** the optimization performance of GWO and PSO.  
2. **Analyze** the computational efficiency and stability of both algorithms.  
3. **Identify** the best approach for inventory management optimization.  

---

## 🛠 Methodology  
### **1. Problem Definition (MCBK Model)**  
The **Multiple Constraints Bounded Knapsack Problem (MCBK)** is formulated as:  

\[
\text{Maximize } z = \sum p_i x_i
\]  
subject to:  
\[
\sum w_i x_i \leq W, \quad \sum v_i x_i \leq V, \quad \sum c_i x_i \leq M
\]  
where:  
- \( p_i \) = profit of item \( i \)  
- \( x_i \) = quantity of item \( i \) (decision variable)  
- \( w_i \) = weight per unit  
- \( v_i \) = volume per unit  
- \( c_i \) = cost per unit  
- \( W, V, M \) = maximum weight, volume, and budget  

### **2. Algorithm Implementations**  
#### **🦊 Grey Wolf Optimization (GWO)**  
- Inspired by **wolf pack hunting behavior**.  
- Uses **alpha, beta, delta wolves** to guide search space updates.  
- **Formula for position update:**  
  \[
  X(t+1) = X_{\alpha} - A \cdot |C \cdot X_{\alpha} - X|
  \]  
  where \( A, C \) are control parameters.  

#### **🐦 Particle Swarm Optimization (PSO)**  
- Inspired by **bird flocking behavior**.  
- Particles adjust their velocity and position based on:  
  \[
  v_i(t+1) = w v_i(t) + c_1 r_1 (pbest_i - x_i) + c_2 r_2 (gbest - x_i)
  \]  
  \[
  x_i(t+1) = x_i(t) + v_i(t+1)
  \]  
  where \( w \) is the inertia factor, \( c_1, c_2 \) are acceleration coefficients.  

### **3. Computational Setup**  
- **Processor:** Intel Core i5-6200U @ 2.30 GHz  
- **Programming Language:** Python (VS Code)  
- **Parameters:**  
  - **Population:** 25, 50, 100, 250, 500  
  - **Max Iterations:** 1,000, 2,000, 5,000, 7,000  

---

## 📊 Results & Discussion  
### **Performance Comparison**  
| Algorithm | Best Profit | Avg. Profit | Std Dev (%) | Avg. Iterations | Avg. Computation Time (s) |
|-----------|------------|------------|------------|-----------------|--------------------------|
| **GWO**   | Rp 3,923,000 | Rp 3,915,500 | **0.167%** | 553.8 | 134.49 |
| **PSO**   | Rp 3,908,000 | Rp 3,680,300 | **4.3695%** | 18.31 | 18.875 |

✅ **GWO had higher stability** with the **lowest deviation (0.167%)**.  
✅ **PSO converged faster**, but its solutions were **more variable**.  
✅ **Best solution**: **GWO (Profit: Rp 3,923,000, Budget: Rp 19,998,000, Std Dev: 0.13%)**.  

### **Inventory Selection (Optimized Result)**  
| No | Item Name | Quantity | Unit |
|----|----------|----------|------|
| 1  | Altex Emulsion Paint 1 kg | 50 | Cans |
| 2  | Altex Emulton Paint 5 kg | 30 | Cans |
| 3  | Altex Cat Synthetic | 31 | Cans |
| 4  | Altex Plamir Kayu 1 kg | 45 | Cans |
| 5  | Paku 1" | 100 | kg |
| 6  | Bendrat | 51 | kg |
| 7  | Karbit | 50 | kg |

---

## 🏆 Conclusion  
- **GWO is more effective** for solving MCBK due to its **higher stability** and **better profit optimization**.  
- **PSO is faster**, but its solutions are **less consistent**.  
- **GWO achieved the best profit (Rp 3,923,000) with a stable standard deviation (0.13%)**.  
- Future research should **combine GWO and PSO** to balance **speed and stability**.  
