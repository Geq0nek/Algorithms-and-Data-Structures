import time
import numpy as np

def string_compare(P: str, T: str, i: int, j: int):
    if i == 0:
        return len(T[:j])
    if j == 0:
        return len(P[:i])
    
    z = string_compare(P, T, i-1, j-1) + (P[i] != T[j])
    w = string_compare(P, T, i, j-1) + 1
    u = string_compare(T, T, i-1, j) + 1

    return min(z, w, u)


def PD(P: str, T: str, i: int, j: int, is_d=False):
    m, n = len(P), len(T)

    if is_d:
        D = np.zeros((m ,n), dtype=int)
        parent = np.full((m, n), 'X')

        for i in range(1, len(D)):
            D[i][0] = i

        for i in range(1, len(parent)):
            parent[i][0] = 'D'
    else:
        D = np.zeros((m ,n), dtype=int)
        parent = np.full((m, n), 'X')


        for i in range(len(D)):
            D[i][0] = i
            D[0][i] = i

        for i in range(1, len(parent)):
            parent[i][0] = 'D'
            parent[0][i] = 'I'

    
    for i in range(1, D.shape[0]):
        for j in range(1, D.shape[1]):
            z = D[i-1][j-1] + (P[i] != T[j])
            w = D[i][j-1] + 1
            u = D[i-1][j] + 1
            
            min_cost = min(z, w, u)

            if min_cost == z:
                if P[i]!=T[j]:
                    parent[i][j] = 'S'
                else:
                    parent[i][j] = 'M'
            elif min_cost == w:
                parent[i][j] = 'I'
            elif min_cost == u:
                parent[i][j] = 'D'

            D[i][j] = min_cost

    return D, parent


def track_playback(parent):
    lst = []
    i = parent.shape[0] - 1
    j = parent.shape[1] - 1
    elem = parent[-1][-1]


    while elem != 'X':
        lst.append(parent[i][j])

        if parent[i][j] == 'S' or parent[i][j] == 'M':
            i -= 1
            j -= 1
        elif parent[i][j] == 'I':
            j -= 1
        elif parent[i][j] == 'D':
            i -= 1

        elem = parent[i][j]


    lst = lst[::-1]
    return ''.join(lst)

def goal_cell(P, T, D):
    i = len(P) - 1
    j = 0
    for k in range(1, len(T)):
        if D[i][k] < D[i][j]:
            j = k

    return j

def PD_e(P: str, T: str, i: int, j: int):
    m, n = len(P), len(T)
    D = np.zeros((m, n),dtype=int)

    for i in range(D.shape[0]):
        D[i][0]= i

    for i in range(D.shape[1]):
        D[0][i] = i

    parent = np.full((m, n),'X')

    for i in range(1,parent.shape[0]):
        parent[i][0] = 'D'

    for i in range(1,parent.shape[1]):
        parent[0][i] = 'I'


    for i in range(1, D.shape[0]):
        for j in range(1, D.shape[1]):
            if P[i]!=T[j]:
                z = D[i-1][j-1]  + 1e16
            else:
                z = D[i - 1][j - 1]

            w = D[i][j-1] +1
            u = D[i-1][j] +1

            min_cost = min(z, w, u)

            if min_cost == z:
                if P[i]!=T[j]:
                    parent[i][j] = 'S'
                else:
                    parent[i][j] = 'M'

            elif min_cost == w:
                parent[i][j] = 'I'

            elif min_cost == u:
                parent[i][j] = 'D'

            D[i][j] = min_cost

    return D[-1][-1],parent    

if __name__ == '__main__':
    #podpunkt A
    P = ' kot'
    T = ' pies'

    ans = string_compare(P, T, len(P)-1, len(T)-1)
    print(ans)

    #podpunkt B
    P = ' biały autobus'
    T = ' czarny autokar'

    D, parent = PD(P, T, len(P)-1, len(T)-1)
    print(D[-1][-1])

    #podpunkt C
    P = ' thou shalt not'
    T = ' you should not'

    D, parent = PD(P, T, len(P)-1, len(T)-1)

    print(track_playback(parent))

    #podpunkd D
    P = ' ban'
    D, parent = PD(P, T, len(P)-1, len(T)-1, is_d=True)
    idx = goal_cell(P, T, D)
    print(idx - (len(P)-1))

    #podpunkt E
    P = ' democrat'
    T = ' republican'

    D, parent = PD_e(P, T, len(P)-1, len(T)-1)
    path = track_playback(parent)
    lst = [elem for elem in path if elem != 'D']
    help_lst = []
    for i in range(len(lst)):
        if lst[i] == 'M':
            help_lst.append(i)
    label = ''.join([T[elem + 1] for elem in help_lst])
    print(label)


    #podpunkt F
    T = ' 243517698'
    P_lst = [2,4,3,5,1,7,6,9,8]
    P_lst.sort()
    P = ' '
    P_label = ''.join(map(str,P_lst))
    P += P_label

    D, parent = PD_e(P, T, len(P)-1, len(T)-1)
    path = track_playback(parent)
    lst = [elem for elem in path if elem != 'D']
    help_lst = []
    for i in range(len(lst)):
        if lst[i] == 'M':
            help_lst.append(i)
    label = ''.join([T[elem + 1] for elem in help_lst])
    print(label)