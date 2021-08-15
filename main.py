##########################################################
# Arquivos com bibliotecas
##########################################################

import menu
import textualT7
import escolhidoT1
import graficolinhasL17
import graficobarrasB16
import graficoboxplotX8

##########################################################
# Menu com chamada de funções
##########################################################

while True:
  resp = menu.gerar_menu(['Gráfico de Linhas', 'Gráfico de Barras', 'Gráfico Boxplot', 'Resposta Textual','Resposta Textual Escolhida', 'Encerrar'])
  if resp == 1:
      graficolinhasL17.apresentar_graflinhas()
  elif resp == 2:
      graficobarrasB16.apresentar_grafico_barras()
  elif resp == 3:
      graficoboxplotX8.apresentar_GraficoBoxplot()
  elif resp == 4:
      textualT7.apresentar_textualT7()
  elif resp == 5:
      escolhidoT1.apresentar_escolhidoT1()
  elif resp == 6:
      menu.gerar_cabecalho('Até logo!')
      break
  else:
      print('\033[31mERRO! Por gentileza, digite um número válido!\033[m')