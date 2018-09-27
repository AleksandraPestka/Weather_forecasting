from statsmodels.tsa.arima_model import ARIMA

def function_to_avoid_bug():
    
    def __getnewargs__(self):
        return ((self.endog),(self.k_lags, self.k_diff, self.k_ma))

    ARIMA.__getnewargs__ = __getnewargs__
