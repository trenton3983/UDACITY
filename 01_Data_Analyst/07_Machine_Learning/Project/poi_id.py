#!/usr/bin/python


import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from feature_format import featureFormat, targetFeatureSplit
from classifier_tester import dump_classifier_and_data
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.preprocessing import MinMaxScaler

from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score
import itertools
# Classifiers
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression


# Task 1: Select what features you'll use.
# features_list is a list of strings, each of which is a feature name.
# The first feature must be "poi".
financial_features = ['salary', 'deferral_payments', 'total_payments', 'loan_advances', 'bonus',
                      'restricted_stock_deferred', 'deferred_income', 'total_stock_value', 'expenses',
                      'exercised_stock_options', 'other', 'long_term_incentive', 'restricted_stock', 'director_fees']

email_features = ['to_messages', 'email_address', 'from_poi_to_this_person', 'from_messages',
                  'from_this_person_to_poi', 'shared_receipt_with_poi']

poi_label = ['poi']

features_list = []
features_list.extend(poi_label)
features_list.extend(financial_features)
features_list.extend(email_features)

# Load the dictionary containing the dataset
with open("final_project_dataset_unix.pkl", "rb") as data_file:
    data_dict = pickle.load(data_file)

# Create pandas DataFrame
df = pd.DataFrame.from_dict(data_dict, orient='index')
df = df.loc[:, features_list]
df = df.replace('NaN', np.nan)

# Task 2: Remove outliers
outlier_keys = ['TOTAL', 'LOCKHART EUGENE E', 'THE TRAVEL AGENCY IN THE PARK']
df = df.drop(outlier_keys)

# Task 3: Create new feature(s)
# df['ratio_bonus_salary'] = df['bonus']/df['salary']
# df['ratio_from_this_person_to_poi'] = df['from_this_person_to_poi']/df['from_messages']
# df['ratio_from_poi_to_this_person'] = df['from_poi_to_this_person']/df['to_messages']
df = df.replace(np.nan, 0.)
df['poi'] = df['poi'].replace([False, True], [0, 1])  # Convert from Boolean to int

# new_features = ['ratio_bonus_salary', 'ratio_from_this_person_to_poi', 'ratio_from_poi_to_this_person']

# features_list.extend(new_features)

# Create final features list
# remove_list = ['email_address', 'other', 'from_messages', 'to_messages', 'deferral_payments']
remove_list = ['email_address']  # because it's text
for value in remove_list:
    features_list.remove(value)

# Transform DataFrame back to dictionary and Store to my_dataset for easy export below.
my_dataset = df.to_dict(orient="index")

# Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys=True)
labels, features = targetFeatureSplit(data)


# Evaluate Current Features
def select_k_best(features: np.ndarray, labels: list, k: int, classifier=f_classif) -> np.ndarray:
    """
    Wrapper function for SelectKBest
    input:
        features (np.ndarray)
        labels (list)
        k (int or 'all'): how many features to use
        classifier (function): http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html#sklearn.feature_selection.SelectKBest
    """
    # Feature scaling with MinMaxScaler
    scaler = MinMaxScaler()
    features = scaler.fit_transform(features)
    feature_selector = SelectKBest(classifier, k)
    feature_selector.fit(features, labels)
    features = feature_selector.transform(features)
    feature_scores = list(zip(features_list[1:], feature_selector.scores_))
    score_chart_df = pd.DataFrame(feature_scores, columns=['Feature', 'Score'])
    score_chart_df = score_chart_df.sort_values(by=['Score'], ascending=False).head(k)
    new_features_list = list(score_chart_df['Feature'])
    new_features_list = ['poi'] + new_features_list
    print(score_chart_df)
    print('\n')
    return features, new_features_list


# Plot Confusion Matrix
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    From:
        http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html#sphx-glr-auto-
        examples-model-selection-plot-confusion-matrix-py
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    # print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


np.set_printoptions(precision=2)
class_names = ['Not POI', 'POI']


# Model Output
def model_response(clf, features, labels):
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.3, random_state=42)
    clf = clf.fit(features_train, labels_train)
    score_ = clf.score(features_test, labels_test)
    print('Score: ', score_)
    prediction_ = clf.predict(features_test)
    unique, counts = np.unique(prediction_, return_counts=True)
    pois_in_test_set = dict(zip(unique, counts))
    print('Test Set: ', pois_in_test_set)
    try:
        print('POIs in Test Set: ', pois_in_test_set[1])
    except KeyError:
        print('POIs in Test Set: ', 0)
    precision_ = precision_score(labels_test, prediction_)
    print('Precision: ', precision_)
    recall_ = recall_score(labels_test, prediction_)
    print('Recall: ', recall_)
    f1_ = f1_score(labels_test, prediction_)
    print('F1: ', f1_)

    # Plot non-normalized confusion matrix
    poi_confusion_matrix = confusion_matrix(labels_test, prediction_, labels=[0, 1])
    plt.figure()
    plot_confusion_matrix(poi_confusion_matrix, classes=class_names, title='Confusion Matrix')
    plt.show()

    print('Number of True Positives: ', poi_confusion_matrix[1][1])
    return clf


# Call the SelectKBest wrapper
features, features_list = select_k_best(features=features, labels=df['poi'].values, k=6)

# Task 4: Try a variety of classifiers
# Please name your classifier clf for easy export below.
# Note that if you want to do PCA or other multi-stage operations,
# you'll need to use Pipelines. For more info:
# http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.

# Decision Tree
# dt = DecisionTreeClassifier()
# param_grid = {'max_depth': [1, 2, 3, 4, 5],
#               'max_features': [1, 2, 3, 4]}
# clf = GridSearchCV(dt, param_grid, cv=5, iid=False)

# Extra Trees
# etc = ExtraTreesClassifier(n_estimators=10)
# param_grid = {'bootstrap': [True, False],
#               'max_depth': [10, 20, 30, None],
#               'max_features': ['auto', 'sqrt'],
#               'min_samples_leaf': [1, 2, 4],
#               'min_samples_split': [2, 5, 10],
#               'n_estimators': [10, 50, 100]}
# clf = GridSearchCV(etc, param_grid, cv=5, iid=False)

# AdaBoost
# abc = AdaBoostClassifier(random_state=0)
# param_grid = {'n_estimators': [50, 100],
#               'learning_rate': [0.01, 0.05, 0.1, 0.3, 1]}
# clf = GridSearchCV(abc, param_grid, cv=5, iid=False)

# Logistic Regression
# lr = LogisticRegression(solver='lbfgs', max_iter=1000)
# param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000]}
# clf = GridSearchCV(lr, param_grid, cv=5, iid=False)

# Random Forest
# rfc = RandomForestClassifier(n_estimators=20)
# param_grid = {"max_depth": [3, None],
#               "max_features": [1, 3, 10],
#               "min_samples_split": [2, 3, 10],
#               "bootstrap": [True, False],
#               "criterion": ["gini", "entropy"]}
# clf = GridSearchCV(rfc, param_grid, cv=5, iid=False)

# Naive-Bayes Gaussian
clf = GaussianNB()

# Task 5: Tune your classifier to achieve better than .3 precision and recall
# using our testing script. Check the classifier_tester.py script in the final project
# folder for details on the evaluation method, especially the test_classifier
# function. Because of the small size of the dataset, the script uses
# stratified shuffle split cross validation. For more info:
# http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!

clf = model_response(clf, features, labels)

# Task 6: Dump your classifier, dataset, and features_list so anyone can
# check your results. You do not need to change anything below, but make sure
# that the version of poi_id.py that you submit can be run on its own and
# generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)
