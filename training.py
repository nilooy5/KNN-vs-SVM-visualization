from sklearn import datasets, neighbors, metrics, svm
from sklearn.model_selection import train_test_split, GridSearchCV
import matplotlib.pyplot as plt


# this method does the whole calculations for modeling and matplotlib plot creation, this has been directly copied from
# tutorial 12 with minor changes where necessary
# this method takes necessary data and configurations from select_widget_values of tk_gui.py such as
# dataset name, classification name, number of folds, object of best parameter label and object of accuracy
def run_classification(dataset_name, classification_name, number_of_folds, label_best_parameter, label_accuracy):
    # here we are checking the selected radiobutton value for datasets and selecting the dataset according to
    # the selected radio button from GUI
    if dataset_name == 'iris':
        dataset = datasets.load_iris()
    elif dataset_name == 'breast_cancer':
        dataset = datasets.load_breast_cancer()
    elif dataset_name == 'wine':
        dataset = datasets.load_wine()

    # here we are checking the selected radiobutton value for classification method and selecting the
    # classification technique according to the selected classifier from gui also setting parameter & x_label for
    # respective technique which is needed for plotting (according to assignment manual)
    if classification_name == 'KNN':
        classifier = neighbors.KNeighborsClassifier()
        parameter = [{'n_neighbors': range(30)}]
        x_label = 'Value of K for KNN'
    elif classification_name == 'svc':
        classifier = svm.SVC()
        parameter = [{'gamma': [0.0001, 0.001, 0.01, 0.1, 1.0]}]
        x_label = 'Parameter C'

    # assigning training and target data and their class names
    x = dataset.data
    y = dataset.target
    class_names = dataset.target_names
    # we are splitting data into training and test sets. here we train with 80% data and
    # will be testing it with 20% data
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=0)

    # creating a GridSerachCV object from its class with selected classifier and its parameter also passing
    # the number of folds as integer value (taken from tutorial 12 directly)
    gscv_classifier = GridSearchCV(
        estimator=classifier,
        param_grid=parameter,
        cv=number_of_folds,  # k-fold cross validation
        scoring='accuracy'
    )

    # fitting the training datasets to target values in the Grid Search CV object
    gscv_classifier.fit(X_train, Y_train)

    # extracting means, standard deviation & params for each parameter
    means = gscv_classifier.cv_results_['mean_test_score']
    stds = gscv_classifier.cv_results_['std_test_score']
    results = gscv_classifier.cv_results_['params']

    # printing in console
    print("Grid scores on validation set:")
    print()

    for mean, std, param in zip(means, stds, results):
        print("Parameter: %r, accuracy: %0.3f (+/-%0.03f)" % (param, mean, std * 2))
    print()

    # replacing the best parameter label in the gui with found result from best parameter and its accuracy score
    label_best_parameter.config(
        text='Best parameter: '
             + str(gscv_classifier.best_params_)
             + ' score: {0:.2f}'.format(gscv_classifier.best_score_)
    )
    # printing the best parameter and its accuracy score on console
    print("Best parameter:"
          + str(gscv_classifier.best_params_)
          + ' & accuracy score: {0:.2f}'.format(gscv_classifier.best_score_))

    # trying to predict the dataset with test data
    y_pred = gscv_classifier.predict(X_test)

    # • Plotting confusion matrix and accuracy
    accuracy = metrics.accuracy_score(Y_test, y_pred) * 100
    # printing overall accuracy on console for debugging
    print('overall accuracy: {0:.2f}%'.format(accuracy))

    # replacing the accuracy label in the gui with found result from best parameter and its accuracy score
    label_accuracy.config(text='Accuracy = {0:.2f}%'.format(accuracy))
    # plotting the confusion matrix using gscv_classifier object & test data
    plotcm = metrics.ConfusionMatrixDisplay.from_estimator(gscv_classifier, X_test, Y_test, display_labels=class_names)
    # setting the title of the plot
    plotcm.ax_.set_title('Accuracy = {0:.2f}%'.format(accuracy))
    # showing the plot
    plt.show()

    # generalizing the the parameter name for both classification technique parameters
    # such as 'parameter' and 'gamma' from the 'parameter' that has been changed via GridSearchCV class's method
    # and assigning the parameters to x-axis
    x_axis = list(parameter[0].values())[0]
    y_axis = means  # assigning the means to y_axis of the 2nd plot
    plot_axes = plt.axes()  # creating an axes using plot.axes()

    # setting x and y label for plot
    plt.xlabel(x_label)
    plt.ylabel('CV score')
    # creating the plot using x and y axis
    plot_axes.plot(x_axis, y_axis)
    plt.show()

