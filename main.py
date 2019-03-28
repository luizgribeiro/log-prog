# -*- coding: utf-8 -*- 
from parser import Atom, is_valid, run

if __name__ == "__main__":



    A = Atom(True)
    B = Atom(False)

    states_dict= {
        'p': {'A':Atom(True), 'B': Atom(False), 'C': Atom(True)},
        'q': {'A':Atom(False), 'B': Atom(False), 'C': Atom(True)}
    }

    neighbours_list = {
        'p': ['q']
    } 



    is_valid('p-A', states_dict)
    print(run('p-!AvB->B', states_dict))

    #print(IMPLICA(B,AND(A,B)))