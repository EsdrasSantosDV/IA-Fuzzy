import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Antecedentes (entradas)
proteina = ctrl.Antecedent(np.arange(0, 11, 1), 'proteina')
acucar = ctrl.Antecedent(np.arange(0, 11, 1), 'acucar')
carboidratos = ctrl.Antecedent(np.arange(0, 11, 1), 'carboidratos')
gordura = ctrl.Antecedent(np.arange(0, 11, 1), 'gordura')
fibra = ctrl.Antecedent(np.arange(0, 11, 1), 'fibra')
agua = ctrl.Antecedent(np.arange(0, 11, 1), 'agua')

# Consequentes (saídas)
carnes = ctrl.Consequent(np.arange(0, 11, 1), 'carnes')
frutas_doces = ctrl.Consequent(np.arange(0, 11, 1), 'frutas_doces')
graos = ctrl.Consequent(np.arange(0, 11, 1), 'graos')
laticinios = ctrl.Consequent(np.arange(0, 11, 1), 'laticinios')
vegetais = ctrl.Consequent(np.arange(0, 11, 1), 'vegetais')
legumes = ctrl.Consequent(np.arange(0, 11, 1), 'legumes')

# Funções de pertinência para proteína, açúcar, carboidratos e gordura
proteina.automf(names=['baixo', 'medio', 'alto'])
acucar.automf(names=['baixo', 'medio', 'alto'])
carboidratos.automf(names=['baixo', 'medio', 'alto'])
gordura.automf(names=['baixo', 'medio', 'alto'])
fibra.automf(names=['baixo', 'medio', 'alto'])
agua.automf(names=['baixo', 'medio', 'alto'])

# Funções de pertinência para carnes, frutas doces, grãos e laticínios
carnes.automf(names=['muito baixo', 'baixo', 'medio', 'alto', 'muito alto'])
frutas_doces.automf(names=['muito baixo', 'baixo', 'medio', 'alto', 'muito alto'])
graos.automf(names=['muito baixo', 'baixo', 'medio', 'alto', 'muito alto'])
laticinios.automf(names=['muito baixo', 'baixo', 'medio', 'alto', 'muito alto'])
vegetais.automf(names=['muito baixo', 'baixo', 'medio', 'alto', 'muito alto'])
legumes.automf(names=['muito baixo', 'baixo', 'medio', 'alto', 'muito alto'])

# Visualizando as funções de pertinência
proteina.view()
acucar.view()
carboidratos.view()
gordura.view()
fibra.view()
agua.view()

carnes.view()
frutas_doces.view()
graos.view()
laticinios.view()
vegetais.view()
legumes.view()

plt.show()

# Regras de lógica fuzzy para carnes
rule1 = ctrl.Rule(proteina['alto'] & acucar['baixo'], carnes['muito alto'])
rule2 = ctrl.Rule(proteina['alto'] & acucar['medio'], carnes['alto'])
rule3 = ctrl.Rule(proteina['alto'] & acucar['alto'], carnes['medio'])
rule4 = ctrl.Rule(proteina['medio'] & acucar['baixo'], carnes['medio'])
rule5 = ctrl.Rule(proteina['medio'] & acucar['medio'], carnes['medio'])
rule6 = ctrl.Rule(proteina['medio'] & acucar['alto'], carnes['baixo'])
rule7 = ctrl.Rule(proteina['baixo'] & acucar['baixo'], carnes['baixo'])
rule8 = ctrl.Rule(proteina['baixo'] & acucar['medio'], carnes['baixo'])
rule9 = ctrl.Rule(proteina['baixo'] & acucar['alto'], carnes['muito baixo'])

# Regras de lógica fuzzy para frutas doces
rule10 = ctrl.Rule(proteina['alto'] & acucar['baixo'], frutas_doces['muito baixo'])
rule11 = ctrl.Rule(proteina['alto'] & acucar['medio'], frutas_doces['medio'])
rule12 = ctrl.Rule(proteina['alto'] & acucar['alto'], frutas_doces['medio'])
rule13 = ctrl.Rule(proteina['medio'] & acucar['baixo'], frutas_doces['baixo'])
rule14 = ctrl.Rule(proteina['medio'] & acucar['medio'], frutas_doces['medio'])
rule15 = ctrl.Rule(proteina['medio'] & acucar['alto'], frutas_doces['alto'])
rule16 = ctrl.Rule(proteina['baixo'] & acucar['baixo'], frutas_doces['baixo'])
rule17 = ctrl.Rule(proteina['baixo'] & acucar['medio'], frutas_doces['medio'])
rule18 = ctrl.Rule(proteina['baixo'] & acucar['alto'], frutas_doces['muito alto'])

