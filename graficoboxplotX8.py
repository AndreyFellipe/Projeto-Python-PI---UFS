#X8.Quantidade de atletas de cada país a cada ano em <Tipo de Olimpíada>, um boxplot por cada país..
import menu
import csv
import matplotlib.pyplot as plt

def gerar_quantidades(noc, tipo_olimpiada):
    cont = dict()
    with open('./csv/athlete_events.csv', 'r') as events:
        eventler = csv.reader(events)
        next(eventler)
        for event in eventler:
            if event[10] == tipo_olimpiada and event[7] == noc:
                cont[event[9]] = cont.get(event[9], 0) + 1
    return list(cont.values())

def armazenar_quantidade(tipo_olimpiada):
    FRA = gerar_quantidades('FRA', tipo_olimpiada)
    CAN = gerar_quantidades('CAN', tipo_olimpiada)
    BRA = gerar_quantidades('BRA', tipo_olimpiada)
    ITA = gerar_quantidades('ITA', tipo_olimpiada)
    GER = gerar_quantidades('GER', tipo_olimpiada)
    return(FRA, CAN, BRA, ITA, GER)

def plotar_grafico(FRA, CAN, BRA, ITA, GER):
    plt.xlabel('Países', weight = 'bold')
    plt.ylabel('Quantidade de Atletas', weight = 'bold')
    paises = ['França', 'Canadá', 'Brasil', 'Itália', 'Alemanha']
    plt.boxplot([FRA, CAN, BRA, ITA, GER], labels=paises)
    plt.title('Gráfico Boxplot', weight = 'bold')
    plt.savefig('./png/GráficoBoxPlot.png')

def apresentar_GraficoBoxplot():
 tipo_olimpiada = menu.entrar_argumento_boxplot()
 FRA, CAN, BRA, ITA, GER = armazenar_quantidade(tipo_olimpiada)
 plotar_grafico(FRA, CAN, BRA, ITA, GER)
