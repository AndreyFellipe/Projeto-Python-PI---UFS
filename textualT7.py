import csv
import menu

#T7. Vencedores de medalhas em diferentes esportes numa mesma olimpíada.
#tipomedalha, games

def filtrar_vencedores(tipodemedalha, games):
  vencedores = list()
  with open('./csv/athlete_events.csv', 'r') as events:
            eventler = csv.reader(events)
            next(eventler)
            for i in eventler:
              if i[14] == tipodemedalha and i[8] == games:
                vencedores.append((i[1], i[12]))
  return(vencedores)              

def printar_vencedores(vencedores):
  for nome, esporte in set(vencedores):
        print('\033[33mNome: \033[m' + nome + '\033[31m | \033[m' + '\033[32mTipo de Esporte: \033[m'+ esporte)

def apresentar_textualT7():
  tipodemedalha, games = menu.entrar_argumentos_textualT7()
  vencedores = filtrar_vencedores(tipodemedalha, games)
  printar_vencedores(vencedores)