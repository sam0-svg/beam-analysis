import numpy as np
import matplotlib.pyplot as plt

def calculate_reactions(P, L, a):
    R_A = P * (L - a) / L
    R_B = P * a / L
    return R_A, R_B

def calculate_shear(x, R_A, P, a):
    return np.where(x <= a, R_A, R_A - P)

def calculate_moment(x, R_A, P, a):
    return np.where(x <= a, R_A * x, R_A * x - P * (x - a))

def plot_beam(x, V, M):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
    
    ax1.plot(x, V, color='red', linewidth=2)
    ax1.fill_between(x, V, alpha=0.2, color='red')
    ax1.axhline(0, color='black', linewidth=0.8)
    ax1.set_title("نمودار نیروی برشی")
    ax1.set_ylabel("برش (kN)")
    ax1.grid(True)

    ax2.plot(x, M, color='blue', linewidth=2)
    ax2.fill_between(x, M, alpha=0.2, color='blue')
    ax2.axhline(0, color='black', linewidth=0.8)
    ax2.set_title("نمودار لنگر خمشی")
    ax2.set_ylabel("لنگر (kN.m)")
    ax2.set_xlabel("طول تیر (m)")
    ax2.grid(True)

    plt.tight_layout()
    plt.show()

# --- اجرای اصلی ---
L, P, a = 8, 10, 3
x = np.linspace(0, L, 500)

R_A, R_B = calculate_reactions(P, L, a)
V = calculate_shear(x, R_A, P, a)
M = calculate_moment(x, R_A, P, a)

plot_beam(x, V, M)