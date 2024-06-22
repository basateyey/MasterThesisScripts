import os
import pandas as pd
import matplotlib.pyplot as plt
from brokenaxes import brokenaxes
import numpy as np

##########################
#Gewicht Progben
#Li50AL50 0.08443 g
#Li60Al40 0.08525 g
##########################

plt.rcParams['font.family'] = 'Times New Roman'


def comparing_ZFC_FC(filename1, filename2, filename3, filename4, mass):

    #fig = plt.figure(figsize=(6,4))


    # Lese die Daten aus der ersten Datei
    file_path1 = os.path.join(filename1)
    data1 = pd.read_csv(file_path1, skiprows=30)
    LongMoment1 = data1['Long Moment (emu)'] / mass
    Temp1 = data1['Temperature (K)']

    # Lese die Daten aus der zweiten Datei
    file_path2 = os.path.join(filename2)
    data2 = pd.read_csv(file_path2, skiprows=30)
    LongMoment2 = data2['Long Moment (emu)'] / mass
    Temp2 = data2['Temperature (K)']

    # Lese die Daten aus der zweiten Datei
    file_path3 = os.path.join(filename3)
    data3 = pd.read_csv(file_path3, skiprows=30)
    LongMoment3 = data3['Long Moment (emu)'] / mass
    Temp3 = data3['Temperature (K)']

    # Lese die Daten aus der zweiten Datei
    file_path4 = os.path.join(filename4)
    data4 = pd.read_csv(file_path4, skiprows=30)
    LongMoment4 = data4['Long Moment (emu)'] / mass
    Temp4 = data4['Temperature (K)']


    baxes = brokenaxes(ylims=((0,1.6),(13,14.6)))

    baxes.scatter(Temp3, LongMoment3, s = 30, color = 'black', label = 'FC')
    baxes.scatter(Temp4, LongMoment4, s = 30, fc='none', color = 'black', label='ZFC')
    baxes.scatter(Temp1, LongMoment1, s = 30, color = 'red', label = 'FC')
    baxes.scatter(Temp2, LongMoment2,s = 30, fc='none', color = 'red', label='ZFC')



    # Beschrifte die Achsen
    baxes.set_xlim(0, 400)
    #baxes.axs[0].set_yticks([0.1, 0.5, 1, 1.5])
    #baxes.axs[1].set_yticks([13.1, 13.5, 14, 14.5])
    baxes.set_xlabel('Temperature [K]', labelpad=35, fontsize = 24)
    baxes.set_ylabel('Magnetic Moment [emu/g]', labelpad=50, fontsize = 24)
    baxes.standardize_ticks(10, 50)



    baxes.legend(fontsize = 20, loc="best")
    baxes.tick_params(which='both', labelsize=25)
    plt.plot()
    plt.show()
    #plt.savefig('filename.png', dpi=600)
    
comparing_ZFC_FC('MPMS_Li0.6Al0.4 FC 10 Oe.dc.dat', 'MPMS_Li0.6Al0.4 ZFC 10 Oe.dc.dat',
                 'MPMS_Li0.6Al0.4 FC 1k Oe.dc.dat', 'MPMS_Li0.6Al0.4 ZFC 1k Oe.dc.dat', 0.08525)