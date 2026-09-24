import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

#ordering the arrays using argsort (gives the index of which the array should be ordered) and then applying that order to the array. Preserves T and E pairs but orders the data
#to include the extra data collected seperatly in intrestind sections
T = np.array([
    0.1014,
    0.2091,
    0.3039,
    0.4036,
    0.5042,
    0.6183,
    0.7006,
    0.8041,
    0.9275,
    1.0942,
    1.1039,
    1.2056,
    1.3221,
    1.4278,
    1.5214,
])
E = np.array([
    -1391.25,
    -1290.07,
    -1152.48,
    -744.96,
    -125.24,
    80.09,
    148.29,
    224.27,
    307.86,
    404.12,
    409.69,
    474.43,
    536.91,
    578.17,
    645.32
])
T_extra = np.array([
    0.3563,
    0.3795,
    0.4244,
    0.4593,
    0.4784,
    0.5239,
    0.5488,
    0.5866
])
E_extra = np.array([
    -942.3,
    -883.41,
    -677.47,
    -420.54,
    -207.35,
    -55.61,
    -4.29,
    48.6
])
T_all = np.concatenate((T,T_extra))
E_all = np.concatenate((E,E_extra))
order = np.argsort(T_all)
T_all = T_all[order]
E_all = E_all[order]
N=500

x_min, x_max = 0, 1.6
y_min, y_max = -1500, 1000

#First plot
plt.figure(figsize=(7, 5))
plt.scatter(T_all,E_all,s=15)
plt.title("Energy vs Temperature")
plt.xlabel("Temperature")
plt.ylabel("Energy")
plt.xlim(x_min,x_max)
plt.ylim(y_min,y_max)
plt.grid(alpha=0.8)
plt.tight_layout()
plt.savefig("09_23_26/Temperature_with_Energy.png", dpi=300)

#second plot setup
liquid_mask = T_all <= 0.3795
gas_mask = T_all >= 0.7006
liquid_fit = linregress(T_all[liquid_mask],E_all[liquid_mask])
gas_fit = linregress(T_all[gas_mask],E_all[gas_mask])
# ^ Lineregress gives stats for values that satisfy the mask boolean. 
#Gas Data
print(f"\nGas Data")
print(f"slope: {gas_fit.slope}")
print(f"slope uncert: {gas_fit.stderr}")
print(f"Heat capacity per particle: {gas_fit.slope / N}")
print(f"Uncertainty per particle: {gas_fit.stderr / N}")
#Liquid Data
print(f"\nLiquid Data")
print(f"slope: {liquid_fit.slope}")
print(f"slope uncert: {liquid_fit.stderr}")
print(f"Heat capacity per particle: {liquid_fit.slope / N}")
print(f"Uncertainty per particle: {liquid_fit.stderr / N}")

#Second plot
T_liquid_line = np.linspace(T_all[liquid_mask].min(),T_all[liquid_mask].max(),100)
T_gas_line = np.linspace(T_all[gas_mask].min(),T_all[gas_mask].max(),100)
# Corresponding fitted energies
E_liquid_line = (liquid_fit.intercept + liquid_fit.slope * T_liquid_line)
E_gas_line = (gas_fit.intercept+ gas_fit.slope * T_gas_line)
# Plot data and fitted lines
plt.figure(figsize=(7, 5))
plt.scatter(T_all,E_all,label="Simulation data",s=15)
plt.plot(T_liquid_line,E_liquid_line,color="red",label="Liquid linear fit")
plt.plot(T_gas_line,E_gas_line,color="green",label="Gas linear fit")
plt.xlabel("Temperature")
plt.ylabel("Energy")
plt.xlim(x_min,x_max)
plt.ylim(y_min,y_max)
plt.title("Energy vs. Temperature with Linear Fits")
plt.legend()
plt.grid(alpha=0.8)
plt.tight_layout()
plt.savefig("09_23_26/Energy_with_linear_fits.png", dpi=300)

#third plot - Cv vs Temp
T_mid = (T_all[1:] + T_all[:-1]) / 2
Cv_discrete = (E_all[1:] - E_all[:-1]) / (T_all[1:] - T_all[:-1])
plt.figure(figsize=(7, 5))
plt.plot(T_mid, Cv_discrete)
plt.xlabel("Temperature")
plt.ylabel(r"$C_v$")
plt.title("Heat Capacity vs Temperature")
plt.grid(alpha=0.8)
plt.tight_layout()
plt.savefig("09_23_26/Heat_Cap_with_Temp.png", dpi=300)