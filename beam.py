import numpy as np
import matplotlib.pyplot as plt

class Beam:
    def __init__(self, L, P, a):
        self.L = L
        self.P = P
        self.a = a
        self.x = np.linspace(0, L, 500)
    
    def calculate_reactions(self):
        self.R_A = self.P * (self.L - self.a) / self.L
        self.R_B = self.P * self.a / self.L
    
    def calculate_shear(self):
        return np.where(self.x <= self.a, self.R_A, self.R_A - self.P)
    
    def calculate_moment(self):
        return np.where(self.x <= self.a, 
                       self.R_A * self.x, 
                       self.R_A * self.x - self.P * (self.x - self.a))
    
    def summary(self):
        self.calculate_reactions()
        print(f"Beam Length: {self.L} m")
        print(f"Load: {self.P} kN at x={self.a}")
        print(f"R_A = {self.R_A:.2f} kN")
        print(f"R_B = {self.R_B:.2f} kN")
        print(f"Max Moment: {self.R_A * self.a:.2f} kN.m at x={self.a}")
    
    def plot(self):
        self.calculate_reactions()
        V = self.calculate_shear()
        M = self.calculate_moment()
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
        
        ax1.plot(self.x, V, color='red', linewidth=2)
        ax1.fill_between(self.x, V, alpha=0.2, color='red')
        ax1.axhline(0, color='black', linewidth=0.8)
        ax1.set_title("Shear Force Diagram")
        ax1.set_ylabel("Shear (kN)")
        ax1.grid(True)

        ax2.plot(self.x, M, color='blue', linewidth=2)
        ax2.fill_between(self.x, M, alpha=0.2, color='blue')
        ax2.axhline(0, color='black', linewidth=0.8)
        ax2.set_title("Bending Moment Diagram")
        ax2.set_ylabel("Moment (kN.m)")
        ax2.set_xlabel("Beam Length (m)")
        ax2.grid(True)

        plt.tight_layout()
        plt.show()

beam = Beam(L=8, P=10, a=3)
beam.summary()
beam.plot()