# -*- coding: utf-8 -*- 
from parser import Atom, is_valid, test

if __name__ == "__main__":

    states_dict= {
        's1': {'A':Atom(False), 'B': Atom(False), 'C': Atom(False)},
        's2': {'A':Atom(False), 'B': Atom(False), 'C': Atom(True)},
        's3': {'A':Atom(False), 'B': Atom(True), 'C': Atom(False)},
        's4': {'A':Atom(False), 'B': Atom(True), 'C': Atom(True)},
        's5': {'A':Atom(True), 'B': Atom(False), 'C': Atom(False)},
        's6': {'A':Atom(True), 'B': Atom(False), 'C': Atom(True)},
        's7': {'A':Atom(True), 'B': Atom(True), 'C': Atom(False)},
        's8': {'A':Atom(True), 'B': Atom(True), 'C': Atom(True)},
    }

    neighbours_dict= {
        's1': {'R1':['s2'], 'R2':['s2']},
        's2': {'R1':['s1', 's3', 's8']},
        's4': {'R2': ['s2', 's5'], 'R3': ['s3']}
    } 

    agentes_dict = {
        'R1': {'all': '#', 'any':'@'},
        'R2': {'all': '$', 'any': '&'},
        'R3': {'all': '?', 'any': '*'}
    }



    # ####sintaxe:
    #     #estado inicial no começo seguido de -. Ex:
    #         #'s-'
    #     #operacoes validas:
    #         #^ -> and
    #         #v -> or
    #         #! -> not
    #         #-> -> implica
            
    #         ####operações de mudança de estados
    #         todas as operações declaradas em agented dict são válidas;
    #         as arestas de um estado para o outro são declaradas utilizando o neighbours dict
            

    #exemplos
    expr1 = 's4-$C->*!A'
    print(expr1)
    print(test(expr1, states_dict, neighbours_dict, agentes_dict))

    print("##########")
    
    expr2 = 's1-@!(C^Bv(A^B))^!(C)->C'
    print(expr2)
    print(test(expr2, states_dict, neighbours_dict, agentes_dict))
    print("##########")


    expr3 = 's1-@!((!(C^Bv(A^B))^!(C)))->C^A^(BvA)'
    print(expr3)
    print(test(expr3, states_dict, neighbours_dict, agentes_dict))
    print("##########")

    expr4 = 's1-@!((!(C^Bv(A^B))^!(C)))->C^A^(BvA)->!(A)v(B^!C)->C'
    print(expr4)
    print(test(expr4, states_dict, neighbours_dict, agentes_dict))
    print("##########")

    expr5 = 's4-@(C^B)'
    print(expr5)
    print(test(expr5, states_dict, neighbours_dict, agentes_dict))
    print("##########")
