import os
import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt
import numpy as np

##########################
#Gewicht Progben
#Li50AL50 0.08443 g
#Li60Al40 0.08525 g
##########################

mlp.rcParams['font.family'] = 'Times New Roman'


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def comparing_hysteresis_loops(filename1, x_column, y_column, mass1, label1,
                              filename2, mass2, label2):
    # File No. 1
    file_path1 = os.path.join(filename1)
    data1 = pd.read_csv(file_path1, skiprows=30)
    data1[y_column] = data1[y_column] / mass1

    # File No. 2
    file_path2 = os.path.join(filename2)
    data2 = pd.read_csv(file_path2, skiprows=30)
    data2[y_column] = data2[y_column] / mass2

    # Plotting
    plt.plot(data1[x_column], data1[y_column], linewidth=1, label=label1, color = 'green', linestyle='-', marker='o')
    plt.plot(data2[x_column], data2[y_column], linewidth=1, label=label2, color = 'orange', linestyle='-', marker='<')

    #Plot setting
    plt.xlabel('Magnetic Field [Oe]', size = 24)
    plt.ylabel('Magnetization [emu/g]', size = 24)
    plt.title('Hysteresis Loop at 5 K', size = 24)
    plt.xticks(np.arange(-10000, 10001, 2500), size = 24)
    plt.yticks(size = 24)

    #Optional for zoom
    #plt.xlim(-250, 250)
    #plt.ylim(-5, 5)

    plt.legend(fontsize = 20)

    plt.show()

comparing_hysteresis_loops('Li0.6Al0.4 Loop 5K.dc.dat', 'Field (Oe)', 'Long Moment (emu)', 0.08526, 'Li60Al40',
                           'Li0.5Al0.5 Loop 5K iter.dc.dc.dat', 0.08443, 'Li50Al50')




