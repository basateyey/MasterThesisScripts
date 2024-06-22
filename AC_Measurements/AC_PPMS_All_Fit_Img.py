import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import data
data = pd.read_csv('PPMS_Li0.6Al0.4Fe5O8 Xac.dat', skiprows=21)

# Group data
grouped_data = {i: g for i, (freq, g) in enumerate(data.groupby('Frequency (Hz)'), 1)}


# Prparation return min values
try:
    max_values_df = pd.read_csv('PPMS_max_values.txt', sep='\t', index_col='Index')
except FileNotFoundError:
    max_values_df = pd.DataFrame(columns=['Index', 'mdoublebar']).set_index('Index')

# Graph fitting to find minimum
for index, (freq, group) in enumerate(data.groupby('Frequency (Hz)'), 1):
    xdata = np.asarray(group['Temperature (K)'])
    magnetic_moment_img = np.asarray(group['Mdoublebar (emu)'])
    magnetic_moment_real = np.asarray(group['Mbar (emu)'])
    # magnetic moment = susceptibility, as hac = 1 Oe
    susceptibility_img = magnetic_moment_img
    susceptibility_per_gram = susceptibility_img / 0.08526
    ydata = susceptibility_per_gram
    model = np.poly1d(np.polyfit(xdata, ydata, 10))
    polyline = np.linspace(min(xdata), max(xdata), 100)
    model_y = model(polyline)

    max_y_index = np.argmax(model_y)
    max_y = model_y[max_y_index]
    max_x = polyline[max_y_index]
    print(max_y)

    # retruen new min values
    max_values_df.loc[freq, 'mdoublebar'] = max_y
    max_values_df.loc[freq, 'Temp'] = max_x

    # plots
    plt.scatter(xdata, ydata, label=f'Group {index}')
    plt.plot(polyline, model(polyline), label=f'Fit Group {index}', linewidth=0.5)

# return minimum values
max_values_df.to_csv('PPMS_max_values.txt', sep='\t')


# Plot settings
plt.xlabel('Temperature [K]', labelpad=12, fontsize = 12)
plt.ylabel('m\" [emu/g]', labelpad=10, fontsize = 12)
plt.title('Polynomial Fit of the PPMS magnetic susceptibility measurement', fontsize = 12)
plt.legend(bbox_to_anchor=(1.01, 1.0), loc='upper left')
plt.xlim(0, 350)
plt.show()
