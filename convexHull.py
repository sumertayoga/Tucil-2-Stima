from cmath import sqrt
from webbrowser import Elinks
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
import numpy as np
import pandas as pd
from sklearn import datasets
import math

data = datasets.load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['a'] = pd.DataFrame(data.target)

bucket = df[df['a'] == 0]
bucket = bucket.iloc[:, [0, 1]].values
bucket = sorted(bucket, key=lambda x: [x[0], x[1]])
bucket = np.asarray(bucket)


def findIndex(bucket, array):
    idx = 0
    for i in bucket:
        if(i[0] == array[0] and i[1] == array[1]):
            return idx
        idx += 1


def farthestPoint(point1, pointn, setOfPoint):
    # Mencari titik terjauh
    # Persamaan ax+by+c=0
    m = (point1[1] - pointn[1])/(point1[0] - pointn[0])
    a = m
    b = -1
    c = point1[1] - m*point1[0]
    maks = 0
    pmaks = []
    # Iterate in set
    for i in setOfPoint:
        temp = abs((a*i[0] + b*i[1] + c)/sqrt(a*a + b*b))
        if temp >= maks:
            maks = temp
            pmaks = i
    return pmaks


def convexHull(bucket):
    arrayLength = len(bucket)
    p1 = bucket[0]
    pn = bucket[arrayLength-1]

    # Membuat dua area baru
    # s1 untuk det positif atau dikiri
    # s2 untuk det negatif atau dikanan
    s1 = np.array([p1])
    s1 = np.append(s1, [pn], axis=0)
    s2 = s1

    for i in range(1, arrayLength-1):
        det = bucket[0, 0] * bucket[arrayLength-1, 1] + bucket[i, 0] * bucket[0, 1] + bucket[arrayLength-1, 0] * bucket[i,
                                                                                                                        1] - bucket[i, 0] * bucket[arrayLength-1, 1] - bucket[arrayLength-1, 0] * bucket[0, 1] - bucket[0, 0] * bucket[i, 1]
        if det > 0:
            s1 = np.append(s1, [bucket[i]], axis=0)
        elif det < 0:
            s2 = np.append(s2, [bucket[i]], axis=0)
    s2 = np.unique(s2, axis=0)
    s1 = np.unique(s1, axis=0)
    hull1 = DandC(p1, pn, s1)
    hull2 = DandC(pn, p1, s2)
    hull = np.append(hull1, hull2, axis=0)

    return hull


def outerPoint(p1, p2, s):
    part = np.array([p1, p2])
    for i in range(len(s)):
        a = p1[0] * p2[1] + s[i, 0] * p1[1] + p2[0] * s[i, 1]
        b = s[i, 0] * p2[1] + p2[0] * p1[1] + p1[0] * s[i, 1]
        det = a-b
        if det > 0:
            part = np.append(part, [s[i]], axis=0)
    part = np.unique(part, axis=0)
    return part


def DandC(p1, p2, s):
    if(len(s) == 2):
        #print(p1, p2)
        pos1 = findIndex(bucket, p1)
        pos2 = findIndex(bucket, p2)
        hull = np.array([[pos1, pos2]])
    else:
        pmaks = farthestPoint(p1, p2, s)
        s1 = outerPoint(p1, pmaks, s)
        s2 = outerPoint(pmaks, p2, s)
        hull1 = DandC(p1, pmaks, s1)
        hull2 = DandC(pmaks, p2, s2)
        hull = np.append(hull1, hull2, axis=0)
    return hull


hull = convexHull(bucket)
plt.scatter(bucket[:, 0], bucket[:, 1])
#plt.plot(bucket[[37, 35], 0], bucket[[37, 35], 1], 'r')
#plt.plot(bucket[[16, 39], 0], bucket[[16, 39], 1], 'r')

for i in hull:
    plt.plot(bucket[i, 0], bucket[i, 1], 'b')


bucket = df[df['a'] == 2]
bucket = bucket.iloc[:, [0, 1]].values
bucket = sorted(bucket, key=lambda x: [x[0], x[1]])
bucket = np.asarray(bucket)
hull = convexHull(bucket)
plt.scatter(bucket[:, 0], bucket[:, 1])
#plt.plot(bucket[[37, 35], 0], bucket[[37, 35], 1], 'r')
#plt.plot(bucket[[16, 39], 0], bucket[[16, 39], 1], 'r')

for i in hull:
    plt.plot(bucket[i, 0], bucket[i, 1], 'g')

bucket = df[df['a'] == 1]
bucket = bucket.iloc[:, [0, 1]].values
bucket = sorted(bucket, key=lambda x: [x[0], x[1]])
bucket = np.asarray(bucket)
hull = convexHull(bucket)
plt.scatter(bucket[:, 0], bucket[:, 1])
#plt.plot(bucket[[37, 35], 0], bucket[[37, 35], 1], 'r')
#plt.plot(bucket[[16, 39], 0], bucket[[16, 39], 1], 'r')

for i in hull:
    plt.plot(bucket[i, 0], bucket[i, 1], 'r')
plt.show()
# print(s1)
# print(s2)
# print(hull)


# print(bucket[[41, 13]])
# plt.scatter(bucket[:, 0], bucket[:, 1])
# plt.plot(bucket[[0, 9], 0], bucket[[0, 9], 1], 'r')
# plt.show()
