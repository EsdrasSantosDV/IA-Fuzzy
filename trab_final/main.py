import random
import matplotlib.pyplot as plt

# Parâmetros configuráveis
population_size = 50
generations = 50
selection_method = "roulette"  # "roulette" ou "tournament"
elitism = True  # True ou False
elitism_size = 2

# Função para gerar uma população aleatória
def generate_population(size, items_length):
    population = []
    for _ in range(size):
        chromosome = [random.choice([0, 1]) for _ in range(items_length)]
        population.append(chromosome)
    return population

# Função para calcular o fitness de um cromossomo
def calculate_fitness(chromosome, items, max_weight):
    total_weight = 0
    total_value = 0
    for i in range(len(chromosome)):
        if chromosome[i] == 1:
            total_weight += items[i][0]
            total_value += items[i][1]
    if total_weight > max_weight:
        return 0
    else:
        return total_value

# Função para selecionar dois cromossomos para crossover
def select_chromosomes(population, items, max_weight, selection_method):
    fitness_values = [calculate_fitness(ch, items, max_weight) for ch in population]
    if selection_method == "roulette":
        fitness_values = [float(i) / sum(fitness_values) for i in fitness_values]
        return random.choices(population, weights=fitness_values, k=2)
    else: # torneio
        return random.sample(population, 2)

# Função para realizar crossover entre dois cromossomos
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Função para realizar mutação em um cromossomo
def mutate(chromosome):
    mutation_point = random.randint(0, len(chromosome) - 1)
    chromosome[mutation_point] = 1 - chromosome[mutation_point]
    return chromosome

# Itens que podem ser colocados na mochila
items = [[i+1, (i+1)**2] for i in range(20)]  # 20 itens

# Parâmetros para o algoritmo genético
max_weight = 50
mutation_probability = 0.2

# Listas para armazenar evolução de peso e valor
weight_evolution = []
value_evolution = []

# Variáveis para acompanhar a melhor solução e a geração em que foi encontrada
best_solution = None
best_generation = -1

# Gerar uma população aleatória
population = generate_population(population_size, len(items))

# Evoluir
