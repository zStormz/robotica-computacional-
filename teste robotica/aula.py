import numpy as np
import os


def matriz_rotacao_x(theta: float)-> np.array:
    res = np.zeros([3,3])
    res [0,0] = 1 
    res[1,1], res[2,2] = np.cos(theta), np.cos(theta)
    res[2,1], res [1,2] = -np.sin(theta), np.sin(theta)
    return res

def cria_vetor3(vlist):
    #testa se lista tem no minimo 3 elementos
    if len(vlist) == 3:
        for item in vlist:
            try:
                n=float(item)
            except:
                raise ValueError('Valores Invalidos')
        #cria matriz vazia com numpy
        res= np.zeros([3,1])
        for cl in range(0,len(vlist)):
            res[cl,0] = vlist[cl]
        return res
    raise ValueError("A sua lista deveria ter 3 posições")



def checa_vetor4(v: np.ndarray) -> None:

    if v.shape != (4, 1):
        raise ValueError('O vetor não é 4x1')


def checa_matriz33(m: np.array)-> None:
    
    if m.shape != (3,3):
        raise ValueError('Matriz deve ser 3x3')

def checa_matriz44(m: np.array)-> None:

    if m.shape !=(4,4):
        raise ValueError('Matriz deve ser 4x4')

def checa_vetor3(m):

    if m.shape != (3,1):
        raise ValueError("O seu vetor deve ter 3 linha e 1 coluna")
    else: print('Vetor correto')

def checa_matriz_rotacao(m3: np.ndarray, det_tol: float = 0.01) -> None:

    checa_matriz33(m3)
    if np.abs(1-np.linalg.det(m3)) > det_tol:
        raise ValueError('O determinante da matriz não é 1.')
    else:
        print('Matriz correta')

def cria_vetor4(v3: np.ndarray) -> np.ndarray:

    checa_vetor3(v3)
    aux = np.ones([4, 1])
    aux[0:3, 0] = v3[0:3, 0]
    return aux
    
def teste(v1):
    checa_vetor4(v1)


if __name__=='__main__':
    os.system('cls')

 

    v1 = np.array([[1],[1],[2],[5]])
    print(v1)
    try:
        teste(v1)
        print('ok ')
    except ValueError as v:
        print(v)

def cria_operador4(m_rot_b_a: np.ndarray = np.eye(3), v_o_a: np.ndarray = np.zeros([3, 1]), det_tol: float = 0.01) \
        -> np.ndarray:

    checa_matriz33(m_rot_b_a)
    checa_matriz_rotacao(m_rot_b_a, det_tol=det_tol)
    checa_vetor3(v_o_a)
    T = np.append(m_rot_b_a, v_o_a, axis=1)
    T = np.append(T, np.asarray([[0, 0, 0, 1]]), axis=0)
    return T

nat = np.append([[1,2,3],[3,4,5]],[[7,8,9]], axis=0)

vet = np.array([[9],[8],[7]])
res = np.append(nat,vet,axis=1)

res = np.append(res,np.array([[0,0,0,1]]),axis=0)


def constroi_vetor(v_b: np.ndarray,m_rot_b_a: np.ndarray = np.eye(3),v_o_a: np.ndarray = np.zeros([3, 1]),det_tol: float = 0.01) -> np.ndarray:

    checa_vetor3(v_b)
    checa_matriz33(m_rot_b_a)
    checa_matriz_rotacao(m_rot_b_a)
    checa_vetor3(v_o_a)

    T = cria_operador4(m_rot_b_a, v_o_a, det_tol=det_tol)
    v_b4 = cria_vetor4(v_b)

    v = T @ v_b4

    return np.asarray(v[0:3, :])
