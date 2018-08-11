import numpy as np

def highest_possible(digits, ops):
    #create matrix of max answers
    matrix_side = len(ops) + 1
    M = np.zeros((matrix_side, matrix_side),  dtype= int)
    m = np.zeros((matrix_side, matrix_side),  dtype= int)
    for idx in range(matrix_side):
        M[idx,idx] = digits[idx]
        m[idx,idx] = digits[idx]
    i = 0
    j = 1

    diagonals = get_diags(6)
    count = 0
    for i,j in diagonals:
        M[i, j], m[i,j] = find_max_min(i, j ,M,m,ops)
    return M[0][-1]


def find_max_min(i,j,M,m, ops):

    highest = float("-inf")
    lowest = float("inf")
    k = j - i - 1
    rel_pairs = get_pairs(k)
    #print("relative pairs are", rel_pairs)
    ops_idx = k
    for first_diff, second_diff in rel_pairs:
        first_coord = [i + first_diff[0], j + first_diff[1]]
        second_coord = [i + second_diff[0], j + second_diff[1]]
        #print("for cell",i,j, "we are looking at cells:", first_coord,second_coord)

        x,y = first_coord, second_coord

        op = ops[x[1]]
        #print("operation is", op)

        a = calc(M[x[0], x[1]], op, M[y[0], y[1]])
        b = calc(M[x[0], x[1]], op, m[y[0], y[1]])
        c = calc(m[x[0], x[1]], op, M[y[0], y[1]])
        d = calc(m[x[0], x[1]], op, m[y[0], y[1]])
        ops_idx += 1

        temp_max = max(a,b,c,d)
        if temp_max > highest:
            highest = temp_max
        temp_min = min(a,b,c,d)
        if temp_min < lowest:
            lowest = temp_min
    return highest, lowest




def calc(num1, operation, num2):
    """
    Performs operation on num1 and num2 then returns the answer
    :param num1: int/float
    :param operation: char
    :param num2: int/float
    :return: int/float
    """

    if operation == "+":
        ans = num1 + num2
    elif operation == "-":
        ans = num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "%":
        ans = num1 % num2
    else:
        print(operation)
        raise invalid_op
    return ans


def get_diags(n):
    """
    returns a the indices of the diagonals of a matrix
    starts after the diagonal has been done at
    row 0 column 1 going in a down and left direction till it reaches the end
    then it goes to row 0 column 2 etc
    :param n:
    :return:
    """
    diags = []
    for x in range(1,n):
        diags.extend((idx, idx + x) for idx in range(n - x))
    return diags


def get_pairs(k):
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


invalid_op = Exception("invalid operator")

data = "5-8+7*4-8+9"
digits = list(map(int, data[ : :2]))
ops = list(data[1: :2])

ans = highest_possible(digits,ops)
print(ans)