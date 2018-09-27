def split_into_train_and_test_sets(series):
    X=series.values
    X=X.astype('float32')                                                       #make sure that it's saved as float
    train_size=int(len(X)*0.5)
    train,test=X[0:train_size],X[train_size:]                                   #50% train, 50% test and convert into list
    return train,test
