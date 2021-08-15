#T1. Quantos países participaram da Olimpíada de <Cidade>?
import csv
import menu


def filtrar_paises(cidade, ano):
  paises = list()

  with open('./csv/athlete_events.csv', 'r') as events:
      eventler = csv.reader(events)
      next(eventler)
      for i in eventler:
          if i[11] == cidade and i[9] == ano:
              paises.append(i[7])
  return(paises)

def printar_paises(paises):
  paisesn = set(paises)
  print(f'Participaram dessa olimpíada: {len(paisesn)} países')

def apresentar_escolhidoT1():
  cidade, ano = menu.entrar_argumentos_escolhidoT1()
  paises = filtrar_paises(cidade, ano)
  printar_paises(paises)