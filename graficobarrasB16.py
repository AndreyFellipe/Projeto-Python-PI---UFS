import csv
import matplotlib.pyplot as plt
import menu
#B16 - IMC médio dos atletas para um grupo de <Eventos> na olimpíada de <Ano> de <Tipo de Olimpíada>.

def gerar_imcs_summer(ano, tipo_olimpiada):
    lista_imcs_summer = list()
    lista_imc_bask = list()
    lista_imc_foot = list()
    lista_imc_cem = list()
    lista_imc_pairs = list()
    lista_imc_feather = list()
    with open('./csv/athlete_events.csv', 'r') as events:
        eventler = csv.reader(events)
        next(eventler)
        for i in eventler:
            if i[13] == "Basketball Men's Basketball" and i[9] == ano and i[10] == tipo_olimpiada:
                if i[5] != 'NA' and i[4] != 'NA':
                    imc = float(i[5]) / ((float(i[4])/100) * (float(i[4])/100))

                    lista_imc_bask.append(imc)
            if i[13] == "Football Men's Football" and i[9] == ano and i[10] == tipo_olimpiada:
                if i[5] != 'NA' and i[4] != 'NA':
                    imc = float(i[5]) / ((float(i[4])/100) * (float(i[4])/100))
                    lista_imc_foot.append(imc)
            if i[13] == "Athletics Women's 100 metres" and i[9] == ano and i[10] == tipo_olimpiada:
                if i[5] != 'NA' and i[4] != 'NA':
                    imc = float(i[5]) / ((float(i[4])/100) * (float(i[4])/100))
                    lista_imc_cem.append(imc)
            if i[13] == "Rowing Women's Coxless Pairs" and i[9] == ano and i[10] == tipo_olimpiada:
                if i[5] != 'NA' and i[4] != 'NA':
                    imc = float(i[5]) / ((float(i[4])/100) * (float(i[4])/100))
                    lista_imc_pairs.append(imc)
            if i[13] == "Weightlifting Women's Featherweight" and i[9] == ano and i[10] == tipo_olimpiada:
                if i[5] != 'NA' and i[4] != 'NA':
                    imc = float(i[5]) / ((float(i[4])/100) * (float(i[4])/100))
                    lista_imc_feather.append(imc)
    if len(lista_imc_bask) != 0:
        lista_imcs_summer.append(sum(lista_imc_bask) / len(lista_imc_bask))
    else:
        lista_imcs_summer.append(0)
    if len(lista_imc_foot) != 0:
        lista_imcs_summer.append(sum(lista_imc_foot) / len(lista_imc_foot))
    else:
        lista_imcs_summer.append(0)
    if len(lista_imc_cem) != 0:
        lista_imcs_summer.append(sum(lista_imc_cem) / len(lista_imc_cem))
    else:
        lista_imcs_summer.append(0)
    if len(lista_imc_pairs) != 0:
        lista_imcs_summer.append(sum(lista_imc_pairs) / len(lista_imc_pairs))
    else:
        lista_imcs_summer.append(0)
    if len(lista_imc_feather):
        lista_imcs_summer.append(sum(lista_imc_feather) / len(lista_imc_feather))
    else:
        lista_imcs_summer.append(0)
    return (lista_imcs_summer)


