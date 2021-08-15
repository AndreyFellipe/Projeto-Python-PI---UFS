def ler_Int(msg):
    while True:
        try:
            i = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mErro. Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print(f'\033[31mUsuário não digitou valor.\033[m')
            return 0
        else:
            return i


def gerar_linha(tam = 62):
    return '-' * tam

def gerar_cabecalho(txt):
    print(gerar_linha())
    print(txt.center(62))
    print(gerar_linha())

def gerar_menu(lista):
    gerar_cabecalho('MENU PRINCIPAL')
    cont = 1
    for i in lista:
        print(f'\033[33m{cont}\033[m - \033[34m{i}\033[m')
        cont += 1
    print(gerar_linha())
    opcao = ler_Int('\033[32mSua escolha: \033[m')
    return opcao



def entrar_argumentos():
    medalha = input('Qual o tipo de medalhas você busca na sua evolução(Gold, Silver e Bronze)? ')
    tempo = input('Qual o intervalo de anos, você quer na comparação? ').split()
    ano01 = int(tempo[0])
    ate = int(tempo[1])
    tipoOlimpiada = input('Qual o tipo de olimpiada que você busca Winter ou Summer: ')

    if tipoOlimpiada == 'Winter':
        while True:
            if ano01 % 4 == 2:
                de = ano01
                break
            elif ano01 % 4 != 2:
                ano01 += 1
        if ate >= 2018:
            ate = 2014
    else:
        while True:
            if ano01 % 4 == 0:
                de = ano01
                break
            elif ano01 % 4 != 0:
                ano01 += 1
        if ate >= 2020:
            ate = 2016
    return (medalha, de, ate, tipoOlimpiada)

def entrar_argumentos_barras():
    ano = input('Digite o ano desejado: ')
    tipo_olimpiada = input('Digite o tipo de Olimpíada: ')
    return (ano, tipo_olimpiada)


def entrar_argumentos_textualT7():
    tipodemedalha = input('Qual o tipo de medalha desejada(Gold, Silver, Bronze)? ')
    games = input('Qual a olímpiada desejada(Ano Tipo)? ')
    return (tipodemedalha, games)


def entrar_argumentos_escolhidoT1():
  cidade = input('Digite uma cidade onde fora realizada a olímpiada: ')
  ano = input('Digite o ano correspondente à olímpiada: ')
  return (cidade, ano)


def entrar_argumento_boxplot():
  tipo_olimpiada = input('Digite o tipo de olimpíada: ')
  return tipo_olimpiada