'''The newly-improved calibration document consists of lines of text;
each line originally contained a specific calibration value that the Elves now need to recover. 
On each line, the calibration value can be found by combining the first digit and the last 
digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?'''

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