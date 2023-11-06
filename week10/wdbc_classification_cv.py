import numpy as np
from sklearn import (datasets, tree, model_selection, svm)
from sklearn.ensemble import (RandomForestClassifier, BaggingClassifier, AdaBoostClassifier)
from sklearn.linear_model import (SGDClassifier)

if __name__ == '__main__':
    # Load a dataset
    wdbc = datasets.load_breast_cancer()

    # Train a model
    cv_result = []
    model = [tree.DecisionTreeClassifier(), svm.SVC(), SGDClassifier(), RandomForestClassifier(), BaggingClassifier(), AdaBoostClassifier()]
    for classifier in model:
        cv_result.append(model_selection.cross_validate(classifier, wdbc.data, wdbc.target, cv=5, return_train_score=True))
    name = ["Decision tree", "SVM", "SGD", "RandomForest", "Bagging", "Adaboost"]
    best_score = 0
    best_classifier = ""
    for element in zip(cv_result, name):
        acc_train = np.mean(element[0]['train_score'])
        acc_test = np.mean(element[0]['test_score'])
        score = max(10 + 100 * (acc_test - 0.9), 0)
        print(f'* {element[1]} : Accuracy @ training data: {acc_train:.3f}')
        print(f'* {element[1]} : Accuracy @ test data: {acc_test:.3f}')
        print(f'* {element[1]} : Your score: {score:.0f}')
        if best_score < score:
            best_score = score
            best_classifier = element[1]
    print(f'best classifier : {best_classifier} / score : {best_score:.0f}')