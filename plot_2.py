from matplotlib import pyplot as plt
from pandas import TimeGrouper

def seasonal_plot(series,plot_file):
    groups=series['2007':'2017'].groupby(TimeGrouper('A'))
    n_groups=len(groups)                                                        
    plt.clf() #automatically removed inner labels on the grid to make the plot cleaner.
    plt.figure(figsize=(10,10))
    plt.title('Seasonal per year line plots')
    #fig, ax = plt.subplots(n_groups,1, sharex='col', sharey='row')
    #fig.subplots_adjust(hspace=0.3, wspace=0.2)                                 #specify the spacing along the height and width of the figure
    i=1                                                                         #helpful for subplot
    for name, group in groups:
        plt.subplot(n_groups,1,i)
        i += 1
        group.plot()
        plt.xticks([])                                                              #in order to gain readability of data
        plt.xlabel('')
        
    plt.savefig(plot_file)