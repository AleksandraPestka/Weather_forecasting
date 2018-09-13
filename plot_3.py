from matplotlib import pyplot as plt
from pandas import DataFrame, TimeGrouper 

def time_grouper_plot(series,plot_file):
    plt.clf()
    plt.figure(figsize=(10,7))
    groups = series['2007':'2017'].groupby(TimeGrouper('A'))
    print(type(groups))
    years = DataFrame()
    for name, group in groups:
        years[name.year] = group.values
    years.boxplot()
    plt.xticks(rotation=45)
    plt.xlabel('Year')
    plt.ylabel('Temperature [°C]')
    plt.title('Temperature changes box and whisker plots')
    plt.savefig(plot_file)