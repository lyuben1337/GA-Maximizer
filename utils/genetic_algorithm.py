import random

class GeneticAlgorithm:
    """
    A class implementing a Genetic Algorithm to maximize a given function.
    """

    def __init__(self, function, variable_ranges, pop_size, num_generations, mutation_rate, crossover_rate):
        """
        Initialize the GA parameters.

        Parameters
        ----------
        function : callable
            The objective function to maximize. It should accept a list of variables and return a float.
        pop_size : int, optional
            The size of the population.
        num_generations : int, optional
            The number of generations to run the GA.
        mutation_rate : float, optional
            The probability of mutating a gene in an individual.
        crossover_rate : float, optional
            The probability of performing crossover between two parents.
        variable_ranges : list of tuples, optional
            A list of (low, high) tuples defining the range for each variable.
        """
        self.function = function
        self.pop_size = pop_size
        self.num_generations = num_generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.chromosome_length = 5
        self.VARIABLE_RANGES = variable_ranges

        self.best_individual = None
        self.best_function = float('-inf')

    def generate_initial_population(self):
        population = []
        for _ in range(self.pop_size):
            individual = [random.uniform(low, high) for low, high in self.VARIABLE_RANGES]
            population.append(individual)
        return population

    def tournament_selection(self, population, function_values, k=3):
        selected = []
        for _ in range(self.pop_size):
            aspirants = random.sample(list(zip(population, function_values)), k)
            selected.append(max(aspirants, key=lambda x: x[1])[0])
        return selected

    def crossover(self, parent1, parent2):
        if random.random() < self.crossover_rate:
            child1, child2 = [], []
            for gene1, gene2 in zip(parent1, parent2):
                if random.random() < 0.5:
                    child1.append(gene1)
                    child2.append(gene2)
                else:
                    child1.append(gene2)
                    child2.append(gene1)
            return child1, child2
        else:
            return parent1[:], parent2[:]

    def mutate(self, individual):
        for i in range(len(individual)):
            if random.random() < self.mutation_rate:
                low, high = self.VARIABLE_RANGES[i]
                # Apply a Gaussian perturbation
                individual[i] += random.gauss(0, (high - low) * 0.1)
                # Ensure gene is within bounds
                individual[i] = max(min(individual[i], high), low)
        return individual

    def run(self, callback=None):
        """
        Run the GA optimization process.

        Parameters
        ----------
        callback : callable, optional
            A function that will be called after each generation with arguments:
            (generation_number, best_function_value, best_individual, population, function_values)

            This allows for decoupled visualization or logging.

        Returns
        -------
        tuple
            (best_individual, best_function_value) found by the GA.
        """
        population = self.generate_initial_population()
        
        for generation in range(self.num_generations):
            # Evaluate function
            function_values = [self.function(ind) for ind in population]

            # Keep track of best individual
            for individual, f_val in zip(population, function_values):
                if f_val > self.best_function:
                    self.best_function = f_val
                    self.best_individual = individual[:]

            # Optional callback for reporting
            if callback is not None:
                callback(generation, self.best_function, population, function_values)

            # Selection
            selected = self.tournament_selection(population, function_values)

            # Crossover and Mutation
            next_generation = []
            for i in range(0, self.pop_size, 2):
                parent1 = selected[i]
                parent2 = selected[i+1 if i+1 < self.pop_size else 0]
                child1, child2 = self.crossover(parent1, parent2)
                child1 = self.mutate(child1)
                child2 = self.mutate(child2)
                next_generation.extend([child1, child2])

            population = next_generation[:self.pop_size]

        return self.best_individual, self.best_function