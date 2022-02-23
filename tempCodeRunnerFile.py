from sklearn import datasets
import pandas as pd
import numpy as np

data = datasets.load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['a'] = pd.DataFrame(data.target)

bucket = df[df['a'] == 0]
bucket = bucket.iloc[:, [0, 1]].values
bucket = np.sort(bucket, axis=0)
print(bucket)
