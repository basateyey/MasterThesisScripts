import matplotlib.pyplot as plt
import pandas as pd
import math

# Data import
data = pd.read_csv('PPMS_Li0.6Al0.4Fe5O8 Xac.dat', skiprows=21)

# Group the data by 'Frequency (Hz)'
grouped_data = data.groupby('Frequency (Hz)')

#emu/gram
data['Mdoublebar (emu)'] = data['Mdoublebar (emu)'] / 0.08526
data['Mbar (emu)'] = data['Mbar (emu)'] / 0.08526


# Fig
fig, ax = plt.subplots()

# Plot each group
for frequency, group in grouped_data:
    # Round up the frequency to the nearest whole number and add 'Hz' to the label
    frequency_label = f"{math.ceil(frequency)} Hz"
    ax.plot(group['Mbar (emu)'], group['Mdoublebar (emu)'], label=frequency_label)

# Plot settings
ax.set_xlabel('m\' [emu/g]', labelpad=20, fontsize = 12)
ax.set_ylabel('m\" [emu/g]', labelpad=15, fontsize = 12)
ax.set_title('Argand Plot', fontsize = 12)
plt.legend(bbox_to_anchor=(1.01, 1.0), loc='upper left')



plt.show()
