from webbrowser import Elinks
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
import numpy as np
import pandas as pd
from sklearn import datasets


data = datasets.load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['a'] = pd.DataFrame(data.target)

bucket = df[df['a'] == 0]
bucket = bucket.iloc[: 10, [0, 1]].values
bucket = sorted(bucket, key=lambda x: [x[0], x[1]])
bucket = np.asarray(bucket)

# Mengambil dua titik dengan jarak terjauh
p1 = bucket[0]
pn = bucket[9]

# Membuat dua area baru
# s1 untuk det positif atau dikiri
# s2 untuk det negatif atau dikanan
s1 = np.array([p1])
s1 = np.append(s1, [pn], axis=0)
s2 = s1

for i in range(1, 9):
    det = bucket[0, 0] * bucket[9, 1] + bucket[i, 0] * bucket[0, 1] + bucket[9, 0] * bucket[i,
                                                                                            1] - bucket[i, 0] * bucket[9, 1] - bucket[9, 0] * bucket[0, 1] - bucket[0, 0] * bucket[i, 1]
    if det > 0:
        s1 = np.append(s1, [bucket[i]], axis=0)
        print("pos")
    elif det < 0:
        s2 = np.append(s2, [bucket[i]], axis=0)
        print("neg")
    else:
        print("nol")

print(s1)
print(s2)

#print(bucket[[41, 13]])
plt.scatter(bucket[:, 0], bucket[:, 1])
plt.plot(bucket[[0, 9], 0], bucket[[0, 9], 1], 'r')
plt.show()
