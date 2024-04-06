import pandas as pd
import numpy as np
import csv
import math
import matplotlib. pyplot as plt
import matplotlib
from sklearn.preprocessing import MinMaxScaler
from keras.layers import LSTM, Dense, Dropout
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.dates as mandates
from sklearn.preprocessing import MinMaxScaler
from sklearn import linear_model
from keras.models import Sequential
from keras.layers import Dense
import keras.backend as K
from keras.callbacks import EarlyStopping
from keras.optimizers import Adam
from keras.models import load_model
from keras.layers import LSTM
from keras.utils.vis_utils import plot_model
from sklearn.preprocessing import MinMaxScaler


def mse(pre, act):
    er = 0
    for i in range(len(pre)):
        er +=(pre[i][0]-act[i])**2
    er = er/len(pre)
    er = er**(1/2)
    er = er/(sum(act)/len(act))
    return (1-er)*100

def add_data(filename, data):
    to_add = []
    with open(filename, mode='r')as csvfile:
        csvFile = csv.reader(csvfile)
        for lines in csvFile:
            to_add.append(lines)

    # data rows of csv file
    rows = [data]

    for i in rows:
        to_add.append(i)

    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the data rows
        for j in to_add:
            if (j == []):
                continue
            else:
                csvwriter.writerow(j)

to_add = []
for k in range(100):
    data = pd.read_csv("data_age.csv")
    data = data.sample(frac=1)
    #Set Target Variable
    output_var = pd.DataFrame(data['Retirement'])
    #Selecting the Features
    features = [
        "Debut Age (yrs)","No of innings",	"cummulative runs", "number of fiftees"]

    scaler = MinMaxScaler()
    feature_transform = scaler.fit_transform(data[features])
    feature_transform= pd.DataFrame(columns=features, data=feature_transform, index=data.index)
    feature_transform.head()
    timesplit= TimeSeriesSplit(n_splits=4)
    for train_index, test_index in timesplit.split(feature_transform):
            X_train, X_test = feature_transform[:len(train_index)], feature_transform[len(train_index): (len(train_index)+len(test_index))]
            y_train, y_test = output_var[:len(train_index)].values.ravel(), output_var[len(train_index): (len(train_index)+len(test_index))].values.ravel()
    trainX =np.array(X_train)
    testX =np.array(X_test)
    X_train = trainX.reshape(X_train.shape[0], 1, X_train.shape[1])
    X_test = testX.reshape(X_test.shape[0], 1, X_test.shape[1])
    lstm = Sequential()
    lstm.add(LSTM(32, input_shape=(1, trainX.shape[1]), activation='relu', return_sequences=False))
    lstm.add(Dense(5))
    lstm.add(Dense(1))
    lstm.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy']
                )
    # plot_model(lstm, show_shapes=True, show_layer_names=True)
    history=lstm.fit(X_train, y_train, epochs=500, batch_size=12, verbose=0, shuffle=False)
    y_pred= lstm.predict(X_test, verbose = 0)
    mean_sqaure_error = mse(y_pred, y_test)
    print(mean_sqaure_error)
    # plt.plot(y_test, label='True Value')
    # plt.plot(y_pred, label='LSTM Value')
    # plt.title("Prediction by LSTM")
    # plt.xlabel('Player')
    # plt.ylabel('Retirement Age')
    # plt.legend()
    # plt.show()
    
    # add = []
    # for i in y_pred:
    #     add.append(i[0])
    # add_data("predicted_age.csv",add)
    add_data("accuracy_age.csv",[mean_sqaure_error])
