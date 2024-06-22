import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import data
data = pd.read_csv('PPMS_Li0.6Al0.4Fe5O8 Xac.dat', skiprows=21)

# Group group data
grouped_data = {i: g for i, (freq, g) in enumerate(data.groupby('Frequency (Hz)'), 1)}

# Def Indexing
def get_group_data(index):
    if index in grouped_data:
        group = grouped_data[index]
        xdata = np.asarray(group['Temperature (K)'])
        magnetic_moment = np.asarray(group['Mdoublebar (emu)'])
        susceptibility = magnetic_moment/-0.084
        susceptibility_per_gram = susceptibility / 0.08526
        ydata = susceptibility_per_gram
        # Return the frequency value as well
        freq = group['Frequency (Hz)'].iloc[0]
        return xdata, ydata, freq
    else:
        print("Invalid group index.")
        return None, None, None

# Select group
index_to_select = 3
xdata, ydata, frequency = get_group_data(index_to_select)

# Check if data is valid before proceeding
if xdata is not None and ydata is not None:
    # Fit polynomial models up to degree 15
    model1 = np.poly1d(np.polyfit(xdata, ydata, 10))

    # Plot data
    polyline = np.linspace(5, 345, 100)
    plt.scatter(xdata, ydata)

    # Plot fit
    plt.plot(polyline, model1(polyline), color='green', label=f'Freq: {frequency} Hz')
    plt.xlim(0, 350)
    plt.legend()

    plt.show()

    print(model1)

    # Def R value
    def adjR(x, y, degree):
        results = {}
        coeffs = np.polyfit(x, y, degree)
        p = np.poly1d(coeffs)
        yhat = p(x)
        ybar = np.sum(y)/len(y)
        ssreg = np.sum((yhat-ybar)**2)
        sstot = np.sum((y - ybar)**2)
        results['r_squared'] = 1- (((1-(ssreg/sstot))*(len(y)-1))/(len(y)-degree-1))

        return results


    adj_r_squared = adjR(xdata, ydata, 15)
    print(f'Adjusted R-squared: {adj_r_squared["r_squared"]}')
else:
    print("No data available for the selected index.")
