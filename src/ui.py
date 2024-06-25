import tkinter as tk
from tkinter import ttk
from main import handleSubmit


def update_number_range(event):
    selected_platform = dropdown_var.get()
    if selected_platform == "Kubernetes":
        number_combobox["values"] = list(range(1, 31))
    elif selected_platform == "Mesos":
        number_combobox["values"] = list(range(31, 61))
    number_combobox.current(0)


def submit():
    selected_number = number_var.get()
    selected_platform = dropdown_var.get()
    selected_checkbox = checkbox_var.get()
    open_new_window(selected_platform, selected_number, selected_checkbox)


def open_new_window(selected_platform, selected_number, selected_checkbox):
    new_window = tk.Toplevel(root)
    new_window.title("Bug Detail")
    text_label = ttk.Label(new_window, text=f"Bug {selected_number}")
    text_label.pack()

    # Create a Text widget for displaying dynamic text
    text_widget = tk.Text(new_window, height=30, width=150)
    text_widget.pack()

    # Continuously add new lines of text dynamically
    handleSubmit(
        text_widget,
        new_window,
        selected_platform,
        selected_number,
        selected_checkbox,  # noqa E501
    )


# Create main window
root = tk.Tk()
root.title("PaaS Bug Inspector")

# Create dropdown menu
dropdown_label = ttk.Label(root, text="Select the PaaS platform:")
dropdown_label.grid(row=0, column=0, padx=10, pady=5)
dropdown_var = tk.StringVar()
dropdown_combobox = ttk.Combobox(
    root, textvariable=dropdown_var, values=["Kubernetes"]
)  # noqa E501
dropdown_combobox.grid(row=0, column=1, padx=10, pady=5)
dropdown_combobox.current(None)
dropdown_combobox.bind("<<ComboboxSelected>>", update_number_range)

# Create number selection
number_label = ttk.Label(root, text="Select the bug ID:")
number_label.grid(row=1, column=0, padx=10, pady=5)
number_var = tk.IntVar()
number_combobox = ttk.Combobox(root, textvariable=number_var)
number_combobox.grid(row=1, column=1, padx=10, pady=5)

# Create checkbox
checkbox_label = ttk.Label(root, text="Reproduce the bug:")
checkbox_label.grid(row=2, column=0, padx=10, pady=5)
checkbox_var = tk.BooleanVar()
checkbox = ttk.Checkbutton(root, variable=checkbox_var)
checkbox.grid(row=2, column=1, padx=10, pady=5)

# Create submit button
submit_button = ttk.Button(root, text="Submit", command=submit)
submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
