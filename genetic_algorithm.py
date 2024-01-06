import random


def generate_random_permutation():
    permutation = list(range(8))
    random.shuffle(permutation)
    return permutation


def fitness(permutation):
    conflicts = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if abs(i - j) == abs(permutation[i] - permutation[j]):
                conflicts += 1
    return 28 - conflicts  # 28 is the maximum number of non-attacking pairs


def crossover(parent1, parent2):
    crossover_points = sorted(random.sample(range(1, 7), 2))
    child = [None] * 8

    # Copy the values between crossover points from parent1 to child
    child[crossover_points[0]:crossover_points[1]] = parent1[crossover_points[0]:crossover_points[1]]

    # Fill in the remaining positions with values from parent2
    remaining_indices = [i for i in range(8) if child[i] is None]
    remaining_values = [val for val in parent2 if val not in child]
    for i, val in zip(remaining_indices, remaining_values):
        child[i] = val

    # If there are still None values in child, fill them randomly
    for i in range(8):
        if child[i] is None:
            child[i] = random.choice([val for val in range(8) if val not in child])

    return child


def mutation(child):
    mutation_points = random.sample(range(8), 2)
    child[mutation_points[0]], child[mutation_points[1]] = child[mutation_points[1]], child[mutation_points[0]]
    return child


def genetic_algorithm(population_size, generations, crossover_rate, mutation_rate, elite_count):
    population = [generate_random_permutation()for _ in range(population_size)]

    generation_found = None

    for generation in range(generations):
        population = sorted(population, key=fitness, reverse=True)
        # Select top individuals for elitism
        new_population = population[:elite_count]

        for _ in range(population_size - elite_count):
            parent1, parent2 = random.choices(population[:50], k=2)

            # Crossover
            if random.random() < crossover_rate:
                child = crossover(parent1, parent2)
            else:
                child = parent1

            # Mutation
            if random.random() < mutation_rate:
                child = mutation(child)

            new_population.append(child)

        population = new_population

        best_solution = max(population, key=fitness)

        if fitness(best_solution) == 28:
            generation_found = generation + 1
            break

    print("\nBest Solution:", best_solution)
    print("Fitness:", fitness(best_solution))

    if generation_found is not None:
        print(f"Solution found in generation {generation_found}")
    else:
        print("Solution not found within the specified generations.")

    return best_solution
