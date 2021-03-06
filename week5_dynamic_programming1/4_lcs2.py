#Uses python3

import sys
import numpy as np

def align_score(word1,word2, scores):
    """
    :param word1: string
    :param word2:  string
    :param scores: tuple of (match score, mismatch score, indel score)
    :return: max alignment score
    """


    # add - to start of each string
    word1 = [0] + word1
    word2 = [0] + word2

    # for convience
    match, mismatch, indel = scores
    # create our array of scores
    m = np.zeros( (len(word1), len(word2) ), dtype = int)

    #fill out the edges
    for word1_idx in range(np.size(m,0)):
        m[word1_idx][0] = word1_idx * indel
    for word2_idx in range(np.size(m,1)):
        m[0][word2_idx] = word2_idx * indel

    # fill in rest of the array
    for word2_idx in range(1, np.size(m,1)):
        for word1_idx in range(1, np.size(m,0)):
            #find match score
            if word1[word1_idx] == word2[word2_idx]:
                s = match
            else:
                s = mismatch

            match_score = s + m[word1_idx-1][word2_idx-1]

            insert_score = indel + m[word1_idx-1][word2_idx]
            del_score = indel + m[word1_idx][word2_idx-1]

            m[word1_idx][word2_idx] = max(match_score, insert_score, del_score)

    

    return m[-1][-1]


def lcs2(a, b):
    return align_score(a,b,(1,0,0))

if __name__ == '__main__':
    input = sys.stdin.read()
    #input = "4 2 7 8 3 4 5 2 8 7"
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))

