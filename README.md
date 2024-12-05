# GA-Maximizer

## Overview  
**GA-Maximizer** is a desktop application that uses a Genetic Algorithm (GA) to find the maximum of user-defined mathematical functions. It features a simple interface for setting up functions, variable ranges, and algorithm parameters, and provides visualizations of the optimization process.

## Features  
- Select or define custom mathematical functions.  
- Configure variable ranges and GA parameters (population size, generations, mutation rate, etc.).  
- Visualize optimization results and track best solutions over generations.  
- Save logs and results for later analysis.

## Requirements  
- Python 3.8+  
- `Tkinter`

## Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/username/ga-maximizer.git
   cd ga-maximizer
   ```

## Usage  
1. Run the app:  
   ```bash
   python __main__.py
   ```
2. Follow the on-screen instructions to select functions, configure parameters, and run the GA.

<div align="center"> <img width="300" alt="image" src="https://github.com/user-attachments/assets/4f9a51ef-2a05-4e3b-9ed1-57c828d8dc48"> </div>

3. View and save the results.

## Notes  
- Results are saved in the `results/` folder.  
- To add or modify functions, update the following section in the code (utils/app.py):
```python
self.functions = [
    Function("3*x1 - 2*x2 + 1*x3 - 4*x4 + 9*x5"),
    Function("sin(x1)*cos(x2) + log(x3 + 5) + exp(x4) - x5"),
    Function("sin(x1)*cos(x2)*exp(-((x3-5)**2))")
]
```
- You can extend or modify the Genetic Algorithm logic in utils/genetic_algorithm.py.
