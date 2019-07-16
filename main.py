# -*- coding: utf-8 -*- 
from parser import Atom, is_valid, test
from colorama import Fore, Style

def poda_inicial(estado_real, states_dict):

    #criando lista de estados que serao deletados
    estados_deletados = []
    for estado, agentes in states_dict.items():
        deletado = True
        for key, value in estado_real.items():
            if agentes[key] == value:
                deletado = False
        if deletado == True:
            estados_deletados.append(estado)

    for estado in estados_deletados:
        del states_dict[estado]

def print_estados_duvidas(states_dict, agentes):

    #print dos estados que exitem
    for estado, valores in states_dict.items():
        print(Fore.MAGENTA + f'Estado {estado} valores {valores}')

    print(Style.RESET_ALL)

def generate_trans_duvida(states_dict, agentes):
    
    duvida = {ag:[] for ag in agentes}
    for est, val in states_dict.items():
        for estados, config in states_dict.items():
            for agente in agentes:
                if est != estados and val[agente] == config[agente]:
                    duvida[agente].append(est)

    return duvida

def check_end(duvida_dict, estado_real, states_dict):

    vencedores = []
    for agente, duvidas in duvida_dict.items():
        duvidas_reais = 0
        #para cada estado em que ele está em dúvida
        for duvida in duvidas:
            #se ele não tiver a carta 
            if states_dict[duvida][agente] == estado_real[agente]:
                duvidas_reais += 1
        if duvidas_reais == 0:
            vencedores.append(agente)

    if vencedores:
        return True, vencedores

    return False, None

def poda_geral(anuncio, states_dict):

    deletados = []
    agente = anuncio[0]
    info = anuncio[1:]
    for estado, valores in states_dict.items():
        if not eval(f'{valores[agente]}{info}'):
            deletados.append(estado)

    for estado in deletados:
        del states_dict[estado]

if __name__ == "__main__":

    termino = False

    states_dict= {
        's1': {'A':1, 'B':2, 'C':3},
        's2': {'A':1, 'B':3, 'C':2},
        's3': {'A':2, 'B':1, 'C':3},
        's4': {'A':2, 'B':3, 'C':1},
        's5': {'A':3, 'B':2, 'C':1},
        's6': {'A':3, 'B':1, 'C':2},
    }

    agentes = ['A', 'B', 'C']

    neighbours_dict= {
        's1': {'a':['s2'], 'b':['s5'], 'c':['s3']},
        's2': {'a':['s1'], 'b':['s4'], 'c':['s6'], },
        's3': {'a':['s4'], 'b':['s6'], 'c':['s1'], },
        's4': {'a':['s3'], 'b':['s2'], 'c':['s5'], },
        's5': {'a':['s6'], 'b':['s1'], 'c':['s4'], },
        's6': {'a':['s5'], 'b':['s3'], 'c':['s2'], },
    } 

    #irrelevante nesse caso
    agentes_dict = {}


    estado_real = {}


    # ####sintaxe:
    #     #estado inicial no começo seguido de -. Ex:
    #         #'s-'
    #     #operacoes validas:
    #         #^ -> and
    #         #v -> or
    #         #! -> not
    #         #-> -> implica

    print("Qual é o estado real em que o sistema se encontra?")
    for agt in agentes:
        print(f'Insira o valor de {agt}')
        estado_real[agt] = int(input())

    print("#######")


    duvidas = generate_trans_duvida(states_dict, agentes)

    while not termino:
        print_estados_duvidas(states_dict, agentes)
        for agente, estados in duvidas.items():
            print(Fore.GREEN + f'Agente {agente} em dúvida nos estados {estados}')
        print(Style.RESET_ALL)

        acao = input(f'Insira o anuncio realizado pelo agente (utilize a sintaxe do python)\n')

        poda_geral(acao, states_dict)

        duvidas = generate_trans_duvida(states_dict, agentes)
        status, agente_vencedor = check_end(duvidas, estado_real, states_dict)

        print_estados_duvidas(states_dict, agentes)
        for agente, estados in duvidas.items():
            print(Fore.GREEN + f'Agente {agente} em dúvida nos estados {estados}')
        print(Style.RESET_ALL)
        if status == True:
            for agente in agente_vencedor:
                print(Fore.RED + f"Agente vencedor: {agente}")
            print(Style.RESET_ALL)
            termino = True
        
