"""
http://scikit-learn.org/stable/modules/cross_validation.html
http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
"""

from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm

iris = datasets.load_iris()
features = iris.data
labels = iris.target

features_train, features_test, labels_train, labels_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)

clf = svm.SVC(kernel="linear", C=1.)
clf.fit(features_train, labels_train)

print(clf.score(features_test, labels_test))
