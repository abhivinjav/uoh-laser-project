import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# spectrum files to df
ref_df = pd.read_csv("spectrum\\spectrum_files\\reference.csv", delimiter=',')

water_df = pd.read_csv("spectrum\\spectrum_files\\water.csv", delimiter=',')

# spectrum file columns to numpy arrays
ref_df_x = ref_df['Wavelength'].to_numpy()
ref_df_y = ref_df['Intensity'].to_numpy()

water_df_x = water_df['Wavelength'].to_numpy()
water_df_y = water_df['Intensity'].to_numpy()

#graph
plt.plot(water_df_x, water_df_y, color='black', marker=None, linewidth=0.75)
plt.scatter(water_df_x, water_df_y, marker="o", linewidth=0.75)

plt.title("Water Aerosol Spectrum")
plt.xlabel(r"Wavelength $\lambda$ (nm)")
plt.ylabel("Intensity")
plt.minorticks_on()
plt.xticks(np.arange(100,1000,100))
plt.yticks(np.arange(0,60000, 5000))

plt.savefig("spectrum\\water_spectrum.png", bbox_inches='tight', dpi=150)

plt.show()