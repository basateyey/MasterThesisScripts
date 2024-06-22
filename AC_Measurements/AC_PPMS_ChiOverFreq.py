import matplotlib.pyplot as plt
import pandas as pd
import math

# Data import
data = pd.read_csv('PPMS_Li0.6Al0.4Fe5O8 Xac.dat', skiprows=21)

# Group data
data['Temperature (K)'] = data['Temperature (K)'].apply(lambda x: int(x))
grouped_data = data.groupby('Temperature (K)')
print(data['Temperature (K)'])

#emu/gram
data['Mdoublebar (emu)'] = data['Mdoublebar (emu)'] / 0.08526

# Fig
fig, ax = plt.subplots()

# Plot
for temperature, group in grouped_data:
    frequency_label = f"{math.ceil(temperature)} K"
    ax.plot(group['Frequency (Hz)'], group['Mdoublebar (emu)'], label=frequency_label)

# Plot settings
ax.set_xlabel('Frequency (Hz)', labelpad=20, fontsize = 12)
ax.set_ylabel('m\" [emu/g]', labelpad=15, fontsize = 12)
ax.set_title('PPMS magnetic susceptibility measurement', fontsize = 12)
plt.legend(bbox_to_anchor=(1.01, 1.0), loc='upper left')



plt.show()
