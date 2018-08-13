#Uses python3

import sys
import numpy as np

INSERTION = 0
DELETION = 1
MATCH = 2
MISMATCH = 3


def alignment_info(seq1, seq2, seq3, scores):
    """
    :param seq1:
    :param seq2:
    :param scores: tuple of (match score, mismatch score, indel score)
    :return: alignment score matrix, path taken(as values)
    """

    assert len(scores) == 3
    #### NOTE ###
    # x axis and y axis are fecked up for this
    # they are in the classic matriz (row,column,coords)

    # X coord is how far down it is(what row its in)
    # Y coords is how far across it is(what col its in)

    # add - to start of each string for convience
    seq1 = [0] + seq1
    seq2 = [0] + seq2
    seq3 = [0] + seq3
    # also for convience
    match, mismatch, indel = scores
    # create our array of scores
    m = np.zeros((len(seq1), len(seq2), len(seq3)), dtype = int)
    #fill out the edges and
    for seq1_idx in range(np.size(m,0)):
        m[seq1_idx][0] = seq1_idx * indel
    for seq2_idx in range(np.size(m,1)):
        m[0][seq2_idx] = seq2_idx * indel
    for seq3_idx in range(np.size(m,1)):
        m[0][seq3_idx] = seq3_idx * indel


    # fill in rest of the array
    for seq1_idx in range(1, np.size(m,0)):
        for seq2_idx in range(1, np.size(m, 1)):
            for seq3_idx in range(1,np.size(m,2)):
            #find match score
                if seq1[seq1_idx] == seq2[seq2_idx] and seq2[seq2_idx] == seq3[seq3_idx]:
                    s = match
                else:
                    s = mismatch
                # find possible scores
                match_score = s + m[seq1_idx - 1][seq2_idx - 1][seq3_idx - 1] # score for matching or mismatching
                del_word1_score = indel + m[seq1_idx-1][seq2_idx][seq3_idx]
                del_word2_score = indel + m[seq1_idx][seq2_idx-1][seq3_idx]
                del_word3_score = indel + m[seq1_idx][seq2_idx][seq3_idx - 1]
                #find max score
                max_score = max(match_score, del_word1_score, del_word2_score, del_word3_score)
                m[seq1_idx][seq2_idx][seq3_idx] = max_score

    return m




def path_as_instructions(path_as_pts):
    instructions = []
    for idx in range(1, len(path_as_pts)):
        diff = np.array(path_as_pts[idx]) - np.array(path_as_pts[idx - 1])
        if np.array_equal(diff, np.array([1, 1])):
            instructions.append(MATCH)
        elif np.array_equal(diff, np.array([0, 1])):
            instructions.append(INSERTION)
        else:
            instructions.append(DELETION)



    return instructions


def words_aligned(word1, word2, instructions):
    idx1 = 0
    idx2 = 0
    matched_words = [[], []]
    for instruction in instructions:
        if instruction == MATCH:
            matched_words[0].append(word1[idx1])
            idx1 += 1
            matched_words[1].append( word2[idx2])
            idx2 += 1
        elif instruction == INSERTION:
            matched_words[0].append("-")
            # idx1 stays the same
            matched_words[1].append(word2[idx2])
            idx2 += 1
        else:
            matched_words[0].append(word1[idx1])
            idx1 += 1
            matched_words[1].append("-")

    return matched_words


def max_subsequence(word1,word2):
    scores = [1,0,0]
    score_matrix, path_pts = alignment_info(word1, word2, scores)
    path_instructions = path_as_instructions(path_pts)
    words_align = words_aligned(word1,word2, path_instructions)

    max_subseq = []
    for idx in range(len(words_align[0])):
        if words_align[0][idx] == words_align[1][idx]:
            max_subseq.append( (words_align[0][idx]) )
    return max_subseq

def lcs3(a, b, c):
    #write your code here
    return min(len(a), len(b), len(c))

if __name__ == '__main__':
    input = sys.stdin.read()
    #input = "5 8 3 2 1 7 7 8 2 1 3 8 9 7 6 6 8 3 1 4 7" # ans is 3

    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]

    scores = alignment_info(a,b,c,[1,0,0])
    print(scores[-1][-1][-1])

