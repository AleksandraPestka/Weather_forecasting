from math import sqrt 
from sklearn.metrics import mean_squared_error

def walk_forward_validation(test,train):
    history = [x for x in train]
    predictions = list()
    for i in range(len(test)):
        yhat = history[-1]
        predictions.append(yhat)
        history.append(test[i])
        #print('>Predicted=%.3f, Expected=%3.f' % (yhat, test[i]))
    
    mse = mean_squared_error(test, predictions)
    rmse = sqrt(mse)
    print('RMSE: %.3f' % rmse)