import numpy as np
import os 


def checa_vetor4(v:np.array) -> None:

    if v.shape != (4,1):
        raise ValueError('O seu valor deveria possuir 4 linhas e um ')

def checa_vetor3(v:np.array) -> None:

    if v.shape != (3,3):
        raise ValueError('O seu valor deveria possuir 3 linhas e 3 colunas ')       

if __name__=='__main__':

    v1 = np.array([1,1])
    v2 = np.array([[1,1,1],[2,2,3],[4,3,1]])
    print(v1)
    print('\n',v2)
    try:
        checa_vetor4(v1)

    except ValueError as v:
        print(v)

    try:
        checa_vetor3(v2)

    except ValueError as v:
        print(v)


        