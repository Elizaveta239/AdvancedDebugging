"""

Code insight with Scientific Libraries

Smart code completion and code editing
Quick docs for np.zeros() (F1)
Show parameters Cmd P

"""
from random import randint

import numpy as np
from sklearn.tree import DecisionTreeRegressor
import pandas as pd


def get_features_targets(data):
    features = np.zeros((data.shape[0], 4))
    features[:, 0] = data['u'] - data['g']
    features[:, 1] = data['g'] - data['r']
    features[:, 2] = data['r'] - data['i']
    features[:, 3] = data['i'] - data['z']

    return features, data['redshift']


def train_model(feat, targs):
    # initialize model
    dtr = DecisionTreeRegressor()
    # train the model
    dtr.fit(feat, targs)
    # make predictions using the same features
    predictions = dtr.predict(feat)
    return predictions


def generate_df():
    size = 100
    return pd.DataFrame({'row': [randint(0, 100) for _ in range(size)],
                         'One_X': [randint(0, 100) for _ in range(size)],
                         'One_Y': [randint(0, 100) for _ in range(size)],
                         'Two_X': [randint(0, 100) for _ in range(size)],
                         'Two_Y': [randint(0, 100) for _ in range(size)]})


loaded_data = np.load('../data/sdss_galaxy_colors.npy')
features, targets = get_features_targets(loaded_data)
generated_df = generate_df()

predicts = train_model(features, targets)

# print out the first 4 predicted redshifts
print(predicts[:4])
