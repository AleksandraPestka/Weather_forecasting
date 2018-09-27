from pandas import Series
from statsmodels.tsa.arima_model import ARIMA #importing ARIMA
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import difference
import finalize_model

def forecast(series, filename):

    X = series.values
    months_in_year = 12
    differenced = np.array(difference.difference(X, months_in_year)) #compare current value with last year value
    # fit model
    model = ARIMA(differenced, order=(6,0,2)) #adjust model to dataset
    model_fit = model.fit(disp=0)
    # multi-step out-of-sample forecast
    forecast = model_fit.forecast(steps=12)[0]
    # invert the differenced forecast to something usable
    history = [x for x in X]
    #generate monthly data
    times = list(pd.date_range('2018-09-01', periods=12, freq='MS'))

    month = 1
    for yhat in forecast:
        inverted = difference.inverse_difference(history, yhat, months_in_year)
        print('Month {:%Y-%m} Predicted temperature: {:.2f}'.format(times[month-1], inverted))
        history.append(inverted)
        month += 1

   
    #plotting
    plt.clf()
    plt.figure(figsize=(10,7))
    plt.grid()
    plt.title('Multi-step out-of-sample forecast for Kraków within 12 upcoming months')
    plt.xlabel('Date')
    plt.ylabel('Temperature [°C]')
    plt.plot(times,history[len(X):], label='Average temperature') #we want to plot only the last 12 predicted values
    plt.legend()
    RMSE=3.114
    plt.fill_between(times,[(item-RMSE) for item in history[len(X):]],[(item+RMSE) for item in history[len(X):]]  , color='k', alpha=.15)
    plt.xticks(rotation=45)
    plt.yticks([item for item in range(-6,26,2)])
    plt.savefig(filename)




