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

def comparing_Magnetization_saturation(filename1, x_column, y_column, mass1,
                              filename2, mass2):


    #File No.1
    file_path1 = os.path.join(filename1)
    data1 = pd.read_csv(file_path1, skiprows=30)
    data1[y_column] = data1[y_column] / mass1

    # File No. 2
    file_path2 = os.path.join(filename2)
    data2 = pd.read_csv(file_path2, skiprows=30)
    data2[y_column] = data2[y_column] / mass2




    # Plotting
    #plt.rcParams['figure.figsize'] = [9,7]
    plt.plot(data1[x_column], data1[y_column], label='Li50Al50', color = 'orange', linestyle='-', marker='o')
    plt.plot(data2[x_column], data2[y_column], label='Li60Al40', color = 'green', linestyle='-', marker='o')


    # Plot settings
    plt.xlabel('Temperature [K]', fontsize =24)
    plt.ylabel('Saturation Magnetization [emu/g]', fontsize =24, labelpad=15)
    plt.xticks(np.arange(0, 350.01, 50))
    plt.yticks(np.arange(13, 30, 2))
    plt.xticks(fontsize=24)
    plt.yticks(fontsize=24)
    plt.xlim(0, 351)
    plt.legend(fontsize = 20)

    plt.show()

comparing_Magnetization_saturation('LiAl0.5 Ms(T).dc.dat', 'Temperature (K)', 'Long Moment (emu)', 0.08443, 'Li0.6Al0.4 Ms(T).dc.dat', 0.08525)

def comparing_Magnetization_saturation_with_Lit(filename1, x_column, y_column,
                              filename2, mass2,
                              filename3, mass3):

    #Plot No. 1
    file_path1 = os.path.join(filename1)
    data1 = pd.read_csv(file_path1, skiprows=30)
    data1[y_column] = data1[y_column]

    #Plot No. 2
    file_path2 = os.path.join(filename2)
    data2 = pd.read_csv(file_path2, skiprows=30)
    data2[y_column] = data2[y_column] / mass2

    #Plot No. 3
    file_path3 = os.path.join(filename3)
    data3 = pd.read_csv(file_path3, skiprows=30)
    data3[y_column] = data3[y_column] / mass3


    # Plotting
    plt.rcParams['figure.figsize'] = [9, 7]
    plt.plot(data1[x_column], data1[y_column], label = 'Liu(2019)', linestyle='-', marker='o')
    plt.plot(data2[x_column], data2[y_column], label='Li50Al50', linestyle='-', marker='o')
    plt.plot(data3[x_column], data3[y_column], label='Li60Al40', linestyle='-', marker='o')

    # Plot settings
    plt.xlabel('Temperature [K]', fontsize =24, labelpad= 10)
    plt.ylabel('Saturation Magnetization [emu/g]', fontsize =24, labelpad= 15)
    plt.xticks(np.arange(0, 350.01, 50))
    plt.yticks(np.arange(20, 100, 10))
    plt.xticks(fontsize=24)
    plt.yticks(fontsize=24)
    plt.ylim(10, 70)
    plt.xlim(0, 351)
    plt.legend(fontsize=20, loc='right')

    plt.show()

#comparing_Magnetization_saturation_with_Lit('MsValuesLiu2019.dat', 'Temperature (K)', 'Long Moment (emu)', 'LiAl0.5 Ms(T).dc.dat', 0.08443, 'Li0.6Al0.4 Ms(T).dc.dat', 0.08525)



