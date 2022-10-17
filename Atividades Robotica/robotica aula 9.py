import numpy as np


def _distancia_entre_retas_p(po1:np.array,po2: np.array, vs: np.array) -> float:


    vsu = vs/norma_vetor(vs)
    ws = po2 - po1 - proj_vetores(po2-po1,vs)
    return norma_vetor(ws)

def distancia_entre_retas(po1: np.array,vs1: np.array,po2: np.array,vs2: np.array, angtol=1e-3) -> float:

    checa_vetor(po1)
    checa_vetor(po2)
    checa_vetor(vs1)
    checa_vetor(vs2)

    if np.abs(ang_vetores(vs1,vs2)) <= angtol:
        return _distancia_entre_retas_p(po1,po2,vs1)
    else:
        _distancia_entre_retas_p(po1,po2,vs2)