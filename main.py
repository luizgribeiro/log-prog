
from operations import AND, IMPLICA, NOT, OR
from parser import Atom

if __name__ == "__main__":



    A = Atom(True)
    B = Atom(False)


    print(IMPLICA(B,AND(A,B)))