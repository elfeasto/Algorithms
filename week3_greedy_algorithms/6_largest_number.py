#Uses python3

import sys

def is_greater_or_equal(first_digits, second_digits):
    first_dig_list = [int(x) for x in str(first_digits)]
    second_dig_list = [int(x) for x in str(second_digits)]
    first_second = [x for x in first_dig_list]
    first_second.extend(second_dig_list)
    second_first = [x for x in second_dig_list]
    second_first.extend(first_dig_list)
    first_second = list_to_number(first_second)
    second_first = list_to_number(second_first)
    if first_second >= second_first:
        return True
    else:
        return False

def list_to_number(num_list):
    num_string = ''.join(str(x) for x in num_list)
    num = int(num_string)
    return num


def largest_number(nums):
    """
    :param nums: list of digits
    :return:
    """
    ans = []
    while nums:
        max_digit_idx = 0
        max_digits = nums[max_digit_idx]
        for idx  in range(len(nums)):
            if is_greater_or_equal(nums[idx], max_digits):
                max_digits = nums[idx]
                max_digit_idx = idx
        ans.append(max_digits)
        del nums[max_digit_idx]

    ans = list_to_number(ans)
    return  ans



if __name__ == '__main__':
    input = sys.stdin.read()
    #input = "3 55 57 1 8 2"
    data = input.split()
    data = list(map(int , data))
    a = data[1:]
    print(largest_number(a))
    
