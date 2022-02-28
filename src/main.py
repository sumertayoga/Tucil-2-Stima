# Berikut merupakan contoh visualisasi hasil convexHull
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
import myConvexHull as ch

# create a DataFrame
data = datasets.load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
df.head()
plt.figure(figsize=(10, 6))
colors = ['b', 'r', 'g']
plt.title('Sepal Length vs Sepal Width')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    print(bucket)
    bucket = bucket.iloc[:, [0, 1]].values
    # bagian ini diganti dengan hasil implementasi
    hull = ch.convexHull(bucket)
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    for simplex in hull:
        # Simple disini isinya pasangan urutan titik di bucket
        # pasangan tersebut akan dihubungkan garis/diplotkan
        plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i])
plt.legend()
plt.show()
