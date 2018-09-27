from statsmodels.tsa.stattools import adfuller
from matplotlib import pyplot as plt
from pandas import Series
import difference
 

def Dickey_Fuller_test(series,filename_csv,filename_plot):
    X = series.values
    X = X.astype('float32')
    months_in_year = 12
    stationary =Series(difference.difference(X, months_in_year))
    stationary.index = series.index[months_in_year:]
    result = adfuller(stationary)
    print('ADF Statistic: %f' % result[0])
    print('p-value: %f' % result[1])
    print('Critical Values:')
    for key, value in result[4].items():
        print('\t%s: %.3f' % (key, value))
    stationary.to_csv(filename_csv)
    plt.clf()
    plt.figure(figsize=(10,7))
    stationary.plot()
    plt.grid()
    plt.title('Seasonal differenced temperature line plot')
    plt.ylabel('Temperature [°C]')
    plt.savefig(filename_plot)
