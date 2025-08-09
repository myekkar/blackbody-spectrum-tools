import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Constants
h = 6.626e-34      # Planck's constant (J·s)
c = 2.998e8        # Speed of light (m/s)
k = 1.381e-23      # Boltzmann's constant (J/K)

# Planck's law: Spectral radiance in W/sr/m^3
def blackbody(lambda_m, T):
    term1 = (2 * h * c**2) / (lambda_m**5)
    term2 = 1 / (np.exp((h * c) / (lambda_m * k * T)) - 1)
    return term1 * term2  # W·sr⁻¹·m⁻³

# Plot graph for different temperatures
def stellar_radiation_graph(start_temperature, y_axis_label, color_to_use):
    # Wavelength: 0.1 µm to 10 µm
    lambda_m = np.linspace(0.1e-6, 10e-6, 200)  # meters
    lambda_um = lambda_m * 1e6  # µm for x-axis

    # Compute the spectral radiance
    spectral_radiance = blackbody(lambda_m, start_temperature)
    # Convert units to W/cm²·sr·µm from W/sr/m³
    # 1 m³ = 10^6 µm × 10^4 cm² → multiply by 1e-10
    conversion_factor = 1e-10
    spectral_radiance *= conversion_factor

    # Plot
    fig, ax = plt.subplots()
    ax.plot(lambda_um, spectral_radiance, label=y_axis_label, color=color_to_use)
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0e'))

    # Correct spectral bands (in µm)
    ax.axvspan(0.1, 0.4, alpha=0.2, color='violet', label='UV (<0.4 µm)')
    ax.axvspan(0.4, 0.7, alpha=0.2, color='green', label='Visible (0.4–0.7 µm)')
    ax.axvspan(0.7, 5, alpha=0.2, color='red', label='IR (>0.7 µm)')

    # Labels and title
    ax.set_xlabel('Wavelength (µm)')
    ax.set_ylabel('Spectral Radiance (W/cm²·sr·µm)')
    ax.set_title('Blackbody Radiation Spectra for Different Star Types')
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    plt.show()

stellar_radiation_graph(3000, 'Red Dwarf (3000 K)', 'red')
stellar_radiation_graph(6000, 'Sun-like (6000 K)', 'orange')
stellar_radiation_graph(20000, 'Blue Giant (20000 K)', 'blue')
