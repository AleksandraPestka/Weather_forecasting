from pandas import Series
from statsmodels.tsa.arima_model import ARIMA, ARIMAResults
from scipy.stats import boxcox
import numpy as np
import difference
from matplotlib import pyplot as plt
from math import sqrt
from sklearn.metrics import mean_squared_error


def finalize(filename=None):
    dataset= Series.from_csv('Krakow_data.csv')
    X = dataset.values.astype('float32')
    history = [x for x in X]
    months_in_year = 12
    diff = difference.difference(X, months_in_year)
    model = ARIMA(diff, order=(6, 0, 2))
    model_fit = model.fit(trend='nc', disp=0)
    model_fit.save('model.pkl')
    np.save('model_bias.npy', [0.237574])
    validation = Series.from_csv('Krakow_validation.csv')
    y = validation.values.astype('float32')
    model_fit = ARIMAResults.load('model.pkl')
    bias = np.load('model_bias.npy')
    predictions = list()
    yhat = float(model_fit.forecast()[0])
    yhat = bias + difference.inverse_difference(history, yhat, months_in_year)
    predictions.append(yhat)
    history.append(y[0])
    label_for_x=['2017-06', '2017-07', '2017-08','2017-09','2017-10','2017-11','2017-12','2018-01','2018-02','2018-03','2018-04','2018-05','2018-06','2018-07','2018-08']
    print('For month: {} Predicted= {} , Expected= {}'.format(label_for_x[0],str(yhat), str(y[0])))
    
    
    
    for i in range(1, len(y)):
        months_in_year = 12
        diff = difference.difference(history, months_in_year)
        model = ARIMA(diff, order=(6,0,2))
        model_fit = model.fit(trend='nc', disp=0)
        yhat = model_fit.forecast()[0]
        yhat = bias + difference.inverse_difference(history, yhat, months_in_year)
        predictions.append(yhat)
        obs = y[i]
        history.append(obs)
        print('For month: {} Predicted= {} , Expected= {}'.format(label_for_x[i],str(yhat), str(obs)))
        
    mse = mean_squared_error(y, predictions)
    rmse = sqrt(mse)
    print('RMSE: {:0.3f}'.format(rmse))
   
    
    plt.figure(figsize=(10,7))
    plt.title('Forecast for temperature in Kraków')
    plt.xlabel('Data')
    plt.ylabel('Temperature')
    plt.xticks(list(range(0,15)), label_for_x)
    plt.xticks(rotation=45)
    plt.grid()
    plt.plot(y, label="Observational values")
    plt.plot(predictions, color='red', label="Foreseen values")
    plt.legend()
    plt.savefig(filename)
    
    return rmse
    