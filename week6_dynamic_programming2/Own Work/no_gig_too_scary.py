## own work on solving the parenthesis problem ##

def do_ops(digits, operations, op_order):
    """
    CHECK TIME COMPLEXITY, may be too slow
    :param data:
    :param op_order:
    :return:
    """

    for op_idx in op_order:
        new_num = do_op(data, op_idx)
        nums = digits[:op_idx] + [new_num] + digits[op_idx + 2:]



def do_op(data, op_idx):
    num1 = int( data[2 * op_idx] )
    num2 = int( data[2 * (op_idx + 1)] )
    print(num1,num2)
    op = data[2 * op_idx + 1]
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
        raise
    return ans

data = "1+4-3+2+7*6"

digits = list(map(int, data[ : :2]))

ops = list(data[1: :2])

op_idx = 4

new_num = do_op(data, op_idx)
print(type(digits[:op_idx]))
print(type([new_num]))
print(type(digits[op_idx + 1]))
nums = digits[:op_idx] + [new_num] + digits[op_idx + 2:]
print(nums)
del ops[op_idx]
print(ops)