from numpy import pi



InD_R = float(input("Enter the inner diameter of the dish in mm: ")) / 2
H = float(input("Enter the desired sheet height in mm: "))

# Volume in mm^3
v = pi * (InD_R ** 2) * H

# 10:1 volume ratio
PDMS_base_volume = v * 10 / 11
PDMS_curing_volume = v / 11

# Enter densities from your PDMS product datasheet in g/cm^3
base_density = float(input("Enter PDMS base density in g/cm^3: "))
curing_density = float(input("Enter curing agent density in g/cm^3: "))

# Convert volumes from mm^3 to cm^3
PDMS_base_volume_cm3 = PDMS_base_volume / 1000
PDMS_curing_volume_cm3 = PDMS_curing_volume / 1000

# Calculate masses
PDMS_base_mass = PDMS_base_volume_cm3 * base_density
PDMS_curing_mass = PDMS_curing_volume_cm3 * curing_density
total_mass = PDMS_base_mass + PDMS_curing_mass

PDMS_base_mass = total_mass * 10 / 11
PDMS_curing_mass = total_mass / 11

print("-- PDMS Mass Calculation --")
print(f"Total volume: {v:.2f} mm^3")
print(f"PDMS base: {PDMS_base_mass:.4f} g")
print(f"Curing agent: {PDMS_curing_mass:.4f} g")
print(f"Total mass: {total_mass:.4f} g")


