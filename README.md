# Eight Queens Puzzle Solver

This Python project uses a genetic algorithm to solve the Eight Queens Puzzle, a classic problem in combinatorial optimization. The goal is to place eight queens on an 8x8 chessboard in a way that no two queens threaten each other.

## Requirements
- Python 3.x
- Tkinter (for UI)

## Usage
1. Clone the repository:

    ```bash
    git clone https://github.com/Parsa-Baniamerian/Genetic_Algorithm_Eight_Queens.git
    ```

2. Change directory to the project folder:

    ```bash
    cd Genetic_Algorithm_Eight_Queens
    ```

3. Run the application:

    ```bash
    python GUI.py
    ```

## Description

### Files
- **GUI.py**: Contains the GUI for visualizing the solution of the Eight Queens Puzzle.
- **genetic_algorithm.py**: Implements the genetic algorithm to solve the puzzle.

### Genetic Algorithm
- `generate_random_permutation()`: Generates a random permutation representing a possible queen placement on the chessboard.
- `fitness(permutation)`: Calculates the fitness of a permutation based on the number of non-attacking pairs of queens.
- `crossover(parent1, parent2)`: Performs crossover between two parent permutations to create a child permutation.
- `mutation(child)`: Applies mutation to a permutation.
- `genetic_algorithm()`: The main function that runs the genetic algorithm to find a solution.

## Configuration
You can customize the genetic algorithm parameters in the `main()` function of `GUI.py`. Adjust the values for `population_size`, `generations`, `crossover_rate`, `mutation_rate`, and `elite_count` according to your preferences.

## Results
The best solution found by the genetic algorithm, along with its fitness score, will be displayed in the console. If a solution is found within the specified generations, the generation number will also be shown.

## GUI
The GUI displays the chessboard with queens placed according to the best solution found. Queens are represented by "♛" and are highlighted in red.

Feel free to explore and modify the code to experiment with different algorithm parameters or improve the UI.

Happy coding!
