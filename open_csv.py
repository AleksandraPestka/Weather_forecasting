from pandas import Series
def open_file(filename,data_name=None,validation_name=None):
    series=Series.from_csv(filename,header=0)                                   #to ignore the first row
    print(series.describe())
    split_point=round(len(series)*0.89)                                         #validation dataset is about 11% of the original dataset
    dataset,validation=series[0:split_point],series[split_point:]               #split dataset into model development and validation
    #print('Dataset: {}, Validation: {} '.format((len(dataset)),len(validation)))
    dataset.to_csv(data_name)
    validation.to_csv(validation_name)
    return series