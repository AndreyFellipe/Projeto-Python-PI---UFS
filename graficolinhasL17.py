#Opções de medalha: NA, Gold, Silver e Bronze
#Tipo de olimp : Summer e Winter

import csv
import matplotlib.pyplot as plt
import menu

def geradorDeCountries():
    Africa = list()
    Asia = list()
    Europe = list()
    NorthAmerica = list()
    Oceania = list()
    SouthAmerica = list()

    with open('./csv/countries-continents.csv', 'r') as arquivo:
        countries = csv.reader(arquivo)
        next(countries)
        for countrie in countries:
            if countrie[0] == 'North America':
                NorthAmerica.append(countrie[1])
            if countrie[0] == 'Oceania':
                Oceania.append(countrie[1])
            if countrie[0] == 'Africa':
                Africa.append(countrie[1])
            if countrie[0] == 'Europe':
                Europe.append(countrie[1])
            if countrie[0] == 'Asia':
                Asia.append(countrie[1])
            if countrie[0] == 'South America':
                SouthAmerica.append(countrie[1])
    return (Africa, Asia, Europe, NorthAmerica, SouthAmerica, Oceania)

def geradorDeNocs(Africa, Asia, Europe, NorthAmerica, SouthAmerica, Oceania):

    nocsAfrica = list()
    nocsAsia = list()
    nocsEurope = list()
    nocsNorthAmerica = list()
    nocsOceania = list()
    nocsSouthAmerica = list()

    with open('./csv/noc_regions.csv', 'r') as arquivo:
        nocs = csv.reader(arquivo)
        next(nocs)
        for noc in nocs:
            if noc[1] == 'USA':
                nocsNorthAmerica.append('US')
                nocsNorthAmerica.append('USA')
            if noc[1] == 'Czech Republic' or noc[1] == 'UK':
                nocsEurope.append('CZE')
                nocsEurope.append('CZ')
                nocsEurope.append('GBR')
            if noc[1] in Africa or noc[2] in Africa:
                nocsAfrica.append(noc[0])
            if noc[1] in Asia or noc[2] in Asia:
                nocsAsia.append(noc[0])
            if noc[1] in Europe or noc[2] in Europe:
                nocsEurope.append(noc[0])
            if noc[1] in NorthAmerica or noc[2] in NorthAmerica:
                nocsNorthAmerica.append(noc[0])
            if noc[1] in SouthAmerica or noc[2] in SouthAmerica:
                nocsSouthAmerica.append(noc[0])
            if noc[1] in Oceania or noc[2] in Oceania:
                nocsOceania.append(noc[0])
            nocsSouthAmerica.append('AHO')
    return (nocsAsia, nocsNorthAmerica, nocsSouthAmerica, nocsAfrica, nocsEurope, nocsOceania)

def gerarPaisesFiltrados(medalha, de, ate, tipoOlimpiada, nocsNorthAmerica, nocsOceania, nocsAfrica, nocsEurope, nocsAsia, nocsSouthAmerica):
    listaDeAnos = list()
    listaAfrica = []
    listaAsia = []
    listaEurope = []
    listaNorthAmerica = []
    listaOceania = []
    listaSouthAmerica = []

    for ano in range(de, ate+1, 4):
        listaDeAnos.append(ano)
        with open('./csv/athlete_events.csv', 'r') as info:
            infoAtletas = csv.reader(info)
            africa = 0
            asia = 0
            europe = 0
            northAmerica = 0
            oceania = 0
            southAmerica = 0

            for info in infoAtletas:
                if info[10] == tipoOlimpiada and int(info[9]) == ano and info[14] == medalha:
                    if info[7] in nocsNorthAmerica:
                        northAmerica += 1
                    if info[7] in nocsOceania:
                        oceania += 1
                    if info[7] in nocsAfrica:
                        africa += 1
                    if info[7] in nocsEurope:
                        europe += 1
                    if info[7] in nocsAsia:
                        asia += 1
                    if info[7] in nocsSouthAmerica:
                        southAmerica += 1

            listaAfrica.append(africa)
            listaAsia.append(asia)
            listaEurope.append(europe)
            listaNorthAmerica.append(northAmerica)
            listaOceania.append(oceania)
            listaSouthAmerica.append(southAmerica)
    return (listaDeAnos, listaEurope, listaAsia, listaAfrica, listaOceania, listaNorthAmerica, listaSouthAmerica)

def gerarGrafLinhas(x, y, y1, y2, y3, y4, y5, medalha):

    plt.ylim(0, 500)
    plt.xlim(0, 100)
    plt.title(f'Quantidade de medalhas de {medalha}s por Continentes', weight= 'bold')

    plt.xlabel('Anos das Olimpiadas', weight= 'bold')
    plt.ylabel('Quantidade de Medalhas', weight= 'bold')
    plt.grid()

    plt.plot(x, y, c='r', ls='-', lw='1', marker='o', ms=10, fillstyle='full', label ='Africa')
    plt.plot(x, y1, c='g', ls='-', lw='1', marker='o', ms=10, fillstyle='full', label ='Oceania')
    plt.plot(x, y2, c='b', ls='-', lw='1', marker='o', ms=10, fillstyle='full', label ='Asia')
    plt.plot(x, y3, c='c', ls='-', lw='1', marker='o', ms=10, fillstyle='full', label ='South America')
    plt.plot(x, y4, c='m', ls='-', lw='1', marker='o', ms=10, fillstyle='full', label ='North America')
    plt.plot(x, y5, c='y', ls='-', lw='1', marker='o', ms=10, fillstyle='full', label ='Europe')
    plt.axis('auto')
    plt.legend()
    plt.savefig('./png/GráficoLinhas.png')

def apresentar_graflinhas():
    medalha, de, ate, tipoOlimpiada = menu.entrar_argumentos()
    Africa, Asia, Europe, NorthAmerica, SouthAmerica, Oceania = geradorDeCountries()
    nocsAsia, nocsNorthAmerica, nocsSouthAmerica, nocsAfrica, nocsEurope, nocsOceania = geradorDeNocs(Africa,
        Asia, Europe, NorthAmerica, SouthAmerica, Oceania)
    listaDeAnos, listaEurope, listaAsia, listaAfrica, listaOceania, listaNorthAmerica, listaSouthAmerica = gerarPaisesFiltrados(medalha,
        de, ate, tipoOlimpiada, nocsNorthAmerica, nocsOceania, nocsAfrica, nocsEurope, nocsAsia, nocsSouthAmerica)
    gerarGrafLinhas(listaDeAnos, listaAfrica, listaOceania, listaAsia, listaSouthAmerica, listaNorthAmerica, listaEurope, medalha)