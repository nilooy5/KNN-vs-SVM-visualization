import tkinter as tk
import training as training

# some font configurations for GUI
myFont = "Arial, 12"
myFont_big = "Arial, 15 bold"
myFont_medium = "Arial, 10"
myFont_small = "Arial, 8"


# main method that contains the tkinter widgets and methods
def main_gui():
    window = tk.Tk()
    window.title('Programming for Data Science')
    window.geometry("700x500+400+100")

    # a label for the header
    lbl_header = tk.Label(
        text="Assignment 2 by Fazal Mahmud Niloy (u3228358)",
        font=myFont_big,
        height=1
    )
    lbl_header.place(x=150, y=10)   # placement of header label

    # a label for prompting to select dataset
    lbl_dataset = tk.Label(
        text="Select a dataset: ",
        fg="navy",
        anchor="w",
        width=25,
        height=1,
        font=myFont
    )
    lbl_dataset.place(x=10, y=50)   # placement of the previous label

    # label to display which dataset is selected
    lbl_selected_dataset = tk.Label(
        text="",
        fg="red",
        anchor="w",
        width=25,
        height=1,
        font=myFont_small
    )
    lbl_selected_dataset.place(x=10, y=70)

    # this method gets the string value from dataset_name and assigns it in lbl_selected_dataset label
    def select_dataset():
        selected = dataset_name.get()
        selected_dataset_string = selected + ' dataset selected'

        lbl_selected_dataset.config(text=selected_dataset_string)   # assigning the selected dataset value to this label

    # Add variable var and 2 radio buttons
    dataset_name = tk.StringVar(value="iris")   # a string value for the selected dataset initially set to 'iris'

    # radio button configuration for iris dataset
    rb_iris = tk.Radiobutton(
        text="Iris",
        variable=dataset_name,
        value='iris',
        font=myFont,
        command=select_dataset
    )
    rb_iris.place(x=180, y=50)

    # radio button configuration for breast_cancer dataset
    rb_breast_cancer = tk.Radiobutton(
        text="Breast Cancer",
        variable=dataset_name,
        value='breast_cancer',
        font=myFont,
        command=select_dataset
    )
    rb_breast_cancer.place(x=250, y=50)

    # radio button configuration for wine dataset
    rb_wine = tk.Radiobutton(
        text="Wine",
        variable=dataset_name,
        value='wine',
        font=myFont,
        command=select_dataset
    )
    rb_wine.place(x=450, y=50)

    # A label to prompt the user to select a classifier
    lbl_classifier = tk.Label(
        text="Select a Classifier: ",
        fg="navy",
        anchor="w",
        width=25,
        height=1,
        font=myFont
    )
    lbl_classifier.place(x=10, y=120)

    # Label to display which classifier is currently selected
    lbl_selected_classifier = tk.Label(
        text="",
        fg="red",
        width=20,
        height=1,
        font=myFont_small
    )
    lbl_selected_classifier.place(x=10, y=140)

    # a string variable value for the radio buttons of classifiers initial value set to KNN
    classifier_name = tk.StringVar(value="KNN")

    # this method gets the value from classifier_name stringVar and assigns it to lbl_selected_classifier
    def select_classifier():
        output = classifier_name.get() + ' classifier selected'
        lbl_selected_classifier.config(text=output)

    # radio button for knn classification
    rb_knn = tk.Radiobutton(
        text="K-Nearest Neighbor",
        variable=classifier_name,
        value='KNN',
        font=myFont,
        command=select_classifier
    )
    rb_knn.place(x=180, y=120)

    # radio button for support vector classification
    rb_svc = tk.Radiobutton(
        text="Support Vector Classification",
        variable=classifier_name,
        value='svc',
        font=myFont,
        command=select_classifier
    )
    rb_svc.place(x=350, y=120)

    # label to display the best parameter for a selected dataset and classifier technique
    lbl_best_param = tk.Label(
        text="",
        fg="navy",
        width=50,
        height=1,
        font=myFont_big
    )
    lbl_best_param.place(x=10, y=350)

    # label to display the accuracy for a selected dataset and classifier technique
    lbl_accuracy = tk.Label(
        text="",
        fg="navy",
        width=50,
        height=1,
        font=myFont_big
    )
    lbl_accuracy.place(x=10, y=380)

    # setting initial fold_value string variable value for TK Entry Box as 5
    fold_value = tk.StringVar(value="5")

    # a label that prompts the user that the entry box is for k-fold numbers
    lbl_folds = tk.Label(window, text="K-folds", font=myFont, fg="navy")
    lbl_folds.place(x=10, y=200)

    # an entry box for inputting number of k-folds
    entry_fold = tk.Entry(window, bd=5, textvariable=fold_value)
    entry_fold.place(x=180, y=200)

    # an additional label that pops a message if there is an error entering the fold number values
    lbl_error = tk.Label(window, text="", font=myFont_small, fg="red")
    lbl_error.place(x=180, y=220)

    # this method is triggered when the run model button is pressed
    # this will show and handle error if anything other than number that are bigger than 1 is inputted
    # this will also pass the necessary data and configurations such as
    # dataset name, classification name, number of folds, object of best parameter label and object of accuracy to
    # run_classification() of training.py module
    def select_widget_values():
        lbl_error.config(text="")
        try:
            folds = int(fold_value.get())
            select_dataset()
            select_classifier()
            training.run_classification(
                dataset_name=dataset_name.get(),
                classification_name=classifier_name.get(),
                number_of_folds=folds,
                label_best_parameter=lbl_best_param,
                label_accuracy=lbl_accuracy
            )
        except ValueError:
            lbl_error.config(text='put a valid number > 1')

    # Run button configuration. it runs the select_widget_values method
    button = tk.Button(
        text="Run Model",
        fg="black",
        bg="white",
        width=10,
        height=1,
        font=myFont,
        command=select_widget_values
    )

    button.place(x=10, y=300)

    window.mainloop()
