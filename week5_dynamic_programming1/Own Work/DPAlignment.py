"""
TODO

CONVERT it to sequence based
easier to go sequence to string
rather than string to sequence

refer to lcs2 and lcs3



have it so that various functions return:
1. just the score
2. the score matrix
3. the path as values
4. the path as instructions (insert delete etc.)
5. visual of the strings aligned
6. the longest subsequence(sequence itself no just length)


"""

import numpy as np

INSERTION = 0
DELETION = 1
MATCH = 2
MISMATCH = 3



def alignment_info(word1, word2, scores):
    """
    :param word1: string
    :param word2:  string
    :param scores: tuple of (match score, mismatch score, indel score)
    :return: alignment score matrix, path taken(as values)
    """

    assert type(word1) == str
    assert  type(word2) == str
    assert len(scores) == 3
    #### NOTE ###
    # x axis and y axis are fecked up for this
    # they are in the classic matriz (row,column,coords)

    # X coord is how far down it is(what row its in)
    # Y coords is how far across it is(what col its in)

    # add - to start of each string for convience
    word1 = "-" + word1
    word2 = "-" + word2
    # also for convience
    match, mismatch, indel = scores
    # create our array of scores
    m = np.zeros( (len(word1), len(word2) ), dtype = int)
    # each entry of paths array is a point(2d point)
    paths = np.zeros( (len(word1), len(word2) ), dtype = (int, 2) )

    #fill out the edges and
    for x_idx in range(np.size(m,0)):
        m[x_idx][0] = x_idx * indel
    for y_idx in range(np.size(m,1)):
        m[0][y_idx] = y_idx * indel

    #add in the paths for the edges
    #note paths[0][0] = (0, 0) is already done by default
    #hence both ranges start at 1
    for y_idx in range(1,np.size(m,0)):
        paths[y_idx][0] =   y_idx - 1,0
    for x_idx in range(1, np.size(m,1)):
        paths[0][x_idx] = 0 , x_idx - 1
    # fill in rest of the array
    for y_idx in range(1, np.size(m,1)):
        for x_idx in range(1, np.size(m,0)):
            #find match score
            if word1[x_idx] == word2[y_idx]:
                s = match
            else:
                s = mismatch
            # find possible scores
            match_score = s + m[x_idx-1][y_idx-1]
            insert_score = indel + m[x_idx-1][y_idx]
            del_score = indel + m[x_idx][y_idx-1]
            #find max score
            max_score = max(match_score, insert_score, del_score)
            m[x_idx][y_idx] = max_score
            # record previous pt
            if max_score == match_score:
                paths[x_idx][y_idx] = x_idx - 1, y_idx - 1
            elif max_score == insert_score:
                paths[x_idx][y_idx] = x_idx - 1, y_idx
            else:
                paths[x_idx][y_idx] = x_idx, y_idx - 1


    path = []
    curr_idx = (len(word1) -1, len(word2) - 1)
    path.append(curr_idx)
    while not ( curr_idx[0] == 0 and curr_idx[1] == 0 ):
        prev_idx = paths[curr_idx[0]][curr_idx[1]]
        curr_idx = prev_idx
        path.append((curr_idx[0], curr_idx[1]))
    path.reverse()
    return m, path


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
    matched_words = ["", ""]
    for instruction in instructions:
        if instruction == MATCH:
            matched_words[0] += word1[idx1]
            idx1 += 1
            matched_words[1] += word2[idx2]
            idx2 += 1
        elif instruction == INSERTION:
            matched_words[0] += "-"
            # idx1 stays the same
            matched_words[1] += word2[idx2]
            idx2 += 1
        else:
            matched_words[0] += word1[idx1]
            idx1 += 1
            matched_words[1] += "-"

    return matched_words


def max_subsequence(word1,word2):
    scores = [1,0,0]
    score_matrix, path_pts = alignment_info(word1, word2, scores)
    path_instructions = path_as_instructions(path_pts)
    words_align = words_aligned(word1,word2, path_instructions)

    max_subseq = ""
    for idx in range(len(words_align[0])):
        if words_align[0][idx] == words_align[1][idx]:
            max_subseq += (words_align[0][idx])
    return max_subseq


def alignment_score(word1, word2, scores):
    score_matrix = alignment_info(word1,word2, scores)[0]
    return score_matrix[-1][-1]

word1 = "ABBG"
word2 = "BAGATG"
scores = [5,-2,-4]

print(word1)
print(word2)

scores, path = alignment_info(word1, word2, [1,0,0])

instructions = path_as_instructions(path)

aligned = words_aligned(word1,word2, instructions)

print(aligned)