import numpy as np
from collections import defaultdict
import time

def hash(word, d=256, q=101):
    N = len(word)
    hw = 0
    for i in range(N):  # N - to długość wzorca
        hw = (hw*d + ord(word[i])) % q  # dla d będącego potęgą 2 można mnożenie zastąpić shiftem uzyskując pewne przyspieszenie obliczeń

    return hw


def RabinKarp(path, words, d=256, q=101, P=0.001, b_base=1):
    with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

    S = ''.join(text).lower()
    M = len(S)
    n = len(words)
    N = len(words[0])

    b = -n * np.log(P/(np.log(2)**2))
    k = int(b/(n*np.log(2)))

    b = int(np.round(b))
    b = b * b_base
    k = int(np.round(k))

    hsubs = set()
    bloom_tab = [0 for _ in range(b)]

    prime_numbers = [103, 107, 109, 113, 127, 131, 137, 139,151]
    for sub in words:
        hsubs.add(hash(sub))
        for elem in prime_numbers:
            bloom_tab[hash(sub,q=elem) % b] = 1

    h = 1
    for i in range(N- 1):
        h = (h * d) % q

    hS = hash(S[0:0 + N])
    m = 0
    occur_elem = defaultdict(list)
    false_positive = 0
    while m < M - N + 1:

        if hS in hsubs:

            flag = True

            for elem in prime_numbers:
                if bloom_tab[hash(S[m:m+N],q=elem) % b] == 0:
                    flag = False
            if flag:
                if S[m:m + N] in words:
                    occur_elem[S[m:m+N]].append(m)
                else:
                    false_positive += 1

        if m + N < M :
            hS = (d*(hS - ord(S[m]) * h) + ord(S[m+N])) % q

            if hS < 0:
                hS+=q

        m += 1

    return dict(occur_elem),false_positive


if __name__ == '__main__':
    words = ['gandalf', 'looking', 'blocked', 'comment', 'pouring', 'finally', 'hundred', 'hobbits', 'however', 'popular', 'nothing', 'enjoyed', 'stuffed', 'relaxed', 'himself', 'present', 'deliver', 'welcome', 'baggins', 'further']
    word = ['gandalf']

    t_start_words = time.perf_counter()
    value, false_positive = RabinKarp('lotr.txt', words)
    t_stop_words =  time.perf_counter()

    t_start_word = time.perf_counter()
    value2, false_positive2 = RabinKarp('lotr.txt', word)
    t_stop_word =  time.perf_counter()

    print(f'Wynik: {value}')

    print(f'Czas działania dla 1 wzorca: {t_stop_word - t_start_word}')
    print(f'Czas działania dla 22 wzorców: {t_stop_words - t_start_words}')

    print(f'Fałszywe pozytywne detekcję dla 1 wzorca: {false_positive2}')
    print(f'Fałszywe pozytywne detekcję dla 22 wzorców: {false_positive}')

    value, false_positive = RabinKarp('lotr.txt', word,b_base=2)
    print(f'Fałszywe pozytywne detekcję dla 1 wzorca po dwukrotnym zwiększeniu rozmiaru tablicy: {false_positive}')

    value, false_positive = RabinKarp('lotr.txt', words, b_base=2)
    print(f'Fałszywe pozytywne detekcję dla 22 wzorców po dwukrotnym zwiększeniu rozmiaru tablicy: {false_positive}')