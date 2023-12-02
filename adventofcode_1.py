list_of_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
counter = 0

with open('d:\\python\\AOC_input_1.txt', 'r') as file:
    all_strings = file.readlines()

for string_with_numbers in all_strings:
    temp_sum = ''
    for left_num in string_with_numbers:
        if left_num in list_of_numbers:
            temp_sum += left_num
            break
    for right_num in string_with_numbers[::-1]:
        if right_num in list_of_numbers:
            temp_sum += right_num
            break
    counter += int(temp_sum)
print(counter)