import tkinter as tk
from tkinter import ttk
from utils.constants import DEFAULT_CROSSOVER_RATE, DEFAULT_GENERATIONS, DEFAULT_MUTATION_RATE, DEFAULT_POP_SIZE, DEFAULT_RANGE

class AlgorithmParameters:
    def __init__(self, master):
        self.frame = ttk.LabelFrame(master, text="GA Parameters")
        self.frame.pack(pady=10, padx=10, fill='x', expand=True)

        self.pop_size_var = self.add_parameter("Population Size:", DEFAULT_POP_SIZE)
        self.num_generations_var = self.add_parameter("Number of Generations:", DEFAULT_GENERATIONS)
        self.mutation_rate_var = self.add_parameter("Mutation Rate:", DEFAULT_MUTATION_RATE)
        self.crossover_rate_var = self.add_parameter("Crossover Rate:", DEFAULT_CROSSOVER_RATE)

    def add_parameter(self, label_text, default_value):
        frame = ttk.Frame(self.frame)
        frame.pack(pady=2, fill='x', expand=True)

        ttk.Label(frame, text=label_text).pack(side=tk.LEFT, padx=(0, 5))
        var = tk.StringVar(value=str(default_value))
        entry = ttk.Entry(frame, textvariable=var, width=10)
        entry.pack(side=tk.LEFT)

        return var

    def get_parameters(self):
        try:
            pop_size = int(self.pop_size_var.get())
            num_generations = int(self.num_generations_var.get())
            mutation_rate = float(self.mutation_rate_var.get())
            crossover_rate = float(self.crossover_rate_var.get())
            return pop_size, num_generations, mutation_rate, crossover_rate
        except ValueError as e:
            raise ValueError(f"Error in GA parameters: {e}")