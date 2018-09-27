# Cheat-sheet 

- importing more modules:
```
  import module1, module2
```
- to disable all warnings emitted
```
  import warnings
  warnings.filterwarnings('ignore')
```
- how to continue a code in the next row
```
  there is a long code\
  and I continue it there
```
- you have to import necessary modules and libraries in each separate file
- Cast a pandas object to a specified dtype dtype. (Pandas imported)
```
  X = series.values
  X = X.astype('float32')
```
- The index (axis labels) of the Series.
```
  series.index
```
- Return Series as ndarray or ndarray-like depending on the dtype
```
  series.values
```
- To write sth to csv file
```
  series.to_csv(filename_csv)
```
- How to set some value to inf
```
  value=float("inf")
```
- How to format printed value
```
  print('RMSE={:0.3f}'.format(value)) #display to 3 decimal places 
```
- If there is an error for some iteration, use:
```
  try:
    code
  except:
    continue
```
- Calculate difference between some values in a dataset (value on every interval place)
```
  def difference(dataset, interval=1):                             
    diff = list()
    for i in range(interval, len(dataset)):
        value = dataset[i] - dataset[i - interval]
        diff.append(value)
    return diff
```
- ARIMA code
```
  model = ARIMA(diff, order=arima_order)
  model_fit = model.fit(trend='nc', disp=0) 
```
  The model is prepared on the training data by calling the fit() function,  turn the debug informations off by setting the disp argument to 0.
```
  yhat = model_fit.forecast()[0]      
```
  forecast() function, which performs a one-step forecast using the model.The prediction made by the model is called yhat for convention
- Mean squared error between some values 
```
   from sklearn.metrics import mean_squared_error
   ...
   mse = mean_squared_error(test, predictions)
```
- Density plot (kind='kde')
```
  residuals.plot(kind='kde', ax=plt.gca())
```
- If you want to call the function only with particular parameters, you have to set other paratemetrs in function definition=None
```
  def some_function(series, filename=None):
```
- Save an array to a binary file in NumPy .npy format
```
  np.save('file.npy', array)
```
- Copy a list (using list comprehension)
```
  history = [item for item in lst]
```
- Generate data
```
  times = list(pd.date_range('2018-09-01', periods=12, freq='MS')) # monthly data
```
- Print data in a specific format
```
   print('Month {:%Y-%m}'.format(data))
```
- Group Series by year
```
   groups = series['2007':'2017'].groupby(TimeGrouper('A'))
```
- Print cutted string
```
  print('My string is : {:0.5}'.format('verylonglongstring')
```


## Plots

- IMPORTANT thing is to clear the figure
```
  from matplotlib import pyplot as plt
  ...
  plt.clf()
```
- Set the size of figure
```
  plt.figure(figsize=(width,height))
```
- Display the grids
```
  plt.grid()
```
- Save fig
```
  plt.savefig(filename)
```
- Not to display ticks
```
  plt.xticks([]) #empty 
```
- Rotate xtricks
```
  plt.xticks(rotation=45)
```
- During ploting, label the line
```
  plt.plot(y, label="Name of y")
```
- Add legend
```
  plt.legend()
```
- Fill between y1 and y2 line
```
   plt.fill_between(x,y1,y2, color='k', alpha=.15) #the lower the alpha, the brighter area
```
- Boxplot
```
  years.boxplot()
```
