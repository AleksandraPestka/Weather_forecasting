from statsmodels.tsa.arima_model import ARIMA
import difference
from sklearn.metrics import mean_squared_error
from pandas import DataFrame, Series
from math import sqrt
from matplotlib import pyplot as plt

def inverse_difference(history, yhat, interval=1):
    return yhat + history[-interval]

def evaluate_arima_model(series_values, arima_order, filename=None):
    series_values = series_values.astype('float32')
    train_size = int(len(series_values) * 0.50)
    train, test = series_values[0:train_size], series_values[train_size:]
    history = [x for x in train]
    predictions = list()
    for t in range(len(test)):
        months_in_year = 12
        diff = Series(difference.difference(history, months_in_year))
        model = ARIMA(diff, order=arima_order)
        model_fit = model.fit(trend='nc', disp=0) #The model is prepared on the training data by calling the fit() function,  turn the debug informations off by setting the disp argument to 0.
        yhat = model_fit.forecast()[0] #forecast() function, which performs a one-step forecast using the model.The prediction made by the model is called yhat for convention
        yhat = inverse_difference(history, yhat, months_in_year)
        predictions.append(yhat)
        history.append(test[t])
        
    residuals = [test[i]-predictions[i] for i in range(len(test))]
    residuals = DataFrame(residuals)
    print(residuals.describe())
    # plot
    plt.clf()
    plt.figure(figsize=(10,7))
    plt.title('Distribution of the residuals')
    plt.subplot(211)
    residuals.hist(ax=plt.gca())
    plt.subplot(212)
    residuals.plot(kind='kde', ax=plt.gca())
    plt.savefig(filename)
    
    mse = mean_squared_error(test, predictions)
    rmse = sqrt(mse)
    return rmse
