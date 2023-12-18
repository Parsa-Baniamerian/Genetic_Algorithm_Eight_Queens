import tkinter as tk
from genetic_algorithm import genetic_algorithm


class EightQueensUI(tk.Tk):
    def __init__(self, solution, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Eight Queens Puzzle Solution")
        self.geometry("480x480")
        self.resizable(width=False, height=False)

        self.solution = solution
        self.create_board()

    def create_board(self):
        board_frame = tk.Frame(self)
        board_frame.pack()

        for i in range(8):
            for j in range(8):
                color = "white" if (i + j) % 2 == 0 else "black"
                label = tk.Label(board_frame, text="", width=6, height=3,
                                 bg=color, relief="ridge", padx=0, pady=0, font=("Arial", 12))
                label.grid(row=i, column=j)

        for row, col in enumerate(self.solution):
            if 0 <= row < 8 and 0 <= col < 8:
                label = tk.Label(board_frame, text="♛", font=(
                    "Arial", 14), width=2, height=1, bg="red", fg="white", relief="ridge")
                label.grid(row=row, column=col, padx=0, pady=0)


def main():
    population_size = 30
    generations = 300
    crossover_rate = 0.8
    mutation_rate = 0.05
    elite_count = 5  # Number of individuals selected for elitism

    best_solution = genetic_algorithm(
        population_size, generations, crossover_rate, mutation_rate, elite_count)

    app = EightQueensUI(best_solution)
    app.mainloop()


if __name__ == "__main__":
    main()
