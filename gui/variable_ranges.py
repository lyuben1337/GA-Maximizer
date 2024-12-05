import tkinter as tk
from tkinter import ttk
from utils.constants import DEFAULT_RANGE

class VariableRanges:
    def __init__(self, master, num_variables):
        self.frame = ttk.LabelFrame(master, text="Variable Ranges (min, max)")
        self.frame.pack(pady=10, padx=10, fill='x', expand=True)
        self.entries = []

        for i in range(1, num_variables + 1):
            row_frame = ttk.Frame(self.frame)
            row_frame.pack(pady=2, fill='x', expand=True)

            label = ttk.Label(row_frame, text=f"x{i} range:")
            label.pack(side=tk.LEFT, padx=(0, 5))

            min_var = tk.StringVar(value=str(DEFAULT_RANGE[0]))
            max_var = tk.StringVar(value=str(DEFAULT_RANGE[1]))

            min_entry = ttk.Entry(row_frame, textvariable=min_var, width=5)
            min_entry.pack(side=tk.LEFT)

            sep = ttk.Label(row_frame, text=" to ")
            sep.pack(side=tk.LEFT)

            max_entry = ttk.Entry(row_frame, textvariable=max_var, width=5)
            max_entry.pack(side=tk.LEFT)

            self.entries.append((min_var, max_var))

    def get_ranges(self):
        ranges = []
        for i, (min_var, max_var) in enumerate(self.entries, start=1):
            try:
                low = float(min_var.get())
                high = float(max_var.get())
                if low > high:
                    raise ValueError(f"Invalid range for x{i}: min > max")
                ranges.append((low, high))
            except ValueError as e:
                raise ValueError(f"Error in x{i} range: {e}")
        return ranges