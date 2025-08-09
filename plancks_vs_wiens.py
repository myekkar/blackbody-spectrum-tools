import numpy as np
# Wien's displacement constant (m·K)
B = 2.897771955e-3

# Physical constants for Planck's law
h = 6.626e-34      # Planck's constant (J·s)
c = 2.998e8        # Speed of light (m/s)
k = 1.381e-23      # Boltzmann's constant (J/K)

def blackbody(lambda_m, T):
    """Spectral radiance in W·sr⁻¹·m⁻³"""
    term1 = (2 * h * c**2) / (lambda_m**5)
    term2 = 1 / (np.exp((h * c) / (lambda_m * k * T)) - 1)
    return term1 * term2

def wien_peak(T):
    """Wien's displacement law in meters"""
    return B / T

temperatures = [3000, 6000, 20000]

# Wavelength grid (in meters)
lambda_m = np.linspace(0.1e-6, 10e-6, 50000)  # 0.1 µm to 10 µm

# Run comparison
print(f"{'Temp (K)':>8} | {'Wien λ_peak (µm)':>18} | {'Numeric λ_peak (µm)':>22} | {'Diff (%)':>8}")
print("-"*70)

for T in temperatures:

    # Wien's law
    lambda_wien = wien_peak(T) * 1e6  # µm
    # Numeric peak from Planck's law
    spectral_radiance = blackbody(lambda_m, T)
    lambda_num = lambda_m[np.argmax(spectral_radiance)] * 1e6  # µm
    # Percent difference
    diff_percent = abs(lambda_num - lambda_wien) / lambda_wien * 100
    print(f"{T:8} | {lambda_wien:18.6f} | {lambda_num:22.6f} | {diff_percent:8.4f}")