def gerar_imcs_winter(ano, tipo_olimpiada):
    lista_imcs_winter = list()
    lista_imc_croos = list()
    lista_imc_sprint = list()
    lista_imc_biathlon = list()
    lista_imc_ski = list()
    lista_imc_speed = list()

    with open('./csv/athlete_events.csv', 'r') as events:
        eventler = csv.reader(events)
        next(eventler)
        for i in eventler:
            if i[13] == "Cross Country Skiing Men's 15 kilometres" and i[9] == ano and i[10] == tipo_olimpiada:
                if i[5] != 'NA' and i[4] != 'NA':
                    imc = float(i[5]) / ((float(i[4])/100) * (float(i[4])/100))
                    lista_imc_croos.append(imc)
            if i[13] == "Biathlon Women's 7.5 kilometres Sprint" and i[9] == ano and i[10] == tipo_olimpiada:
                if i[5] != 'NA' and i[4] != 'NA':
                    imc = float(i[5]) / ((float(i[4])/100) * (float(i[4])/100))
                    lista_imc_sprint.append(imc)
            if i[13] == "Biathlon Women's 15 kilometres" and i[9] == ano and i[10] == tipo_olimpiada:
                if i[5] != 'NA' and i[4] != 'NA':
                    imc = float(i[5]) / ((float(i[4])/100) * (float(i[4])/100))
                    lista_imc_biathlon.append(imc)
            if i[13] == "Ski Jumping Men's Normal Hill, Individual" and i[9] == ano and i[10] == tipo_olimpiada:
                if i[5] != 'NA' and i[4] != 'NA':
                    imc = float(i[5]) / ((float(i[4])/100) * (float(i[4])/100))
                    lista_imc_ski.append(imc)
            if i[13] == "Speed Skating Men's 500 metres" and i[9] == ano and i[10] == tipo_olimpiada:
                if i[5] != 'NA' and i[4] != 'NA':
                    imc = float(i[5]) / ((float(i[4])/100) * (float(i[4])/100))
                    lista_imc_speed.append(imc)
    if len(lista_imc_croos) != 0:
        lista_imcs_winter.append(sum(lista_imc_croos) / len(lista_imc_croos))
    else:
        lista_imcs_winter.append(0)
    if len(lista_imc_sprint) != 0:
        lista_imcs_winter.append(sum(lista_imc_sprint) / len(lista_imc_sprint))
    else:
        lista_imcs_winter.append(0)
    if len(lista_imc_biathlon) != 0:
        lista_imcs_winter.append(sum(lista_imc_biathlon) / len(lista_imc_biathlon))
    else:
        lista_imcs_winter.append(0)
    if len(lista_imc_ski) != 0:
        lista_imcs_winter.append(sum(lista_imc_ski) / len(lista_imc_ski))
    else:
        lista_imcs_winter.append(0)
    if len(lista_imc_speed):
        lista_imcs_winter.append(sum(lista_imc_speed) / len(lista_imc_speed))
    else:
        lista_imcs_winter.append(0)
    return (lista_imcs_winter)

def gerar_barras_summer(lista_imcs_summer):
    eventos = ["Basketball", "Football", "100 metres", "Rowing", "Weightlifting"]
    x = range(len(eventos))
    width = 0.2

    fig, ax = plt.subplots()
    plt.bar(eventos, lista_imcs_summer, color = ['b', 'g', 'r', 'm', 'y'])
    plt.setp(ax.get_xticklabels(), rotation=90, ha='right', rotation_mode='anchor')

    plt.ylim(0, 30)
    plt.title('Gráfico de Barras Summer', weight= 'bold')
    plt.xlabel('Modalidades', weight= 'bold')
    plt.ylabel('IMC Médio', weight= 'bold')
    fig.tight_layout()
    plt.savefig('./png/GráficodeBarrasSummer.png')
    plt.clf()

def gerar_barras_winter(lista_imcs_winter):

    eventos = ["Cross Country", "Biathlon 7.5 Km", "Biathlon 15 Km", "Ski Jumping", "Speed Skating"]
    x = range(len(eventos))
    width = 0.2

    fig, ax = plt.subplots()
    plt.bar(eventos, lista_imcs_winter, color = ['b', 'g', 'r', 'm', 'y'])

    plt.setp(ax.get_xticklabels(), rotation=90, ha='right', rotation_mode='anchor')
    plt.ylim(0,30)
    plt.title('Gráfico de Barras Winter', weight= 'bold')
    plt.xlabel('Modalidades', weight= 'bold')
    plt.ylabel('IMC Médio', weight= 'bold')
    fig.tight_layout()
    plt.savefig('./png/GráficodeBarrasWinter.png')
    plt.clf()

def apresentar_grafico_barras():
    ano, tipo_olimpiada = menu.entrar_argumentos_barras()
    if tipo_olimpiada == 'Summer':
        lista_imcs_summer = gerar_imcs_summer(ano, tipo_olimpiada)
        gerar_barras_summer(lista_imcs_summer)
    else:
        lista_imcs_winter = gerar_imcs_winter(ano, tipo_olimpiada)
        gerar_barras_winter(lista_imcs_winter)