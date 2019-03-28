from parser import Atom
# -*- coding: utf-8 -*- 

def AND(atm1, atm2):
    if (isinstance(atm1, Atom) and isinstance(atm2,Atom)):
        return atm1.val() and atm2.val()

    elif (isinstance(atm1, Atom) and not isinstance(atm2, Atom)):
        return atm1.val() and atm2

    elif (isinstance(atm2, Atom) and not isinstance(atm1, Atom)):
        return atm2.val() and atm

    else:
        return atm1 and atm2

def OR(atm1, atm2):
    if (isinstance(atm1, Atom) and isinstance(atm2,Atom)):
        return atm1.val() or atm2.val()

    elif (isinstance(atm1, Atom) and not isinstance(atm2, Atom)):
        return atm1.val() or atm2

    elif (isinstance(atm2, Atom) and not isinstance(atm1, Atom)):
        return atm2.val() or atm

    else:
        return atm1 or atm2



def NOT(atm):
    if (isinstance(atm, Atom)):
        return not atm.val()
    else:
        return not atm

def IMPLICA(atm1, atm2):
    return OR(NOT(atm1), atm2)


