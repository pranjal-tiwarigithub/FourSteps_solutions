import numpy as np 

np.mean([1,2,3,4])






import pandas as pd 

from sklearn.datasets import load_iris


iris = load_iris()

x = iris.data 

y = iris.feature_names

df = pd.DataFrame(x, columns= y)

df.head()


