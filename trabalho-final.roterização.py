import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import tkinter
from tkinter import *
from matplotlib.backends.backend_pdf import PdfPages
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



# Cria o sistema de controle
grocery_ctrl = ctrl.ControlSystem([rule1, rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,
                                   rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,
                                   rule20, rule21, rule22, rule23, rule24,rule25, rule26, rule27,
                                   rule28, rule29, rule30, rule31, rule32, rule33,rule34, rule35, rule36,
                                   rule37, rule38, rule39, rule40, rule41, rule42, rule43, rule44, rule45
                        ])
grocery = ctrl.ControlSystemSimulation(grocery_ctrl)



def submit_button_event():
    proteinaInput = float(form_proteina.get())
    acucarInput = float(form_acucar.get())
    carboidratosInput = float(form_carboidratos.get())
    gorduraInput = float(form_gordura.get())
    fibraInput = float(form_fibra.get())
    aguaInput = float(form_agua.get())

    grocery.input['proteina'] = proteinaInput
    grocery.input['acucar'] = acucarInput
    grocery.input['carboidratos'] = carboidratosInput
    grocery.input['gordura'] = gorduraInput
    grocery.input['fibra'] = fibraInput
    grocery.input['agua'] = aguaInput

    grocery.compute()

    result_carnes.config(text=f"Carnes: {grocery.output['carnes']}")
    result_frutas_doces.config(text=f"Frutas doces: {grocery.output['frutas_doces']}")
    result_graos.config(text=f"Grãos: {grocery.output['graos']}")
    result_laticinios.config(text=f"Laticínios: {grocery.output['laticinios']}")
    result_vegetais.config(text=f"Vegetais: {grocery.output['vegetais']}")

    # Cria uma nova instância de PdfPages
    pdf = PdfPages('pertinencias.pdf')

    # Lista com todas as variáveis
    variables = [proteina, acucar, carboidratos, gordura, fibra, agua, carnes, frutas_doces, graos, laticinios,
                 vegetais]

    # Para cada variável
    for var in variables:
        # Cria uma nova figura
        fig, ax = plt.subplots()

        # Plota cada função de pertinência
        for name in var.terms:
            ax.plot(var.universe, var[name].mf, label=name)

        # Configura a visualização do gráfico
        ax.legend()
        plt.title( var.label)

        # Salva a figura na página atual do PDF
        pdf.savefig(fig)

        # Fecha a figura
        plt.close(fig)



    # Fecha o objeto PdfPages
    pdf.close()


def fill_form():
    form_proteina.delete(0, tkinter.END)
    form_proteina.insert(0, str(8.5))
    form_acucar.delete(0, tkinter.END)
    form_acucar.insert(0, str(3.2))
    form_carboidratos.delete(0, tkinter.END)
    form_carboidratos.insert(0, str(6.5))
    form_gordura.delete(0, tkinter.END)
    form_gordura.insert(0, str(7.3))
    form_fibra.delete(0, tkinter.END)
    form_fibra.insert(0, str(6.5))
    form_agua.delete(0, tkinter.END)
    form_agua.insert(0, str(3.3))


window = Tk()
window.title("IA-TRABALHO-GRUPO-ESDRAS-JOAO-OTAVIO-FELIPE MENDES")
window.geometry('600x600')
window.configure(background="gray")

# Criando os campos de entrada para os antecedentes
label_proteina = tkinter.Label(window, text="Proteína:",background="gray")
label_acucar = tkinter.Label(window, text="Açúcar:",background="gray")
label_carboidratos = tkinter.Label(window, text="Carboidratos:",background="gray")
label_gordura = tkinter.Label(window, text="Gordura:",background="gray")
label_fibra = tkinter.Label(window, text="Fibra:",background="gray")
label_agua = tkinter.Label(window, text="Água:",background="gray")

form_proteina = Entry(window)
form_acucar = Entry(window)
form_carboidratos = Entry(window)
form_gordura = Entry(window)
form_fibra = Entry(window)
form_agua = Entry(window)

label_proteina.place(x=100,y=50)
form_proteina.place(x=325,y=50)
label_acucar.place(x=100,y=80)
form_acucar.place(x=325,y=80)
label_carboidratos.place(x=100,y=110)
form_carboidratos.place(x=325,y=110)
label_gordura.place(x=100,y=140)
form_gordura.place(x=325,y=140)
label_fibra.place(x=100,y=170)
form_fibra.place(x=325,y=170)
label_agua.place(x=100, y=200)
form_agua.place(x=325, y=200)

submit_button = Button(window, text="Submit", command=submit_button_event)
submit_button.place(x=350, y=300)
# Criação do botão "Fill"
fill_button = tkinter.Button(window, text="Fill", command=fill_form)
fill_button.place(x=350, y=350)
# Criando labels para mostrar as saídas
result_carnes = Label(window, text="")
result_frutas_doces = Label(window, text="")
result_graos = Label(window, text="")
result_laticinios = Label(window, text="")
result_vegetais = Label(window, text="")
result_legumes = Label(window, text="")

result_carnes.place(x=100, y=400)
result_frutas_doces.place(x=100, y=420)
result_graos.place(x=100,y=440)
result_laticinios.place(x=100,y=460)
result_vegetais.place(x=100,y=480)
result_legumes.place(x=100,y=500)

window.mainloop()
