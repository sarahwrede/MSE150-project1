import matplotlib.pyplot as plt
import numpy as np
import sys

filename = sys.argv[1]        # Stores ARG1 in filename, as in: $ python plot.py ARG1 ARG2 
data1 = np.loadtxt(filename, skiprows=32, max_rows=1000, delimiter=" ", usecols=(1,5))   # Attempts to load filename into local variable data.
data2 = np.loadtxt(filename, skiprows=1051, max_rows=1000, delimiter=" ", usecols=(1,5))
data3 = np.loadtxt(filename, skiprows=2070, max_rows=1000, delimiter=" ", usecols=(1,5))

stress = np.concatenate((data1[:, 0], data2[:, 0], data3[:, 0]), axis=0)
strain = np.concatenate((data1[:, 1], data2[:, 1], data3[:, 1]), axis=0)
plt.plot(strain, stress)
plt.xlabel('Strain (%)')
plt.ylabel('Stress (Pa)')
plt.title('Stress vs. Strain')

linear_range = range(300)
slope, intercept = np.polyfit(strain[linear_range], stress[linear_range], deg=1)
youngs_modulus = slope
plt.plot(strain[linear_range], intercept + slope * strain[linear_range], color='red',label='linear regression' )
plt.legend()
plt.show()
print(f"Young's Modulus = {youngs_modulus} Pa")

plt.savefig(f"{filename}.png")

## Part 4
# Modify your code to save your plots to a file and see if you can generate
# plots and Young's moduli for all of the cleaned up files in your data 
# directory. If you haven't already, this is a good time to add text to 
# your .gitignore file so you're not committing the figures to your repository.


