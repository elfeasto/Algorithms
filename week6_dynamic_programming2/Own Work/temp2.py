import numpy as np


def get_diags(n):
    diags = []
    for x in range(n):
        diags.extend((idx, idx + x) for idx in range(n - x))
    return diags



def get_pairs(k):
    """
    for each k return a list of paris of indices to be added to the given coords
    then you have the correct indices for the calculation
    :param k:
    :return:
    """
    rel_indices = get_relative_indices(k)
    pairs = []
    for num in range(len(rel_indices) - 1):
        pairs.append(np.array( (rel_indices[num], rel_indices[num + 1]) ) )
    return pairs


def get_relative_indices(k):
    """
    for each k return a list of indices to be added to the given coords
    then you have the correct indices for the matrix
    :param k:
    :return:
    """
    rel_indices = []
    for num in range(k + 2):
        idx = (num, -(k + 1 - num))
        rel_indices.append(idx)
    return rel_indices


def get_pairs2(k):
    """
    for each k return a list of indices of offsets
    :param k:
    :return:
    """
    pairs = []
    for left in range(k + 1, 0, -1):
        down = k + 2 - left
        pairs.append([(0, -left), (down, 0)])
    return pairs

# k = 0 : 1 left ,1 down
# k = 1: 2 left , 1 left 1 down, 0 left 2 down
# k = 2: 3 left , 2 left 1 down, 1 left 3 down, 0 left 3 down

# k = 0: (i-1,j) , (i,j + 1)
# k = 1: (i-2,j), (i-1,j+1),

ans = get_pairs2(2)
print(ans)