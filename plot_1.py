from matplotlib import pyplot as plt

def basic_plot(series,plot_file):
    plt.clf()
    plt.figure(figsize=(10,7))
    plt.title('Temperature over the years in Kraków- Obserwatorium')
    plt.ylabel('Temperature [°C]')
    series.plot()
    plt.grid()
    plt.savefig(plot_file)