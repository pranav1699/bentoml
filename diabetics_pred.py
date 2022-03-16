import string
import bentoml
from sklearn import svm
from sklearn import datasets
import numpy as np

iris = datasets.load_iris()
X, y = iris.data, iris.target

clf = svm.SVC(gamma='scale')
clf.fit(X, y)

bentoml.sklearn.save("iris_clss", clf)

iris_clf_runner = bentoml.sklearn.load_runner("iris_clss:latest")

print(iris_clf_runner.run(np.array([5.9, 3. , 5.1, 1.8])))






