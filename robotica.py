import numpy as np
import os 


def checa_vetor4(v:np.array) -> None:

    if v.shape != (4,1):
        raise ValueError('O seu valor deveria possuir 4 linhas e um ')

def checa_vetor3x3(v:np.array) -> None:

    if v.shape != (3,3):
        raise ValueError('O seu valor deveria possuir 3 linhas e 3 colunas ')       
        
def checa_matriz_rotação(v: np.array, det_tol:float =0.01)->None:
    checa_vetor3x3(v2)
    detm = np.linalg.det(v2)
    if not ((1-det_tol) <= detm <= (1+ det_tol)):
        raise ValueError('o determinante sla o q')



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
        checa_vetor3x3(v2)

    except ValueError as v:
        print(v)

    try:
        checa_matriz_rotação(v2)

    except ValueError as v:
        print(v)

def cria_operador4(m_rot_b_a:np.array = np.eye[3],v_o_a: np.array = np.zeros([3],[1]), det_tol: float = 0.01) -> np.array:

    checa_matriz_rotação(m_rot_b_a, det_tol)
    checa_vetor3x3(v_o_a)
    res=np.append(m_rot_b_a,v_o_a,axis=1)
    res=np.append(res,np.array([[0,0,0,1]]),axis=0)
    return res 

nat = np.append([1,2,3],[4,5,6],[7,8,9],axis=0)
print (nat)

vet = np.array([[9],[8],[7]])
res = np.append(nat, vet, axis=1)
print(res)
res= np.append(res,np.append([0,0,0,1]), axis=0)