from prep_terrain_data import makeTerrainData
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC


features_train, labels_train, features_test, labels_test = makeTerrainData()

# SVM
# we handle the import statement and SVC creation for you here

clf = SVC(kernel="linear")

# now your job is to fit the classifier
# using the training features/labels, and to
# make a set of predictions on the test data

clf.fit(features_train, labels_train)

# store your predictions in a list named pred

pred = clf.predict(features_test)

acc = accuracy_score(pred, labels_test)


def submitAccuracy():
    return acc


if __name__ == "__main__":

    print(submitAccuracy())
