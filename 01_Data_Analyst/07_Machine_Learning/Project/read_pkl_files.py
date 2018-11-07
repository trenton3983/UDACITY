"""
Short script to print the contents of the pkl files
"""

import pickle
from pprint import pprint as pp

with open('my_feature_list.pkl', 'rb') as f:
    data = pickle.load(f, encoding='latin1')

print('Features Len: ', len(data))
print('Features: ')
pp(data)

with open('my_classifier.pkl', 'rb') as f:
    data = pickle.load(f, encoding='latin1')

print('Classifier: \n', data)

with open('my_dataset.pkl', 'rb') as f:
    data = pickle.load(f, encoding='latin1')

print('Data Len: ', len(data))
print('Data: ')
pp(data)
