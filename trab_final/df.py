import random

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def generate_population(num_individuals, num_items):
    population = []
    for _ in range(num_individuals):
        individual = [random.randint(0, 1) for _ in range(num_items)]
        population.append(individual)
    return population

def calculate_fitness(individual, items, max_weight):
    total_value = 0
    total_weight = 0
    for i in range(len(individual)):
        if individual[i] == 1:
            total_value += items[i].value
            total_weight += items[i].weight
    if total_weight > max_weight:
        total_value = 0
    return total_value

def select_parents(population, items, max_weight):
    parents = []
    for _ in range(2):
        parent = max(population, key=lambda x: calculate_fitness(x, items, max_weight))
        parents.append(parent)
        population.remove(parent)
    return parents

def crossover(parents):
    child = []
    crossover_point = random.randint(1, len(parents[0]) - 1)
    child.extend(parents[0][:crossover_point])
    child.extend(parents[1][crossover_point:])
    return child

def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]
    return individual

def genetic_algorithm(items, max_weight, num_generations, population_size, mutation_rate):
    population = generate_population(population_size, len(items))
    best_fitness = 0
    best_solution = None

    for generation in range(num_generations):
        parents = select_parents(population, items, max_weight)
        child = crossover(parents)
        child = mutate(child, mutation_rate)
        population.append(child)

        fitness_values = [calculate_fitness(individual, items, max_weight) for individual in population]
        best_individual = population[fitness_values.index(max(fitness_values))]
        best_fitness = max(fitness_values)
        best_solution = [items[i] for i in range(len(best_individual)) if best_individual[i] == 1]

    return best_solution, best_fitness

# Exemplo de uso:
items = [Item(2, 3), Item(3, 4), Item(4, 5), Item(5, 8), Item(9, 10)]
max_weight = 15
num_generations = 100
population_size = 50
mutation_rate = 0.1

best_solution, best_fitness = genetic_algorithm(items, max_weight, num_generations, population_size, mutation_rate)

print("Melhor solução encontrada:")
for item in best_solution:
    print(f"Peso: {item.weight}, Valor: {item.value}")
print(f"Valor total: {best_fitness}")