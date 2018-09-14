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











