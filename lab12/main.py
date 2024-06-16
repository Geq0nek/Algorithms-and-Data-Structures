import time

def NaiveMethod(S, W):
    m = 0
    counter = 0
    ans = 0

    t_start = time.perf_counter()
         
    while m != len(S) - len(W):
        i = 0
        while i < len(W) and S[m + i] == W[i]:
            counter += 1
            i += 1

            if i == len(W):
                ans += 1

        m += 1
        
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start)) 
    print(f'{ans} ; {counter}')
    

def hash(word, d=256, q=101):
    N = len(word)
    hw = 0
    for i in range(N):  # N - to długość wzorca
        hw = (hw*d + ord(word[i])) % q  # dla d będącego potęgą 2 można mnożenie zastąpić shiftem uzyskując pewne przyspieszenie obliczeń

    return hw

def RabinKarp(S, W, d=256, q=101):
    counter = 0
    compare = 0
    collision_number = 0

    M = len(S)
    N = len(W)
    hW = hash(W)
    hS = hash(S[0:N])
    h = 1

    for i in range(N - 1):
        h = (h * d) % q

    t_start = time.perf_counter()
    
    for m in range(M - N + 1):
        compare += 1

        if hS == hW:
            if S[m:m+N] == W:
                counter += 1
            else:
                collision_number += 1

        if m + N < M:
            hS = (d * (hS - ord(S[m]) * h) + ord(S[m+N])) % q
            if hS < 0:
                hS += q

    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start)) 

    return counter, compare, collision_number


if __name__ == '__main__':
    with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

    S = ''.join(text).lower()
    W = 'time.'
    NaiveMethod(S, W)

    ans = RabinKarp(S, W)
    print(f'{ans[0]} ; {ans[1]} ; {ans[2]}')