# Adicionando novas regras para grãos
rule19 = ctrl.Rule(carboidratos['alto'] & gordura['baixo'], graos['muito alto'])
rule20 = ctrl.Rule(carboidratos['alto'] & gordura['medio'], graos['alto'])
rule21 = ctrl.Rule(carboidratos['alto'] & gordura['alto'], graos['medio'])
rule22 = ctrl.Rule(carboidratos['medio'] & gordura['baixo'], graos['alto'])
rule23 = ctrl.Rule(carboidratos['medio'] & gordura['medio'], graos['medio'])
rule24= ctrl.Rule(carboidratos['medio'] & gordura['alto'], graos['baixo'])
rule25= ctrl.Rule(carboidratos['baixo'] & gordura['baixo'], graos['medio'])
rule26 = ctrl.Rule(carboidratos['baixo'] & gordura['medio'], graos['baixo'])
rule27= ctrl.Rule(carboidratos['baixo'] & gordura['alto'], graos['muito baixo'])

# Adicionando regras para laticínios
rule28 = ctrl.Rule(gordura['alto'] & proteina['baixo'], laticinios['muito alto'])
rule29 = ctrl.Rule(gordura['alto'] & proteina['medio'], laticinios['alto'])
rule30 = ctrl.Rule(gordura['alto'] & proteina['alto'], laticinios['medio'])
rule31 = ctrl.Rule(gordura['medio'] & proteina['baixo'], laticinios['alto'])
rule32 = ctrl.Rule(gordura['medio'] & proteina['medio'], laticinios['medio'])
rule33= ctrl.Rule(gordura['medio'] & proteina['alto'], laticinios['baixo'])
rule34= ctrl.Rule(gordura['baixo'] & proteina['baixo'], laticinios['medio'])
rule35 = ctrl.Rule(gordura['baixo'] & proteina['medio'], laticinios['baixo'])
rule36= ctrl.Rule(gordura['baixo'] & proteina['alto'], laticinios['muito baixo'])

# Regras de lógica fuzzy para vegetais
rule37 = ctrl.Rule(fibra['alto'] & agua['baixo'], vegetais['muito alto'])
rule38 = ctrl.Rule(fibra['alto'] & agua['medio'], vegetais['alto'])
rule39 = ctrl.Rule(fibra['alto'] & agua['alto'], vegetais['medio'])
rule40 = ctrl.Rule(fibra['medio'] & agua['baixo'], vegetais['alto'])
rule41 = ctrl.Rule(fibra['medio'] & agua['medio'], vegetais['medio'])
rule42= ctrl.Rule(fibra['medio'] & agua['alto'], vegetais['baixo'])
rule43= ctrl.Rule(fibra['baixo'] & agua['baixo'], vegetais['medio'])
rule44 = ctrl.Rule(fibra['baixo'] & agua['medio'], vegetais['baixo'])
rule45= ctrl.Rule(fibra['baixo'] & agua['alto'], vegetais['muito baixo'])

# Regras de lógica fuzzy para legumes
rule46 = ctrl.Rule(fibra['alto'] & agua['baixo'], legumes['muito alto'])
rule47 = ctrl.Rule(fibra['alto'] & agua['medio'], legumes['alto'])
rule48 = ctrl.Rule(fibra['alto'] & agua['alto'], legumes['medio'])
rule49 = ctrl.Rule(fibra['medio'] & agua['baixo'], legumes['alto'])
rule50 = ctrl.Rule(fibra['medio'] & agua['medio'], legumes['medio'])
rule51= ctrl.Rule(fibra['medio'] & agua['alto'], legumes['baixo'])
rule52= ctrl.Rule(fibra['baixo'] & agua['baixo'], legumes['medio'])
rule53 = ctrl.Rule(fibra['baixo'] & agua['medio'], legumes['baixo'])
rule54= ctrl.Rule(fibra['baixo'] & agua['alto'], legumes['muito baixo'])

# Cria o sistema de controle
grocery_ctrl = ctrl.ControlSystem([rule1, rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,
                                   rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,
                                   rule20, rule21, rule22, rule23, rule24,rule25, rule26, rule27,
                                   rule28, rule29, rule30, rule31, rule32, rule33,rule34, rule35, rule36,
                                   rule37, rule38, rule39, rule40, rule41, rule42, rule43, rule44, rule45,
                                   rule46, rule47, rule48, rule49, rule50, rule51, rule52, rule53, rule54])
grocery = ctrl.ControlSystemSimulation(grocery_ctrl)

# Passa as entradas para o Sistema de Controle
proteinaInput = 8.5
acucarInput = 3.2
carboidratosInput = 6.5
gorduraInput = 7.3
fibraInput = 6.5
aguaInput = 3.3

grocery.input['proteina'] = proteinaInput
grocery.input['acucar'] = acucarInput
grocery.input['carboidratos'] = carboidratosInput
grocery.input['gordura'] = gorduraInput
grocery.input['fibra'] = fibraInput
grocery.input['agua'] = aguaInput

# Computa o sistema de controle
grocery.compute()

# Imprime as saídas
print(grocery.output['carnes'])
print(grocery.output['frutas_doces'])
print(grocery.output['graos'])
print(grocery.output['laticinios'])
print(grocery.output['vegetais'])
print(grocery.output['legumes'])

# Visualiza o resultado
carnes.view(sim=grocery)
frutas_doces.view(sim=grocery)
graos.view(sim=grocery)
laticinios.view(sim=grocery)
vegetais.view(sim=grocery)
legumes.view(sim=grocery)
plt.show()
