import tkinter

import numpy as np
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from sklearn import datasets, neighbors, metrics, mixture, svm
from sklearn.model_selection import train_test_split, GridSearchCV
import matplotlib.pyplot as plt


def run_classification(dataset_name, classification_name, number_of_folds, root, label_best_parameter, label_accuracy):
    if dataset_name == 'iris':
        dataset = datasets.load_iris()
    elif dataset_name == 'breast_cancer':
        dataset = datasets.load_breast_cancer()
    elif dataset_name == 'wine':
        dataset = datasets.load_wine()

    if classification_name == 'KNN':
        classifier = neighbors.KNeighborsClassifier()
        parameter = [{'n_neighbors': range(30)}]
    elif classification_name == 'svc':
        classifier = svm.SVC()
        parameter = [{'gamma': [0.0001, 0.001, 0.01, 0.1, 1.0]}]

    x = dataset.data
    y = dataset.target
    class_names = dataset.target_names
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=0)

    gscv_classifier = GridSearchCV(
        estimator=classifier,
        param_grid=parameter,
        cv=number_of_folds,  # k-fold cross validation
        scoring='accuracy'
    )

    gscv_classifier.fit(X_train, Y_train)

    means = gscv_classifier.cv_results_['mean_test_score']
    stds = gscv_classifier.cv_results_['std_test_score']
    results = gscv_classifier.cv_results_['params']

    print("Grid scores on validation set:")
    print()

    for mean, std, param in zip(means, stds, results):
        print("Parameter: %r, accuracy: %0.3f (+/-%0.03f)" % (param, mean, std * 2))
    print()
    label_accuracy.config(text='Best parameter: ' + str(gscv_classifier.best_params_))
    label_best_parameter.config(text='Accuracy (%): ' + str(gscv_classifier.best_score_))
    print("Best parameter:", gscv_classifier.best_params_)
    print("accuracy: %0.3f" % gscv_classifier.best_score_)

    y_pred = gscv_classifier.predict(X_test)
    # • Plot confusion matrix and accuracy
    accuracy = metrics.accuracy_score(Y_test, y_pred) * 100
    plotcm = metrics.ConfusionMatrixDisplay.from_estimator(gscv_classifier, X_test, Y_test, display_labels=class_names)
    plotcm.ax_.set_title('Accuracy = {0:.2f}%'.format(accuracy))
    plt.show()

    # fig2 = Figure(figsize=(3, 3), dpi=100)
    # t2 = np.arange(0, 3, .01)
    # fig2.add_subplot(111).plot(y_pred)
    #
    # canvas2 = FigureCanvasTkAgg(fig2, master=root)  # A tk.DrawingArea.
    # canvas2.draw()
    # canvas2.get_tk_widget().pack(side=tkinter.TOP, expand=0)

    # toolbar2 = NavigationToolbar2Tk(canvas2, root)
    # toolbar2.update()
    # canvas2.get_tk_widget().pack(side=tkinter.TOP, expand=0)

    x_axis = list(parameter[0].values())[0]
    y_axis = means
    line_style = 'b--'
    plot_axes = plt.axes()
    plot_axes.plot(x_axis, y_axis, line_style)
    plt.show()

    # fig3 = Figure(figsize=(3, 3), dpi=100)
    # t3 = np.arange(0, 3, .01)
    # fig3.add_subplot(111).plot(x_axis, y_axis)
    #
    # canvas3 = FigureCanvasTkAgg(fig3, master=root)  # A tk.DrawingArea.
    # canvas3.draw()
    # canvas3.get_tk_widget().pack(side=tkinter.TOP, expand=0)

