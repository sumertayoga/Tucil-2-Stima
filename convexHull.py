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
bucket = bucket.iloc[: 10, [0, 1]].values
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

    for i in range(arrayLength):
        det = bucket[0, 0] * bucket[9, 1] + bucket[i, 0] * bucket[0, 1] + bucket[9, 0] * bucket[i,
                                                                                                1] - bucket[i, 0] * bucket[9, 1] - bucket[9, 0] * bucket[0, 1] - bucket[0, 0] * bucket[i, 1]
        if det > 0:
            s1 = np.append(s1, [bucket[i]], axis=0)
        elif det < 0:
            s2 = np.append(s2, [bucket[i]], axis=0)
    pmaks = farthestPoint(p1, pn, s1)
    pmaks2 = farthestPoint(p1, pn, s2)

    hull3 = DandC(pn, pmaks2, s2)
    hull4 = DandC(pmaks2, p1, s2)
    hull5 = np.append(hull3, hull4, axis=0)

    hull1 = DandC(p1, pmaks, s1)
    hull2 = DandC(pmaks, pn, s1)
    hull = np.append(hull1, hull2, axis=0)
    hull = np.append(hull, hull5, axis=0)
    #hull = np.append(hull, [DandC(pmaks, pn, s1)], axis=0)
    #hull = np.append(hull, DandC(p1, pmaks, s1), axis=0)
    #print(DandC(p1, pmaks, s1))

    # print(hull)
    print("SEMANGAT")
    return hull


def DandC(p1, p2, s):
    part = np.array([])
    for i in range(2, len(s)):
        a = p1[0] * p2[1] + s[i, 0] * p1[1] + p2[0] * s[i, 1]
        b = s[i, 0] * p2[1] + p2[0] * p1[1] + p1[0] * s[i, 1]
        det = a-b
        if det > 0:
            print(i)
    if(len(part) == 0):
        pos1 = findIndex(bucket, p1)
        pos2 = findIndex(bucket, p2)
        a = [pos1, pos2]
        hull = np.array([[pos1, pos2]])
    return hull


hull = convexHull(bucket)
plt.scatter(bucket[:, 0], bucket[:, 1])
for i in hull:
    plt.plot(bucket[i, 0], bucket[i, 1], 'r')
plt.show()

# print(s1)
# print(s2)
# print(hull)


# print(bucket[[41, 13]])
#plt.scatter(bucket[:, 0], bucket[:, 1])
#plt.plot(bucket[[0, 9], 0], bucket[[0, 9], 1], 'r')
# plt.show()
