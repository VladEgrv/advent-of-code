rounds_of_game = [{'red': 9, 'green': 12, 'blue': 2}, {'blue': 1, 'green': 11, 'red': 32}, {'red': 10, 'green': 87}]

minimum_set = {'red' : 1, 'green' : 1, 'blue' : 1}

dict1 = {'blue': 1, 'green': 11, 'red': 10}
dict2 = {'red': 1, 'green': 1, 'blue': 1}


for run_of_game in rounds_of_game:
    for colour, value in run_of_game.items():
        if colour in minimum_set and minimum_set[colour] < value:
            minimum_set[colour] = value

print(minimum_set)