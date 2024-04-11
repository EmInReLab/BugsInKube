import tkinter as tk
from tkinter import ttk

def update_number_range(event):
    selected_platform = dropdown_var.get()
    if selected_platform == "Kubernetes":
        number_combobox['values'] = list(range(1, 31))
    elif selected_platform == "Mesos":
        number_combobox['values'] = list(range(31, 61))
    number_combobox.current(0)

def submit():
    selected_number = number_var.get()
    selected_platform = dropdown_var.get()
    selected_checkbox = checkbox_var.get()
    print("Selected Platform:", selected_platform)
    print("Selected Bug ID:", selected_number)
    print("Checkbox Checked:", selected_checkbox)

# Create main window
root = tk.Tk()
root.title("PaaS Bug Inspector")

# Create dropdown menu
dropdown_label = ttk.Label(root, text="Select the PaaS platform:")
dropdown_label.grid(row=0, column=0, padx=10, pady=5)
dropdown_var = tk.StringVar()
dropdown_combobox = ttk.Combobox(root, textvariable=dropdown_var, values=["Kubernetes", "Mesos"])
dropdown_combobox.grid(row=0, column=1, padx=10, pady=5)
dropdown_combobox.current(0)
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
