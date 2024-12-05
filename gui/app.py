import os
from datetime import datetime
from utils.function import Function
from utils.genetic_algorithm import GeneticAlgorithm
import tkinter as tk
from tkinter import ttk
from gui.algortihm_parameters import AlgorithmParameters
from gui.function_selector import FunctionSelector
from gui.variable_ranges import VariableRanges
from gui.result_plotter import ResultPlotter

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Function Maximum with Genetic Algorithm")
        self.master.resizable(False, False)

        # Initialize Functions
        self.functions = [
            Function("3*x1 - 2*x2 + 1*x3 - 4*x4 + 9*x5"),
            Function("sin(x1)*cos(x2) + log(x3 + 5) + exp(x4) - x5"),
            Function("sin(x1)*cos(x2)*exp(-((x3-5)**2))")
        ]

        # Subcomponents
        self.function_selector = FunctionSelector(master, self.functions)
        
        self.params_frame = ttk.Frame(master)
        self.params_frame.pack(fill='x', padx=10, pady=5)

        self.variable_ranges = VariableRanges(self.params_frame, num_variables=5)
        self.variable_ranges.frame.pack(side='left', padx=10, expand=True)

        self.ga_parameters = AlgorithmParameters(self.params_frame)
        self.ga_parameters.frame.pack(side='right', padx=10, expand=True)

        # Run Button
        self.run_button = ttk.Button(master, text="Run GA", command=self.run)
        self.run_button.pack(pady=5, fill='x', expand=True)

        # Output
        self.output_text = tk.Text(master, width=80, height=20)
        self.output_text.pack(pady=10, fill='both', expand=True)

        self.full_log = ""
        self.history_best_function = []
        self.plotter = ResultPlotter(master)

    def log(self, message):
        self.full_log += f"{message}\n"
        self.output_text.insert(tk.END, f"{message}\n")
        self.output_text.see(tk.END)

    def save_results_to_file(self):
        if not os.path.exists("results"):
            os.makedirs("results")
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = os.path.join("results", f"{current_time}.txt")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.full_log)

    def run(self):
        try:
            selected_function = self.function_selector.get_selected_function(self.functions)
            ranges = self.variable_ranges.get_ranges()
            pop_size, num_generations, mutation_rate, crossover_rate = self.ga_parameters.get_parameters()
        except ValueError as e:
            self.log(e)
            return

        # Run Genetic Algorithm
        self.full_log = ""
        self.history_best_function.clear()

        self.log("Running Genetic Algorithm...")
        ga = GeneticAlgorithm(
            selected_function,
            variable_ranges=ranges,
            pop_size=pop_size,
            num_generations=num_generations,
            mutation_rate=mutation_rate,
            crossover_rate=crossover_rate,
        )

        def report_generation(gen, best_func, population, values):
            self.history_best_function.append((gen, best_func))
            self.log(f"Generation {gen}: Best = {best_func}")
            for ind, val in zip(population, values):
                self.full_log += f"Individual: {ind}, Value: {val}\n"

        best_individual, best_value = ga.run(callback=report_generation)

        self.log(f"Best Individual: {best_individual}")
        self.log(f"Best Value: {best_value}")

        self.plotter.plot(self.history_best_function)
        self.save_results_to_file()