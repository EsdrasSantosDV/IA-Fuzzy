import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Cria as variáveis fuzzy
preco = ctrl.Antecedent(np.arange(0, 270000, 1), 'preco')
avaliacao = ctrl.Antecedent(np.arange(0, 11, 1), 'avaliacao')
vendas = ctrl.Consequent(np.arange(0, 11, 0.5), 'vendas')

preco.automf(number=3, names=['baixo', 'medio', 'alto'])
avaliacao.automf(number=3, names=['ruim', 'media', 'boa'])

preco.view()
avaliacao.view()

vendas['baixa'] = fuzz.trimf(vendas.universe, [0, 2.5, 5.0])
vendas['media'] = fuzz.trimf(vendas.universe, [2.5, 5.0, 7.5])
vendas['alta'] = fuzz.trimf(vendas.universe, [5.0, 7.5, 10.0])

# Define as regras fuzzy
regra1 = ctrl.Rule(preco['baixo'] & avaliacao['ruim'], vendas['baixa'])
regra2 = ctrl.Rule(preco['baixo'] & avaliacao['media'], vendas['media'])
regra3 = ctrl.Rule(preco['baixo'] & avaliacao['boa'], vendas['alta'])
regra4 = ctrl.Rule(preco['medio'] & avaliacao['ruim'], vendas['baixa'])
regra5 = ctrl.Rule(preco['medio'] & avaliacao['media'], vendas['media'])
regra6 = ctrl.Rule(preco['medio'] & avaliacao['boa'], vendas['media'])
regra7 = ctrl.Rule(preco['alto'] & avaliacao['ruim'], vendas['baixa'])
regra8 = ctrl.Rule(preco['alto'] & avaliacao['media'], vendas['baixa'])
regra9 = ctrl.Rule(preco['alto'] & avaliacao['boa'], vendas['media'])


# Cria o sistema de controle fuzzy
sistema_ctrl = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5, regra6, regra7, regra8, regra9])
sistema_simulacao = ctrl.ControlSystemSimulation(sistema_ctrl)

# Entrada dos valores de preço e avaliação
preco_input = 150000
avaliacao_input = 8

# Passa os valores de entrada para o sistema de controle fuzzy
sistema_simulacao.input['preco'] = preco_input
sistema_simulacao.input['avaliacao'] = avaliacao_input

# Realiza a avaliação do sistema fuzzy
sistema_simulacao.compute()


# Obtém o valor de saída (previsão de vendas)
previsao_vendas = sistema_simulacao.output['vendas']

# Exibe o resultado
print(f"A previsão de vendas é: {previsao_vendas:.2f}")

vendas.view(sim=sistema_simulacao)

plt.show()