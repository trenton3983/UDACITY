#!/usr/bin/python

""" lecture and example code for decision tree unit """


from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData
from sklearn.metrics import accuracy_score
# from classifyDT import classify
from sklearn import tree
from pprint import pprint as pp

features_train, labels_train, features_test, labels_test = makeTerrainData()

# the classify() function in classifyDT is where the magic
# happens--fill in this function in the file 'classifyDT.py'!

min_samples = [2, 10, 20, 30, 40, 50]
acc_samples = {}

for sample in min_samples:

    clf = tree.DecisionTreeClassifier(min_samples_split=sample)
    clf = clf.fit(features_train, labels_train)

    # clf = classify(features_train, labels_train)

    pred = clf.predict(features_test)

    accuracy = accuracy_score(pred, labels_test)

    acc_samples[f'acc_min_samples_split_{sample}'] = accuracy

    print(f'Accuracy for min_samples_split = {sample}: {accuracy}')

    prettyPicture(clf, features_test, labels_test, pic_name=f'test_{sample}')
    output_image(f"test_{sample}.png", "png", open(f"test_{sample}.png", "rb").read())

    print('\n')


def submit_accuracies():
    return acc_samples


if __name__ == "__main__":

    pp(submit_accuracies())
