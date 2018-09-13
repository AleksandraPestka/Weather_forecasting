from pandas.tools.plotting import autocorrelation_plot
from matplotlib import pyplot as plt

def autocorrelation_plot_function(series, filename):
    plt.clf()
    plt.figure(figsize=(10,7))
    plt.xticks([])
    plt.yticks([])
    plt.title('Autocorrelation plot with fewer lags of series_Krakow')
    autocorrelation_plot(series[0:36])
    plt.savefig(filename)