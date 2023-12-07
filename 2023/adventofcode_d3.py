#this code doesn't work, need to finish task

input_matrix = []
matrix__with_index = {}
import re

input_matrix = []
matrix__with_index = []
list_of_symbols = ['!', '@', '#', '$', '%', '+', '&', '*', '/', '-', '=']
counter = 0

def matrix_generate(input_matrix):
    with open('d:\\python\\AOC_input_3.txt', 'r') as file:
        for line in file:
            row = row = list(line.strip())
            input_matrix.append(row)
    return input_matrix

def dictionary_with_map(input_matrix):
    for row in input_matrix:
        pattern = re.compile(r'\d+')
        numbers = pattern.findall(''.join(row))
        temp_dict = {number: ''.join(row).find(number) for number in numbers}
        matrix__with_index.append(temp_dict)
    return matrix__with_index

def find_element_1_symb(key, value, string, input_matrix, flag):
    for i in input_matrix[string]:
        if i[value - 1] != '.' and i[value + 1] != '.': flag = False
    for i in input_matrix[string - 1]:
        if '.' not in i[value - 1: value + 1]: flag = False
    for i in input_matrix[string + 1]:
        if '.' not in i[value - 1: value + 1]: flag = False
    return flag

        




def find_element_2_symb(key, value, string, input_matrix, flag):
    for i in input_matrix[string]:
        if i[value - 1] != '.' and i[value + 2] != '.': flag = False
    for i in input_matrix[string - 1]:
        if '.' not in i[value - 1: value + 2]: flag = False
    for i in input_matrix[string + 1]:
        if '.' not in i[value - 1: value + 2]: flag = False
    return flag


def find_element_3_symb(key, value, string, input_matrix, flag):
    for i in input_matrix[string]:
        if i[value - 1] != '.' and i[value + 3] != '.': flag = False
    for i in input_matrix[string - 1]:
        if '.' not in i[value - 1: value + 3]: flag = False
    for i in input_matrix[string + 1]:
        if '.' not in i[value - 1: value + 3]: flag = False
    return flag


matrix_generate(input_matrix)
dictionary_with_map(input_matrix)

for string in range (0, len(matrix__with_index)):
    for key, value in matrix__with_index[string].items():
        flag = True
        if len(key) == 1:
            find_element_1_symb(key, value, string, input_matrix, flag)
        if len(key) == 2:
            find_element_2_symb(key, value, string, input_matrix, flag)
        if len(key) == 3:
            find_element_3_symb(key, value, string, input_matrix, flag)
        if flag == False:
            counter += int(key)

print(counter)