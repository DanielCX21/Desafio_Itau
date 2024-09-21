import numpy as np

def determinante(A):
    linhas, colunas = A.shape
    if linhas == colunas and linhas != 0 and colunas != 0:
        return np.linalg.det(A)
    else:
        print("não")

def ver_pos(det):
    if det == 0:
        print("Reta!")
        return False
    else:
        return True

def eliminGauss(inA, inB):
    A = np.copy(inA)
    B = np.copy(inB)
    n = len(B)

    for i in range(n):
        for j in range(i + 1,n):
            m = A[j][i] / A[i][i]
            A[j] = A[j] - m * A[i]
            B[j] = B[j] - m * B[i]
    
    return A, B

def subs_retro(A, B):
    n = len(B)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (B[i] - np.dot(A[i,i+1:],x[i+1:])) / A[i,i]
    return x

#vou receber 3 pontos da forma [x,y]
#vou ter q retornar o valor do ponto de inflexão 
#caso tenha desse intervalo
#[[x1,y1 - 1],[x2,y2 - 1],[x3,y3 - 1]]
#  I       I       I 
#  0,0     1,0     2,0
def resolve_sistema(pontos):
    b = np.array(pontos)
    coefs = np.array([[(b[0,0]) ** 3,(b[0,0]) ** 2,b[0,0]],
                    [(b[1,0]) ** 3,(b[1,0]) ** 2,b[1,0]],
                    [(b[2,0]) ** 3,(b[2,0]) ** 2,b[2,0]]], dtype=float)
    results = np.array([[b[0,1]],[b[1,1]],[b[2,1]]], dtype=float)
    
    if ver_pos(determinante(coefs)):
        A,B = eliminGauss(coefs,results)
        sol = subs_retro(A,B)
        return sol
    else:
        return -1

def pontos_inflexao(pontos):


    sol = resolve_sistema(pontos)

    #intervalo analisado [[1,y1],[3,y2]]

    if sol[0] == 0:
        return -1

    ponto_provavel = - (sol[1] / (3 * sol[0]))

    if ponto_provavel >= 1 and ponto_provavel <= 3:
        return ponto_provavel
    else:
        return -1
    
def pol(sol,x):
    a = sol[0]
    b = sol[1]
    c = sol[2]
    return (a * (x ** 3) + b * (x ** 2) + c *x)

def reta(ang,lin,x):
    return ((ang*x) + lin)
