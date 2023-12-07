# with open('d:\\python\\AOC_input_1.txt', 'r') as file:
#     all_strings = file.readlines()
all_strings = ['2gkjsdfjgkjtwoflg1seven2']
def sum_of_the_calibration_values_with_spell(all_strings):
    counter = 0
    list_of_substring = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    dict_of_int = {'one' : '1','two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
    dict_of_substring_occurrences = {}
    for string_with_numbers in all_strings:
        for spell in list_of_substring:
            if spell in string_with_numbers:
                dict_of_substring_occurrences[spell] = string_with_numbers.find(spell)
        min_index = min(dict_of_substring_occurrences, key = dict_of_substring_occurrences.get)
        max_index = max(dict_of_substring_occurrences, key = dict_of_substring_occurrences.get)
        result_dict = {min_index: dict_of_substring_occurrences[min_index], max_index: dict_of_substring_occurrences[max_index]}
        print(result_dict)
        temp_num = ''
        for key, value in result_dict.items():           
            if len(key) > 1:
                temp_num += dict_of_int.get(key)
            else:
                temp_num += key
        counter += int(temp_num)
        print(counter)

sum_of_the_calibration_values_with_spell(all_strings)