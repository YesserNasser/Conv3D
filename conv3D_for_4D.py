# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 12:12:19 2019
@author: Yesser
"""

from keras.layers import Conv3D, MaxPool3D, Flatten, Dense
from keras.layers import Dropout, Input, BatchNormalization
from sklearn.metrics import confusion_matrix, accuracy_score
from plotly.offline import iplot, init_notebook_mode
from keras.losses import categorical_crossentropy
from keras.optimizers import Adadelta
import plotly.graph_objs as go
from matplotlib.pyplot import cm
from keras.models import Model
import numpy as np
import keras
import h5py


with h5py.File('../Input/full_dataset_vectors.h5', 'r') as dataset:
    


