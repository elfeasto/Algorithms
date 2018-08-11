import numpy as np

def highest_possible(digits, ops):
    #create matrix of max answers
    matrix_side = len(ops) + 1
    M = np.zeros((matrix_side, matrix_side),  dtype= int)
    m = np.zeros((matrix_side, matrix_side),  dtype= int)
    for idx in range(matrix_side):
        M[idx,idx] = digits[idx]
        m[idx,idx] = digits[idx]
    print(M)

    diagonals = get_diags(6)
    for i,j in diagonals:
        M[i, j], m[i,j] = find_max_min(i, j ,M,m,ops)
    print(M)

    return

def find_max_min(i,j,M,m, ops):

    highest = float("-inf")
    lowest = float("inf")
    for k in range(j-i):

        print("we are looking at entry", i, j, end="    ")
        print("the entries in the matrix are at", (i,j-1), (i + k + 1,j + k))
        a = calc(M[i, j - 1], ops[k], M[k+1, j])
        b = calc(M[i, j - 1], ops[k], m[k+1, j])
        c = calc(m[i, j - 1], ops[k], M[k+1, j])
        d = calc(m[i, j - 1], ops[k], m[k+1, j])
        temp_max = max(a,b,c,d)
        if temp_max > highest:
            highest = temp_max
        temp_min = min(a,b,c,d)
        if temp_min < lowest:
            lowest = temp_min

    return highest, lowest

def do_ops(numbers, operations, ops_order):
    """
    CHECK TIME COMPLEXITY, may be too slow
    :param data:
    :param op_order:
    :return:
    """
    digits = numbers
    ops = [x for x in operations]

    for idx in range(len(ops_order)):
        # calculate the number from doing this operation
        new_num = do_op(digits, ops, ops_order[idx])
        # make a new updated digits list
        digits = digits[:ops_order[idx]] + [new_num] + digits[ops_order[idx] + 2:]

        # remove the operation we have done from ops list
        del ops[ops_order[idx]]
        # update the ops_order so it relates to the updated ops list
        temp_ops_order = []
        for inner_idx in ops_order:
            if inner_idx <= ops_order[idx]:
                temp_ops_order.append(inner_idx)
            else:
                temp_ops_order.append(inner_idx - 1)
        ops_order = temp_ops_order

    return digits[0]


def do_op(digits, ops, op_idx):
    num1 = int( digits[op_idx] )
    num2 = int( digits[op_idx + 1] )
    op = ops[op_idx]
    return calc(num1, op, num2)


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
    diags = []
    for x in range(1,n):
        diags.extend((idx, idx + x) for idx in range(n - x))
    return diags


invalid_op = Exception("invalid operator")


data = "5-8+7*4-8+9"
digits = list(map(int, data[ : :2]))
ops = list(data[1: :2])

highest_possible(digits,ops)
