from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from matplotlib import pyplot as plt

def acf_pacf_function(stationary_series,filename_plot, lags=50):
    plt.clf()
    plt.figure(figsize=(10,7))
    plt.title('ACF and PACF plots of seasonally differenced temperature')
    plt.subplots_adjust(hspace=0.3)
    plt.subplot(211)
    plot_acf(stationary_series,lags=lags, ax=plt.gca())
    plt.subplot(212)
    plot_pacf(stationary_series,lags=lags, ax=plt.gca())
    plt.savefig(filename_plot)