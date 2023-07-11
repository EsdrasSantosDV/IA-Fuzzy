import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Antecedentes (entradas)
proteina = ctrl.Antecedent(np.arange(0, 11, 1), 'proteina')
acucar = ctrl.Antecedent(np.arange(0, 11, 1), 'acucar')

# Consequentes (saídas)
carnes = ctrl.Consequent(np.arange(0, 11, 1), 'carnes')
frutas_doces = ctrl.Consequent(np.arange(0, 11, 1), 'frutas_doces')

# Funções de pertinência para proteína e açúcar
proteina.automf(names=['baixo', 'medio', 'alto'])
acucar.automf(names=['baixo', 'medio', 'alto'])

# Funções de pertinência para carnes e frutas doces
carnes.automf(names=['muito baixo', 'baixo', 'medio', 'alto', 'muito alto'])
frutas_doces.automf(names=['muito baixo', 'baixo', 'medio', 'alto', 'muito alto'])

# Visualizando as funções de pertinência
proteina.view()
acucar.view()
carnes.view()
frutas_doces.view()
plt.show()

# Regras de lógica fuzzy
rule1 = ctrl.Rule(proteina['alto'] & acucar['baixo'], carnes['muito alto'])
rule2 = ctrl.Rule(proteina['alto'] & acucar['medio'], carnes['alto'])
rule3 = ctrl.Rule(proteina['alto'] & acucar['alto'], carnes['medio'])
rule4 = ctrl.Rule(proteina['medio'] & acucar['baixo'], carnes['medio'])
rule5 = ctrl.Rule(proteina['medio'] & acucar['medio'], carnes['medio'])
rule6 = ctrl.Rule(proteina['medio'] & acucar['alto'], carnes['baixo'])
rule7 = ctrl.Rule(proteina['baixo'] & acucar['baixo'], carnes['baixo'])
rule8 = ctrl.Rule(proteina['baixo'] & acucar['medio'], carnes['baixo'])
rule9 = ctrl.Rule(proteina['baixo'] & acucar['alto'], carnes['muito baixo'])


rule10 = ctrl.Rule(proteina['alto'] & acucar['baixo'], frutas_doces['muito baixo'])
rule11 = ctrl.Rule(proteina['alto'] & acucar['medio'], frutas_doces['medio'])
rule12 = ctrl.Rule(proteina['alto'] & acucar['alto'], frutas_doces['medio'])
rule13 = ctrl.Rule(proteina['medio'] & acucar['baixo'], frutas_doces['baixo'])
rule14 = ctrl.Rule(proteina['medio'] & acucar['medio'], frutas_doces['medio'])
rule15 = ctrl.Rule(proteina['medio'] & acucar['alto'], frutas_doces['alto'])
rule16 = ctrl.Rule(proteina['baixo'] & acucar['baixo'], frutas_doces['baixo'])
rule17 = ctrl.Rule(proteina['baixo'] & acucar['medio'], frutas_doces['medio'])
rule18 = ctrl.Rule(proteina['baixo'] & acucar['alto'], frutas_doces['muito alto'])

# Adicione mais regras conforme necessário

# Cria o sistema de controle
grocery_ctrl = ctrl.ControlSystem([rule1, rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,
rule14,rule15,rule16,rule17,rule18])
grocery = ctrl.ControlSystemSimulation(grocery_ctrl)

# Passa as entradas para o Sistema de Controle
proteinaInput = 8.5
acucarInput = 3.2


grocery.input['proteina'] = proteinaInput
grocery.input['acucar'] = acucarInput

# Computa o sistema de controle
grocery.compute()


# Imprime as saídas
print(grocery.output['carnes'])
print(grocery.output['frutas_doces'])

# Visualiza o resultado
carnes.view(sim=grocery)
frutas_doces.view(sim=grocery)
plt.show()