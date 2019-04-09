# -*- coding: utf-8 -*- 
from parser import Atom, is_valid, run, sub_expr

if __name__ == "__main__":



    A = Atom(True)
    B = Atom(False)

    states_dict= {
        'p': {'A':Atom(True), 'B': Atom(False), 'C': Atom(True)},
        'q': {'A':Atom(False), 'B': Atom(False), 'C': Atom(True)}
    }

    neighbours_dict= {
        'p': ['q']
    } 

    expression = 'p-(A)'

    print(sub_expr(expression))

    is_valid(expression, states_dict)
    print(run(expression, states_dict, neighbours_dict))

    print(run('p-#!CvC->C', states_dict, neighbours_dict))
