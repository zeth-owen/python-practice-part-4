def max_num(num1, num2, num3):
    maximum = max(num1, num2, num3)
    print(maximum)
    return maximum
max_num(3, 4, 5)

def multi_list(lst):
    result = 1
    for num in lst:
        result *= num
        print (result)
    return result

my_lst = [3, 2, 3, 5, 6]
multi_list(my_lst)

def rev_string(input):
    reversed_string = input[::-1]
    print(reversed_string)
    return reversed_string
    
my_input = 'Cow'
rev_string(my_input)


def num_within(num, begin_range, end_range):
    if (num >= begin_range and num <= end_range): 
     return True
    else:
     return False

print(num_within(7, 1, 10))
    


def pascal(n):
    triangle = [[1]]
    for _ in range(1, n):
        new_row = [1]
        prev_row = triangle[-1]
        for i in range(len(prev_row) - 1):
            new_element = prev_row[i] + prev_row[i + 1]
            new_row.append(new_element)
        new_row.append(1)
        triangle.append(new_row)
    for row in triangle:
        print(row)
        return triangle

rows = pascal(5)
print(rows) 


