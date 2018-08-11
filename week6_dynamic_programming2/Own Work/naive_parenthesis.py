import itertools

def naive_parenthesis_sln(digits, ops):
    highest = naive_highest_ans(digits,ops)
    lowest = naive_lowest_ans(digits, ops)
    return highest, lowest

def naive_highest_ans(digits,ops):
    perms = list(itertools.permutations([x for x in range(len(ops))]))
    highest_ans = float("-inf")
    best_perm = []
    for perm in perms:
        curr_ans = do_ops(digits, ops, perm)
        if curr_ans >= highest_ans:
            highest_ans = curr_ans
            best_perm = perm
    return highest_ans

def naive_lowest_ans(digits,ops):
    perms = list(itertools.permutations([x for x in range(len(ops))]))
    lowest_ans = float("inf")
    best_perm = []
    for perm in perms:
        curr_ans = do_ops(digits, ops, perm)
        if curr_ans <= lowest_ans:
            lowest_ans = curr_ans
            best_perm = perm
    return lowest_ans

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

invalid_op = Exception("invalid operator")


data = "5-8+7*4-8+9"
digits = list(map(int, data[ : :2]))
ops = list(data[1: :2])
ans = naive_parenthesis_sln(digits,ops)
print(ans)