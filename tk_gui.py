import tkinter as tk
import training as training

# Set font
myFont = "Arial, 12"
myFont_medium = "Arial, 10"
myFont_small = "Arial, 8"


def main_gui():
    window = tk.Tk()
    window.title('Programming for Data Science')
    window.geometry("1400x750+100+100")

    # Add a label
    lbl_header = tk.Label(
        text="Assignment 2",
        font=myFont,
        height=1
    )
    lbl_header.place(x=150, y=10)
    # Add label
    lbl_dataset = tk.Label(
        text="Select a dataset: ",
        fg="navy",
        anchor="w",
        width=25,
        height=1,
        font=myFont
    )
    lbl_dataset.place(x=10, y=50)

    # Label to display output when button is clicked
    lbl_selected_dataset = tk.Label(
        text="",
        fg="red",
        anchor="w",
        width=25,
        height=1,
        font=myFont_small
    )
    lbl_selected_dataset.place(x=10, y=70)

    def select_dataset():
        selected = dataset_name.get()
        selected_dataset_string = selected + ' dataset selected'

        lbl_selected_dataset.config(text=selected_dataset_string)

    # Add variable var and 2 radio buttons
    dataset_name = tk.StringVar(value="iris")

    rb_iris = tk.Radiobutton(
        text="Iris",
        variable=dataset_name,
        value='iris',
        font=myFont,
        command=select_dataset
    )
    rb_iris.place(x=180, y=50)

    rb_breast_cancer = tk.Radiobutton(
        text="Breast Cancer",
        variable=dataset_name,
        value='breast_cancer',
        font=myFont,
        command=select_dataset
    )
    rb_breast_cancer.place(x=250, y=50)

    rb_wine = tk.Radiobutton(
        text="Wine",
        variable=dataset_name,
        value='wine',
        font=myFont,
        command=select_dataset
    )
    rb_wine.place(x=450, y=50)

    # Add label
    lbl_classifier = tk.Label(
        text="Select a Classifier: ",
        fg="navy",
        anchor="w",
        width=25,
        height=1,
        font=myFont
    )
    lbl_classifier.place(x=10, y=120)

    # Label to display output when button is clicked
    lbl_selected_classifier = tk.Label(
        text="",
        fg="red",
        width=25,
        height=1,
        font=myFont_small
    )
    lbl_selected_classifier.place(x=10, y=140)

    # Add variable var and 2 radio buttons
    classifier_name = tk.StringVar(value="KNN")

    def select_classifier():
        output = classifier_name.get() + ' classifier selected'
        lbl_selected_classifier.config(text=output)

    rb_knn = tk.Radiobutton(
        text="K-Nearest Neighbor",
        variable=classifier_name,
        value='KNN',
        font=myFont,
        command=select_classifier
    )
    rb_knn.place(x=180, y=120)

    rb_svc = tk.Radiobutton(
        text="Support Vector Classification",
        variable=classifier_name,
        value='svc',
        font=myFont,
        command=select_classifier
    )
    rb_svc.place(x=350, y=120)

    # Label to display output when button is clicked
    lbl_best_param = tk.Label(
        text="",
        fg="navy",
        width=25,
        height=1,
        font=myFont
    )
    lbl_best_param.place(x=10, y=220)

    # Label to display output when button is clicked
    lbl_accuracy = tk.Label(
        text="",
        fg="navy",
        width=25,
        height=1,
        font=myFont
    )
    lbl_accuracy.place(x=10, y=250)

    fold_value = tk.StringVar(value="5")

    lbl_folds = tk.Label(window, text="K-folds", font=myFont, fg="navy")
    lbl_folds.place(x=10, y=200)
    entry_fold = tk.Entry(window, bd=5, textvariable=fold_value)
    entry_fold.place(x=180, y=200)

    lbl_error = tk.Label(window, text="", font=myFont_small, fg="red")
    lbl_error.place(x=180, y=220)

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
                root=window,
                label_best_parameter=lbl_best_param,
                label_accuracy=lbl_accuracy
            )
        except ValueError:
            lbl_error.config(text='put a valid number > 1')

    # Run button
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
