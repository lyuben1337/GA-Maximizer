import tkinter as tk
from tkinter import ttk

class FunctionSelector:
    def __init__(self, master, functions):
        self.label = ttk.Label(master, text="Select Function:")
        self.label.pack(pady=5, fill='x', expand=True)

        self.function_names = [str(f) for f in functions]
        self.selected_function = tk.StringVar(value=self.function_names[0])

        self.combo = ttk.Combobox(
            master,
            textvariable=self.selected_function,
            values=self.function_names,
            state="readonly"
        )
        self.combo.pack(pady=5, fill='x', expand=True)

    def get_selected_function(self, functions):
        idx = self.function_names.index(self.selected_function.get())
        return functions[idx]