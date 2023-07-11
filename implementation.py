import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Cria as variáveis fuzzy
avaliacao_usuarios = ctrl.Antecedent(np.arange(0, 11, 1), 'avaliacao_usuarios')
avaliacao_especialistas = ctrl.Antecedent(np.arange(0, 11, 1), 'avaliacao_especialistas')
qualidade = ctrl.Consequent(np.arange(0, 11, 0.5), 'qualidade')

#Definição  criação das funçoes de pertinencia
avaliacao_usuarios.automf(number=3, names=['ruim', 'media', 'boa'])
avaliacao_especialistas.automf(number=3, names=['ruim', 'media', 'boa'])

#VISUALIZAÇÃO DAS FUNÇOES DE PERTINENCIA
avaliacao_usuarios.view()
avaliacao_especialistas.view()

qualidade['baixa'] = fuzz.trimf(qualidade.universe, [0, 2.5, 5.0])
qualidade['media'] = fuzz.trimf(qualidade.universe, [2.5, 5.0, 7.5])
qualidade['alta'] = fuzz.trimf(qualidade.universe, [5.0, 7.5, 10.0])

# Define as regras fuzzy
regra1 = ctrl.Rule(avaliacao_usuarios['ruim'] & avaliacao_especialistas['ruim'], qualidade['baixa'])
regra2 = ctrl.Rule(avaliacao_usuarios['media'] & avaliacao_especialistas['ruim'], qualidade['baixa'])
regra3 = ctrl.Rule(avaliacao_usuarios['boa'] & avaliacao_especialistas['ruim'], qualidade['media'])
regra4 = ctrl.Rule(avaliacao_usuarios['ruim'] & avaliacao_especialistas['media'], qualidade['baixa'])
regra5 = ctrl.Rule(avaliacao_usuarios['media'] & avaliacao_especialistas['media'], qualidade['media'])
regra6 = ctrl.Rule(avaliacao_usuarios['boa'] & avaliacao_especialistas['media'], qualidade['alta'])
regra7 = ctrl.Rule(avaliacao_usuarios['ruim'] & avaliacao_especialistas['boa'], qualidade['media'])
regra8 = ctrl.Rule(avaliacao_usuarios['media'] & avaliacao_especialistas['boa'], qualidade['alta'])
regra9 = ctrl.Rule(avaliacao_usuarios['boa'] & avaliacao_especialistas['boa'], qualidade['alta'])

# Cria o sistema de controle fuzzy
sistema_ctrl = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5, regra6, regra7, regra8, regra9])
sistema_simulacao = ctrl.ControlSystemSimulation(sistema_ctrl)

# Entrada dos valores de avaliações de usuários e especialistas
avaliacao_usuarios_input = 4
avaliacao_especialistas_input = 7

# Passa os valores de entrada para o sistema de controle fuzzy
sistema_simulacao.input['avaliacao_usuarios'] = avaliacao_usuarios_input
sistema_simulacao.input['avaliacao_especialistas'] = avaliacao_especialistas_input

# Realiza a avaliação do sistema fuzzy
sistema_simulacao.compute()

# Obtém o valor de saída (previsão da qualidade do jogo)
previsao_qualidade = sistema_simulacao.output['qualidade']

# Exibe o resultado
print(f"A previsão da qualidade do jogo é: {previsao_qualidade:.2f}")

qualidade.view(sim=sistema_simulacao)

plt.show()