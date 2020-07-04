import numpy as np
from sklearn.cluster import dbscan, KMeans
from distance import levenshtein
data = ["ACCTCCTAGAAG", "ACCTCCTAGAAGD", "GAATATTAGGCCGA"]

# data = open('id.txt', encoding='utf-8').read().split('\n')

def lev_metric(x, y):
    i, j = int(x[0]), int(y[0])  # extract indices
    return levenshtein(data[i], data[j])


X = np.arange(len(data)).reshape(-1, 1)
r = dbscan(X, metric=lev_metric, min_samples=2)
print('X', X)
print('R', r)