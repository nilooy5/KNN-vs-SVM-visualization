import tkinter as tk

window = tk.Tk()
window.title('Programming for Data Science')
window.geometry("1400x750+100+100")

# Set font
myFont = "Arial, 16"
# Add a label
lbl_header = tk.Label(text="A Simple GUI App",
                      font=myFont,
                      height=1)
lbl_header.place(x=150, y=10)
# Add label
lbl_dataset = tk.Label(text="Select a dataset: ",
                       fg="navy",
                       anchor="w",
                       width=25,
                       height=1,
                       font=myFont)
lbl_dataset.place(x=10, y=50)


#################################

def select_dataset():
    selected = dataset_name.get()
    if selected == 'iris':
        output = 'Iris selected'
    elif selected == 'breast_cancer':
        output = 'Breast Cancer selected'
    elif selected == 'wine':
        output = 'Wine selected'
    else:
        output = "Please select a dataset"

    lbl_selected_dataset.config(text=output)


#################################


# Add variable var and 2 radio buttons
dataset_name = tk.StringVar(value="iris")

rb_iris = tk.Radiobutton(text="Iris",
                         variable=dataset_name,
                         value='iris',
                         font=myFont,
                         command=select_dataset)
rb_iris.place(x=180, y=50)

rb_breast_cancer = tk.Radiobutton(text="Breast Cancer",
                                  variable=dataset_name,
                                  value='breast_cancer',
                                  font=myFont,
                                  command=select_dataset)
rb_breast_cancer.place(x=250, y=50)

rb_wine = tk.Radiobutton(text="Wine",
                         variable=dataset_name,
                         value='wine',
                         font=myFont,
                         command=select_dataset)
rb_wine.place(x=450, y=50)

# Label to display output when button is clicked
lbl_selected_dataset = tk.Label(text="",
                                fg="navy",
                                anchor="w",
                                width=25,
                                height=1,
                                font=myFont)
lbl_selected_dataset.place(x=10, y=100)

# Add button
button = tk.Button(text="Run Model",
                   fg="black",
                   bg="lightblue",
                   width=10,
                   height=1,
                   font=myFont,
                   command=select_dataset)
button.place(x=10, y=150)

window.mainloop()
